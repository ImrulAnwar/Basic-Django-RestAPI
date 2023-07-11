from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # in model serializer i just need to describe my model and its fields
    class Meta:
        model = Article
        # fields = ['id', 'title', 'body']
        fields = '__all__'
