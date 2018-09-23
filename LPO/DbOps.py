import sqlite3
import GetWebData as web
import datetime
import time
import statistics
#from datetime import timedelta

#what should be the path of the .db file

def_db='lpo_data.db'
def create_db(db_name=def_db):
    global db_in_use
    db_in_use=db_name
    db_ob=sqlite3.connect(db_name)
    cur=db_ob.cursor()
    cur.execute('''CREATE TABLE if not exists lpom (
                    date       text(10) not null,
                    time       text(8)  not null,
                    wind_speed real,
                    air_temp   real,
                    bar_press  real,
                    primary key(date,time))
                ''')
    db_ob.commit()
    db_ob.close()
    
def load_data(YYYY_MM_DD):
    year=YYYY_MM_DD.split('_')[0]
    db_ob=sqlite3.connect(db_in_use)
    cur=db_ob.cursor()
    try:
        yr_data_cnt=cur.execute('select count(*) from lpom where substr(date,1,4) = ? ',(year,))
        if yr_data_cnt.fetchone()[0] > 0:
            print("Data of the year {} is present in the DB".format(year))
        else:
            web_data=web.get_web_data(YYYY_MM_DD)
            data_list=[]
            starttime = time.time()
            i = 0
            for rec in web_data:
                data_list.append(rec)
                i += 1
                #Following code can be used to have commit frequency as 10000.
                #print(i, " => ", rec)
                #if i == 10000:
                #    print("10000 records fetched")
                #    cur.executemany('insert into lpom values (:date,:time,:wind_speed,:air_temp,:baro_press)',data_list)
                #    db_ob.commit()
                #    data_list=[]
            else:
                #print("EXECUTE COMMIT IN ELSE")
                cur.executemany('insert into lpom values (:date,:time,:wind_speed,:air_temp,:baro_press)',data_list)
                db_ob.commit()
            endtime=time.time()
            print("Time taken to load {} records : {}".format(i,datetime.timedelta(seconds=endtime-starttime)))
            db_ob.close()   
    except Exception as e:
        db_ob.close()   
        print("Load function failed at i = {}, error {}".format(i, e))
        
#Function to calc mean median
def calc_reqd_values(from_YYYY_MM_DD, to_YYYY_MM_DD):
    db_ob=sqlite3.connect(db_in_use)
    cur=db_ob.cursor()
    return_data={}
    #get list of wind speeds
    wind_speed=[]
    w=cur.execute('select wind_speed from lpom where date between ? and ?',(from_YYYY_MM_DD,to_YYYY_MM_DD))
    for i in w:
        wind_speed.append(i[0])
    #print("Wind speeds collected : {}".format(len(wind_speed)))
    w_mean=round(statistics.mean(wind_speed),3)
    w_median=round(statistics.median(wind_speed),3)
    
    #get list of air temps
    air_temps=[]
    a=cur.execute('select air_temp from lpom where date between ? and ?',(from_YYYY_MM_DD,to_YYYY_MM_DD))
    for i in a:
        air_temps.append(i[0])
    #print("air temps collected : {}".format(len(air_temps)))
    a_mean=round(statistics.mean(air_temps),3)
    a_median=round(statistics.median(air_temps),3)

    #get list of baro press
    baro_press=[]
    b=cur.execute('select bar_press from lpom where date between ? and ?',(from_YYYY_MM_DD,to_YYYY_MM_DD))
    for i in b:
        baro_press.append(i[0])
    #print("baro press collected : {}".format(len(baro_press)))
    b_mean=round(statistics.mean(baro_press),3)
    b_median=round(statistics.median(baro_press),3)
    db_ob.close()
    return_data={'w_mean':w_mean,'w_median':w_median,'a_mean':a_mean,'a_median':a_median,'b_mean':b_mean,'b_median':b_median}
    return (return_data)
    
    
      
if __name__=='__main__':
   create_db('test1.db')
   load_data('2012_01_01')
   print(calc_reqd_values('2012_01_01','2012_01_01'))
   dbconn=sqlite3.connect('test1.db')
   cur=dbconn.cursor()
   cnt=cur.execute('select count(*) from lpom')
   print(f"Number of records present in the db = {cnt.fetchone()[0]}")
   dbconn.close()
