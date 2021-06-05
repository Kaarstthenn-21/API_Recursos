from django.db.models import fields
from rest_framework import serializers
from .models import DNI

class DNISerializer(serializers.Serializer):
    
    id = serializers.IntegerField(read_only=True)
    dni = serializers.CharField()
    nombres = serializers.CharField()
    apellidos = serializers.CharField()

    def create(self, validated_data):
        return DNI.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dni = validated_data.get('dni' , instance.dni)
        instance.nombres = validated_data.get('nombres' , instance.nombres)
        instance.apellidos = validated_data.get('apellidos' , instance.apellidos)
        instance.save()
        return instance

    class Meta:
        model = DNI
        fields = ('id' , 'dni' , 'nombres' , 'apellidos')
