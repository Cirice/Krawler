import validators

# importing BeautifulSoup
try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

# project specific imports
from .internals.debug import print_stack_trace
from .internals.crawler_exceptions import CrawlerException
from .internals.custom_logger import INFO, WARN, ERR, log_says
from .internals.colours import ColouredText
from .internals.flags import VERBOSE, DEBUG
from .internals.web_objects import URL


class HTMLParser(object):
    """ HTML Parser Class """

    def extract_links(self, page):

        def extract(html, tag, parent_link=page.LINK):
            links = set()
            for link in html.find_all(tag, href=True):
                if validators.url(link['href']) is True:
                    url = link['href']
                else:
                    url = parent_link.strip().rstrip("/") + "/" + \
                        link['href'].strip().lstrip("/")

                    if VERBOSE >= 5:
                        log_says(
                            message="LINK: " +
                            ColouredText.magenta(url),
                            agent="HTMLParser",
                            log_type=INFO)

                # adding the link into the list of found links
                links.add(URL(link=url, depth=0, parent=parent_link))
            return links

        try:
            urls = set()
            html = BeautifulSoup(page.TEXT, "lxml")

            anchors = extract(html, tag="a")  # <a> .. </a>
            links = extract(html, tag="link")  # <link> .. </link>
            if anchors:
                urls = urls | anchors  # joining urls with anchors
            if links:
                urls = urls | links  # joining urls with links
        except:
            if DEBUG:
                print_stack_trace()
            return set()
        else:
            return urls
