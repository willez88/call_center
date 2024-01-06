from django.contrib.auth.decorators import login_required
from django.urls import path

from .ajax import ComboUpdateView
from .views import (
    Error403TemplateView,
    HomeTemplateView,
    WomCreateView,
    WomDeleteView,
    WomListView,
    WomUpdateView,
)

app_name = 'base'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('error-403/', Error403TemplateView.as_view(), name='error_403'),

    path('wom/list/', WomListView.as_view(), name='wom_list'),
    path('wom/create/', WomCreateView.as_view(), name='wom_create'),
    path('wom/update/<int:pk>/', WomUpdateView.as_view(), name='wom_update'),
    path('wom/delete/<int:pk>/', WomDeleteView.as_view(), name='wom_delete'),

    path(
        'ajax/combo-update/', login_required(ComboUpdateView.as_view()),
        name='combo_update'
    ),
]
