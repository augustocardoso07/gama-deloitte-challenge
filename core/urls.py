from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Portal da Cronos API"
admin.site.index_title = "Administração do banco de dados da Cronos API"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cronosapi/', include('cronosapi.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
