from rest_framework import serializers
from omniclass35.models import (
    OMC35Nivel1,
    OMC35Nivel2,
    OMC35Nivel3,
    OMC35Nivel4,
    OMC35Nivel5,
    OMC35Nivel6,
)

class OMC35Nivel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel1
        fields = ['idOmc35N1','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','fk_EnvOMC']

class OMC35Nivel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel2
        fields = ['idOmc35N2','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','fk_Omc35N1']

class OMC35Nivel3Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel3
        fields = ['idOmc35N3','cveHe','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc35N2']

class OMC35Nivel4Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel4
        fields = ['idOmc35N4','cveHe','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc35N3']

class OMC35Nivel5Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel5
        fields = ['idOmc35N5','cveHe','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc35N4']

class OMC35Nivel6Serializer(serializers.ModelSerializer):
    class Meta:
        model = OMC35Nivel6
        fields = ['idOmc35N6','cveHe','codigo','descriEng','descriSpa','definicionEng','definicionSpa','anioReg','regFinal','fk_Omc35N5']