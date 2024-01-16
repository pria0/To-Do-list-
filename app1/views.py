from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ToDo
# Create your views here.
def index(request):
    # return HttpResponse('Pws')

    data = ToDo.objects.all()
    return render(request,'index.html',{'data':data})


def to_do(request):

    if request.method == 'POST':
        desc2 = request.POST['desc1']

        t = ToDo(desc=desc2)
        t.save()
        print("Data saved...")
    return redirect('/')

def todo_delete(request,tid):
    data = ToDo.objects.get(tid=tid)
    data.delete()
    print("data Deleted....")
    return redirect('/')