def add_time(start,dura,d=None):
        noon=start[-2:]
        p=dura.index(":")
        hourd=int(dura[:p])
        minuted=int(dura[p+1:])
        q=start.index(":")
        hours=int(start[:q])
        minutes=int(start[q+1:q+3])
        days=hourd//24
        rem=hourd%24
        if noon=="PM":
                if hours==12:
                        value=720+minutes
                else:
                        value=((12+hours)*60)+minutes
        elif noon=="AM":
                if hours==12:
                        value=minutes
                else:
                        value=(hours*60)+minutes
        if noon=="PM":
                valued=(rem*60)+minuted
                if 1440<valued+value<2160:
                        days+=1
                        nd=valued+value-1440
                        nd_hour=nd//60
                        nd_minute=nd-(nd_hour*60)
                        noon="AM"
                        if nd_hour==0:
                                nd_hour="12"
                elif valued+value>2160:
                        days+=1
                        nd=valued+value-2160
                        nd_hour=nd//60
                        nd_minute=nd-(nd_hour*60)
                elif valued+value<1440:
                        nd=valued+value-720
                        nd_hour=nd//60
                        nd_minute=nd-(nd_hour*60)
                elif valued+value==1440:
                        nd_hour=12
                        nd_minute="00"
                        noon="AM"
                        days+=1
                elif valued+value==2160:
                        days+=1
                        nd_hour=12
                        nd_minute="00"
        elif noon=="AM":
                valued=(rem*60)+minuted
                if valued+value<720:
                        nd_hour=(valued+value)//60
                        nd_minute=(valued+value)%60
                elif 720<valued+value<1440:
                        nd=valued+value-720
                        nd_hour=nd//60
                        nd_minute=nd-(nd_hour*60)
                        noon="PM"
                        if nd_hour==0:
                                nd_hour="12"
                elif valued+value>1440:
                        days+=1
                        nd=valued+value-1440
                        nd_hour=nd//60
                        nd_minute=nd-(nd_hour*60)
                elif valued+value==720:
                        nd_hour=12
                        nd_minute="00"
                        noon="PM"
                elif valued+value==1440:
                        nd_hour=12
                        nd_minute="00"
                        days+=1
        if len(str(nd_minute))==1:
                nd_minute="0"+str(nd_minute)
        if days==0:
                day=None
        elif days==1:
                day="(next day)"
        else:
                day="("+str(days)+" days later)"
        arr=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        if d!=None:
                d=d.lower()
                stri=arr[arr.index(d)+(days%7)]
        elif d==None:
                stri=None
        s=""
        s=str(nd_hour)+":"+str(nd_minute)+" "+noon
        if stri!=None:
                caps=stri[0].upper()
                stri=caps+stri[1:]
                s=s+", "+stri
        if day!=None:
                s=s+" "+day
        return s                  
print(add_time("6:30 PM", "205:12"))
        
        
