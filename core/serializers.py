from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Appointment,
    BlogPost,
    ContactMessage,
    Doctor,
    GalleryImage,
    HealthPackage,
    PharmacyItem,
    Service
)

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
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

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
