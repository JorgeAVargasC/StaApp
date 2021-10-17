from rest_framework import serializers
from staApp.models.user import User
from staApp.models.vuelo import Vuelo
from staApp.serializers.vueloSerializer import VueloSerializer

class UserSerializer(serializers.ModelSerializer):
    vuelo = VueloSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'vuelo']

    def create(self, validated_data):
        vueloData = validated_data.pop('vuelo')
        userInstance = User.objects.create(**validated_data)
        Vuelo.objects.create(user=userInstance, **vueloData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        vuelo = Vuelo.objects.get(user=obj.id_vuelo)       
        return {
                    'id': user.id, 
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'vuelo': {
                        'id_vuelo': vuelo.id_vuelo,
                        'nombrePiloto': vuelo.nombrePiloto,
                        'origen': vuelo.origen,
                        'destino': vuelo.destino,
                        'fechaSalida': vuelo.fechaSalida,
                        'fechaLlegada': vuelo.fechaLlegada,
                        'horaSalida': vuelo.horaSalida,
                        'horaLlegada': vuelo.horaLlegada,
                        'cantidadPasajeros': vuelo.cantidadPasajeros,
                    }
                }