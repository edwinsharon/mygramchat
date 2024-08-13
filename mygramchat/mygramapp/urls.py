from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index"),
    path('signin',views.usersignin,name="usersignin"),
    path('createuser',views.usersignup,name="usersignup"),
    path('myfeed',views.myfeed,name="myfeed")

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)