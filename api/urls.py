from django.urls import path,include
from . import views


urlpatterns=[  
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('create/',views.create_post),
    path('stories/',views.get_post),
    path('user/',views.user_stories),
    path('edit/<int:pk>/',views.update_post)

]