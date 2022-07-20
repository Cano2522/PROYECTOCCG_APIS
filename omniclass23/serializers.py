from rest_framework import serializers, pagination
from omniclass23.models import (
    OMC23Nivel1,
    OMC23Nivel2,
    OMC23Nivel3,
    OMC23Nivel4,
    OMC23Nivel5,
    OMC23Nivel6,
)

class OMC23Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel1
        fields = ['idOmc23N1','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','ejemploEng','ejemploSpa','anioReg']

class OMC23Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel2
        fields = ['idOmc23N2','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','ejemploEng','ejemploSpa','regFinal','anioReg','regUsuario','fk_Omc23N1']

class OMC23Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel3
        fields = ['idOmc23N3','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','ejemploEng','ejemploSpa','anioReg','regFinal','regUsuario','fk_Omc23N2']

class OMC23Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel4
        fields = ['idOmc23N4','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','ejemploEng','ejemploSpa','anioReg','regFinal','regUsuario','fk_Omc23N3']

class OMC23Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel5
        fields = ['idOmc23N5','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','ejemploEng','ejemploSpa','anioReg','regFinal','regUsuario','fk_Omc23N4']

class OMC23Nivel6Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC23Nivel6
        fields = ['idOmc23N6','numMat','Codigo','descriEng','descriSpa','definicionEng','definicionSpa','ejemploEng','ejemploSpa','anioReg','regFinal','regUsuario','fk_Omc23N5']