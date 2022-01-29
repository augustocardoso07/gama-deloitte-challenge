from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('members', views.MemberView)
router.register('posts', views.PostView)
router.register('services', views.ServiceView)

urlpatterns = [
    path('', include(router.urls))
]
