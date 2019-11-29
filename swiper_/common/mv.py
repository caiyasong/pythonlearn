from django.utils.deprecation import MiddlewareMixin

from common import error
from common.func import reader_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):

    white_url = ['/api/user/sms/', '/api/user/login/']

    def process_request(self, reuqest):
        url = reuqest.path

        if url in self.white_url:
            return

        uid = reuqest.session.get('uid')
        if not uid:
            return reader_json('用户未登陆', error.USER_NOT_LOGIN)
        else:
            reuqest.user = User.objects.get(id=uid)