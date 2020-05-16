from django.shortcuts import render
from secondapp.models import Users
from secondapp import forms
# Create your views here.
def help(request):
    #give_content = {'insert_me':'Hello darkness my old friend'}
    udict = Users.objects.order_by('userfirst')
    users_dict = {'insert_user':udict}
    return render(request,'secondapp/help.html',context = users_dict)

def formsplay(request):
    formget = forms.FormsgetModel()
    if request.method == 'POST':
        formget = forms.FormsgetModel(request.POST)
        if formget.is_valid():
            formget.save(commit=True)
            return help(request)
    return render(request,'secondapp/redirect.html',context = {'form':formget})
