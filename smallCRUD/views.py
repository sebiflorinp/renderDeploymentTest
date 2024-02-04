from .models import Country
from .serializers import CountrySerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class ListCountries(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateContry(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)