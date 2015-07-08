from datetime import datetime
import jalali

def get_date(shams=True):
    td = str(datetime.date(datetime.today()))
    shamsi = jalali.Gregorian(td).persian_string().split('-')
    shamsi_months = ['Farvardin','Ordibehesht','Khordad','Tir','Mordad','Shahrivar','Mehr','Aban','Azar','Dey','Bahman','Esfand']
    miladi = td.split('-')
    miladi_moths = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

    if shams:
        ans = "emrooz "+shamsi[2]+" e "+shamsi_months[int(shamsi[1])-1]+" e "+shamsi[0]+" ast."
    else:
        ans = " emrooz "+miladi[2],' e '+miladi_moths[int(miladi[1])-1]+' e '+miladi[0]+' ast.'
    return ans

def get_time():
    x = datetime.now()
    xx = datetime.time(x)
    m='time:'+str(xx)
    return m[:13]

print get_date()
print get_time()
