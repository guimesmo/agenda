# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from .models import Event
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):

    date = serializers.DateField(input_formats=settings.DATE_INPUT_FORMATS,
        write_only=True)
    time = serializers.TimeField(write_only=True)

    class Meta:
        model = Event
        fields = (
            'id', 'name', 'datetime_repr', 'date', 'time',
            'status',)
        read_only_fields = ('id', 'datetime_repr', 'status')

    def validate(self, data):
        if None not in (data.get('date'), data.get('time'),):
            data['event_datetime'] = datetime.datetime.combine(
                data['date'],
                data['time']
                )
        else:
            raise serializers.ValidationError("Data e hora são obrigatórios")
        return data

    def create(self, validated_data):
        return Event.objects.create(
            creation_user=self.context['request'].user,
            datetime=validated_data['event_datetime'],
            name=validated_data['name']
        )

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
