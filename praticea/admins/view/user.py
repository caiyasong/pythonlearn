from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from admins.serializers.user import UserModelSerializer
from orders.models import User

class PageNum(PageNumberPagination):
    # 指定每页显示多少条记录的参数名称
    page_size_query_param = 'page_size'

    # 每页显示多少条记录
    max_page_size = 1


class UserInfo(APIView):
    def get(self, request):
        userNum = User.objects.count()
        activeNum = User.objects.filter(is_active=1).count()

        return Response({'userNum': userNum, 'emailNum': activeNum})

class User(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    Pagination_class = PageNum

    filter_fields = ('username', )