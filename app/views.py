from django.shortcuts import render

# Create your views here.
def karim(request):
    return render(request,'karim.html')

def jobseeker(request):
    return render(request,'jobseeker.html')

