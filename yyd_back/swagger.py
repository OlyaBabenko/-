from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from .api_urls import urlpatterns


SchemaView = get_schema_view(
    openapi.Info(
        title="DeliveryApp",
        default_version="v1",
        description="Here you can see the endpoints of our api server. Below is a catalog of possible requests to the "
        "server where there are types of requests, names of views, their description, data necessary for "
        "the execution of functions, documentation of answers. It is possible to test the endpoint",
        # contact=openapi.Contact(email="contact@yourapp.com"),
        # terms_of_service="https://www.yourapp.com/terms/",
        # license=openapi.License(name="Your License"),
    ),
    public=True,
    patterns=[path("", include(urlpatterns))],
)
