from django.shortcuts import render

from .forms import SignUpForm
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