from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import *

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),

    # Patients
    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientDetailView.as_view()),

    # Doctors
    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorDetailView.as_view()),

    # Mappings
    path('mappings/', MappingListView.as_view()),
    path('mappings/<int:pk>/', MappingDeleteView.as_view()),
    path('mappings/patient/<int:patient_id>/', PatientMappingsView.as_view()),
    path('mappings/add/', MappingCreateView.as_view()),
]
