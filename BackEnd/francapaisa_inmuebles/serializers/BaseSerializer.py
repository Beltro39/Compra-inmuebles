from rest_framework import serializers as serializers

class BaseSerializer (serializers.ModelSerializer):

    class Meta:

        fields           = []

        read_only_fields = []
