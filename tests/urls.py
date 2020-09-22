# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from nobinobi_core import urls as nobinobi_core_urls
from nobinobi_staff import urls as nobinobi_staff_urls

from nobinobi_child import urls as nobinobi_child_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(nobinobi_core_urls, namespace="nobinobi_core")),
    path('', include(nobinobi_staff_urls, namespace="nobinobi_staff")),
    path('', include(nobinobi_child_urls, namespace="nobinobi_child")),
    path('select2/', include('django_select2.urls')),

]
