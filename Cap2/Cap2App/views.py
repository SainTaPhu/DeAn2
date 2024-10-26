import csv
import os

from django.contrib import messages
from django.http import FileResponse, Http404

from .forms import CSVUploadForm
from .models import CSVData  # Đảm bảo bạn đã import CSVData


def upload_file_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']

            # Define the path and create directories if necessary
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
            print('upload_dir', upload_dir)
            os.makedirs(upload_dir, exist_ok=True)  # Creates the directory if it doesn't exist

            # Full path for saving the uploaded file
            csv_file_path = os.path.join(upload_dir, csv_file.name)
            print('csv_file_path', csv_file_path)
            # Save the file
            with open(csv_file_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)
            # Lưu đường dẫn file vào cơ sở dữ liệu
            CSVData.objects.create(file_path=f'uploads/{csv_file.name}')
            # Show a success message
            messages.success(request, "Dữ liệu đã được xử lý thành công!")

            # Redirect to success page
            # return redirect('../success')
            return render(request, 'Cap2App/success.html', {'csv_file_path': csv_file_path})

    else:
        form = CSVUploadForm()

    return render(request, 'Cap2App/upload.html', {'form': form})


def csv_list_view(request):
    csv_files = CSVData.objects.all()
    return render(request, 'Cap2App/csv_list.html', {'csv_files': csv_files})


def csv_detail_view(request, pk):
    csv_file = get_object_or_404(CSVData, pk=pk)  # Fetch CSV file from DB by primary key
    file_path = csv_file.file_path  # Path stored in database
    data = []

    # Open and read the CSV file
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    with open(full_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)  # Append each row to data

    # Pass CSV content to template
    return render(request, 'Cap2App/csv_detail.html', {'csv_file': csv_file, 'data': data})


# Cap2App/views.py
from django.shortcuts import render, get_object_or_404
from django.conf import settings


def home_view(request):
    # Không cần gọi đến get_template_loaders()
    return render(request, 'Cap2App/home.html')


def success_page_view(request):
    # Lấy đường dẫn file CSV từ GET parameters
    print('request', request.GET.get('csv_file_path'))
    csv_file_path = request.GET.get('csv_file_path')
    return render(request, 'Cap2App/success.html', {'csv_file_path': csv_file_path})


def download_csv(request):
    # Get the file path from the URL parameters
    file_path = request.GET.get('file')

    # Construct the full file path
    full_file_path = os.path.join(settings.BASE_DIR, file_path)

    # Check if the file exists
    if os.path.exists(full_file_path):
        # Serve the file as a response
        return FileResponse(open(full_file_path, 'rb'), as_attachment=True, filename=os.path.basename(full_file_path))
    else:
        raise Http404("File not found")
