from time import sleep
import tkinter.messagebox
from functions.easyprompt import *
import functions.info
from os import system
import tkinter
import functions.update
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

def exitnow():
    sleep(1)
    info('程序运行结束')
    exit()

info('正在检查更新')
if functions.update.check() == '已是最新版本':
    info('已是最新版本' + functions.info.version)
elif functions.update.check() == '无法连接到更新服务器，请检查网络连接':
    warn('无法连接到更新服务器，请检查网络连接')
elif functions.update.check().startswith('有新版本可用'):
    warn('有新版本可用，正在弹出更新窗口')
    if tkinter.messagebox.askyesno('有新版本可用', '有新版本可用，是否更新？'):
        system('start https://github.com/azkbbys/timeToStamp/releases')

info('尝试打开界面')
warn('请不要关闭本界面')
root = tkinter.Tk()
root.title('timeToStamp-v' + functions.info.version)
root.geometry('500x500')
root.resizable(False, False)

# 设置初始值
initial_date = datetime.now().date()
initial_hour = datetime.now().hour
initial_minute = datetime.now().minute
initial_second = datetime.now().second

lable = tkinter.Label(root, text='timeToStamp\n时间转时间戳', font=('微软雅黑', 15))
lable.pack(pady=20)

website_button = tkinter.Button(root, text='bysTools', font=('微软雅黑', 10), command=lambda: system('start https://github.com/azkbbys/bysTools'))
website_button.place(x=430, y=460, width=70, height=30)

def convert_to_timestamp():
    try:
        selected_date = date_entry.get_date()
        selected_time = f"{hour_spinbox.get()}:{minute_spinbox.get()}:{second_spinbox.get()}"
        full_datetime_str = f"{selected_date} {selected_time}"
        full_datetime = datetime.strptime(full_datetime_str, '%Y-%m-%d %H:%M:%S')
        timestamp = int(full_datetime.timestamp())
        timestamp_entry.config(state='normal')
        timestamp_entry.delete(0, tkinter.END)
        timestamp_entry.insert(0, str(timestamp))
        timestamp_entry.config(state='readonly')
    except Exception as e:
        tkinter.messagebox.showerror('错误', f'转换失败: {e}')

# 添加日期选择器
date_label = tkinter.Label(root, text='选择日期:', font=('微软雅黑', 10))
date_label.pack(pady=5)
date_entry = DateEntry(root, selectmode='day', year=initial_date.year, month=initial_date.month, day=initial_date.day)
date_entry.pack(pady=5)

# 添加时间选择器和转换按钮
time_frame = tkinter.Frame(root)
time_frame.pack(pady=5)

time_label = tkinter.Label(time_frame, text='选择时间:', font=('微软雅黑', 10))
time_label.pack(side=tkinter.LEFT, padx=5)

hour_spinbox = ttk.Spinbox(time_frame, from_=0, to=23, width=5, format="%02.0f", textvariable=tkinter.StringVar(value=initial_hour))
hour_spinbox.pack(side=tkinter.LEFT, padx=5)
minute_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, width=5, format="%02.0f", textvariable=tkinter.StringVar(value=initial_minute))
minute_spinbox.pack(side=tkinter.LEFT, padx=5)
second_spinbox = ttk.Spinbox(time_frame, from_=0, to=59, width=5, format="%02.0f", textvariable=tkinter.StringVar(value=initial_second))
second_spinbox.pack(side=tkinter.LEFT, padx=5)

convert_button = tkinter.Button(time_frame, text='转换为时间戳', font=('微软雅黑', 10), command=convert_to_timestamp)
convert_button.pack(side=tkinter.LEFT, padx=10)

# 添加时间戳显示框
timestamp_frame = tkinter.Frame(root)
timestamp_frame.pack(pady=20)

timestamp_label = tkinter.Label(timestamp_frame, text='时间戳:', font=('微软雅黑', 10))
timestamp_label.pack(side=tkinter.LEFT)

timestamp_entry = tkinter.Entry(timestamp_frame, font=('微软雅黑', 10), width=20, state='readonly')
timestamp_entry.pack(side=tkinter.LEFT, padx=5)

# 添加复制功能
def copy_timestamp():
    root.clipboard_clear()
    root.clipboard_append(timestamp_entry.get())

copy_button = tkinter.Button(timestamp_frame, text='复制', font=('微软雅黑', 10), command=copy_timestamp)
copy_button.pack(side=tkinter.LEFT)

root.mainloop()