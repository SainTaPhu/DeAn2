# # Cap2App/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('upload/', views.upload_file_view, name='upload_file'),
#     path('list/', views.csv_list_view, name='csv_list'),
#     path('detail/<int:pk>/', views.csv_detail_view, name='csv_detail'),
# ]


# from django.urls import path
# from .views import upload_view, list_view  # Đảm bảo bạn đã import view tương ứng

# urlpatterns = [
#     path('', upload_view, name='upload'),  # Đường dẫn csv/ trỏ đến upload_view
#     path('upload/', upload_view, name='upload'),  # Đường dẫn csv/upload/ trỏ đến upload_view
#     path('list/', list_view, name='list'),  # Đường dẫn csv/list/ trỏ đến list_view
# ]


# # Cap2App/urls.py
# from django.urls import path
# from .views import upload_file_view, csv_list_view, csv_detail_view

# urlpatterns = [
#     path('upload/', upload_file_view, name='csv_upload'),  # Đường dẫn để tải lên tệp CSV
#     path('list/', csv_list_view, name='csv_list'),         # Đường dẫn để xem danh sách bản ghi CSV
#     path('detail/<int:pk>/', csv_detail_view, name='csv_detail'),  # Đường dẫn để xem chi tiết bản ghi
# ]



# # Cap2App/urls.py
# from django.urls import path
# from .views import upload_file_view, csv_list_view, csv_detail_view

# urlpatterns = [
#     path('upload/', upload_file_view, name='upload_file'),
#     path('list/', csv_list_view, name='csv_list'),
#     path('detail/<int:pk>/', csv_detail_view, name='csv_detail'),
# ]



# # Cap2App/urls.py
# from django.urls import path
# from .views import upload_file_view, csv_list_view, csv_detail_view

# urlpatterns = [
#     path('upload/', upload_file_view, name='upload_file'),
#     path('csv/', csv_list_view, name='csv_list'),
#     path('csv/<int:pk>/', csv_detail_view, name='csv_detail'),
# ]


# Cap2App/urls.py
from django.urls import path
from .views import upload_file_view, csv_list_view, csv_detail_view, home_view

urlpatterns = [
    path('', home_view, name='home'),  # Đường dẫn cho trang chính
    path('upload/', upload_file_view, name='upload_file'),
    path('csv/', csv_list_view, name='csv_list'),  # Danh sách CSV
    path('csv/<int:pk>/', csv_detail_view, name='csv_detail'),
]




