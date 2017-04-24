from django.shortcuts import render

from .forms import SignUpForm, ContactForm
# Create your views here.
def home(request):
    title = "my title"
    form = SignUpForm(request.POST or None)
    context = {
        "title":title,
        "form":form,
    }
    # if request.method== "POST":
    #     print request.POST
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #print request.POST   #not recomended
        # print instance.email
        # print instance.timestamp
        # print instance.full_name
        context = {
            "title": "Thank you"
        }
    
    return render(request, "home.html",context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print key
        #     print form.cleaned_data.get(key)
        email = form.cleaned_data.get("email")
        full_name = form.cleaned_data.get("full_name")
        message = form.cleaned_data.get("message")
        print email,full_name,message
    context = {
        "form": form
    }
    
    return render(request, "forms.html", context)