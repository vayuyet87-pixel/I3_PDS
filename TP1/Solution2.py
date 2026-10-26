#Calculate
total_sec=9875
hour=total_sec//3600
minutes=(total_sec % 3600)//60
second=(total_sec %3600) % 60
print(hour,minutes,second)
#check

print("Check:",(hour*3600)+(minutes*60)+second==total_sec)

#Test code with 3600,59 aand 86399 seconds
#case1
total_sec=3600  
hour=total_sec//3600
minutes=(total_sec % 3600)//60
second=(total_sec %3600) % 60
print(hour,minutes,second)
#case2
total_sec=59
hour=total_sec//3600
minutes=(total_sec % 3600)//60
second=(total_sec %3600) % 60
print(hour,minutes,second)
#case3
total_sec=86399
hour=total_sec//3600
minutes=(total_sec % 3600)//60
second=(total_sec %3600) % 60
print(hour,minutes,second)