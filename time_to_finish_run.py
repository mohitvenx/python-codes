#To find how long it takes for a person to complete a run
start_hour= int(input('Enter start hour: '))
start_minute= int(input('Enter start minute: '))
start_seconds= (start_hour*3600)+(start_minute*60)
easy_pace= int(input('Distance covered in easy pace: '))
#given time for easy pace is 8min 15sec 
easy_time= (easy_pace*8*60)+(easy_pace*15)
tempo_pace= int(input('Distance covered in tempo pace: '))
#given time for tempo pace is 7min 12sec
tempo_time= (tempo_pace*7*60)+(tempo_pace*12)
run_time= tempo_time + easy_time
#the time to reach home is run_time plus start time 
reach_seconds=start_seconds + run_time
reach_hour= reach_seconds//3600
reach_minute= (reach_seconds-(reach_hour*3600))//60
print('The time person reaches home for breakfast is',reach_hour,':',reach_minute,'am')
print('The time person reaches in seconds is ', reach_seconds)
print('The time to finish the complete run is ', run_time) 

