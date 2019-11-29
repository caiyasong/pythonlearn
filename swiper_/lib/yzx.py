import random

import requests
from django_redis import get_redis_connection

from common.func import reader_json
from common import error
from worker import celery_app


@celery_app.task
def send_sms(phone):
    sms_code = rand_num(6)
    print('111')
    data = {
         "sid":"4c6c61b3759ec0da50e0f3beae3911e4",
         "token":"036b1998a30253c72c9db20f943b2f21",
         "appid":"b97ef7416b83475b865e10454cdb7879",
         "templateid":"505140",
         "param": sms_code,
         "mobile": phone,
        }
    res = requests.post('https://open.ucpaas.com/ol/sms/sendsms', json=data)
    con = res.json()

    if con.get('code') == '000000':
        redis_cli = get_redis_connection()
        redis_cli.set(f'smscode-{phone}', sms_code, 180)

        return reader_json('短信发送成功')
    else:
        return reader_json('短信发送失败', error.SEND_SMS_FAIL)


def rand_num(num):
    start = 10**(num-1)
    end = 10**num - 1

    return random.randint(start, end)