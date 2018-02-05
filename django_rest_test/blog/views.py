# -*- coding:UTF-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post
from rest_framework import serializers,mixins
from rest_framework.generics import GenericAPIView

def blog_page(request):
    post_list = Post.objects.all()
    return HttpResponse('hello'+post_list[0].title)

class PostSerializer(serializers.ModelSerializer): # Serializer REST로 데이터를 주고 받을 때 모델을 어떻게 주고 받을 것인가 정의하는 클래스
    class Meta:
        model = Post
        fields = '__all__'
        # ModelsSerializer 데이터 모델 그 자체를 주고 받을 것이므로 기본적으로 모델 전체를 자동으로 변환해주는 것
        # 자신이 필요한 정보들을 파악하여 자동으로 serialize를 수행함
        # serialize 일렬 번호 지정

class blog_api(GenericAPIView,mixins.ListModelMixin): # GenericAPIView 기본적인 REST Framework 웹페이지를 출력해줌 , 기본적인 REST 기능 제공
    # ListModelMixin GenericAPIView에 queryset과 serializer_class를 기반으로 리스트를 만들어줌
    # mixin 클래스의 조합으로 쉽고 빠르게 구현 가능
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # method get_serializer_class()
    # REST Framework는 GET/POST/PATCH/DELETE 등의 요청에 대한 기본 처리를 제공해줌

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    # ListModelMixin 상속받은 list함수 목록 조회 기능 요청



