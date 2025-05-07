from django.urls import path
from . import views
from .views import EnquiryListCreateView

urlpatterns = [
    path('', views.index, name='landing-page'),
    path('service/', views.service, name='service'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add/', views.add_service, name='add_service'),
    path('dashboard/edit/<int:pk>/', views.edit_service, name='edit_service'),
    path('dashboard/delete/<int:pk>/',views.delete_service, name='delete_service'),
    path('api/enquiries/', EnquiryListCreateView.as_view(), name='enquiry-list-create'),
]
