# -*- coding:utf-8 -*-
from collections import Counter
from zhon.hanzi import punctuation
import re

def getChainWords(filename, topN):
    '''
    Input Chinese text file , return topN counted chain Words

    filename: file path
    topN: the number of top valus return
    '''
    # Read and Rearrange File
    sourceFile = open(filename,"r",encoding="utf-8")
    sourceText = sourceFile.read()
    cleanText = re.sub("([%s\n\s]+) | (― ―)"%punctuation," ",sourceText,0).split(" ") 

    # Initial cleanText with a list
    tempList = []
    for i in range(len(cleanText)-1):
        tempList.append(cleanText[i] + " | " + cleanText[i+1])

    # Use Counter to count and sort, return the topN items
    BinaryWords = Counter(tempList).most_common(topN)
    for i in BinaryWords:
        print (i)
    
    # close the opened file
    sourceFile.close()

if __name__ == "__main__":
    textpath = "C:/Users/sdhx/Desktop/happiness_seg.txt"
    getChainWords(textpath,10)
