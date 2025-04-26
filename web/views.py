from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pyzbar.pyzbar import decode
from PIL import Image
import os
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .pintata import upload_file_to_pinata


# Create your views here.
def index(request):
    return render(request, 'try.html')

def history(request):
     return render(request, "userhistory.html")

def dashboard(request):
     return render(request, "dashboard.html")

def evidence(request, id):
     return render(request, "evidence.html", {'id': id})

def ipfs(request):
     return render(request, "ipfs.html")

def landing(request):
     return render(request, "landing-main.html")


def addevidence(request):
     if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_path = os.path.join('temp', uploaded_file.name)

        try:
            # Save the uploaded file temporarily
            os.makedirs('temp', exist_ok=True)
            with open(file_path, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)

            # Upload the file to Pinata
            ipfs_hash = upload_file_to_pinata(file_path)

            # Clean up the temporary file
            os.remove(file_path)

            # Return the IPFS hash as a JSON response
            return render(request,'addevidence.html',{'success': True, 'ipfs_hash': ipfs_hash})

        except Exception as e:
            # Log the error
            logger.error(f"Error during file upload: {str(e)}", exc_info=True)

            # Handle errors during the upload process
            return render(request,'addevidence.html',{'success': False, 'error': str(e)}, status=500)

     else:
          return render(request, 'addevidence.html')

def case(request):
     return render(request, "dashboard.html")

def camera(request):
     return render(request, "camera.html")

def report(request):
     return render(request, "report.html")
def addreport(request):
     if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_path = os.path.join('temp', uploaded_file.name)

        try:
            # Save the uploaded file temporarily
            os.makedirs('temp', exist_ok=True)
            with open(file_path, 'wb') as f:
                for chunk in uploaded_file.chunks():
                    f.write(chunk)

            # Upload the file to Pinata
            ipfs_hash = upload_file_to_pinata(file_path)

            # Clean up the temporary file
            os.remove(file_path)

            # Return the IPFS hash as a JSON response
            return render(request,'addreport.html',{'success': True, 'ipfs_hash': ipfs_hash})

        except Exception as e:
            # Log the error
            logger.error(f"Error during file upload: {str(e)}", exc_info=True)

            # Handle errors during the upload process
            return render(request,'addreport.html',{'success': False, 'error': str(e)}, status=500)

     else:
          return render(request, "addreport.html")

