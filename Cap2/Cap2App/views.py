# # from django.shortcuts import render

# # # Create your views here.
# # # Cap2App/views.py
# # import csv
# # from django.shortcuts import render, redirect, get_object_or_404
# # from .models import CSVData
# # from .forms import CSVUploadForm

# # def upload_file_view(request):
# #     if request.method == "POST":
# #         form = CSVUploadForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             file = request.FILES['file']
# #             decoded_file = file.read().decode('utf-8').splitlines()
# #             reader = csv.reader(decoded_file)
# #             for row in reader:
# #                 CSVData.objects.create(name=row[0], value=int(row[1]))  # Adjust indices as per your CSV format
# #             return redirect('csv_list')
# #     else:
# #         form = CSVUploadForm()
# #     return render(request, 'Cap2App/upload.html', {'form': form})

# # def csv_list_view(request):
# #     csv_data = CSVData.objects.all()
# #     return render(request, 'Cap2App/csv_list.html', {'csv_data': csv_data})

# # def csv_detail_view(request, pk):
# #     csv_record = get_object_or_404(CSVData, pk=pk)
# #     return render(request, 'Cap2App/csv_detail.html', {'csv_record': csv_record})



# # Cap2App/views.py
# import csv
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import CSVData
# from .forms import CSVUploadForm

# def upload_file_view(request):
#     """Xử lý việc tải lên tệp CSV."""
#     if request.method == "POST":
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
#             decoded_file = file.read().decode('utf-8').splitlines()
#             reader = csv.reader(decoded_file)
#             # Bỏ qua tiêu đề nếu có
#             next(reader, None)  # Bỏ qua hàng đầu tiên nếu có tiêu đề
#             for row in reader:
#                 # Tạo đối tượng CSVData từ từng hàng trong tệp CSV
#                 CSVData.objects.create(name=row[0], value=int(row[1]))  # Điều chỉnh chỉ số theo định dạng CSV của bạn
#             return redirect('csv_list')  # Chuyển hướng đến danh sách CSV sau khi tải lên thành công
#     else:
#         form = CSVUploadForm()
#     return render(request, 'Cap2App/upload.html', {'form': form})

# def csv_list_view(request):
#     """Hiển thị danh sách các bản ghi CSV."""
#     csv_data = CSVData.objects.all()  # Lấy tất cả dữ liệu từ model CSVData
#     return render(request, 'Cap2App/csv_list.html', {'csv_data': csv_data})

# def csv_detail_view(request, pk):
#     """Hiển thị chi tiết một bản ghi CSV cụ thể."""
#     csv_record = get_object_or_404(CSVData, pk=pk)  # Lấy bản ghi theo primary key
#     return render(request, 'Cap2App/csv_detail.html', {'csv_record': csv_record})




# # Cap2App/views.py
# from django.shortcuts import render, redirect
# import csv
# from .models import CSVData
# from .forms import CSVUploadForm


# def upload_file_view(request):
#     if request.method == "POST":
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
#             decoded_file = file.read().decode('utf-8').splitlines()
#             reader = csv.reader(decoded_file)
#             for row in reader:
#                 CSVData.objects.create(name=row[0], value=int(row[1]))  # Adjust indices as per your CSV format
#             return redirect('csv_list')  # Đảm bảo bạn đã định nghĩa url với name 'csv_list'
#     else:
#         form = CSVUploadForm()
#     return render(request, 'Cap2App/upload.html', {'form': form})







# # Cap2App/views.py
# from django.shortcuts import render, redirect
# import csv
# from .models import CSVData  # Đảm bảo bạn đã import CSVData
# from .forms import CSVUploadForm


# def upload_file_view(request):
#     if request.method == "POST":
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = request.FILES['file']
#             decoded_file = file.read().decode('utf-8').splitlines()
#             reader = csv.reader(decoded_file)
#             for row in reader:
#                 CSVData.objects.create(name=row[0], value=int(row[1]))  # Điều chỉnh chỉ số theo định dạng CSV của bạn
#             return redirect('csv_list')  # Đảm bảo bạn đã định nghĩa URL với tên 'csv_list'
#     else:
#         form = CSVUploadForm()
#     return render(request, 'Cap2App/upload.html', {'form': form})


# def csv_list_view(request):
#     csv_data = CSVData.objects.all()
#     return render(request, 'Cap2App/csv_list.html', {'csv_data': csv_data})




# Cap2App/views.py
from django.shortcuts import render, redirect
import csv
from .models import CSVData  # Đảm bảo bạn đã import CSVData
from .forms import CSVUploadForm
from io import TextIOWrapper
from django.contrib import messages

def upload_file_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']

            # Đọc tệp CSV và xử lý dữ liệu
            csv_file_wrapper = TextIOWrapper(csv_file.file, encoding='utf-8')
            reader = csv.reader(csv_file_wrapper)

            # Lặp qua các hàng của tệp CSV (bỏ qua hàng đầu nếu là tiêu đề)
            for row in reader:
                print(row)  # Thay `print` bằng xử lý dữ liệu của bạn
            
            # Lưu file tạm thời để có thể cung cấp đường dẫn tải xuống
            csv_file_path = f'media/uploads/{csv_file.name}'  # Đường dẫn lưu file
            with open(csv_file_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            messages.success(request, "Dữ liệu đã được xử lý thành công!")
            # Redirect đến success_page và truyền đường dẫn file CSV
            return redirect('success_page', csv_file_path=csv_file_path)

    else:
        form = CSVUploadForm()

    return render(request, 'Cap2App/upload.html', {'form': form})



def csv_list_view(request):
    csv_data = CSVData.objects.all()
    return render(request, 'Cap2App/csv_list.html', {'csv_data': csv_data})

def csv_detail_view(request, pk):
    csv_record = CSVData.objects.get(pk=pk)
    return render(request, 'Cap2App/csv_detail.html', {'csv_record': csv_record})


# Cap2App/views.py
from django.shortcuts import render
from django.conf import settings

def home_view(request):
    # Không cần gọi đến get_template_loaders()
    return render(request, 'Cap2App/home.html')


def success_page_view(request):
    # Lấy đường dẫn file CSV từ GET parameters
    csv_file_path = request.GET.get('csv_file_path')
    return render(request, 'Cap2App/success_page.html', {'csv_file_path': csv_file_path})