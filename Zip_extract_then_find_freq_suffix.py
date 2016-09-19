#http://stackoverflow.com/questions/2212643/python-recursive-folder-read
# 4 spaces to indent
#if zip/RAR files are encrypted, user need to press Enter manualy to skip

import os
import sys
import subprocess
import collections
import pandas as pd
import matplotlib
import seaborn as sns

rootdir = sys.argv[1]
ExtractDir = sys.argv[2]

all_filename=[]
all_fileext=[]
all_filewords=[]

print "When program pauses (encountering zip/RAR files that are encrypted), user need to press Enter manualy to skip/abort"

for folder, subs, files in os.walk(rootdir):
    
        for filename in files:
            
                  list1=filename.split('.')
                  l2=["rar","zip"]#set()
                  if list1[-1] in l2:#
                     try:
                       subprocess.check_call(["7z.exe","x",os.path.join(folder,filename) ,"-r","-O"+ExtractDir])
                     except subprocess.CalledProcessError, e:
                       print "Ping stdout output:\n", e.output
                  else:
                     src=open(os.path.join(folder, filename), 'r')
                     dest=open(os.path.join(ExtractDir, filename), 'w')  #What if file duplicate??
                     dest.write(src.read())
                     dest.close()
                     src.close()


                

for folder, subs, files in os.walk(ExtractDir):
   for filename in files:

      list_words=''.join(list1[0:filename.count('.')]).replace(' ','_').split('_')  #remove suffix. Underscore, not space is dividing file names
      all_filewords.append(list_words) #file title,how to append one element by 1
      all_filename.append(list1[0:filename.count('.')])
      all_fileext.append(list1[-1])
                
                 
counter=collections.Counter(all_fileext)


df=pd.DataFrame([counter.values(),counter.keys()])
df2=df.transpose()
df2.columns=['cnt','fname']
df3=df2.sort_values(['cnt'],ascending=[True])
print df3
df2.head()
ax = sns.barplot(x="fname", y="cnt", data=df3)
sns.plt.show()
