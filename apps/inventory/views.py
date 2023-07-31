import json

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.utils import timezone

from .forms import FilterForm
from .models import Item
from .utils import filter_to_item_query


class ItemsListView(ListView):
    model = Item
    paginate_by = 20
    filters = {}

    def dispatch(self, request, *args, **kwargs):
        self.filters = json.loads(self.request.session.get('filters', '{}'))
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        query_filter = filter_to_item_query(self.filters)
        return self.model.objects.filter(**query_filter).prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['form'] = FilterForm(self.filters)
        return context


def set_filters(request):
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            request.session['filters'] = json.dumps(form.cleaned_data)
            return HttpResponseRedirect(reverse_lazy('items_list'))
    return HttpResponse(status=400)


def clear_filters(request):
    url = request.GET.get('next', reverse_lazy('items_list'))
    try:
        del request.session['filters']
    except KeyError:
        print('no filters')
    return HttpResponseRedirect(url)
