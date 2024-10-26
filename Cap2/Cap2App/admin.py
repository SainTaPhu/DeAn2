
# Cap2App/admin.py
from django.contrib import admin
from .models import CSVData

@admin.register(CSVData)
class CSVDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_path',)  # Hiển thị các trường bạn muốn trong danh sách
    search_fields = ('file_path',)  # Cho phép tìm kiếm theo trường name

