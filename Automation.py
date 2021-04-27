#----------------------------------------------------------------------------Automated.py----------------------------------------------------------------------------#
#Importing modules:os,shutil,time,dropbox,datetime,timedelta(from datetime) and random
import os 
import shutil
import time
import dropbox
import datetime
from datetime import timedelta 
import random





#Formal introduction and requesting of inputs 
print("Welcome to Automation.py. Tired of constantly creating files monotonously?Well, drear no more, for Automation.py will save the day! Generate files everyday, automatically!")
print("The guidelines mentioned below serve the purpose of ensuring quality service to our customers. Hence, we request you to adhere to them.")
print("1.When mentioning the file locations and folder names, please refrain for using a slash at the end.")
print("2.While the entering the primary location for the files, a file as the end of the path is highly unrecommended as it causes errors to the program, hence, a folder as the end is preferred")
print("3.Avoid using inappropriate symbols, such as providing letters and mathematical constants and symbols such as '/\*:' ")

folder_name=input("Please enter the name of the  folder in which you want to generate the folders:")
main_path=input("Please enter the path where you want to store the files under the mentioned circumstances:")
interval=int(input("Please enter the time interval between the creation of two folders(in seconds):"))

print("As a mandatory feature, we also upload the folders to Dropbox for backup. Hence, owning a Dropbox account is imperative.")
print("If you lack a Dropbox Developer's Account, please visit 'https://www.dropbox.com/developers' ")
access_token=input("Please enter your dropbox access token here:")
dbx=dropbox.Dropbox(access_token) 
print("Thank You for using Automated.py")  
   




#The main function: Upoads files to Dropbox and creates files
def CreateFolderAutomatically(folder_name,times,delta_time,formatted_final_time,path_eligible_formatted_final_time):
        current_path=main_path
        #To test wether mentioned path exists or not
        if(os.path.exists(current_path+"/"+folder_name)):
            unique_id=random.randint(0,100000000)
            os.mkdir(current_path+"/"+folder_name+"/"+path_eligible_formatted_final_time+str(unique_id))
            with open(current_path+"/"+folder_name+"/"+path_eligible_formatted_final_time+str(unique_id)+"/Automated.txt",'w') as f:
                f.write("The folders and sub-folders which contain this file are autonomously generated")
            with open(current_path+"/"+folder_name+"/"+path_eligible_formatted_final_time+str(unique_id)+"/Automated.txt",'rb') as e:    
                dbx.files_upload(e.read(),"/"+folder_name+"/"+str(formatted_final_time)+"/Automated.txt",mode=dropbox.files.WriteMode.overwrite)   
        else:
            os.mkdir(current_path+"/"+folder_name)
            unique_id=random.randint(0,100000000)
            os.mkdir(current_path+"/"+folder_name+"/"+path_eligible_formatted_final_time+str(unique_id))
            with open(current_path+"/"+folder_name+"/"+path_eligible_formatted_final_time+str(unique_id)+"/Automated.txt",'w') as f:
                f.write("The folders and sub-folders which contain this file are autonomously generated")
            with open(current_path+"/"+folder_name+"/"+path_eligible_formatted_final_time+str(unique_id)+"/Automated.txt",'rb') as e:    
                dbx.files_upload(e.read(),"/"+folder_name+"/"+str(formatted_final_time)+"/Automated.txt",mode=dropbox.files.WriteMode.overwrite) 
#Function Main, for calling all subordinated functions
def main():
    #Declaration, conversion and printing of the initial time
    start_time=datetime.datetime.now()
    start_time_timestamp=datetime.datetime.timestamp(start_time)
    print(start_time_timestamp)
    
    
    
    #Never ending while loop
    while True:
        #Ensuring that the code is executed at the interval
        if(round(time.time()-start_time_timestamp)%interval==0):
            times=datetime.datetime.now()
            delta_time=timedelta(seconds=-(interval))
            final_time=times-delta_time
            formatted_final_time=final_time.strftime("%d:%H:%M:%S")
            print("Current time is "+str(times.strftime("%d:%H:%M:%S")))
            print("Next file will be created at "+str(formatted_final_time))
            path_eligible_formatted_times=times.strftime("%d-%m-%Y @ %H hours %M mins %S sec")
            final_time_timestamp=datetime.datetime.timestamp(final_time)
            #Calling the main function "CreateFolderAutomatically"
            CreateFolderAutomatically(folder_name,times,delta_time,formatted_final_time,path_eligible_formatted_times)
#Calling the Function Main        
main()
#----------------------------------------------------------------------------Automated.py----------------------------------------------------------------------------#