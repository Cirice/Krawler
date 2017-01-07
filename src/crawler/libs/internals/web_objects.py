from .timestamp import TIMESTAMP


class BaseWebObject(object):
    """ Base Web Object Class """
    pass


class URL(BaseWebObject):
    """ A Web URL Class """

    def __init__(self, link, depth, parent):
        self.DEPTH = int(depth)
        self.LINK = link.strip()
        self.FAILURES = 0
        self.PARENT = parent


class WebPage(BaseWebObject):
    """ A WebPage Class """

    def __init__(self, text, link, headers, status_code):
        self.TEXT = text
        self.LINK = link.strip()
        self.STATUS_CODE = status_code
        self.HEADERS = headers
        self.DATE = TIMESTAMP.get_date()
        self.TIME = TIMESTAMP.get_time()
