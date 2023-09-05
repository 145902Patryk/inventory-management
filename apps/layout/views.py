from django.views.generic import ListView

from apps.layout.forms import LocationForm
from apps.layout.models import Layout


class MainLayoutView(ListView):
    template_name = 'layout/layout.html'
    model = Layout

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        js_obj = {}
        for layout in self.object_list:
            spots = layout.location_set.all()
            arr = [{'x': sp.x, 'y': sp.y, 'name': sp.name, 'pk': sp.pk} for sp in spots]
            js_obj[f'imagePreview{layout.pk}'] = arr
        ctx['js_obj'] = js_obj
        ctx['form'] = LocationForm()
        return ctx


def add_location(request):
    """Set amount of items per page."""
    if request.method == 'POST':
        form = LocationForm(request.POST)
        print(form.is_valid())
        print(form.cleaned_data)