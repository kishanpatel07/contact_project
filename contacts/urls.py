
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('contact/login',include('django.contrib.auth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#setting admin site...
admin.site.site_title='Control Panel'
admin.site.site_header='Contacts'
admin.site.index_title='Welcome to Project'

