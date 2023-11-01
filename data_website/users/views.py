from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserRigesterForm

from django.shortcuts import render

from django.contrib.auth.views import LoginView


# class MyLoginView(LoginView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["department"] = "其他属性"
#         return context


def register(request):
    """
    This function is used to register a new user.
    """
    if request.method == "POST":
        form = UserRigesterForm(request.POST)

        if form.is_valid():
            form.save()  # save the user
            username = form.cleaned_data.get("username")  # get the username
            messages.success(
                request, f"Account created for {username}!"
            )  # send a success message

            return redirect("home")
    else:
        form = UserRigesterForm()
    return render(request, "users/register.html", {"form": form})


# @login_required
# def user_update(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     if request.method == "POST":
#         form = UserRigesterForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect("user_detail", pk=user.pk)
#     else:
#         form = UserRigesterForm(instance=user)
#     return render(request, "users/user_form.html", {"form": form})
