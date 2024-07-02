from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from Engine.common_util import ResponseMessage
from Service.data import DataService

class DataView(APIView):

    @staticmethod
    def get(request):
        response_return = ResponseMessage()
        try:
            request_data = dict()
            request_data['name'] = request.GET.get('name', '')
            response_return = DataService(request=request).getData(request_data)

        except Exception as e:
            response_return.set_error_status(f'Hello error : {e}')

        return Response(response_return)

    @staticmethod
    def post(request):
        response_return = ResponseMessage()
        if not request.data:
            return Response({'Error': "Please provide data of category"})

        try:
            request_data = dict()
            request_data['name'] = request.data.get('name', '')
            request_data['lat'] = request.data.get('lat', '')
            request_data['long'] = request.data.get('long', '')
            request_data['speed'] = request.data.get('speed', '')
            response_return = DataService(request=request).recieveData(request_data)

        except Exception as e:
            response_return.set_error_status(f'Hello Error : {e}')

        return Response(response_return)


