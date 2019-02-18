from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messageboard/',include('posts.urls')),
    path('blog/',include('blog.urls'))
]
