from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView,status
from .models import UserAdmin,MovieInformation,MovieTop
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import MovieSerializer,MovieTopsSerializer,MovieUser
import requests,json
import pymysql
from django.contrib.auth import authenticate,login

from rest_framework.authtoken.models import Token

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
#验证token
class TokenAuth(BaseAuthentication):
    def authenticate(self,request):
        token = request.META.get("HTTP_AUTHENTICATION",None)
        # print(request.META)
        print(token)
        if token:
            obj = Token.objects.filter(key=token)
            if obj:
                return None
        raise exceptions.AuthenticationFailed('token 异常')


# Create your views here.
def index(request):
    return HttpResponse('Hello world')

#智能推荐
class MovieInformations(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuth]
    #查询
    def get(self,request,*args,**kwargs):
        movies = MovieInformation.objects.all()
        se = MovieSerializer(movies,many=True)
        # print(se.data)
        return Response({'code':200,'data':se.data})
    #增加信息
    def post(self,request):
        moviesser = MovieSerializer(data=request.data)
        #验证
        if moviesser.is_valid():
            moviesser.save()
            return Response(moviesser.data,status=status.HTTP_200_OK)
        print(moviesser.is_valid())
        return Response(moviesser.errors,status=status.HTTP_400_BAD_REQUEST)

    #修改
    def put(self,request,*args,**kwargs):
        moviesser = MovieSerializer(data=request.data)
        #验证
        if moviesser.is_valid():
            moviesser.update(MovieInformation.objects.filter(id=request.data['id']).first(),request.data)
            return Response(moviesser.data,status=status.HTTP_200_OK)
        return Response(moviesser.errors,status=status.HTTP_400_BAD_REQUEST)
    #删除
    def delete(self,request,*args,**kwargs):
        obj = MovieInformation.objects.filter(id=request.data['id']).first()
        #验证
        if obj:
            obj.delete()
            return Response({'msg':'ok'},status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#验证

#top100
class MovieTops(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuth]
    # 查询
    def get(self, request, *args, **kwargs):
        movies = MovieTop.objects.all()
        se = MovieTopsSerializer(movies, many=True)
        return Response({'code': 200, 'data': se.data})

#查询分类
class MovieClassfiy(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuth]
    # 查询
    def post(self, request, *args, **kwargs):
        # res = json.loads(request.body)
        movies = MovieInformation.objects.filter(mold__contains=request.data['mold'])
        if movies:
            se = MovieSerializer(movies, many=True)
            return Response({'code': 200, 'data': se.data})

#正在热映
class MovieHot(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuth]
    def get(self,request,*args,**kwargs):
        urls= 'https://douban-api.uieee.com/v2/movie/in_theaters'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        r = requests.get(url=urls,headers=headers)
        data = json.loads(r.text)
        vals = []
        for items in data['subjects']:
            item = {}
            item['score'] = items['rating']['average']#评分
            item['mold'] = "/".join(items['genres'])#类型
            item['mname'] = items['title']#名字
            arr = []
            for val in items['casts']:
                a = val['name']
                arr.append(a)
            item['act'] = "/".join(arr)#演员
            arr1 = []
            for val in items['directors']:
                name = val['name']
                arr1.append(name)
            item['director'] = "/".join(arr1)#导演
            item['years'] = items['year']#年份
            item['img'] = items['images']['small']#图片
            item['details'] = items['alt']#详情
            vals.append(item)
        return Response({'code':200,'data':vals})

#注册
class Logon(APIView):
    renderer_classes = [JSONRenderer]
    def post(self,request,*args,**kwargs):
        connect = pymysql.connect(host='127.0.0.1',user='root',password='jz52710',db='movies' ,port=3306,charset='utf8',use_unicode=True,autocommit=True)
        cursor = connect.cursor()
        try:
            cursor.execute(
                """select * from moviebackgrounds_useradmin where username = %s""",
                request.data['username'])
            # 去重
            repetition = cursor.fetchone()
            if repetition is not None:
                pass
            else:
                cursor.execute(
                    "INSERT INTO moviebackgrounds_useradmin(username,password) VALUE (%s,%s)",
                    (request.data['username'],
                     request.data['password'],
                     ))
                connect.commit()
        except Exception as error:
            print(error)
        cursor.close()  # 关游标
        connect.close()  # 关链接
        return Response({'code':200,'msg':'yes'})

#登录
class Login(APIView):
    renderer_classes = [JSONRenderer]
    def post(self,request,*args,**kwargs):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None and user.is_active:
            login(request, user)
            token = Token.objects.filter(user_id=user.id).first()
            return Response({'msg': 'ok', 'token': token.key})
        else:
            return Response({'msg': 'no'})

#频道
class MovieSess(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuth]
    # 查询
    def post(self, request, *args, **kwargs):
        # res = json.loads(request.body)
        movies = MovieInformation.objects.filter(mold__contains=request.data['mold'])
        if movies:
            se = MovieSerializer(movies, many=True)
            return Response({'code': 200, 'data': se.data})

#搜索
class MovieSearch(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuth]
    # 查询
    def post(self, request, *args, **kwargs):
        # res = json.loads(request.body)
        movies = MovieInformation.objects.filter(mname__contains=request.data['mname'])
        if movies:
            se = MovieSerializer(movies, many=True)
            return Response({'code': 200,'msg':'ok', 'data': se.data})
        else:
            return Response({'msg':'no','data':'暂无此电影'})
