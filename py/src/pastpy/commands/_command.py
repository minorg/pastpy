import logging


class _Command(object):
    def __init__(self):
        self.__logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)

    @property
    def _logger(self):
        return self.__logger