#To find the differnce between start and finish time
hour_start = int(input('Enter start hour: '))                #Enter the hour at which starting 
minutes_start = int(input('Enter start minute: '))           #Enter the minutes at which starting
seconds_start = int(input('Enter start seconds: '))         #Enter the seconds at which starting
hour_finish = int(input('Enter finish hour: '))              #Enter the hour at which ending
minutes_finish = int(input('Enter finish minute: '))         #Enter the minutes at which ending
seconds_finish = int(input('Enter finish seconds: '))        #Enter the seconds at which ending
hour_start*=3600                                             #Converting hours to seconds
minutes_start*=60                                            #Converting minutes to seconds
sum_start=hour_start+minutes_start+seconds_start
hour_finish*=3600                                            #Converting hours to seconds
minutes_finish*=60                                           #Converting minutes to seconds
sum_finish=hour_finish+minutes_finish+seconds_finish
print(sum_finish-sum_start)                                  #the difference between start and finish






