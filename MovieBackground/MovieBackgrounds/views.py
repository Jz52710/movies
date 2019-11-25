from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView,status
from .models import UserAdmin,MovieInformation,MovieTop
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import MovieSerializer,MovieTopsSerializer
import requests,json

from django.http.multipartparser import MultiPartParser


# Create your views here.
def index(request):
    return HttpResponse('Hello world')

#智能推荐
class MovieInformations(APIView):
    renderer_classes = [JSONRenderer]
    #查询
    def get(self,request,*args,**kwargs):
        movies = MovieInformation.objects.all()
        se = MovieSerializer(movies,many=True)
        print(se.data)
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

# class MovieOneview(APIView):
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
    # 查询
    def get(self, request, *args, **kwargs):
        movies = MovieTop.objects.all()
        se = MovieTopsSerializer(movies, many=True)
        return Response({'code': 200, 'data': se.data})

#查询分类
class MovieClassfiy(APIView):
    renderer_classes = [JSONRenderer]
    # 查询
    def get(self, request, *args, **kwargs):
        movies = MovieInformation.objects.filter(mold=request.data['mold'])
        if movies:
            se = MovieSerializer(movies, many=True)
            return Response({'code': 200, 'data': se.data})

#正在热映
class MovieHot(APIView):
    renderer_classes = [JSONRenderer]
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
