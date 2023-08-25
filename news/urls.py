from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from rest_framework import routers
from apps.posts.views import NewsViewSet, MediaViewSet, ProfessionsViewSet, ContactViewSet
from apps.users.views import TeamViewSet, StudentViewSet, StakeholderViewSet

router = routers.DefaultRouter()
router.register(r'media', MediaViewSet)
router.register(r'news', NewsViewSet)
router.register(r'professions', ProfessionsViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'students', StudentViewSet)
router.register(r'stakeholder', StakeholderViewSet)
router.register(r'contacts', ContactViewSet)

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('news/', include('apps.posts.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api/', include(router.urls)),
    path('',RedirectView.as_view(url='/api/')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
