from rest_framework.serializers import ModelSerializer,DateTimeField,CharField
from .models import MovieInformation,MovieTop,UserAdmin,MovieCollection

class MovieSerializer(ModelSerializer):
    # time = DateTimeField(format="%Y-%m-%d %H:%M:%S",required=False)
    class Meta:
        model = MovieInformation
        fields = ['id','mname','years','score','director','mold','act','languages','img','details','official']

class MovieTopsSerializer(ModelSerializer):
    class Meta:
        model = MovieTop
        fields = ['mname','years','score','director','mold','act','img','details']

class MovieUser(ModelSerializer):
    class Meta:
        model = UserAdmin
        fields = ['id','username','password']

class MovieColl(ModelSerializer):
    username = CharField(source='uid.username')
    mname = CharField(source='mid.mname')
    years = CharField(source='mid.years')
    score = CharField(source='mid.score')
    director = CharField(source='mid.director')
    mold = CharField(source='mid.mold')
    act = CharField(source='mid.act')
    languages = CharField(source='mid.languages')
    img = CharField(source='mid.img')
    details = CharField(source='mid.details')
    official = CharField(source='mid.official')
    class Meta:
        model = MovieCollection
        fields = ['id','mid','username','mname','years','score','director','mold','act','languages','img','details','official']
