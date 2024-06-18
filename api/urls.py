from django.urls import include, path
from rest_framework import routers

from api import views


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
    openapi.Info(
        title="Garage API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"garage", views.GarageViewSet, basename="garage")
router.register(r"client", views.ClientViewSet, basename="client")
router.register(r"service", views.ServiceViewSet, basename="service")
router.register(r"scheduler", views.SchedulerViewSet, basename="scheduler")
router.register(r"carmechanic", views.SchedulerViewSet, basename="carmechanic")

urlpatterns = [
    path("", include(router.urls)),
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
