from rest_framework import serializers
from omniclass34.models import (
    OMC34Nivel1,
    OMC34Nivel2,
    OMC34Nivel3,
    OMC34Nivel4,
    OMC34Nivel5,
)

class OMC34Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel1
        fields = ['idOmc34N1','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg']

class OMC34Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel2
        fields = ['idOmc34N2','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc34N1']

class OMC34Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel3
        fields = ['idOmc34N3','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','regUsuario','fuenteInf','anioRegInf','fk_Omc34N2']

class OMC34Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel4
        fields = ['idOmc34N4','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','regUsuario','fuenteInf','anioRegInf','fk_Omc34N3']

class OMC34Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC34Nivel5
        fields = ['idOmc34N5','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','regUsuario','fuenteInf','anioRegInf','fk_Omc34N4']