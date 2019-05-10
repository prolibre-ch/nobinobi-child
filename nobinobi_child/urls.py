# -*- coding: utf-8 -*-
import django.contrib.auth.views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'nobinobi_child'

router = DefaultRouter()
router.register(r'child', views.ChildViewSet, base_name="api-child")
router.register(r'absence', views.AbsenceViewSet, base_name="api-absence")

urlpatterns = [
                  path('api/', include(router.urls)),
                  path('accounts/login/', views.AuthLoginView.as_view(), name='login_view'),
                  path('accounts/logout/',
                       auth_views.LogoutView.as_view(template_name='nobinobi_child/pages/login/logout.html'),
                       name='logout_view'),
                  path("", views.HomeView.as_view(), name="home"),
                  # child
                  path("child/", include([
                      path("child/", include([
                          path("",
                               view=views.ChildListView.as_view(),
                               name='Child_list'
                               ),
                          path("~create/",
                               view=views.ChildCreateView.as_view(),
                               name='Child_create'
                               ),
                          path("<uuid:pk>/", include([
                              path("",
                                   view=views.ChildDetailView.as_view(),
                                   name='Child_detail'),
                              path("~delete/",
                                   view=views.ChildDeleteView.as_view(),
                                   name='Child_delete'),
                              path("~update/",
                                   view=views.ChildUpdateView.as_view(),
                                   name='Child_update'),
                          ])
                               ),
                      ])),
                      path("iotd/", include([
                          path("",
                               view=views.InformationOfTheDayListView.as_view(),
                               name='InformationOfTheDay_list'
                               ),
                          path("<int:pk>/", include([
                              path("",
                                   view=views.InformationOfTheDayDetailView.as_view(),
                                   name='InformationOfTheDay_detail'),
                          ])),
                      ])),
                      path("absence/", include([
                          path("",
                               view=views.AbsenceListView.as_view(),
                               name='Absence_list'
                               ),
                          path("~create/",
                               view=views.AbsenceCreateView.as_view(),
                               name='Absence_create'
                               ),
                          path("<int:pk>/", include([
                              path("",
                                   view=views.AbsenceDetailView.as_view(),
                                   name='Absence_detail'),
                              path("~delete/",
                                   view=views.AbsenceDeleteView.as_view(),
                                   name='Absence_delete'),
                              path("~update/",
                                   view=views.AbsenceUpdateView.as_view(),
                                   name='Absence_update'),
                          ])),
                      ])),
                  ])),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
