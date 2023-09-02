from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from rest_framework import routers


router = routers.DefaultRouter()


api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('component/', include('apps.component.urls')),
    path('person/', include('apps.person.urls')),
    path('applications/', include("apps.applications.urls")),
    

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api/', include(router.urls)),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('',RedirectView.as_view(url='/api/')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
