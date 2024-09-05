from rest_framework import serializers
from . models import *

class OfficeSerlializer(serializers.ModelSerializer):

    class Meta:
        model = Office
        fields = '__all__'


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    issue = serializers.CharField(read_only=True)

    class Meta:
        model = Asset
        fields = '__all__'
        extra_fields = ('issue')


    def get_divion_name(self, obj):
        return obj.issue.name

class MaintananceSerializer(serializers.ModelSerializer):

    class Meta:
        models = Maintainance
        fields = '__all__'