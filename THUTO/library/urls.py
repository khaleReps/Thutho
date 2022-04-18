from django.urls import path
from . import views


urlpatterns = [
path('library-development', views.development, name='library-development'),
path('library-featured', views.featured, name='library-featured'),
path('library-filters-development', views.filters_development, name='library-filters-development'),
path('library-filters-development-list', views.filters_development_list, name='library-filters-development_list'),
path('library-filters', views.filters, name='library-filters'),
path('library-filters-list', views.filters_list, name='library-filters-list'),
path('library', views.library, name='library'),

]