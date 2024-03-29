from django.urls import path
from . import views


urlpatterns = [
    path('add-experience/', views.AddExperience, name="AddExperience"),
    path('view-experience/', views.ViewExperience, name="ViewExperience"),
    path('update-experience/', views.UpdateExperience, name="UpdateExperience"),
    path('delete-experience/', views.DeleteExperience, name="DeleteExperience"),
    path('view-qualification/', views.ViewQualification, name="ViewQualification"),
    path('update-qualification/', views.UpdateQualification, name="ViewQualification"),
    path('view-doctor-info/', views.ViewDoctorInfo, name="ViewDoctorInfo"),
    path('change-doctor-profile-photo/', views.ChangeDoctorProfilePic, name="ChangeDoctorProfilePic"),
    path('view-personal-info/', views.ViewPersonalInfo, name="ViewPersonalInfo"),
    path('update-personal-info/', views.UpdatePersonalInfo, name="UpdatePersonalInfo"),
    path('update-doctor-info/', views.UpdateDoctorlInfo, name="UpdateDoctorlInfo"),
    path('add-category/', views.AddCategory, name="AddCategory"),
    path('view-category/', views.ViewCategory, name="SearchCategory"),
    path('search-category/<str:name>', views.SearchCategory, name="SearchCategory"),
    
]
