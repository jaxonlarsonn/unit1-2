year=int(input())
century=(year//100)+1
century2=(year//100)
year1=year%100

if (year1==0) :
    print(century2)
elif year1>0:
    print(century)

