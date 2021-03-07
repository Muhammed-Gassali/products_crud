
from django.contrib import admin
from django.urls import path,include,re_path

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Products operations",
        default_version='v1',
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="creativepanda@gmail.com"),
        license=openapi.License(name="ALL API ENDPOINTS"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ends here

# schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud.url')),
    # url(r'^docs/', schema_view),
    re_path(r'^doc(?P<format>\.json|\.yaml)$',schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc')


    # path('docs/', TemplateView.as_view(template_name='documentation.html',extra_context={'schema_url':'openapi-schema'}), name='swagger-ui'),
    # path('openapi/', get_schema_view(
    #     title="School Service",
    #     description="API developers hpoing to use our service"
    # ), name='openapi-schema'),
    
]
