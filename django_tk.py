
import tkinter as tk
from django_auto import *


window = tk.Tk()
window.title('Django自動產生器')
window.geometry('400x200')
window.configure(background='white')

def project():
    project_name = str(project_entry.get())
    mysite_name = str(mysite_entry.get())
    app_name = str(app_entry.get())
    db = str(db_entry.get())
    project_file, mysite_name, app_name, db = info(project_name, mysite_name, app_name, db)
    settings(project_file, mysite_name, app_name, db)
    urls(project_file, mysite_name, app_name)
    views(project_file, mysite_name, app_name)

    result_label.configure(text='建立完成')
#-----------------------tk---------------------------

#TOP title
header_title = tk.Label(window, text='Django')
header_title.pack()

search_frame = tk.Frame(window)                                
search_frame.pack(side=tk.TOP)                              
search_label = tk.Label(search_frame, text='專案名稱:')      
search_label.pack(side=tk.LEFT)                                        
project_entry = tk.Entry(search_frame)                          
project_entry.pack(side=tk.LEFT) 

search_frame1 = tk.Frame(window)                                
search_frame1.pack(side=tk.TOP)                              
search_label1 = tk.Label(search_frame1, text='Mysite名稱:')      
search_label1.pack(side=tk.LEFT)                                        
mysite_entry = tk.Entry(search_frame1)                          
mysite_entry.pack(side=tk.LEFT)       

search_frame2 = tk.Frame(window)                                
search_frame2.pack(side=tk.TOP)                              
search_label2 = tk.Label(search_frame2, text='App名稱:')      
search_label2.pack(side=tk.LEFT)                                        
app_entry = tk.Entry(search_frame2)                          
app_entry.pack(side=tk.LEFT)

search_frame3 = tk.Frame(window)                                
search_frame3.pack(side=tk.TOP)                              
search_label3 = tk.Label(search_frame3, text='DB/ 預設:1 Mysql:2:')      
search_label3.pack(side=tk.LEFT)                                        
db_entry = tk.Entry(search_frame3)                          
db_entry.pack(side=tk.LEFT)   

#BTN
top_btn_frame = tk.Frame(window)
top_btn_frame.pack(side=tk.TOP)

url_btn = tk.Button(top_btn_frame, text='確定', fg='red',command= project)
url_btn.pack(side=tk.LEFT)


result_label = tk.Label(window)
result_label.pack()



window.mainloop()