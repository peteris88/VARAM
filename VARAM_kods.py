import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook
from pandas import *
from datetime import datetime

#no 14-15 kolonnas izvilk to, cik ilgi viņs ir bijis atvērts
data = pd.read_excel("CherryPicked_Dati/Studentam_2_03_22.xlsx","Rezultāti")
data2 = pd.read_excel("CherryPicked_Dati/Studentam_2_03_22.xlsx","Izsludinātie")
x=0
y=0
iepirkumiRAW = []
#13 N kolonna pasaka, vai ir mazs skaits
#9 J kolonna pasaka, vai ir 
iepirkumi=[]
iepirkumiPieteikušies = []
pagaiduIepirkums = ""
global iepirkumiKopuma
iepirkumiKopuma=0

global maxDienas
global maxPieteikumi
maxDienas = 0
maxPieteikumi = 0

rezultejosieDati = [[]]
dienuSpraudnis = []

for i in range(0,86):
    dienuSpraudnis.append(0)

def createArray(x,y):
    for i in range(0,x+1):
        rezultejosieDati.append([])
        for j in range(0,y+1):
            rezultejosieDati[i].append(0)
    #print(rezultejosieDati)
#createArray(85,69)     
global ievietotoSkaits      
ievietotoSkaits=0

def makeExcel():
    columns=[]
    content=[]
    tempContent=[]
    for i in range(len(rezultejosieDati)):
        if(i==0):
            columns = [rezultejosieDati[i][0]]
            #content = [rezultejosieDati[i][1]]
        else:
            columns = columns + [rezultejosieDati[i][0]]
            #content = content + [rezultejosieDati[i][1]]
    
    for j in range(0,86):
        tempContent=[]
        for i in range(len(rezultejosieDati)):
            tempContent=tempContent + [0]
        content = content+[tempContent]            
        print(tempContent)
    for j in range(0,86):
        for i in range(len(rezultejosieDati)):
            content[j][i]=rezultejosieDati[i][1][j]
            #else:
            #    tempContent = tempContent + [rezultejosieDati[i][1][j]]
    content
    print(columns)
    print(content)
    df = pd.DataFrame(content, columns = columns)
    df.to_excel("rezultejosieDatiMazinatsSkaits.xlsx")
    print(df)
    
    print()

def insertInList(pieteikumi,dienas):
    global rezultejosieDati
    global ievietotoSkaits
    ievietotoSkaits+=1
    #if(ievietotoSkaits%30==0):
    #    print(ievietotoSkaits)
    #    makeExcel()
    #    print()
    ievietoja=0
    if(len(rezultejosieDati)==1 and not rezultejosieDati[0]):
        rezultejosieDati = [[pieteikumi,dienuSpraudnis.copy()]]
        rezultejosieDati[0][1][dienas] += 1 #rezultejosieDati[0][dienas]+
        return 0
    for i in range(len(rezultejosieDati)):
        if(rezultejosieDati[i][0]==pieteikumi):
            #print(rezultejosieDati)
            rezultejosieDati[i][1][dienas]=rezultejosieDati[i][1][dienas]+1
            #print(rezultejosieDati)
            ievietoja=1
            return 0
        elif(pieteikumi<rezultejosieDati[i][0]):
            if(i==0):
                #print(rezultejosieDati)
                rezultejosieDati = [[pieteikumi,dienuSpraudnis.copy()]]+rezultejosieDati[i:]
                #print(rezultejosieDati)
                rezultejosieDati[i][1][dienas] = rezultejosieDati[i][1][dienas]+1
                return 0
                #print(rezultejosieDati)
            else:
            #    #print(rezultejosieDati)
                rezultejosieDati = rezultejosieDati[:i]+[[pieteikumi,dienuSpraudnis.copy()]]+rezultejosieDati[i:]
            #    #print(rezultejosieDati)
                rezultejosieDati[i][1][dienas] = rezultejosieDati[i][1][dienas]+1
                return 0
            #    #print(rezultejosieDati)
            #elif(i==len(rezultejosieDati)):
            #    #print(rezultejosieDati)
            #    rezultejosieDati = rezultejosieDati.append([pieteikumi,dienuSpraudnis.copy()])
            #    rezultejosieDati[i][1][dienas] = rezultejosieDati[i][1][dienas]+1
            #    return 0
            #    #print(rezultejosieDati)
        elif(i<len(rezultejosieDati)-1):
            if(pieteikumi>rezultejosieDati[i][0] and pieteikumi<rezultejosieDati[i+1][0]):
                #print(rezultejosieDati)
                rezultejosieDati = rezultejosieDati[:i+1]+[[pieteikumi,dienuSpraudnis.copy()]]+rezultejosieDati[i+1:]
                #print(rezultejosieDati)
                rezultejosieDati[i][1][dienas] = rezultejosieDati[i][1][dienas]+1
                return 0
                #print(rezultejosieDati)
        elif(i==len(rezultejosieDati)-1):
            #print(rezultejosieDati)
            rezultejosieDati = rezultejosieDati+[[pieteikumi,dienuSpraudnis.copy()]]
            #print(rezultejosieDati)
            rezultejosieDati[i+1][1][dienas] = rezultejosieDati[i+1][1][dienas]+1
            return 0
            #print(rezultejosieDati)
            
            #elif(i==len(rezultejosieDati)):
            #    print(rezultejosieDati)
            #    rezultejosieDati = rezultejosieDati.append([pieteikumi,dienuSpraudnis.copy()])
            #    rezultejosieDati[i][1][dienas] = rezultejosieDati[i][1][dienas]+1
            #    print(rezultejosieDati)
                
        

def AnalThis(i,j):
    #print(str(data.iloc[i,2])+" "+str(data2.iloc[j,2])+"|"+str(data.iloc[i,7])+" "+str(data2.iloc[j,8]))
    #print(str(data.iloc[i,3])+"|"+str(data2.iloc[j,3])+"|"+str(data2.iloc[j,4]))
    global iepirkumiKopuma
    iepirkumiKopuma+=1
    IzsDatStr=str(data2.iloc[j,3])  #Izsludināšanas  Datums
    IesDatStr=str(data2.iloc[j,4])  #Piedāvājuma iesniegšanas termiņš
    PubDatStr=str(data.iloc[i,3])   #Rezultātu Publikācijas Datums
    
    IzsDat = datetime.strptime(IzsDatStr, '%Y-%m-%d %H:%M:%S')
    IesDat = datetime.strptime(IesDatStr, '%Y-%m-%d %H:%M:%S')
    PubDat = datetime.strptime(PubDatStr, '%Y-%m-%d %H:%M:%S')
    piedavataisLaiks = IesDat-IzsDat
    print(str(piedavataisLaiks.days) + " | " + str(data.iloc[i,9])+" |  "+str(i)+"/"+str(data.shape[0])+"    | Kopumā apskatīti iepirkumi līdz šim:"+str(iepirkumiKopuma))
    #x=int(piedavataisLaiks.days)
    #y=int(data.iloc[i,9])
    #rezultejosieDati[x][y]=rezultejosieDati[x][y]+1
    global maxDienas
    global maxPieteikumi
    daudzDaluPieteikumi=0
    if(i<data.shape[0]-1):
        if(data.iloc[i,2]==data.iloc[i+1,2]):
            j=i+1
            daudzDaluPieteikumi = data.iloc[i,9]
            print(str(data.iloc[i,2]))
            print("    Daudzdalu pieteikums ar "+str(daudzDaluPieteikumi)+" pieteikumiem. šajā iterācijā "+ str(data.iloc[i,9])+" pieteikumu")
            while(data.iloc[i,2]==data.iloc[j,2]):
                daudzDaluPieteikumi += data.iloc[j,9]
                print("    Daudzdalu pieteikums ar "+str(daudzDaluPieteikumi)+" pieteikumiem. šajā iterācijā "+ str(data.iloc[j,9])+" pieteikumu")
                j=j+1
            insertInList(daudzDaluPieteikumi,int(piedavataisLaiks.days))
            if(maxPieteikumi < daudzDaluPieteikumi):
                maxPieteikumi = daudzDaluPieteikumi
            
        insertInList(data.iloc[j,9],int(piedavataisLaiks.days))
        if(maxDienas < piedavataisLaiks.days):
            maxDienas = piedavataisLaiks.days
        if(maxPieteikumi < data.iloc[i,9]):
            maxPieteikumi = data.iloc[i,9]
    if(maxDienas < piedavataisLaiks.days):
        maxDienas = piedavataisLaiks.days
    if(maxPieteikumi < data.iloc[i,9]):
        maxPieteikumi = data.iloc[i,9]
    
    #9 J kolonna pasaka, cik cilv ir pieteikušies.
    
    

for i in range(0,int(data.shape[0])):
    firstComp = data.iloc[i,2]          #2. kolonnā "data" ir ID kods
    if(data.iloc[i,2]==data.iloc[i-1,2]):
        continue
    for j in range(0,int(data2.shape[0])):
        secondComp =  data2.iloc[j,2]   #2. kolonnā "data2" ir ID kods
        if(firstComp == secondComp):
            AnalThis(i,j)
            break
print(maxDienas)        #85
print(maxPieteikumi)    #4347

print(rezultejosieDati)
print(rezultejosieDati)
makeExcel()
df = pd.DataFrame(rezultejosieDati)
df.to_excel("rezultejosieDati2.xlsx")
exit()
for i in range(0,int(data.shape[0])):
    temp = data.iloc[i,2]
    pieteikumi = data.iloc[i,9]
    if(temp!=pagaiduIepirkums):
        pagaiduIepirkums=temp
        iepirkums = {}
        iepirkums["ID"]=str(temp)
        iepirkums["pieteikumi"]=int(pieteikumi)
        x=x+1
        iepirkumiRAW.append(iepirkums)
    else:
        iepirkumiRAW[x-1]['pieteikumi'] += int(pieteikumi)
iepirkumi.append(iepirkumiRAW[0])       # obligāti jāpievieno pirmais elements, citādi otrais for loops nestrādās
y=y+1
for i in range(1,x):                    # šis cikls iziet cauri "iepirkumiRAW", kurā ir duplikāti
    atrada = 0 
    for j in range(0,y):                # iziet cauri "iepirkumi", kurā nebūs duplikātu
        if iepirkumiRAW[i]['ID'] == iepirkumi[j]['ID']:
            atrada = 1                  # ja atrod, tad lai nepievieno "iepirkumi"
            #print('-----before-----')
            #print(iepirkumi[j]['pieteikumi'])
            #print(iepirkumiRAW[i]['pieteikumi'])
            iepirkumi[j]['pieteikumi'] += iepirkumiRAW[i]['pieteikumi'] # bet jāpieskaita pietekumi
            #print('-----after-----')
            #print(iepirkumi[j]['pieteikumi'])
            #print(iepirkumiRAW[i]['pieteikumi'])
    if(atrada == 0):                    # ja atrada ==0, tad tāda vēl nav "iepirkumi" un tas jāpievieno sarakstam
        iepirkumi.append(iepirkumiRAW[i])
        y=y+1



print("x="+str(x)+" y="+str(y))


#pēdējā pārbaude, ja tu maini kko kodā un viņš vairs nestrādā, tad šis tiks izvadīts
for i in range(0,y):
    for j in range(0,i-1):
        if iepirkumi[i]['ID'] == iepirkumi[j]['ID']:
            print('apsveicu, tu samisējies!')
            print(iepirkumi[i])
            print(iepirkumi[j])
            exit()
