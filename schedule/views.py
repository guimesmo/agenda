# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import Http404

from rest_framework.renderers import JSONRenderer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event
from .serializers import EventSerializer
from .utils import request_filter_factory


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class EventsListSet(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        list_filter = request_filter_factory(
            self.request.query_params.get('status'))

        return Event.objects.filter(creation_user=user, status__in=list_filter)

    def put(self, request):
        data = self.request.data
        serializer = EventSerializer(data)
        if serializer.is_valid():
            serializer.create()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status_code=400)


class EventDetail(APIView):

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk, creation_user=self.request.user)
        except Event.DoesNotExist:
            raise Http404

    def post(self, request, pk):
        data = self.request.data
        serializer = EventSerializer(data)
        if serializer.is_valid():
            serializer.update()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status_code=400)

    def delete(self, request, pk):
        event = self.get_object(pk, user=request.user)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
