from distutils.command.config import config
from importlib import import_module
from msilib.schema import ComboBox
from tkinter import *
import tkinter
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from datetime import date, datetime, time
import tkinter.font
import hotnow_data2 as hdata
import pandas as pd
from PIL import ImageTk

from pyparsing import col


root = Tk()
root.title ("HOT NOW")
root.geometry("600x800")
font = tkinter.font.Font(family = "잘풀리는하루 Medium",size=14)
sub_font = tkinter.font.Font(family = "잘풀리는하루 Medium",size=10)
#메뉴 객체 생성
# menuAll = Menu(root)
# menu_1 = Menu(menuAll,tearoff=0)

# def cmdbtn():
#     print('click')
    
# menu_1.add_command(label="new",command=cmdbtn)

# menuAll.add_cascade(label = "File", menu = menu_1)
# root.config(menu = menuAll)

hotnow_cnt = 2
photo_li = ['원주무실점 매장사진.jpg','건대스타시티점 매장 안 내부 측면 사진.jpg','대전둔산점 매장 정면 사진.jpg','-.jpg','대치점 매장 정면 사진.jpg','김해봉황점.jpg','울산삼산점 매장 카운터 측면 사진.jpg','영등포점 매장 내부 사진.jpg']
#top텍스트
Label(root,text = "HOT NOW 등이 켜지고 따뜻하고 달콤한 도넛이 나오는 시간입니다.", font=font).place(x=30,y=10)
Label(root,text = "현재 " +str(hotnow_cnt)+ "개의 매장에 'HOT NOW'등이 켜졌습니다.",font=font,pady=3).place(x=100,y=40)

#오늘 날짜
Label(root,text =date.today(), fg="green", font=font).place(x=10,y=95)

input_time = '0'
#선택시간 출력
time_label = Label(root,text="Time : "+ input_time +":00",font=font)
time_label.place(x=140,y=95)

#시간 콤보박스 values
time_values = [str(t) + ":00" for t in range(7,25)]

#시간 콤보박스
time_combo=ttk.Combobox(root, height=5,width=17, values = time_values,state = "readonly")
time_combo.set("시간 선택")
time_combo.place(x=400,y=95)

st_li_frame = LabelFrame(root,text = "LIST").place(x=0,y=0)
def btncmd():
    
    global time_split
    global time_combo_get
    global time_num
    time_combo_get = time_combo.get()
    time_split = time_combo.get().split(':')
    
    #선택한 시간이 화면에 출력
    time_label.config(text="Time : "+ time_combo.get())
    
    #숫자 추출
    if time_split[0] in time_combo_get:
        time_num = time_split[0]
        time_num = int(time_num)
    
    #csv에서 선택한 시간의 index 추출 (변수명 : csv_inputime_idx)
    csv_inputime_idx = hdata.df.query("time == @time_num").index

    global x_var
    global y_var  
    x_var = 300
    y_var = 50
    global photo_li_idx
    #인덱스로 시간에 맞는 데이터 추출
    #NONE 출력
    if hdata.df.loc[csv_inputime_idx[0],'store'] == 'NONE':
        Label(st_li_frame, text = 'HOT NOW 등이 켜진 매장이 없습니다.',font=sub_font,fg="red").place(x=200,y=170) 
    else:    
        for idx in csv_inputime_idx:
            
            
            #사진 제목 list에서 사진찾기
            photo_idx = hdata.df.loc[idx,'imgname']
            photo_m=[s for s in photo_li if photo_idx in s]
            photo_li_idx = photo_li.index(photo_m[0])

            if idx == 0:  #목록중 첫번째 항목에 대한 설정
                photo_file1 = photo_li[photo_li_idx]
                print(photo_file)
                photo = ImageTk.PhotoImage(file=photo_file1)
                Label(root,image = photo,width=150,height=100).place(x=10,y=y_var) #매장사진
                la1 = Label(st_li_frame, text = hdata.df.loc[idx,'store'],font=sub_font,fg="green")
                la1.place(x=x_var,y=y_var) #매장명
                la2 = Label(st_li_frame, text = hdata.df.loc[idx,'times'],font=sub_font,justify="left")
                la2.place(x=x_var,y=(y_var+25)) #영업시간
            else:
                y_var = y_var+90 #위치 조절
                photo_file = photo_li[photo_li_idx]
                print(photo_file)
                photo = ImageTk.PhotoImage(file=photo_file)
                Label(root,image = photo,width=150,height=100).place(x=10,y=y_var)#매장사진
                la1 = Label(st_li_frame, text=hdata.df.loc[idx,'store'],font=sub_font,fg="green")
                la1.place(x=x_var,y=y_var)
                la2 = Label(st_li_frame, text = hdata.df.loc[idx,'times'],font=sub_font,justify="left")
                la2.place(x=x_var,y=(y_var+25)) #영업시간
       

 
#조회버튼
Button(root, text = "확인",width=5, command=btncmd).place(x=545,y=93)


#구분선인데.. 왜 안나오지..?
ttk.Separator(root, orient="horizontal").place(x=0,y=150)



root.mainloop()