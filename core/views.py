from rest_framework import viewsets, generics
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
from .serializers import (
    AdvertisementSerializer,
    AppointmentSerializer,
    BlogPostSerializer,
    CheckupPackageSerializer,
    ContactMessageSerializer,
    DoctorSerializer,
    GalleryImageSerializer,
    HealthPackageSerializer,
    PharmacyItemSerializer,
    ServiceSerializer,
    UserSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class CheckupPackageViewSet(viewsets.ModelViewSet):
    queryset = CheckupPackage.objects.all()
    serializer_class = CheckupPackageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset = GalleryImage.objects.all()
    serializer_class = GalleryImageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class HealthPackageViewSet(viewsets.ModelViewSet):
    queryset = HealthPackage.objects.all()
    serializer_class = HealthPackageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class PharmacyItemViewSet(viewsets.ModelViewSet):
    queryset = PharmacyItem.objects.all()
    serializer_class = PharmacyItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
