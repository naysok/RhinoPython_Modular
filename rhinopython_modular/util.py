import datetime


class Util():

    def get_current_time_yymmdd(self):
        return str(datetime.datetime.now().strftime("%y%m%d"))
