#!/usr/bin/env python
# coding: utf-8

# # DATA CLEANING

# In[3]:


def tokenized_corpus(path):
    import nltk
    from nltk.tokenize import sent_tokenize
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import re
    f=open(path,'r')
    text=f.read()
    replace_sent_4=re.sub('[\n]','.',text)
    replace_sent_3=re.sub('[;_?)*!(:=+"/,\'-]','',replace_sent_4)
    replace_sent_2=re.sub('[0-9]','',replace_sent_3)
    replace_sent=re.sub('\\n','',replace_sent_2)
    sub_sent=re.sub('[\n]','.',replace_sent)
    new_replace_sent=""
    flag=0
    m=len(sub_sent)
    for i in range(m):
        if i<m-2 and sub_sent[i]=='.' and sub_sent[i+1]=='.':
            continue
        elif i<m-2 and sub_sent[i]=='\\' and sub_sent[i+1]=='n':
            flag=1
            continue
        elif i>0 and flag==1 and sub_sent[i]=='n' and sub_sent[i-1]=='\\':
            continue
        else:
            new_replace_sent=new_replace_sent+sub_sent[i]
    tokenize_sent=new_replace_sent.split('.')
    data=[]
    stpwrds=set(stopwords.words("english"))
    stpwrds.update(['s','re','ll','r'])
    
    for i in tokenize_sent:
        if i=='':
            continue
        words=nltk.word_tokenize(i)
        words_tokens=[w for w in words if w not in stpwrds]
        if len(words_tokens)==1 or len(words_tokens)==0:
            continue
        data.append(words_tokens)
    return data
        
        


# In[ ]:




