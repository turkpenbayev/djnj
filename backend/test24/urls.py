from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from new_app.views import *

urlpatterns = [
    url('admin/', admin.site.urls),
    url('.*', TemplateView.as_view(template_name="home.html"), name="home")
]