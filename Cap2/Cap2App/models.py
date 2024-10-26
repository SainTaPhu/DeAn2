# Cap2App/models.py
from django.db import models


class CSVData(models.Model):
    file_path = models.CharField(max_length=255)  # Lưu đường dẫn file
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_path
