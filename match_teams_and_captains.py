#given list of captains and teams(in respective order) assign them to IPL Teams

captain=['Virat Kohli','Dhoni','Rohit Sharma','K L Rahul']
team=['RCB','CSK','MI','KXIP']
res=zip(captain,team)
print(list(res))        #list cause zip is lazy function

