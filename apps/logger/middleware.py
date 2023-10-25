# Standard Library
import time

# Django
from django.conf import settings
from django.utils import dateformat
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

# Project
from apps.logger.models import Log


class LogsMiddleware(MiddlewareMixin):
    """Middleware for logging activity."""

    start = None
    path = ''
    show = False
    save = False
    response_dict = {}

    def __init__(self, get_response):
        super().__init__(get_response)
        self.show = settings.DEBUG

    def process_exception(self, request, exception):
        self.response_dict['exception'] = {'class': str(type(exception)), 'error': str(exception)}

    def process_view(self, request, func, view_args, view_kwargs):  # noqa: D102
        if hasattr(func, 'view_class'):
            name = func.view_class.__name__
        else:
            name = func.__name__
        self.save = self.save and 'static' not in name
        if self.show:
            now = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
            v1 = 'VIEW:'.ljust(7, ' ')
            print(f'{now} {v1} {func.__module__}.{name}')

    def process_request(self, request):  # noqa: D102
        self.start = time.time()
        self.path = request.get_full_path()
        self.save = '/admin/' not in request.get_full_path()

    def process_response(self, request, response):  # noqa: D102
        now = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
        end = time.time() - self.start
        if self.show:
            v1 = 'END:'.ljust(7, ' ')
            print(f'{now} {v1} {end} {self.path} -- {response}')
        if self.save:
            Log.objects.create(
                created=timezone.now(),
                time=end,
                user=f'{request.user} (pk={request.user.id})',
                path=self.path,
                status=response.status_code,
                response={**response.headers.__dict__, **self.response_dict},
            )
        return response
