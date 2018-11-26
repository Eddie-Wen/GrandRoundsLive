import pyautogui, time
import csv
pyautogui.Pause=1
pyautogui.FAILSAFE=True
import shutil, os
import pyperclip
import random

def current_CDT():
    from datetime import datetime
    global now
    now = datetime.now()
    #print(now)
    #print('{:%m/%d/%Y}'.format(now))
    #print('{:%H:%M}'.format(now))
    #global visitmonth
    #visitmonth=('{:%m}'.format(now))
    #print(visitmonth)
    #global visitday
    #visitday=('{:%d}'.format(now))
    #print(visitday)
    #global visityear
    #visityear=('{:%Y}'.format(now))
    #print(visityear)
    global time_str
    time_str=('{:%H:%M:%S}'.format(now))
    #print('Current time_str is: ' + time_str)


#########################################################################################


def chance():
#Generate a random chance of demostrating copeptin levels higher or lower than 4.9 pmol/L.
#Therefore, generate a random chance of demonstrating the diagnosis of Primary Polydipsia or Central Diabetes Insipidus.   
    global chance
    for chance in range(1): #cdi stands for Central Diabetes Insipidus
        chance = random.randint(1,2)
        #print (chance)


def Input_copeptin_level():
    print ('What is the current copeptin level in pmol/Liter? For example 17.8\n')
    global copeptin
    copeptin = input()
    copeptin = copeptin.strip()
    copeptin = float(copeptin)
    current_CDT()
    global time_str
    print ('The Copeptin level before infusion was ' + str(copeptin)  + ' mmol/L at ' + str(time_str) + '\n')
    
def copeptin_pp():
#Diagnostic criteria for Primary Polydipsia is copeptin > 4.9pmol/L
    global copeptin
    for copeptin in range(1): #pp stands for Primary Polydipsia
        copeptin = round(random.uniform(0.1,7), 1)
        current_CDT()
        global time_str
        print ('The copeptin level measured last time was: ' + str(copeptin)  + ' pmol/L at ' + str(time_str)+ '\n')


def copeptin_cdi():
#Diagnostic criteria for Central Diabetes Insipidus is copeptin <= 4.9pmol/L
    global copeptin
    for copeptin in range(1): #cdi stands for Central Diabetes Insipidus
        copeptin = round(random.uniform(0.1,7), 1)
        current_CDT()
        global time_str
        print ('The copeptin level measured last time was: ' + str(copeptin)  + ' pmol/L at ' + str(time_str)+ '\n')


'''def copeptin_ndi():
#Diagnostic criteria for Nephrogenic Diabetes Insipidus is copeptin > 21.4pmol/L
    global copeptin_ndi
    for copeptin_ndi in range(1): #ndi stands for Nephrogenic Diabetes Insipidus
        copeptin_ndi = round(random.uniform(21.5,122), 1)
        print (copeptin_ndi)
'''

def Input_sodium_level():
    print ('What is the current sodium level in pmol/Liter? Normal range for sodium is between 135 and 145 mmol/liter. Just enter the number. For example: 135 \n')
    global sodium
    sodium = input()
    sodium = sodium.strip()
    sodium = float(sodium)
    current_CDT()
    global time_str
    print ('The sodium level before infusion was ' + str(sodium)  + ' mmol/L at ' + str(time_str)+ '\n')

def sodium_infusion():
#Diagnostic criteria for Primary Polydipsia is copeptin > 4.9pmol/L
    global sodium
    for sodium_infusion in range(1): #pp stands for Primary Polydipsia
        sodium_infusion = round(random.uniform(1,5), 1)
        current_CDT()
        print ('sodium level increased ' + str(sodium_infusion)  + ' mmol/L compared to 30 mins ago. \n')

        sodium =round((sodium + sodium_infusion),1)
        current_CDT()
        print ('Last Sodium level reading was ' + str(sodium)  + ' mmol/L measured at ' + str(time_str)+ '\n')


'''def sodium():
#Normal range for sodium is between 135 and 145mmol/liter.
    global sodium
    sodium=135
    sodium=sodium+3
    print ('The sodium level measured last time was: ' + str(sodium)  + ' mmol/liter at ' + str(time))'''

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\n')
        time.sleep(1)
        t -= 1
    print('(Simulation) 30 mins is up, time for next copeptin/sodium measurement. \n')

'''Copeptin Levels Associate with Cardiovascular Events
  in Patients with ESRD and Type 2 Diabetes Mellitus
  Wiebke Fenske,*† Christoph Wanner,*† Bruno Allolio,*† Christiane Drechsler,
  *† Katja Blouin,* Jürgen Lilienthal,‡ Vera Krane,corresponding author*†
  and for the German Diabetes, Dialysis Study Investigators.
  
  The median copeptin level was 81 pmol/L (interquartile range, 81 to 122 pmol/L).''' 

#########################################################################################

def log():
    global visitid
    global patientlastname
    global patientfirstname
    global dob
    global patientgender
    global bdrawtime
    global sodium
    global copeptin
    os.chdir('C:\\Users\Eddie Wen\PythonScripts\GrandRoundsLive\PPDD')    
    with open('log_infusion.csv', 'a', newline='') as csvfile:
        fieldnames = ['visitid', 'patientlastname', 'patientfirstname', 'dob', 'patientgender', 'serialnum', \
                      'bdrawtime', 'sodium', 'copeptin']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        writer.writerow({'visitid': visitid, 'patientlastname':patientlastname , 'patientfirstname':patientfirstname, 'dob': dob, 'patientgender': patientgender, 'serialnum': serialnum, \
                      'bdrawtime': bdrawtime, 'sodium': sodium, 'copeptin': copeptin})

'''def concurrent():#measures plasma osmolality, sodium, urea, and glucose every 30 minutes.

        
    try:
        
        if __name__ == '__main__':
            Thread(target = func1).start()
            Thread(target = func2).start()



    except KeyboardInterrupt:
        input('Press enter to continue')'''


    
def diagnosis():
    global diagnosis
    global conceptin
    global sodium

    if sodium >= 150: #unit mmol/liter
        if copeptin > 4.9: #unit: pmol/L
            diagnosis = 'Primary Polydipsia'
            print ('Because Copeptin level was higher than 4.9 pmol/L when Sodium level reached at 150mmol/L after the hypertonic saline infusion, this patient is diagnosed as Primary Polydipsia. \n') 

        else:
            diagnosis = 'Central Diabetes Insipidus'
            print ('Because Copeptin level was lower than 4.9 pmol/L when Sodium level reached at 150mmol/L after the hypertonic saline infusion, this patient is diagnosed as Central Diabetes Insipidus.\n')
    else:
        print ('Sodium level is still lower than 150 mmol/liter. Keep monitoring! \n')
        
        
    

##################################The above are functions
##################################The program run from here

try:
    input('Press enter to continue\n')

    global visitid
    global patientlastname
    global patientfirstname
    global dob
    global patientgender
    global bdrawtime
    #global copeptin
    #global time_str

    visitid = '62008888'
    patientlastname = 'Smith'
    patientfirstname = 'John'
    dob = '1/1/1950'
    patientgender = 'Male'

       
    print ('You have ruled out Diuretics and Uncontrolled Diabetes Mellitus.\n') 
    print ('The following steps will help with differential diagnosis of Primary Polydipsia, Central Diabetes Insipidus, Nephrogenic Diabetic Insipidus.\n')
    Input_copeptin_level()
    Input_sodium_level()


    if copeptin > 21.4: #unit: pmol/L
        print ('Copeptin level is higher than 21.4 pmol/L. It is likely to be Nephrogenic Diabetic Insipidus.\n')
        input('Press enter to continue')
        
    else:
        print ('You have ruled out Nephrogenic Diabetic Insipidus.\n')
        print ('The following steps will help you with differential diagnosis of Primary Polydipsia and Central Diabetes Insipidus.\n')
        print ('First, order a hypertonic saline infusion procedure.\n')
        input('Press enter to continue after initial 250 ml bolus infusion of 3% saline.\n')
        chance()    
        '''if (chance ==1):                    
            copeptin_pp()
            

        elif (chance ==2):
            copeptin_cdi()'''
            
        countdown(10)
        current_CDT()
        bdrawtime=time_str
        serialnum=1
        log()
        print ('Sodium measurement No. ' + str(serialnum)+ ': \n')

            
        while sodium <=150: 
            if (chance ==1):                    
                copeptin_pp()
                sodium_infusion()

            elif (chance ==2):
                copeptin_cdi()
                sodium_infusion()
                
            if sodium >150:                
                #print ('Measure copeptin level to differentiate Primary Polydipsia or Central Diabetes Insipidus as final diagnosis.')
                current_CDT()
                print ('The copeptin level measured last time was: ' + str(copeptin)  + ' pmol/L at ' + str(time_str)+ '\n')
                diagnosis()
                current_CDT()
                bdrawtime=time_str
                serialnum=serialnum+1
                log()
                print ('Sodium measurement reached 150 mmol/liter at Blood Draw No. ' + str(serialnum)+ '\n')
                input('Press enter to continue')
                break
            
            countdown(10)                     
            current_CDT()
            bdrawtime=time_str
            serialnum=serialnum+1
            log()
            print ('Sodium measurement No. ' + str(serialnum)+ ': \n')

        
         
    
except KeyboardInterrupt:
    input('Press enter to continue')

#########################################################################################

