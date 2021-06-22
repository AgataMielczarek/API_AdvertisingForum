from django.shortcuts import render
from rest_framework.views import APIView
from ads.models import Advertisement
from .serializers import AdSerializer, UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import AllowAny



class ListCreateAds(APIView):
    def get(self, request):
        ads = Advertisement.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response (data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUpdateDeleteAd(APIView):

    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            raise Http404

    def is_owner(self, request, object):
        return request.user == object.user

    def get(self, request, pk):
        ad = self.get_object(pk)
        serializer = AdSerializer(ad)
        return Response(serializer.data)

    def put(self, request, pk):
        ad = self.get_object(pk)
        if self.is_owner(request, ad):
            serializer = AdSerializer(instance=ad, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'response': "You don't have permission to edit this object."})

    def delete(self, request, pk):
        ad = self.get_object(pk)
        if self.is_owner(request, ad):
            ad.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'response': "You don't have permission to delete this object."})


class DisplayIndustry(APIView):
    def get(self, request, pk):
            ads = Advertisement.objects.filter(industry=pk)
            if ads.count() != 0:
                serializer = AdSerializer(instance=ads, many=True)
                return Response (data=serializer.data)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)

class ListUsers(APIView):
    def get(self, request):
        if request.user.is_staff:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response (serializer.data)
        else:
            return Response({'response' : "You don't have permission to get this data."})


class CreateUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMyAds(APIView):
    def get(self, request):
        ads = Advertisement.objects.filter(user=request.user)
        serializer = AdSerializer(instance=ads, many=True)
        return Response(serializer.data)



        

        













