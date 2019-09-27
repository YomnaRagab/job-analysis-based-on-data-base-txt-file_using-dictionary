hand=open("data.txt","r")
data=hand.read() #read tha data from the file
hand.close()
words=data.split("\n") #split each line
data=dict()
for word in words: #make a dictionary ,each item is the job the gender with its weight
    data[word]=data.get(word,0)+1 #if the key (word) exists , then icrease its value by one , if it's not exist , creat new key by zero value and add 1.
#print (data)
d=data.items() #convert the dictionary into dictionary items to read the data
lst=list()
for key,val in d: #make a list with 2 members , the first member is the job+gender the another is their weight
    lst.append([key,val])
#print(lst)
job=input("Enter the job title nurs or cop:") #get the job from the user
tot_job=0 #get the total number for who work this job
for i in lst:
    if job in i[0]: # if the job is in the first element of the list (which has the job name and the gender)
        tot_job+=i[1] #increase the counter by one
#print(tot_job)
gender=input("Enter the gender wom or man:") #get the gender
total_gender_job=0
for i in lst:
    if job+" "+gender in i[0]: #search for the job and the gender in the list to calculate its precentege
        total_gender_job=i[1] #we get the gender+job weight
        break               #so break
#print(total_gender_job)
if(gender=="wom"):
    print("This job for women",(total_gender_job/tot_job)*100) #divide the total people who work this job by the gender number who work this job and get the precentage
    print("This job for men",100-(total_gender_job/tot_job)*100) #the another gender precentage =100-the previous one
else:
    print("This job for men",(total_gender_job/tot_job)*100)
    print("This job for womne",100-(total_gender_job/tot_job)*100)
if (total_gender_job/tot_job>0.5):
    print(job,"is good for",gender)
else:
    print(job,"is not good for",gender)
