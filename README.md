mac 
```
python3 -m venv myenv
source myenv/bin/activate
```

windows
```
virtualenv myenv
myenv\Scripts\activate.bat
```

pip install django
pip install crispy-bootstrap4
pip install django-crispy-forms
django-admin startproject data_website
cd data_website
python manage.py startapp users
python manage.py startapp data_home
# data_home
放置靜態文件的app(templates, static)
## templates
### base.html
{% static 'data_home/main.css' %} -> /static/data_home/main.css
## static
data_home/setting.py 
STATIC_URL = "static/" -> 静态文件对应的URL路径是/static/。
# Users
客戶註冊功能
## data_website/settings.py
新增app功能
```
INSTALLED_APPS = [
    "users.app...."
]
```
## models.py 
```
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
```

python manage.py makemigrations
python manage.py migrate

## admin.py
```
from django.contrib import admin
from .models import User

admin.site.register(User)
```

## views.py
```
# CRUD

from .models import User

def create_user(request):
  # 创建用户逻辑

def update_user(request, id):
  # 更新用户逻辑

def delete_user(request, id):
  # 删除用户逻辑
  
def get_user(request, id):
  # 查询用户逻辑
```

# urls.py

```
from . import views

urlpatterns = [
  path('create/', views.create_user),
  path('update/<int:id>/', views.update_user),
  path('delete/<int:id>/', views.delete_user),
  path('get/<int:id>/', views.get_user),
]
```

# Crispy-forms