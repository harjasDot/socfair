from django.shortcuts import render
from app.models import QUESTION

# Create your views here.
def core(request):
    if request.method=='POST':
        name=request.POST['name']
        q1=request.POST['q1']
        q2=request.POST['q2']
        data=QUESTION.objects.create(
        name=name,
        q1=q1,
        q2=q2,
        )
        data.save()

        return render(request,'thankyou.html')
    return render(request,'core.html')

