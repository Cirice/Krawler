import requests
import requests_cache
import sys

from .internals.debug import print_stack_trace
from .internals.crawler_exceptions import CrawlerException
from .internals.custom_logger import INFO, WARN, ERR, log_says
from .internals.flags import VERBOSE, DEBUG
from .internals.web_objects import WebPage
from .internals.colours import ColouredText

# suppressing warnings
requests.packages.urllib3.disable_warnings()

# how many time shoud requests retry on failure
requests.adapters.DEFAULT_RETRIES = 5

# enabling cache for requests
requests_cache.install_cache('cache/download_cache.db')


class BaseGrabber(object):
    """ Base Grabber Class """

    USER_AGENT = (
        "Bingbot",
        "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)")

    HEADERS = {"User-Agent": USER_AGENT[1],
               "Accept": "*/*",
               "Accept-Encoding": "gzip, deflate",
               "Connection": "keep-alive"}

    VALID_FILES = [
        "text/",
        "application/json",
        "application/html",
        "application/xhtml+xml",
        "application/javascript",
        "application/x-javascript",
        "application/xml"
    ]

    READ_TIMEOUT = 30
    CONNEXION_TIMEOUT = 30
    SESSION = requests.Session()


class PageGrabber(BaseGrabber):
    """ HTML Grabber Class """

    def __get_content_type(self, headers):
        return headers['content-type'].lower()

    def _has_valid_type(self, headers):
        if 'content-type' in headers:
            for file_type in self.VALID_FILES:
                if file_type in self.__get_content_type(headers):
                    return True
            return False
        return None

    def get_page(self, url, verb='GET', use_referer=False):
        try:
            if verb.lower() == "get":
                func = self.SESSION.get
            else:
                func = self.SESSION.head

            # add referer if it's ought to
            if use_referer and url.PARENT:
                if 'referer' in self.HEADERS:
                    self.HEADERS['referer'] = url.PARENT
                else:
                    self.HEADERS.ipdate({'referer': url.PARENT})

            # sending the actual request
            response = func(
                url=url.LINK,
                headers=self.HEADERS,
                stream=False,
                verify=False,
                timeout=(
                    self.CONNEXION_TIMEOUT,
                    self.READ_TIMEOUT))
        except:
            if DEBUG:
                print_stack_trace()

            raise CrawlerException(
                message="COULD NOT RETIEVE LINK'S DATA", code="102")

        else:
            #print(response.status_code, response.headers, response.text)
            # is url contents a html page?
            body_type = self._has_valid_type(response.headers)
            if body_type:
                return WebPage(text=response.text, link=response.url,
                               headers=response.headers,
                               status_code=response.status_code)
            elif body_type is None:
                if VERBOSE >= 3:
                    log_says(
                        message="NO CONTENT-TYPE HEADER",
                        log_type=WARN,
                        agent="PageGrabber.get_page")

                raise CrawlerException(
                    message="COULD NOT DETECT LINK'S BODY TYPE", code="100")

            else:
                if VERBOSE >= 3:
                    log_says(
                        message=(
                            response.url +
                            " (" +
                            ColouredText.blue(
                                response.headers['content-type']) +
                            ")"),
                        log_type=ERR,
                        agent="PageGrabber")

                raise CrawlerException(
                    message="LINK'S BODY DOES NOT HAVE A VALID TYPE", code="101")
