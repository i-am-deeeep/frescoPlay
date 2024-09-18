from django.shortcuts import render
from inventoryApp.models import Item
from inventoryApp.serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class ItemListAV(APIView):
    def get(self,request):
        items=Item.objects.all()
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
    def delete(self,request):
        try:
            item=Item.objects.get(id=request.data.get('id'))
            item.delete()
            items=Item.objects.filter(id=request.data.get('id'))
            serializer=ItemSerializer(items,many=True)
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'error':'something wrong i dont know what'})
        
class ItemAV(APIView):
    def put(self,request,pk):
        item=Item.objects.get(pk=pk)
        serializer=ItemSerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ItemFilterAV(APIView):
    def get(self,request,category):
        items=Item.objects.filter(category=category)
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ItemSortAV(APIView):
    def get(self,request):
        items=Item.objects.all().order_by('-price')
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)