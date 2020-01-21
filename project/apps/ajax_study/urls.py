from django.urls import path
from apps.ajax_study.views import LoginView,ReceiveView

app_name = 'ajax_study'

urlpatterns = [
    path('login/',LoginView.as_view(),name='ajax_study'),
    path('rece/',ReceiveView.as_view(),name='receive'),
]