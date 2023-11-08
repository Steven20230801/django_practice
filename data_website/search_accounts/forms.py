from django import forms
from .models import SearchAccount


class AccountsForm(forms.Form):
    SERVER_CHOICES = [
        ("enfaureport", "enfaureport"),
        ("enfau2report", "enfau2report"),
    ]
    server = forms.ChoiceField(
        label="Server",
        choices=SERVER_CHOICES,
        required=True,
        error_messages={"required": "Please select a server."},
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    login = forms.IntegerField(
        label="Login ID",
        required=True,
        error_messages={"required": "Please enter your login ID."},
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    # brand = forms.CharField(max_length=100)
    def clean_login(self):
        login = self.cleaned_data.get("login")
        if login < 0:
            raise forms.ValidationError(
                "Login ID must be positive.", code="invalid", params={"login": login}
            )
        return login


class AccountsModelForm(forms.ModelForm):
    """搜尋帳號表單"""

    class Meta:
        model = SearchAccount
        fields = ["server", "login"]
        # server = models.CharField(max_length=100, choices=SERVER_CHOICES)
        labels = {"server": "Server", "login": "Login ID"}

        widgets = {
            # 預設start_date = 2020-01-01
            "server": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width:100%;",
                    "placeholder": "enfaureport",
                }
            ),
            "login": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "width:100%;",
                    "placeholder": "6021108",
                }
            ),
        }

    def ertrterterclean_login(self):
        login = self.cleaned_data.get("login")
        if login < 0:
            raise forms.ValidationError(
                "Login ID must be positive.", code="invalid", params={"login": login}
            )
        return login
