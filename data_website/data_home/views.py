from django.shortcuts import render


# Create your views here.
def home(request):
    """
    This function is used to render the home page.
    """
    return render(request, "data_home/home.html")


from django.contrib.auth.decorators import login_required


@login_required
def print123(request):
    return render(request, "data_home/home.html")
