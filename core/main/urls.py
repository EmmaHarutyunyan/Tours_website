from django.urls import path,include
from .views import index, tour_detail, gallery, testimonials, about, tours_list, contact
from .import views
urlpatterns = [
    path('', index, name='index'),
    path('tour/<int:tour_id>/', tour_detail, name='tour_detail'),
    path('gallery/<int:tour_id>/', gallery, name='gallery'),
    path('all-galleries/',views.all_galleries, name='all_galleries'),
    path('testimonials/', testimonials, name='testimonials'),
    path('about/', about, name='about'),
    path('tours/', tours_list, name='tours'),
    path('contact/', contact, name='contact'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout_view, name='logout'),
    path('accounts/', include('allauth.urls')),
    path('search/', views.search, name='search'),


]