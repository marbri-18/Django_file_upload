from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def homepage(request):
    return render(request, 'uploadmb/upload.html')

def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'uploadmb/upload.html', {'file_url': file_url})
    return render(request, uploadmb/upload.html)
