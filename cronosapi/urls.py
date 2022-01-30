from django.urls import path, include, re_path
from . import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register('members', views.MemberView)
router.register('posts', views.PostView)
router.register('services', views.ServiceView)


apipatters = [
    path('', include(router.urls)),
]

schema = get_swagger_view(
    title="Documentação da Cronos API", url='/cronosapi', patterns=apipatters)

urlpatterns = apipatters + [
    re_path('docs', schema),
]
