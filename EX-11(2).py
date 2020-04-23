class time:
    def __init__(obj,h,m,s):
        obj.hour = h
        obj.minute = m
        obj.second = s
    def show(obj,ruz):
        obj.date = ruz
        return(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
    def number_of_seconds(obj):
        return(obj.hour*3600+obj.minute*60+obj.second)
    def sub(obj,obj2):
        obj.hour -= obj2.hour
        obj.minute -= obj2.minute
        obj.second -= obj2.second
    def kam_kardan(obj1,hh,mm,ss):
        obj.hour -= hh
        obj.minute -= mm
        obj.second -= ss
