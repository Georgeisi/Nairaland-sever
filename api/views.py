from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import BlogSerializer
from.models import BlogPost
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
# Create your views here.
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def create_post(request):
    if request.method=='GET':
        return  Response({'message':'provide information'})
    
    elif request.method=='POST':
        story= request.data
        author=request.user
        serializer= BlogSerializer(data=story, many=False)
        if serializer.is_valid():
            serializer.save(author=author)
            return Response({
                'message':'story created sucessfully'
            },status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message':'something went wrong',
                'status':'400 bad request'

            },status=status.HTTP_400_BAD_REQUEST)
        




@api_view(['GET'])
def get_post(request):
    if request.method=='GET':
        story = BlogPost.objects.all()
        paginator =PageNumberPagination()
        paginator.page_size=5
        paginated_blogs = paginator.paginate_queryset(story, request)
        serializer = BlogSerializer(paginated_blogs, many=True)
     
        return paginator.get_paginated_response(serializer.data)

@api_view(['PATCH','GET','DELETE'])
@permission_classes([IsAuthenticated])
def update_post(request,pk ):
    if request.method=='PATCH':
        story = BlogPost.objects.get(id=pk)
        serializer=BlogSerializer(instance=story, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message':'story updated sucessfully',
            }, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='GET':
        stories= BlogPost.objects.get(id=pk)
        serializer= BlogSerializer(stories,many=False)
        return Response(data=serializer.data , status=status.HTTP_200_OK)
    elif request.method=='DELETE':
        story=BlogPost.objects.get(id=pk)
        story.delete()
        return Response({'message':'story deleted sucessfully'})


@api_view(['GET'])  
@permission_classes([IsAuthenticated])
def user_stories(request):
    author =request.user
    user_stories=BlogPost.objects.filter(author=author)
    serializer= BlogSerializer(user_stories,many=True)


    return Response(data=serializer.data, status=status.HTTP_200_OK)      


