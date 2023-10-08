from django.urls import path
from menu.views import index, index_pk

urlpatterns = [
    path('', index, name='index'),
    path('<pk>', index_pk, name='index_pk')
]