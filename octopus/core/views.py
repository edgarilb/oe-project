from django.shortcuts import render
from .models import Data

def home(request):
    return render(request, 'home.html')
    
def upload(request):
    records = Data.objects.all()
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        
        # Read the file
        file1 = open(uploaded_file.name)
        Lines = file1.readlines() 
        # count = 0

        count = 0
        # numOfRecords =  20 
        data = Data.objects.all()
        data.delete()

        for line in Lines:
            count += 1

            if count > 20:
                break
            else:
                print(f'Line{count} {line}')

                data = Data(
                    meterPoint=line,
                    meter =line,
                )
                data.save()
   
    return render(request, 'upload.html', {
        'records':records,
    })

def record_list(request):
    records = Data.objects.all()
    return render(request, 'record_list.html', {
        'records':records,
    })


