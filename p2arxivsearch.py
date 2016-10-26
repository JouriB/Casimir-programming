import urllib
import numpy as np
import matplotlib as plt
%matplotlib inline
# Request library
#Specify URL for search

#Searching for a title
title='novel'
maxresults='10'

def readarxiv(title,maxresults=10):
    url = 'http://export.arxiv.org/api/query?search_query=ti:'+ title + '&start=0&max_results=' + maxresults
    data = urllib.urlopen(url).read()
    return data

#print (data)

# read title, abstract, authors

# search for title (novel, revisit)

def finddate(data):
    dates=[]
    lines=data.split('\n')
    for n in range(len(lines)):
        ind=lines[n].find('<published>')
        if ind != -1:
            dates.append(lines[n][ind+11:ind+21])
    return dates

dates_novel=finddate(readarxiv('novel',maxresults))
dates_revisit=finddate(readarxiv('novel',maxresults))

print(dates_revisit)
matplotlib.plot([0,1],[1,1])

#Search for specific author
author='Kouwenhoven_L'

url = 'http://export.arxiv.org/api/query?search_query=au:'+ author + '&start=0&max_results=10000'
data = urllib.urlopen(url).read()
words=data.split() # extract the words from the query

sumstart=[]
sumend=[]
for i in range(len(words)-1):
    if words[i]=="<summary>": # look up the word <summary> and save the index
        sumstart.append(i)
    elif words[i]=="</summary>": # look up the word </summary> and save the index
        sumend.append(i)       
sumstart=np.array(sumstart) #make a numpy array for processing
sumend=np.array(sumend)
abswcount=sumend-sumstart -1 # count the number of words per abstract

#plot the data as 
plt.hist(abswcount)
plt.xlabel("number of words in abstract")
plt.ylabel("number of papers")