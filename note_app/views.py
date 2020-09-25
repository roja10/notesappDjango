from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
from .models import notetypeyes



def checking(request):
    """
    Head_ing="Here is my to-do list"
    content="Reading Novel,Office work, Walking,writing letter"
    last_updated_date=datetime.datetime.now()
     """
    s=notetypeyes.objects
    if(s==None):
        return  render(request,'frontview.html', 'Details not available')
    return render(request,'frontview.html',{'obj':s})
def deleting(request,pk):
    print(request)
    s=notetypeyes.objects.get(pk=pk)
    s.delete()
    return checking(request)

