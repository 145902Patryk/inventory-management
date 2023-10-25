from django.utils.log import ServerFormatter


class CustomServerFormatter(ServerFormatter):
    default_msec_format = ''

    def format(self, record):
        if self.uses_server_time():
            record.server_time = self.formatTime(record, '%Y-%m-%d %H:%M:%S')
        return super().format(record)
