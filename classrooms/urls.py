
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from api.views import ClassroomList , ClassroomDetail, ClassroomCreate, ClassroomUpdate, ClassroomDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    
    path('classrooms/api/', ClassroomList.as_view() , name='api-classroom-list'),
    path('classrooms/api/detail/<int:classroom_id>/', ClassroomDetail.as_view() , name='api-classroom-detail'),
    path('classrooms/api/update/<int:classroom_id>/', ClassroomUpdate.as_view() , name='api-classroom-update'),
    path('classrooms/api/delete/<int:classroom_id>/', ClassroomDelete.as_view() , name='api-classroom-delete'),
    path('classrooms/api/create/', ClassroomCreate.as_view() , name='api-classroom-create'),

    path('api/token/', TokenObtainPairView.as_view(), name='login'),
    

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
