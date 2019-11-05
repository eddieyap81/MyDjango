from django.urls import path
from .views import (
    chair_create_view,
    chair_detail_view,
    chair_update_view,
    chair_delete_view,
    chair_list_view,
)

app_name = 'products'
urlpatterns = [

    path('chair/', chair_list_view, name='chair-list'),
    path('chair/create/', chair_create_view, name='chair-list'),
    path('chair/<int:my_id>/', chair_detail_view, name='chair-detail'),
    path('chair/<int:my_id>/update/', chair_update_view, name='chair-update'),
    path('chair/<int:my_id>/delete/', chair_delete_view, name='chair-delete'),
    #path('initial/', render_initial_data),
    #path('products/<int:my_id>/', dynamic_lookup_view, name='product-id'),
]
