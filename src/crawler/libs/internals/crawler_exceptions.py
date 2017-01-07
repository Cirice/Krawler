
class CrawlerException(Exception):
    """ Custom Crawler Exception Class """

    def __init__(self, message, code, agent="Unknown"):
        super(Exception, self).__init__()
        self.code = code
        self.message = message
        self.agent = agent
