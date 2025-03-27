import re
from collections import defaultdict
import matplotlib.pyplot as plt

def zipf(txt):
    '''Function to analize Zipf's law, by counting the occurence of words in given text file and then plotting it'''
    wordDict = defaultdict(int)
    f = open(txt,'r')
    file = str(f.readlines())
    f.close()
    words = re.sub('[^A-Za-z0-9]+', ' ', file).lower()
    for i in words.split():
        if i in wordDict:
            wordDict[i] += 1
        else:
            wordDict[i] = 1

    sortedDict = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
    k,v = zip(*sortedDict)
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(v) + 1), v, color='b')
    plt.title("Zipf's Law distibution of words")
    plt.xlabel("Frequency")
    plt.ylabel("Rank")
    plt.yscale('log')
    plt.xscale('log')
    plt.show()

if __name__ == "__main__":
    zipf("test_file.txt")