                                                ######################################
                                                            ## Submitted By- Ajay ####
                                                        ##########################################

################# Q1 ########################
#############################################

print('Question 1 -->')
Number= [386, 462, 47, 418, 907, 344, 236, 375,
         823, 566, 597, 978, 328, 615, 953, 345, 399, 162,
         758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
         626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892,
         894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
         958,743, 527]
j=[]
for i in Number:
    if i==237:
        break;
    elif i%2==0:
        j.append(i)
print('Even Numbers :', j)
print('-'*20)

######## Question 2 #####
print('Question 2 -->')
Color_list_1=set(['White','Black','Red'])
Color_list_2= set(["Red","Green"])
print('List 1 Colors',Color_list_1)
print('List 2 Colors',Color_list_2)
print('Different Color :-')
print(Color_list_1.difference(Color_list_2))
print('-'*20)

################Question 3 ###########
##Given a string check if it is Pangram or not.
##A pangram is a sentence containing every letter in the English Alphabet.
## Lowercase and Uppercase are considered the same.
print('Question 3 (pangram) -->')
UP=LO=0
In=input('Enter a string :--')
for T in In:
    if T.islower():
        LO  = LO+1
    if T.isupper():
         UP =UP+1
if LO>0 and UP>0:
        print('Input String is Pangram')
else :
    print('Input String not a Pangram')
print('-'*20)      
############### Question 4 ############
print('Question 4 (interger Input Only) -->')
IT= int(input('Enter a integer values only :-'))
num= (IT+ ((IT*10)+IT) + ((IT*100)+(IT*10)+IT))
print(num)
print('-'*20)

############### Question 5 ############
print('Question 5 -->')
L1=[]
L2=[]
Hash= input('Enter the input:-')
sp=Hash.split('#')
for k in sp[0].split():
    L1.append(k)
for k1 in sp[1].split():
    L2.append(k1)
print(L1)
print(L2)
print('-'*20)
############### Question 6 ############
############## sorting them alphabetically ###########
print('Question 6 -->')
Alp=input('Input Words :--')
Wor=Alp.split(",")
Wor.sort()
print((',').join(Wor))
print('-'*20)
############### Question 7 ############
############## highest marks ###########
print('Question 7 -->')
dc = {'Student': ['Rahul', 'Kishor', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
Flag=0
for i in dc['Marks']:
    if (i !=max(dc['Marks'])):
        Flag +=1
    elif (i ==max(dc['Marks'])):
        Flag=Flag
        break
print('Class Topper is :- ',dc['Student'][Flag])
print('-'*20)
############### Question 8 ############
############## calculate the number of letters and digits ###########
print('Question 8 -->')
CN=input('Enter the santance :-')
UP1=DN=0
for T1 in CN:
    if T1.isalpha():
         UP1 =UP1+1
    if T1.isdigit():
         DN =DN +1
         
if UP1>0 and DN >0:
        print('Latters is :',UP1)
        print('Digits is :',DN)
else :
    print('Please enter the string')
print('-'*20) 


############### Question 9 ############
############## Data Base ###########
print('Question 9 -->')
data = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

Ent=input('Enter the Subject :- ')
LT1=[]
NewData={}
for o in range(len(data['Subject'])):
    if (data['Subject'][o]!=Ent):
        continue
    else:
        LT1.append(o)
NewData['Name']=[]
NewData['Subject']=[]
NewData['Ratings']=[]
for o in LT1:
    NewData['Name'].append(data['Name'][o])
    NewData['Subject'].append(data['Subject'][o])
    NewData['Ratings'].append(data['Ratings'][o])
print('New Data',NewData)
print('-'*20)


############### Question 10 ############
############## Divide by 7 range 0 and n. ###########
Rag=int(input('Enter the range:-'))
Div_7=[ u for u in range (0,Rag) if (u%7==0)]
print('Divide by 7',Div_7)

def divcheck(Rag):
    for d in range(Rag):
        if d%7==0:
            Nick=True
        else:
            Nick=False
        print(d,Nick)

divcheck(Rag)
print('-'*20)

############### Question 11 ############
############## Robot ###########
import math
pos=[0,0]
movement={"UP":[0,1],
       "DOWN":[0,-1],
       "LEFT":[-1,0],
       "RIGHT":[1,0]}
## Controls
CTRL=["UP 5",
    "DOWN 3",
    "LEFT 3",
    "RIGHT 2"]
for inp in CTRL:
    part=inp.split()
    Mov=part[0]
    Val=part[1]
    if Mov in movement and Val.isnumeric():
        pos[0] += movement[Mov][0]*int(Val)
        pos[1] += movement[Mov][1]*int(Val)
    
CP=((math.sqrt(pos[0]**2+pos[1]**2)))
print('Distance')
print(CP,"from (0,0) to ", pos)
print('-'*20)
## with nearest integer
print('Nearest Distance')
print(round(CP),"from [0,0] to",pos)




    
    
