from datetime import datetime


class TIMESTAMP(object):
    """ TIMESTAMP Class """

    @staticmethod
    def get_time():
        return datetime.now().strftime('%H:%M:%S')

    @staticmethod
    def get_date():
        return datetime.now().strftime('%Y-%m-%d')
