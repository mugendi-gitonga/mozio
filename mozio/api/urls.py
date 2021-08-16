from django.urls import path
from .views import *

urlpatterns = [

    path('', get_providers, name='get-providers'),
    path('get_all_providers/', get_all_providers, name='get-all-providers'), 
    path('get_all_providers/<str:provider_id>/', provider_details, name='provider'),
    path('create_provider/', create_provider, name='create-provider'),

    path('get_all_polygons/<str:provider>/', get_all_polygons, name='get-all-polygons'),
    path('create_polygon/<str:provider>/', create_polygon, name='create-polygon'),
    path('update_polygon/<str:polygon>/', update_polygon, name='update-polygon'),
    path('delete_polygon/<str:polygon>/', delete_polygon, name='delete-polygon'),

    path('nearest/<str:lat>/<str:lon>/', nearest_providers, name='nearest-providers'),

]