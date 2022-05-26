from django.contrib import admin
from django.urls import path, include
from blog.views import post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path("post/<slug>/", post_detail, name="blog-post-detail"),

]
