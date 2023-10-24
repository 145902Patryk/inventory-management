"""Layout views."""
# Django
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView

# Project
from apps.layout.forms import LocationForm
from apps.layout.forms import SetItemForm
from apps.layout.models import Layout
from apps.layout.models import Location


class MainLayoutView(ListView):
    template_name = 'layout/layout.html'
    model = Layout

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        js_obj = {}
        locations = {}
        for layout in self.object_list:
            spots = layout.location_set.all()
            locations[layout.pk] = [{'name': sp.name, 'pk': sp.pk} for sp in spots]
            arr = [{'x': sp.x, 'y': sp.y, 'name': sp.name, 'pk': sp.pk} for sp in spots]
            js_obj[f'imagePreview{layout.pk}'] = arr
        ctx['js_obj'] = js_obj
        ctx['location_form'] = LocationForm()
        ctx['locs'] = locations
        return ctx


class LocationSetItems(FormView):
    template_name = 'layout/item_set_form.html'
    form_class = SetItemForm
    success_url = reverse_lazy('layout:main')

    def form_valid(self, form):
        location = Location.objects.get(pk=self.kwargs['pk'])
        form.cleaned_data['items'].update(location=location)
        return super().form_valid(form)


def add_location(request):
    """Set amount of items per page."""
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            loc = Location.objects.create(**form.cleaned_data)
            dot = {
                'x': loc.x,
                'y': loc.y,
                'layout': loc.layout.pk,
                'name': loc.name,
                'pk': loc.pk,
            }
            return JsonResponse(dot, status=201)
        error = ''
        for key, val in form.errors.get_json_data().items():
            error += f'{key} - {" ".join([el["message"] for el in val])}<br>'
        return HttpResponse(error, status=422)
    return HttpResponse(status=400)


def items_list_for_location(request):
    """Return list of items for selected location."""
    if request.method == 'GET':
        pk = request.GET.get('pk')
        if pk:
            loc = Location.objects.get(pk=pk)
            items = list(loc.item_set.all().values_list('pk', 'name'))

            return JsonResponse({'success': True, 'items': items, 'loc': loc.name}, status=200)
    return HttpResponse(status=400)
