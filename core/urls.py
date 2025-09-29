from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AppointmentViewSet,
    BlogPostViewSet,
    ContactMessageViewSet,
    DoctorViewSet,
    GalleryImageViewSet,
    HealthPackageViewSet,
    PharmacyItemViewSet,
    ServiceViewSet
)

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
router.register(r'blogposts', BlogPostViewSet)
router.register(r'contactmessages', ContactMessageViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'galleryimages', GalleryImageViewSet)
router.register(r'healthpackages', HealthPackageViewSet)
router.register(r'pharmacyitems', PharmacyItemViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]