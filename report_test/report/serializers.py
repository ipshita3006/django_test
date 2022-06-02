from rest_framework import serializers


class UserVisitSerializer(serializers.Serializer):
    policy_id__user_id__name = serializers.CharField()
    count = serializers.IntegerField()
