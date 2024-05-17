from rest_framework import serializers
from .models import Student, FunnelStatus, StatusLog

class FunnelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunnelStatus
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StatusLogSerializer(serializers.ModelSerializer):
    student = serializers.CharField(source='student.name')
    from_status = serializers.SerializerMethodField()
    to_status = serializers.SerializerMethodField()

    class Meta:
        model = StatusLog
        fields = '__all__'

    def get_from_status(self, obj):
        return getattr(obj.from_status, 'name', None)

    def get_to_status(self, obj):
        return getattr(obj.to_status, 'name', None)


