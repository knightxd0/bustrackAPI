from datetime import datetime
import pytz

class ResponseMessage:
    def __init__(self, **kwargs):
        th_tz = pytz.timezone('Asia/Bangkok')
        self.response = dict()
        self.response['meta'] = {}
        self.response['meta']['response_datetime'] = datetime.now(th_tz).strftime('%Y/%m/%d, %H:%M:%S')
        self.response['meta']['response_desc'] = ""

    def set_success_status(self, response_body=None):
        self.response['meta']['response_code'] = 20000
        self.response['meta']['response_desc'] = 'success'
        if response_body or type(response_body) == list:
            self.response['meta']['response_data'] = response_body

    def set_invalid_status(self, response_body=None):
        self.response['meta']['response_code'] = 40001
        self.response['meta']['response_desc'] = 'unauthorized'
        if response_body or type(response_body) == list:
            self.response['meta']['response_data'] = response_body

    def set_error_status(self, err_message, err_code=22000):
        self.response['meta']['response_code'] = err_code
        self.response['meta']['response_desc'] = err_message

    def set_conflict_status(self, err_message, err_code=40009):
        self.response['meta']['response_code'] = err_code
        self.response['meta']['response_desc'] = err_message

    def set_notfound_status(self, err_message, err_code=40004):
        self.response['meta']['response_code'] = err_code
        self.response['meta']['response_desc'] = err_message

    def get_response(self):
        return self.response
