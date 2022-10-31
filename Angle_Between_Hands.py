s=(input())
h,m=map(int,s.split(":"))
hr=m*0.5+h*30
mi=m*6
t=abs(hr-mi)
print(min(t,360-t))