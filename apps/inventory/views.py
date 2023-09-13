# Standard Library
import json

from django.contrib import messages
# Django
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView

# Local
from .forms import FilterForm, ItemForm
from .models import Item
from .utils import filter_to_item_query


class ItemsListView(ListView):
    model = Item
    paginate_by = 9
    filters = {}

    def get_paginate_by(self, queryset):
        """
        todo: Per page elements selection.
        """
        return self.paginate_by

    def dispatch(self, request, *args, **kwargs):
        self.filters = json.loads(self.request.session.get('filters', '{}'))
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query_filter, q_filter = filter_to_item_query(self.filters)
        return self.model.objects.filter(*q_filter, **query_filter).distinct().prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['form'] = FilterForm(self.filters)
        return context


class ItemCreateView(CreateView):
    model = Item
    success_url = reverse_lazy('layout:main')
    form_class = ItemForm

    def get_initial(self):
        return {'location_pk': self.kwargs.get('location_pk')}

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, f'Item "{self.object.name}" created')
        return response


def set_filters(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            request.session['filters'] = json.dumps(form.cleaned_data)
            return HttpResponseRedirect(reverse_lazy('inventory:items_list'))
    return HttpResponse(status=400)


def clear_filters(request):
    url = request.GET.get('next', reverse_lazy('inventory:items_list'))
    try:
        del request.session['filters']
    except KeyError:
        print('no filters')
    return HttpResponseRedirect(url)
