from rest_framework import serializers
from omniclass41.models import (
    OMC41Nivel1,
    OMC41Nivel2,
    OMC41Nivel3,
    OMC41Nivel4,
    OMC41Nivel5,
    OMC41Nivel6,
)

class OMC41Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel1
        fields = ['idOmc41N1','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg']

class OMC41Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel2
        fields = ['idOmc41N2','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','fk_Omc41N1']

class OMC41Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel3
        fields = ['idOmc41N3','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc41N2']

class OMC41Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel4
        fields = ['idOmc41N4','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc41N3']

class OMC41Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel5
        fields = ['idOmc41N5','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc41N4']

class OMC41Nivel6Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC41Nivel6
        fields = ['idOmc41N6','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc41N5']