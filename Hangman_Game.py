#!/usr/bin/env python
# coding: utf-8

# In[3]:


def hangman(word,lifes):
    i=0
    guess=""
    st=""
    for j in word:
        st+=j
    while(lifes):
        w=input("Enter letter: ")
        w=w.lower()
        if w==word[i]:
            guess+=w
            i+=1
            print("Right Letter\n Lifes Remains: "+ str(lifes))
        else:
            lifes-=1
            print("Wrong letter\n Lifes Remains: "+ str(lifes))
        if(len(guess)==len(word)):
            if(st==guess):
                print("You Won")
            else:
                print("You Lost")
            break
    if(lifes==0 and st!=guess):
        print("You Lost")


lifes=int(input("Enter Number of Lifes: "))
word=input("Enter word: ")
word=word.lower()
word=list(word)
hangman(word,lifes)


# In[ ]:





# In[ ]:




