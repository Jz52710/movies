from rest_framework.serializers import ModelSerializer,DateTimeField
from .models import MovieInformation,MovieTop,UserAdmin

class MovieSerializer(ModelSerializer):
    # time = DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
    class Meta:
        model = MovieInformation
        fields = ['mname','years','score','director','mold','act','languages','img','details','official']

class MovieTopsSerializer(ModelSerializer):
    class Meta:
        model = MovieTop
        fields = ['mname','years','score','director','mold','act','img','details']

class MovieUser(ModelSerializer):
    class Meta:
        model = UserAdmin
        fields = ['id','username','password']
