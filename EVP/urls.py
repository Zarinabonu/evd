
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('User.urls')),
    path('api/', include('api.urls')),
    path('idea/', include('Idea.urls')),

]
