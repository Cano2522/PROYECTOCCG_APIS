from rest_framework import serializers
from unidadesmedida.models import (
    TipoUniMed,
    SubTipUni,
    UnidadesMedida,
)

class TipoUniMedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUniMed
        fields = ['idTum','tipo']

class SubTipUniSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTipUni
        fields = ['idStu','subtipo','fk_Tum']

class UnidadesMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadesMedida
        fields = ['idUniMed','cveSat','unidad','descripcion','sistema','fk_Stu']

