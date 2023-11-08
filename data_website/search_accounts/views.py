from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AccountsForm, AccountsModelForm


@login_required
def request_accounts(request):
    button_name = "request_accounts"
    if request.method == "POST":
        form = AccountsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # do something with the data
            return render(
                request,
                "search_accounts/home.html",
                {"form": form, "button_name": button_name},
            )

    else:
        form = AccountsForm()
    return render(
        request, "search_accounts/home.html", {"form": form, "button_name": button_name}
    )


@login_required
def request_accounts_model(request):
    button_name = "request_accounts_model"
    if request.method == "POST":
        form = AccountsModelForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # data.save()
            # do something with the data
            return render(
                request,
                "search_accounts/home.html",
                {"form": form, "button_name": button_name},
            )

    else:
        form = AccountsModelForm()
    return render(
        request, "search_accounts/home.html", {"form": form, "button_name": button_name}
    )
