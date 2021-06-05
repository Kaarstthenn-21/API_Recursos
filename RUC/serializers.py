from rest_framework import serializers
from .models import RUC

class RazonSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RUC
        fields = ('id','rucEmpresa','nombreEmpresa','estado','tipoEmpresa','rutaRUC','titular','identificacion')

    id= serializers.IntegerField(read_only=True)
    rucEmpresa = serializers.CharField()
    nombreEmpresa = serializers.CharField()
    estado = serializers.CharField()
    tipoEmpresa = serializers.CharField()
    rutaRUC = serializers.CharField()
    titular = serializers.CharField()
    identificacion = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return RUC.objects.create(**validated_data)
    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.rucEmpresa = validated_data.get('rucEmpresa',instance.rucEmpresa)
        instance.nombreEmpresa=validated_data.get('nombreEmpresa',instance.nombreEmpresa)
        instance.estado = validated_data.get('estado',instance.estado)
        instance.tipoEmpresa = validated_data.get('tipoEmpresa',instance.tipoEmpresa)
        instance.rutaRUC=validated_data.get('rutaRUC',instance.rutaRUC)
        instance.titular = validated_data.get('titular',instance.titular)
        instance.identificacion = validated_data.get('identificacion',instance.identificacion)
        instance.save()
        return instance