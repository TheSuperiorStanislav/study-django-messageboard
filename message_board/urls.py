from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path('messageboard/',include('posts.urls')),
    path('blog/',include('blog.urls')),
    path('',include('blog.urls'))
]
