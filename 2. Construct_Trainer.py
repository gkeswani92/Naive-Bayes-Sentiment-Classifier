import re
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

#-----------------------------------------------------------------------------------------------
def keep_go_words():    
    #Reading the first line of the file
    line=original.readline()

    mod_tweet=""

    #Creates a list of all the go words mentioned in the stop word file
    go_word_list=[]
    for line in go_words_file:
        go_word_list.append(line[:-1])

    j=0
    
    while line!='':
        print(j)
        #Finds 1st comma of a line in the training set
        com1=line.find(',')
        
        #Stores the original sentiment and tweet
        sentiment=line[:com1]
        tweet=line[com1+1:]
        
        #Splits a tweet into its individual words
        words=tweet.split()
        for current in words:
            mod_current=""

            #Saves words that don't start with numbers
            if current[0] not in "0123456789":

                #Removes multiple characters appearing together
                pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
                current=pattern.sub(r"\1\1", current)

                for char in current:
                    #Removes all special characters
                    if char >='a' and char <='z':
                        mod_current=mod_current+char

                #Removes all words with less than 3 characters
                if len(mod_current)>2:

                    #Saves words that appear in go word list
                    for i in range(len(go_word_list)):
                        if mod_current == go_word_list[i]:
                            bayes_construct(mod_current,sentiment)
                            mod_tweet = mod_tweet + " " + mod_current
                            break

        #Writes modified tweet to new file
        if mod_tweet != "":
            modified.write(sentiment+","+mod_tweet+"\n")
        mod_tweet=""

        #Reads next line of the file
        line=original.readline()

        j=j+1
                             
#----------------------------------------------------------------------------------------------------
def bayes_construct(mod_current,sentiment):
    length=len(naive_bayes)
    flag=0

    #When the naive_bayes list is empty
    if length==0:
        if sentiment=="Positive":
            naive_bayes.append([mod_current,1,0])
        else:
            naive_bayes.append([mod_current,0,1])
    #When the naive_bayes list is not empty
    else:
        #When the naive_bayes list contains the word
        for item in naive_bayes:
            if mod_current == item[0]:
                if sentiment=="Positive":
                    item[1]=item[1]+1   
                else:
                    item[2]=item[2]+1
                flag=1
                break
        #When the naive_bayes list does not contain the word
        if flag==0:
                if sentiment=="Positive":
                    naive_bayes.append([mod_current,1,0])
                else:
                    naive_bayes.append([mod_current,0,1])

#----------------------------------------------------------------------------------------------------

#Opening the file with the training set
original = open('Pre-Processed.csv','r')

#Opening the file with the go words
go_words_file = open('Go Words List.txt','r')
    
#Opening the file to save formatted training set with only go words
modified = open('Feature Vector.csv','w')

#Stores the probability of each word being positive or negative
naive_bayes=[]
sentiment=""

keep_go_words()

#Closing feature vector before writing to classifier
modified.close()

#Opening the file to save the classfier
classifier = open('Trained Set.txt','w')
for i in range(len(naive_bayes)):
    classifier.write(naive_bayes[i][0]+","+str(naive_bayes[i][1])+","+str(naive_bayes[i][2])+"\n")

#Closing all files
original.close()
go_words_file.close()
classifier.close()
