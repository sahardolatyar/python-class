class time:
    def __init__(obj,h,m,s):
        obj.hour = h
        obj.minute = m
        obj.second = s
    def show(obj,ruz):
        obj.date = ruz
        return (obj.hour)+':'+str(obj.minute)+':'+str(obj.second)
    def number_of_seconds(obj):
        return (obj.hour*3600+obj.minute*60+obj.second)
