# django_auto_create

##注意事項
```
建立 app 與 mysite 時可能因為某些單字而無法建立成功 例如 Mysite 輸入 test  

```
##建立與修改的項目
```

1.settings.py
	- import
	- 新增app
	- 設定ip ALLOWED_HOSTS = ['*']
	- 可選擇使用預設 DB 或 MySql(需自行設定帳號密碼) 
	- 設定templates / static 路徑
	- 時區 / 語言更改

2.mysite/urls.py
	- import
	- 建立path
	- 建立app/urls.py設定

3.app/urls.py
	- import
	- 建立index.html路徑

4.views.py
	- import
	- 初始化 index.html

```

##主程式 django_auto.py

```

10.  project_path = '/Users/../Desktop'                 #修改路徑到你要的位置

```

##執行程式 django_tk.py
```

使用 django_tk.py 需自行 install tkinter 套件

```
