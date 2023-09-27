import time

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.utils import dateformat
from django.utils import timezone


class LogsMiddleware(MiddlewareMixin):
    """Middleware for logging activity."""

    start = None
    path = ''
    show = False

    def __init__(self, get_response):
        super().__init__(get_response)
        self.show = settings.DEBUG

    def process_view(self, request, func, view_args, view_kwargs):  # noqa: D102
        if self.show:
            now = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
            v1 = 'VIEW:'.ljust(7, ' ')
            if hasattr(func, 'view_class'):
                name = func.view_class.__name__
            else:
                name = func.__name__
            print(f'{now} {v1} {func.__module__}.{name}')

    def process_request(self, request):  # noqa: D102
        self.start = time.time()

    def process_response(self, request, response):  # noqa: D102
        if self.show:
            now = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
            end = time.time() - self.start
            v1 = 'END:'.ljust(7, ' ')
            print(f'{now} {v1} {request.get_full_path()} {end} -- {response}')
        return response
