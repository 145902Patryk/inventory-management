from django.views.generic import ListView

from apps.layout.models import Layout


class MainLayoutView(ListView):
    template_name = 'layout/layout.html'
    model = Layout

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        js_obj = {}
        for layout in self.object_list:
            arr = [{'x': loc.x, 'y': loc.y, 'name': loc.name} for loc in layout.location_set.all()]
            js_obj[f'image_preview{layout.pk}'] = arr
        print(js_obj)
        ctx['js_obj'] = js_obj
        return ctx
