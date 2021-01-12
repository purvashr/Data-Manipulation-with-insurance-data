#Importing packages....
import pandas as pd
import sys
import numpy as np

#Taking input from command line to initialise input variables

dateFormatType = sys.argv[1]
inputPath= sys.argv[2]
outputPath= sys.argv[3]

#Change the date formats of Birth and Death Date as per the input

if dateFormatType==1:
    df=pd.read_csv(inputPath,parse_dates=['BENE_BIRTH_DT'])
    df['BENE_BIRTH_DT']=df['BENE_BIRTH_DT'].apply(lambda x:x.date().strftime('%d/%m/%Y'))
    df['BENE_DEATH_DT']=df['BENE_DEATH_DT'].apply(lambda x:pd.to_datetime(str(x)[0:8]).date().strftime('%d/%m/%Y') if np.isnan(x)== False else np.nan)

elif dateFormatType==2:
    df=pd.read_csv(inputPath,parse_dates=['BENE_BIRTH_DT'])
    df['BENE_BIRTH_DT']=df['BENE_BIRTH_DT'].apply(lambda x:x.date().strftime('%m/%d/%Y'))
    df['BENE_DEATH_DT']=df['BENE_DEATH_DT'].apply(lambda x:pd.to_datetime(str(x)[0:8]).date().strftime('%m/%d/%Y') if np.isnan(x)== False else np.nan)

else:
    df=pd.read_csv(inputPath,parse_dates=['BENE_BIRTH_DT'])
    df['BENE_BIRTH_DT']=df['BENE_BIRTH_DT'].apply(lambda x:x.date().strftime('%Y/%m/%d'))
    df['BENE_DEATH_DT']=df['BENE_DEATH_DT'].apply(lambda x:pd.to_datetime(str(x)[0:8]).date().strftime('%Y/%m/%d') if np.isnan(x)== False else np.nan)

#Adding today's date
df['Today']=pd.to_datetime('today').date()

#Adding column where if BENE_DEATH_DT is empty column is True
df['DeathFlag']='F'
df.loc[df['BENE_DEATH_DT'].isna() == False,['DeathFlag']]='T'

#Adding 12 digit index column 
a=[]
b=100000000000
for i in range(0,df.shape[0]):
    a.append("{0:010d}".format(b))
    b +=1
df['index']=a

#Saving output file
df.to_csv(outputPath,index=False)
    



        

