from rest_framework import serializers
from rolesorg.models import RolesOrg

class RolesOrgSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesOrg
        fields = ['idRolOrg','cveMo','codigo','consecutivo','descriEng','descriSpa','definicionEng','definicionSpa','fuenteInf','fecRegInf']
