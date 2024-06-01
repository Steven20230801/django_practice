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

```
pip install django
pip install crispy-bootstrap4
pip install django-crispy-forms
```

```
django-admin startproject data_website
cd data_website
python manage.py startapp users
python manage.py startapp data_home
```

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


# 2023.11.4 新增Search功能
```
python manage.py startapp search_accounts
```
1. 新增輸入查詢Accounts表單
* search_accounts/forms.py
建立AccountsForm
- choices: 建立tuple list給輸入表格選擇
- widget: 建立輸入表格的樣式
- label: 輸入表格的標籤
- required: 是否必填
- help_text: 輸入表格的提示文字
- error_messages: 輸入表格的錯誤提示文字
- initial: 輸入表格的預設值
- validators: 輸入表格的驗證器

* search_accounts/templates/search_accounts/search_accounts.html
* search_accounts/templates/search_accounts/search_accounts_results.html
* search_accounts/views.py
* search_accounts/urls.py
* data_website/urls.py
* data_website/settings.py

1. 新增搜尋功能
2. 新增搜尋結果頁面



 ./init.sql:/docker-entrypoint-initdb.d/init.sql：

這行指示 Docker 將宿主機上的當前目錄（即 docker-compose.yml 文件所在的目錄）中的 init.sql 文件掛載到容器內的 /docker-entrypoint-initdb.d/init.sql 位置。
/docker-entrypoint-initdb.d/ 是 MySQL 官方 Docker 映像的一個特殊目錄。當容器第一次啟動時，MySQL 會自動執行這個目錄下的所有 .sql 文件、.sh 腳本和 .sql.gz 文件。
這樣，你可以在 MySQL 容器啟動時自動執行初始化 SQL 腳本，創建數據庫、使用者和資料表。