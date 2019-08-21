from django.urls import path, include

urlpatterns = [
    path('user/', include('api.user.urls')),
    path('idea/', include('api.idea.urls'))

]