from django.urls import path, include
from django.views.generic import TemplateView
# from .routers import router
from .routers import router

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/', include(router.urls))
]