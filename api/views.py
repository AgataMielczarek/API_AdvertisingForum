from django.shortcuts import render
from rest_framework.views import APIView
from ads.models import Advertisement
from .serializers import AdSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.http import Http404



class ListCreateAds(APIView):
    def get(self, request):
        ads = Advertisement.objects.all()
        serializer = AdSerializer(ads, many=True)
        return Response (data=serializer.data)

    def post(self, request):
        serializer = AdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=User.objects.get(is_staff=True))
            return Response (data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST)


class RetrievUpdateDeleteAd(APIView):

    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        ad = self.get_object(pk)
        serializer = AdSerializer(ad)
        return Response (serializer.data)

    def put(self, request, pk):
        ad = self.get_object(pk)
        # check user
        serializer = AdSerializer(instance=ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response (status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk):
        ad = self.get_object(pk)
        ad.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

class DisplayIndustry(APIView):
    try:
        ads = Advertisement.objects.filter(industry=industryKey)
    except ads.DoesNotExist:
        raise Http404
    else:
        pass
        #serializer
        #return Response()

        













