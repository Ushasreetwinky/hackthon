"""Data ranking."""

import pandas as pd
import operator
import datetime
import io
import json

def data_ranking(year):
    """Reading data and ranking the data according to the popularity."""
    df = pd.read_csv('data.csv', header=None)
    print df.size
    rank_words={}
    for x in xrange(0, 2770):
        ab=datetime.datetime.strptime(df.iloc[x][0], "%Y-%m-%d %H:%M:%S.%f").date()
        if(ab.year>year):
            file_name=str(year)+".json"
            with io.FileIO(file_name, "w") as file:
                data=[]
                for a in rank_words:
                    word={}
                    word["text"]=a
                    word["size"]=rank_words.get(a)
                    data.append(word)
                json.dump(data, file, indent=1)
            rank_words={}
            year=ab.year
        for y in xrange(1, df.iloc[x].size):
            if not pd.isnull(df.iloc[x][y]):
                df.iloc[x][y]=df.iloc[x][y].lower()
                if df.iloc[x][y] in rank_words.keys():
                   # print str(rank_words[df.iloc[x][y]])+":"+str(y)
                    rank_words[df.iloc[x][y]]=rank_words[df.iloc[x][y]]+(21-y)
                else:
                    rank_words[df.iloc[x][y]]=21-y
                #print df.iloc[x][y]+" "+str(rank_words[df.iloc[x][y]])
            pass
        pass    
    with io.FileIO("ranked_data.json", "w") as file:
        data=[]
        for a in rank_words:
            word={}
            word["text"]=a
            word["size"]=rank_words.get(a)
            data.append(word)
        json.dump(data, file, indent=1)
        #print sorted_x
        pass

df = pd.read_csv('data.csv', header=None)
#print df.iloc.size
#print df[df.columns[]]
#print df[df.columns[20]]
data_ranking(2009)
