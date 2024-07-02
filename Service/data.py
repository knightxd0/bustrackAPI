import datetime
import psycopg2
import requests
from Engine.common_util import ResponseMessage
from Engine.settings import CONNECTION,SECRET_KEY
from datetime import datetime
import pytz

class DataService:
    def __init__(self, **kwargs):
        self.requests = requests
        self.token = kwargs.get('token','')
    @staticmethod
    def recieveData(request_data):
        response_return = ResponseMessage()
        name = request_data.get('name')
        lat = request_data.get('lat')
        long = request_data.get('long')
        speed = request_data.get('speed')

        try:
            conn = psycopg2.connect(CONNECTION)
            cursor = conn.cursor()
            query = f"""
                      INSERT INTO public.data(name, lat, "long", speed)
	                  VALUES ('{name}', {lat},{long}, {speed});
                    """
            cursor.execute(query)
            response_return.set_success_status()
            conn.commit()
            cursor.close()
            conn.close()

        except Exception as e:
            response_return.set_error_status(f'Hello error : {e}')

        return response_return.get_response()

    @staticmethod
    def getData(request_data):
        response_return = ResponseMessage()
        name = request_data.get('name')
        logic = f"WHERE name = '{name}' AND time_at >= now() - interval '40 seconds'" if name else "WHERE time_at >= now() - interval '40 seconds'"


        try:
            conn = psycopg2.connect(CONNECTION)
            cursor = conn.cursor()
            query = f"""
                          SELECT id, name, lat, "long", speed,TO_CHAR(time_at::DATE, 'DD Mon YYYY') as date, TO_CHAR(time_at::time, 'HH24:MI:SS') as time
	                      FROM public.data
                          {logic}
                          order by time_at desc
                        """
            cursor.execute(query)
            records = cursor.fetchall()

            selectObject = []
            columnNames = [column[0] for column in cursor.description]

            for record in records:
                selectObject.append(dict(zip(columnNames, record)))

            res = {
                "value": selectObject[0]
            }

            response_return.set_success_status(res)
            conn.commit()
            cursor.close()
            conn.close()

        except Exception as e:
            response_return.set_error_status(f'Hello error : {e}')

        return response_return.get_response()