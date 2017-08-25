import sys

from crawler.crawler import CrawlEngine

# low level project imports
from crawler.libs.internals.debug import print_stack_trace
from crawler.libs.internals.custom_logger import ERR, log_says
from crawler.libs.internals.flags import VERBOSE, DEBUG
from crawler.libs.internals.timer import XTimer


def run():
    ce = CrawlEngine()
    ce.start()

# running the code ...
if __name__ == "__main__":
    with XTimer("MyTimer"):
        try:
            run()
        except (SystemExit, KeyboardInterrupt):
            sys.exit(0)
        except CrawlerException as err:
            if VERBOSE >= 3:
                log_says(message=err.message, log_type=ERR, agent="main.py")
            sys.exit(1)
        except:
            if DEBUG:
                print_stack_trace()
            sys.exit(2)
        else:
            pass
        finally:
            sys.exit(0)
