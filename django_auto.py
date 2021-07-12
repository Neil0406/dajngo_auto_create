#Django 生成器

import os

def info(project_name, mysite_name, app_name, db):
    # project_name = str(input('請輸入專案名稱：')) 
    # mysite_name = str(input('請輸入Mysite名稱：'))
    # app_name = str(input('請輸入App名稱：'))
    # db = str(input('資料庫 / 預設：1 Mysql:2 :'))
    project_path = '/Users/weichenho/Desktop'                         #修改路徑到你要的位置
    project_file = project_path + '/' + project_name

    os.mkdir(project_file)     #建立專案資料夾

    os.system(f'cd {project_file} && django-admin startproject {mysite_name}')   #建立mysite資料夾
    os.system(f'cd {project_file}/{mysite_name} && python manage.py startapp {app_name}') #建立app資料夾
    os.mkdir(f'{project_file}/{mysite_name}/templates')                                   #建立templates資料夾
    os.mkdir(f'{project_file}/{mysite_name}/static')                                      #建立static資料夾
    html = open(f'{project_file}/{mysite_name}/templates/index.html','w')                 #建立html檔案
    html.close()

    return project_file, mysite_name, app_name, db

def settings(project_file, mysite_name, app_name, db):
    #更改settings.py設定檔
    #路徑 {project_file}/{mysite_name}/{mysite_name}/settings.py
    file_object1 = open(f'{project_file}/{mysite_name}/{mysite_name}/settings.py','r')    #讀django取生成的原始檔
    l = []                                                                                 #將檔案內容append到list 
    try:
        while True:
            line = file_object1.readline()
            if line:
                l.append(line)
            else:
                break
    finally:
        file_object1.close()

    new_l = []
    for i in l:
        if i == 'from pathlib import Path\n':
            new_l.append('from pathlib import Path\n')
            new_l.append('import os\n')
            new_l.append('import pymysql\n')
            new_l.append('pymysql.version_info = (1, 4, 13, "final", 0)      ##需自行新增\n')
            new_l.append('pymysql.install_as_MySQLdb()                       #####\n')
        elif i == "ALLOWED_HOSTS = []\n":                              
            new_l.append("ALLOWED_HOSTS = ['*']\n")
        elif i == "    'django.contrib.staticfiles',\n":
            new_l.append("    'django.contrib.staticfiles',\n")
            new_l.append(f"    '{app_name}',\n")                                
        elif i == "        'DIRS': [],\n":
            new_l.append("        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\\\', '/')],\n")   
        elif i == "        'ENGINE': 'django.db.backends.sqlite3',\n" and db == '2':                      #Mysql設定區
            new_l.append("        'ENGINE': 'django.db.backends.mysql',\n")
        elif i == "        'NAME': BASE_DIR / 'db.sqlite3',\n" and db == '2':
            new_l.append("        'NAME': '',\n")
            new_l.append("        'USER': 'root',\n") 
            new_l.append("        'PASSWORD': 'root',\n")                       
            new_l.append("        'HOST': '127.0.0.1',\n")
            new_l.append("        'PORT': '3306',\n")
        elif i == "LANGUAGE_CODE = 'en-us'\n":
            new_l.append("LANGUAGE_CODE = 'zh-Hant'\n")
        elif i == "TIME_ZONE = 'UTC'\n":
            new_l.append("TIME_ZONE = 'Asia/Taipei'\n")
        elif i == 'USE_I18N = True\n':
            new_l.append("USE_I18N = True\n")
        elif i == 'USE_L10N = True\n':
            new_l.append("USE_L10N = True\n")
        elif i == 'USE_TZ = True\n':
            new_l.append("USE_TZ = False\n")
        elif i == "STATIC_URL = '/static/'\n":
            new_l.append("STATIC_URL = '/static/'\n")
            new_l.append("\n")
            new_l.append("STATICFILES_DIRS = [\n")
            new_l.append("    os.path.join(BASE_DIR, 'static'),\n")
            new_l.append("]\n")
        else:
            new_l.append(i)

    file_object2 = open(f'{project_file}/{mysite_name}/{mysite_name}/settings.py','w')   
    for i in new_l:
        file_object2.writelines(i)
    file_object2.close()

#---------------------------Mysite裡的urls.py---------------------------------
def urls(project_file, mysite_name, app_name):
    file_object1 = open(f'{project_file}/{mysite_name}/{mysite_name}/urls.py','r')
    l = []                                                             
    try:
        while True:
            line = file_object1.readline()
            if line:
                l.append(line)
            else:
                break
    finally:
        file_object1.close()

    new_l = []
    for i in l:
        if i == 'from django.urls import path\n':
            new_l.append('from django.urls import path\n')
            new_l.append('from django.conf.urls import include, url')
            new_l.append('\n')
            new_l.append('\n')
        elif i == "    path('admin/', admin.site.urls),\n":
            new_l.append("    path('admin/', admin.site.urls),\n")
            new_l.append(f"    path('', include('{app_name}.urls')),\n")
        else:
            new_l.append(i)
    file_object2 = open(f'{project_file}/{mysite_name}/{mysite_name}/urls.py','w')   
    for i in new_l:
        file_object2.writelines(i)
    file_object2.close()
    #-----------------------------Apps裡的urls.py---------------------------------
    file_object3 = open(f'{project_file}/{mysite_name}/{app_name}/urls.py','w')
    l = [
        "from django.conf.urls import url\n",
        f"from {app_name} import views\n",
        "from django.urls import path",
        "\n",
        "\n",
        "\n",
        "urlpatterns = [\n",
        "    path('', views.index),\n",
        "]\n"     
    ]
    for i in l:
        file_object3.writelines(i)
    file_object3.close()

#-----------------------------views.py---------------------------------
def views(project_file, mysite_name, app_name):
    file_object1 = open(f'{project_file}/{mysite_name}/{app_name}/views.py','w')
    l = [
        "from django.shortcuts import render,redirect, HttpResponse\n",
        "from django.urls import reverse\n",
        "from django.http import HttpResponseRedirect\n",
        f"#from {app_name}.models import User\n",
        "\n",
        "\n",
        "\n",
        "def index(request):\n",
        "\n",
        "	return render(request,'index.html')"
    ]
    for i in l:
        file_object1.writelines(i)                                                          
    file_object1.close()

