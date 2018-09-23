from urllib import request
base_url='https://raw.githubusercontent.com/lyndadotcom/LPO_weatherdata/master/Environmental_Data_Deep_Moor_'
def get_web_data(YYYY_MM_DD):
    try:
        url=base_url + YYYY_MM_DD.split('_')[0] + '.txt'
        url_ob = request.urlopen(url)
        data=url_ob.read().decode(encoding='utf_8').split('\n')
        for line in data:
            fields=line.split()
            if (not fields[0].isalpha()):# and (fields[0]== YYYY_MM_DD): #This condn return records of given day only. changed it to have complete file loaded.
                op_rec=dict(date=fields[0],
                            time=fields[1],
                            wind_speed=fields[8],
                            air_temp=fields[2],
                            baro_press=fields[3])
                yield (op_rec)
    except Exception as e:
        yield (e)

if __name__=='__main__':
    #get_web_data('2012_01_01')
    a=1
    for i in get_web_data('2012_01_01'):
        print (i)
        a += 1
        if a >5:
                break

