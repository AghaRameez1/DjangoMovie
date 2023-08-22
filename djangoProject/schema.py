import graphene
from graphene_django import DjangoObjectType
from movies.models import movies

class MovieType(DjangoObjectType):
    class Meta:
        model = movies
        fields = '__all__'

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    movies = graphene.Field(MovieType, user_added=graphene.String(required=True))

    def resolve_moviedetails(root, info, user_added):
        try:
            return movies.objects.get(user_added__first_name=user_added)
        except:
            return None

schema = graphene.Schema(query=Query)