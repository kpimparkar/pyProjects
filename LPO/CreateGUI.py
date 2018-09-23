from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from calendar import monthrange
import sys
import DbOps
from datetime import datetime

root=Tk()
root.title('Weather statisics')
logo=PhotoImage(file=r'C:\Users\kpimp\KeTan\PyHw\Lynda_Code_clinic_2014\lpo_logo.gif')
header=ttk.Label(root,image=logo, padding=10)
header.pack()
info_label=ttk.Label(root, text='Please select a date range to check \nthe weather statistics : ', font=('Verdana',10,'bold'), padding=5)
info_label.pack()

yrs=[2015,2014,2013,2012]#Data of only these years is available
months=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

from_yr=StringVar()
from_month=StringVar()
from_day=IntVar()
to_yr=StringVar()
to_month=StringVar()
to_day=IntVar()
day_values=[]
from_days=[]
to_days=[]

def get_days(year,month,day_combo):
    day_values=[]
    if int(year) not in yrs:
        messagebox.showerror(title='Invalid information',message='Pls correct the year')
        return
    if month not in months:
        messagebox.showerror(title='Invalid information',message='Pls correct the month')
        return
    for i in (range(1,monthrange(int(year),months.index(month)+1)[1]+1)):
        day_values.append(i)
    day_combo.config(values=day_values)    
    
label_frame=ttk.Frame(root)
label_frame.pack()
from_label=ttk.Label(label_frame,text="From date")
from_label.pack(side=LEFT,padx=50)
to_label=ttk.Label(label_frame,text="To date")
to_label.pack(side=LEFT,padx=50)

date_frame=ttk.Frame(root)
date_frame.pack()
from_year=ttk.Combobox(date_frame,values=yrs,textvariable=from_yr,width=4)
from_year.pack(side=LEFT)
from_month=ttk.Combobox(date_frame,values=months, width=4)
from_month.pack(side=LEFT)
from_day=ttk.Combobox(date_frame,values=from_days, width=4,
                      postcommand=lambda : get_days(from_yr.get(),from_month.get(),from_day))
from_day.pack(side=LEFT)
from_yr.set('2012')
from_month.set('JAN')
from_day.set('01')

ttk.Label(date_frame,text='   ').pack(side=LEFT)

to_year=ttk.Combobox(date_frame,values=yrs,textvariable=to_yr,width=4)
to_year.pack(side=LEFT)
to_month=ttk.Combobox(date_frame,values=months, width=4)
to_month.pack(side=LEFT)
to_day=ttk.Combobox(date_frame,values=to_days, width=4,
                      postcommand=lambda : get_days(to_yr.get(),to_month.get(),to_day))
to_day.pack(side=LEFT)
to_yr.set('2012')
to_month.set('JAN')
to_day.set('01')

def get_results(from_YYYY_MM_DD, to_YYYY_MM_DD):
    DbOps.create_db()
    DbOps.load_data(from_YYYY_MM_DD)
    if from_yr.get() != to_yr.get():
        DbOps.load_data(to_YYYY_MM_DD)
    op=DbOps.calc_reqd_values(from_YYYY_MM_DD, to_YYYY_MM_DD)
    return(op)

def validate_ip():
    if int(from_yr.get()) not in yrs:
        messagebox.showerror(title='Invalid information',message='Pls correct the from year')
        return
    if from_month.get() not in months:
        messagebox.showerror(title='Invalid information',message='Pls correct the from month')
        return
    if int(to_yr.get()) not in yrs:
        messagebox.showerror(title='Invalid information',message='Pls correct the to year')
        return
    if to_month.get() not in months:
        messagebox.showerror(title='Invalid information',message='Pls correct the to month')
        return
    if not from_day.get().isdigit():
       messagebox.showerror(title='Invalid information',message='Inavlid from day format.')
       return
    if not to_day.get().isdigit():
       messagebox.showerror(title='Invalid information',message='Inavlid to day format.')
       return
    if not int(from_day.get()) in range(1,32):
       messagebox.showerror(title='Invalid information',message='Inavlid from day')
       return
    if not int(to_day.get()) in range(1,32):
       messagebox.showerror(title='Invalid information',message='Inavlid to day')
       return
    frm=datetime(int(from_yr.get()),months.index(from_month.get())+1,int(from_day.get()))
    to =datetime(int(to_yr.get()),months.index(to_month.get())+1,int(to_day.get()))
    if frm > to:
       messagebox.showerror(title='Invalid information',message='From date greater than to date.')
       return

        
def show_result():
    ####Validate input dates here ********EVen afetr showing the popup, flow calls next frocess
    try:
        validate_ip()
        from_date=from_yr.get()+'_'+'{:>02}'.format(months.index(from_month.get())+1)+'_'+'{:>02}'.format(from_day.get())
        to_date=to_yr.get()+'_'+'{:>02}'.format(months.index(to_month.get())+1)+'_'+'{:>02}'.format(to_day.get())
        op=get_results(from_date,to_date)
        
        op_frame=ttk.Frame(root,width=1000,height=500,relief=SUNKEN)
        op_frame.pack()
        
        ttk.Label(op_frame, text='From date : {}\tTo date : {}'.format(from_date,to_date)).grid(row=0,column=1, columnspan=4)
        ttk.Label(op_frame, text='Mean', font=('Verdana',10,'bold')).grid(row=1,column=3,sticky='sw',padx=5)
        ttk.Label(op_frame, text='Median', font=('Verdana',10,'bold')).grid(row=1,column=5,sticky='sw',padx=5)
        ttk.Label(op_frame, text='Wind Speed', font=('Verdana',10,'bold')).grid(row=2,column=0,sticky='sw',padx=5)
        ttk.Label(op_frame, text='Air Temp.', font=('Verdana',10,'bold')).grid(row=3,column=0,sticky='sw',padx=5)
        ttk.Label(op_frame, text='Barometric\npressure', font=('Verdana',10,'bold')).grid(row=4,column=0,sticky='sw',padx=5)
        ttk.Label(op_frame, text=op['w_mean']).grid(row=2,column=3,sticky='sw',padx=5)
        ttk.Label(op_frame, text=op['a_mean']).grid(row=3,column=3,sticky='sw',padx=5)
        ttk.Label(op_frame, text=op['b_mean']).grid(row=4,column=3,sticky='sw',padx=5)
        ttk.Label(op_frame, text=op['w_median']).grid(row=2,column=5,sticky='sw',padx=5)
        ttk.Label(op_frame, text=op['a_median']).grid(row=3,column=5,sticky='sw',padx=5)
        ttk.Label(op_frame, text=op['b_median']).grid(row=4,column=5,sticky='sw',padx=5)
    except exception as e:
        return

    
btn=ttk.Button(root,text='Submit', command=show_result)
btn.pack()

root.mainloop()
#from_day.bind('<<ComboSelected>>', get_days)

