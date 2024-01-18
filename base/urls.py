from django.contrib.auth.decorators import login_required
from django.urls import path

from .ajax import ComboUpdateView
from .views import (
    CalendarTemplateView,
    Error403TemplateView,
    HomeTemplateView,
    SurveyFormView,
    WomDayArchiveView,
    WomCreateView,
    WomDeleteView,
    WomListView,
    WomUpdateView,
)

app_name = 'base'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('error-403/', Error403TemplateView.as_view(), name='error_403'),

    path('wom/', WomListView.as_view(), name='wom_list'),
    path('wom/create/', WomCreateView.as_view(), name='wom_create'),
    path('wom/update/<int:pk>/', WomUpdateView.as_view(), name='wom_update'),
    path('wom/delete/<int:pk>/', WomDeleteView.as_view(), name='wom_delete'),
    path(
        'wom/<int:year>/<int:month>/<int:day>/',
        WomDayArchiveView.as_view(), name='archive_day'
    ),
    path('surveys/upload/', SurveyFormView.as_view(), name='survey_upload'),
    path('calendar/', login_required(CalendarTemplateView.as_view()), name='calendar'),

    path(
        'ajax/combo-update/', login_required(ComboUpdateView.as_view()),
        name='combo_update'
    ),
]
