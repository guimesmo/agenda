# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404


from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event
from .serializers import EventSerializer
from .utils import request_filter_factory


class EventsListSet(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        user = self.request.user
        list_filter = request_filter_factory(
            self.request.query_params.get('status'))

        return Event.objects.filter(creation_user=user, status__in=list_filter)

    def post(self, request):
        data = self.request.data
        serializer = EventSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.create(validated_data=serializer.validated_data)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class EventDetail(APIView):

    seerializer_class = EventSerializer

    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk, creation_user=self.request.user)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """Gets event object"""
        event = self.get_object(pk)
        return Response(EventSerializer(event).data)

    def patch(self, request, pk):
        """Update event status"""
        event = self.get_object(pk)
        try:
            event.set_status(request.data.get('status'))
        except ValidationError as e:
            return Response(e.message, status=400)
        event.save()
        return Response(EventSerializer(event))

    def put(self, request, pk):
        """Update event data"""
        serializer = EventSerializer(data=self.request.data, context={'request': request})
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @method_decorator(csrf_exempt)
    def delete(self, request, pk):
        """Cancel event (by changing it status)"""
        event = self.get_object(pk)
        event.cancel()
        event.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
