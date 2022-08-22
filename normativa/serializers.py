from rest_framework import serializers
from normativa.models import Normativa

class NormativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Normativa
        fields = ['idNormativa','nombreSpa', 'nombreEng', 'fk_Acronimo']
