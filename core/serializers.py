from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Advertisement,
    Appointment,
    BlogPost,
    CheckupPackage,
    ContactMessage,
    Doctor,
    GalleryImage,
    HealthPackage,
    PharmacyItem,
    Service
)

class AppointmentSerializer(serializers.ModelSerializer):
    date = serializers.DateField(write_only=True, required=True)
    time = serializers.TimeField(write_only=True, required=True)
    reason = serializers.CharField(required=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient_name', 'doctor_name', 'reason', 'status', 'date', 'time']

    def create(self, validated_data):
        date = validated_data.pop('date', None)
        time = validated_data.pop('time', None)
        if date and time:
            from datetime import datetime
            validated_data['appointment_date'] = datetime.combine(date, time)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        date = validated_data.pop('date', None)
        time = validated_data.pop('time', None)
        if date and time:
            from datetime import datetime
            validated_data['appointment_date'] = datetime.combine(date, time)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if hasattr(instance, 'appointment_date') and instance.appointment_date:
            representation['date'] = instance.appointment_date.date()
            representation['time'] = instance.appointment_date.time()
        else:
            representation['date'] = None
            representation['time'] = None
        return representation

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class CheckupPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckupPackage
        fields = '__all__'

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'

class HealthPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthPackage
        fields = '__all__'

class PharmacyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyItem
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
