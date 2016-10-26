import urllib
import matplotlib
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

#    return

# count words in the abstract