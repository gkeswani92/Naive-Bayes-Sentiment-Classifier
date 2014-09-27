from tkinter.filedialog import askopenfile

def naive_bayes_algo(str):
    print("Sentence-->",str)
    words=str.split()
    #print("Words:",words)
    i=0
    #Stores probability of current word
    pos=0
    neg=0
    #Stores probability of overall sentence
    prob_pos=0
    prob_neg=0
    #Variables for negation logic
    current=""
    previous=""
    pre_previous=""
    temp=0
    
    for i in range(len(naive_bayes)):
        for word in words:
            current=word
            
            #If word is found in the trained classifier
            if current == naive_bayes[i][0]:
                print("Word being used--->",current)
                pos=(naive_bayes[i][1]/(naive_bayes[i][1]+naive_bayes[i][2]))
                #print("P(Positive|Original)",pos)
                neg=(naive_bayes[i][2]/(naive_bayes[i][1]+naive_bayes[i][2]))
                #print("P(Negative|Original)",neg)
                
                #If previous word is a negative word
                if previous in negation_list:
                    #print()
                    #print("NEGATION DETECTED FOR ",previous," AND ",current)
                    temp=pos
                    pos=neg
                    neg=temp
                    #print("P(Positive|After Negation)",pos)
                    #print("P(Negative|After Negation)",neg)

                #If previous word is an intensifier
                for item in adv_list:
                    if item[0]==previous:
                        print()
                        #print("INTENSIFIER DETECTED: ",previous)
                        pos=pos*item[1]
                        neg=neg*item[1]
                        #print("P(Positive|After Intensifier)",pos)
                        #print("P(Negative|After Intensifier)",neg)

                        #If negation appears before intensifier
                        if pre_previous in negation_list:
                            print()
                            print("NEGATION DETECTED FOR ",pre_previous," AND ",current)
                            temp=pos
                            pos=neg
                            neg=temp
                            #print("P(Positive|After Negation)",pos)
                            #print("P(Negative|After Negation)",neg)

                print()
                prob_pos=prob_pos+pos
                prob_neg=prob_neg+neg 
                
            pre_previous=previous
            previous=current

    #Logic for adding sentiment due to smileys
    print()
    for current in words:
        if current in pos_smiley:
            #print("POSITIVE SMILEY DETECTED")
            prob_pos=prob_pos+1
        if current in neg_smiley:
            #print("NEGATIVE SMILEY DETECTED")
            prob_neg=prob_neg+1
    #print("P(Overall Positive)",prob_pos)
    #print("P(Overall Negative)",prob_neg)
 
    if prob_pos>prob_neg and prob_pos-prob_neg>0.25:
        print("Sentence is Positive")
    elif prob_pos<prob_neg and prob_neg-prob_pos>0.25:
        print("Sentence is Negative")
    else:
        print("Sentence is Neutral")
    print("---------------------------------------------")

#------------------------------------------------------------------------------

#Opening the file to with the classifier
classifier = open('Trained Set.txt','r')
naive_bayes=[]
for line in classifier:
    com1=line.find(',')
    com2=line.find(',',com1+1)
    naive_bayes.append([line[:com1],int(line[com1+1:com2]),int(line[com2+1:-1])])
naive_bayes.sort()

#Opening the file with the negation words
negation = open('Negation List.txt','r')
negation_list=[]
for word in negation:
    negation_list.append(word[:-1])

#Opening files with smileys and adding to list
pos_file = open('Emoticon List Positive.txt','r',encoding='utf-8')
neg_file = open('Emoticon List Negative.txt','r',encoding='utf-8')
pos_smiley=[]
neg_smiley=[]
for word in pos_file:
    pos_smiley.append(word[:-1])
pos_smiley.remove('\ufeff')
for word in neg_file:
    neg_smiley.append(word[:-1])
neg_smiley.remove('\ufeff')

#Opening file containing adverb list and adding to list
adv = open('Adverb List.txt','r')
adv_list=[]
for line in adv:
    adv_list.append([line[:line.find(',')],float(line[line.find(',')+1:-1])])

#Example tweets to test all combinations
'''naive_bayes_algo("the rock concert caused a headache")
naive_bayes_algo("the iphone screen is such a fail")
naive_bayes_algo("congratulation you just won a phone")
naive_bayes_algo("android is not so difficult to understand :(")
naive_bayes_algo("i hate going to work")
naive_bayes_algo("i love you for this gift")
naive_bayes_algo("i dont want to go to work")
naive_bayes_algo("the screen is not good but the phone is good")
naive_bayes_algo("the screen is good but the phone is bad")
naive_bayes_algo("the screen is not very good")
naive_bayes_algo("the screen is not very good :(")'''

#Examples tweets from twitter about Moto G launch
naive_bayes_algo("moto G's launch is probably the most followed event. Never seen such craze even for Nexus or Iphone series. great job.")
naive_bayes_algo("Same day the dual SIM Moto G launches in India, the KitKat update starts rolling out for dual SIM version. Motorola = awesome")
naive_bayes_algo("Moto G is awesome \m/")
naive_bayes_algo("Got a message from @Flipkart that Moto G is shipped will soon have my hands on it :-)")        
naive_bayes_algo("@Flipkart missed it yet again :'( when will the Moto G be back in stocks again")
naive_bayes_algo("@Flipkart mate, when will you sort your shit out and put Moto G 16 GB in stock again? I've been waiting for about 8 hours now. Very poor")
naive_bayes_algo("*spots the Moto G news* *opens Flipkart* *goes to payment page* *realizes i cannot afford* *closes page* The sad story of being broke")
naive_bayes_algo("MOTO G PLEASE :):) I love THIS PHONE BTW... awesome features definately worth the money :)")
naive_bayes_algo(" If anyone is looking to buy a new phone, check out the deal on Moto g on flipkart! Its crazy")
