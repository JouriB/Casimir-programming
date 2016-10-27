import urllib
import numpy as np
#import matplotlib as plt
#%matplotlib inline

def readarxiv_title(title,maxresults):
    """
    This function searches the arxiv for a specific word in the title
    title has to be given in the form  'title' (example: 'novel')
    maxresults can be any integer and will limit the output number
    data is the HTML string returned
    """
    url = 'http://export.arxiv.org/api/query?search_query=ti:'+ title + '&start=0&max_results=' + str(maxresults)
    data = urllib.urlopen(url).read()
    return data

def readarxiv_author(author,maxresults):
    """
    This function searches the arxiv for a specific author
    author has to be given in the form  'surname_initial' (example: 'Kouwenhoven_L')
    maxresults can be any integer and will limit the output number (although here it does not work)
    data is the HTML string returned
    """
    maxresults=2
    url = 'http://export.arxiv.org/api/query?search_query=au:'+ author + '&start=0&max_results=' + str(maxresults)
    data = urllib.urlopen(url).read()
    return data

def finddate(data):
    """
    data is HTML string
    search for specific string in every line
    save the date found
    """
    dates=[]
    lines=data.split('\n')
    for n in range(len(lines)):
        ind=lines[n].find('<published>')
        if ind != -1:
            dates.append(lines[n][ind+11:ind+21])
    return dates

def abstract_word_count (data):
    """
    This function searches the data file for abstracts and count the number of words in it.
    data is the HTML string
    abswcount is a numpy array with an entry for every abstract.    
    We could split this function up in looking for the index of a string and counting itself.
    """
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
    return abswcount
'''
#Using the functions
maxresults=100
dates_novel=finddate(readarxiv_title('novel',maxresults))
dates_revisit=finddate(readarxiv_title('novel',maxresults))
print(dates_revisit)

#Search for specific author
data=readarxiv_author('Kouwenhoven_L',10000)

#plot the data as 
plt.hist(abstract_word_count(data))
plt.xlabel("number of words in abstract")
plt.ylabel("number of papers")
'''