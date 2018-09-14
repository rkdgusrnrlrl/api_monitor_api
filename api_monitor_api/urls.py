"""api_monitor_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from state_monitor import views

router = routers.SimpleRouter()
router.register(r'applications', views.ApplicationViewSet)

application_router = routers.NestedSimpleRouter(router, r'applications', lookup='application')
application_router.register(r'apis', views.APIViewSet, base_name='apis')


api_router = routers.NestedSimpleRouter(application_router, r'apis', lookup='api')
api_router.register(r'status', views.APIStatusVeiwSet, base_name="status")


urlpatterns = [
    path(r'api/', include(router.urls)),
    path(r'api/', include(application_router.urls)),
    path(r'api/', include(api_router.urls)),
    path(r'auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
