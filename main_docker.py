import string
import socket
import os

def main():
    endResult = open("/home/output/result.txt", "w+")
    path = "/home/data"
    dir_list = os.listdir(path)
    endResult.write("All the files in /home/data are as follows:- ")
    endResult.write(path)
    for x in dir_list:
        endResult.write(" \n")
        endResult.write(x)
    IF_file = open('/home/data/IF.txt','r')
    data = IF_file.read()
    wordsInIFFile=data.split()
    Lime_file = open('/home/data/Limerick-1.txt','r')
    data = Lime_file.read()
    wordsInLimeFile=data.split()
    endResult.write(" \n")
    endResult.write("Total words in Limerick-1.txt file:- "+str(len(wordsInLimeFile)))
    wordIF=[]
    for i in wordsInIFFile:
        jo=i.translate(str.maketrans('', '', string.punctuation))
        jo=jo.capitalize()
        wordIF.append(jo)
    endResult.write(" \n")
    endResult.write("Word count of IF.txt file:- "+str(len(wordIF)))
    endResult.write(" \n")
    endResult.write("Total number of words in IF.txt and Limerick-1.txt are:- "+str(len(wordIF) + len(wordsInLimeFile)))
    countIF = []
    IFSet = set(wordIF)
    for i in IFSet: 
        countIF.append(wordIF.count(i))
    wordIF = list(set(wordIF))
    order_countIF= sorted(countIF,reverse=True)
    endResult.write("\n")
    endResult.write("The top 3 words with maximum number of counts in IF.txt are:- ")
    j=0
    for j in range(0,3):
         for i in range(0,len(countIF)):
             if(countIF[i]== order_countIF[j]):
                 endResult.write("\n")
                 endResult.write(""+wordIF[i]+" - "+ str(countIF[i]) )
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    endResult.write("\n")
    endResult.write("Docker machine IP Address is:" + IPAddr) 
    endResult.close()
    endResult_file = open('/home/output/result.txt','r')
    data_endResult = endResult_file.read()
    print(data_endResult)

if __name__ == "__main__":
    main()
