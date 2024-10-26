"""
URL configuration for Cap2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# # Cap2/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('csv/', include('Cap2App.urls')),  # Kiểm tra rằng Cap2App là tên đúng của ứng dụng
# ]


# # Cap2/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('Cap2App.urls')),  # Bao gồm URL từ Cap2App
# ]


from django.contrib import admin
from django.urls import path
from Cap2App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Đảm bảo rằng bạn đã định nghĩa home_view
    path('csv/', views.csv_list_view, name='csv_list'),
    path('csv/<int:pk>/', views.csv_detail_view, name='csv_detail'),
    path('upload/', views.upload_file_view, name='upload_file'),
    path('success/', views.success_page_view, name='success_page'),
    path('download_csv/', views.download_csv, name='download_csv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
