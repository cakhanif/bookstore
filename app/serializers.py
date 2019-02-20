from rest_framework import serializers
from app.models import *


class BookSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    rls_date= serializers.DateTimeField()
    book_cat= serializers.CharField(max_length=5)
    publisher= serializers.CharField(max_length=20)
    price= serializers.IntegerField()
    stock= serializers.IntegerField()

    def create(self,validated_data):
        return Book.object.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.rls_date= validated_data.get('rls_date',instance.rls_date)
        instance.book_cat= validated_data.get('book_cat',instance.book_cat)
        instance.publisher= validated_data.get('publisher',instance.publisher)
        instance.price= validated_data.get('price',instance.price)
        instance.stock= validated_data.get('stock',instance.stock)
        instance.save()
        return instance


