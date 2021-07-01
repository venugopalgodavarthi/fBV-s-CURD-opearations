from django.urls import path
from product import views
from onlineshop import settings
from django.conf.urls.static import static
my_app="product"

urlpatterns = [
    path('createp/',views.createproduct,name="createp"),
    path('readp/',views.readproduct,name="readp"),
    path('modifyp/<id>',views.modifyproduct,name="modifyp"),
    path('deletep/<id>',views.deleteproduct,name="deletep"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)