from staApp.models.vuelo import Vuelo
from rest_framework import serializers

class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelo
        fields = [
            'id_vuelo',
            'nombrePiloto',
            'origen',
            'destino',
            'fechaSalida',
            'fechaLlegada',
            'horaSalida',
            'horaLlegada',
            'cantidadPasajeros',
        ]