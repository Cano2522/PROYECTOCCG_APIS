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
        fields = ['idOmc34N5','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','regUsuario','fuenteInf','anioRegInf','fk_Omc34N4']

# SERIALIZERS PARA EL ARBOL
class OMC34Nivel4RelationSerializer(serializers.ModelSerializer):
    children = OMC34Nivel5Serializer(many=True)
    class Meta:
        model = OMC34Nivel4
        fields = ['idOmc34N4','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','regUsuario','fuenteInf','anioRegInf','fk_Omc34N3','children']
                 
class OMC34Nivel3RelationSerializer(serializers.ModelSerializer):
    children = OMC34Nivel4RelationSerializer(many=True)
    class Meta:
        model = OMC34Nivel3
        fields = ['idOmc34N3','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','regUsuario','fuenteInf','anioRegInf','fk_Omc34N2','children']

class OMC34Nivel2RelationSerializer(serializers.ModelSerializer):
    children = OMC34Nivel3RelationSerializer(many=True)
    class Meta:
        model = OMC34Nivel2
        fields = ['idOmc34N2','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc34N1','children']
                
class OMC34Nivel1RelationSerializer(serializers.ModelSerializer):
    children = OMC34Nivel2RelationSerializer(many=True)
    class Meta:
        model = OMC34Nivel1
        fields = ['idOmc34N1','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','children']