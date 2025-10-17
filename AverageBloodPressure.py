from statistics import mean

readings= input("Enter BP readings separated by space: \n").split()

split_list=[]
systolic=[]
diastolic=[]

for r in readings:
    split_list+=r.split("/")

systolic = split_list[0::2]
diastolic = split_list[1::2]

average_sys= mean(int(r) for r in systolic)
average_dia= mean(int(r) for r in diastolic)

print(f"Average BP: {int(average_sys)}/{int(average_dia)}")


    
