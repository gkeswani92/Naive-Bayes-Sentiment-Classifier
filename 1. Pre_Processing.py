from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile

def format_training_set():
    #Opening the file with the training set
    original = open('Main Data Set.csv','r')

    #Opening the file to save formatted training set
    modified = open('Pre-Processed.csv','a')
    
    #Reading the first line of the file
    line=original.readline()

    sentiment=""
    i=0
    while line!='':
        print(i)
       
        if line[1]=='0':
            #0 is negative in the training set
            sentiment="Negative,"
        else:
            sentiment="Positive,"
        
        com5=line.find(',',60)

        #Removes white spaces and convert to lower case
        tweet=line[com5+2:].strip().lower()

        #Removes URL's
        if "http" in tweet:
            link_pos=tweet.find('http')
            tweet=tweet[0:link_pos]

        #Removes usernames
        while "@" in tweet:
            start=tweet.find('@')
            end=tweet.find(' ',start)
            tweet=tweet[:start]+tweet[end:]

        #Removing hashtags
        while "#" in tweet:
            pos=tweet.find('#')
            #print(pos)
            tweet=tweet[:pos]+tweet[pos+1:]
            
        line=original.readline()

        #Write sentiment and tweet to the new file
        modified.write(sentiment+tweet+"\n")

        i=i+1

    #Closing both the files
    original.close()
    modified.close()
    
format_training_set()
