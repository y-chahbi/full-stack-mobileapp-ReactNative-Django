from django.contrib             import admin
from django.urls                import path
from user                       import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('getallusers/', views.getAllUsers),
    path('handelRequest/', views.userData)
]
