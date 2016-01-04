
# coding: utf-8

# In[8]:

def A(func,x,y):
    func(x,y)


# In[11]:

def plus (x,y):
    print(x+y)


# In[13]:

A(plus,3,2)


# In[15]:

def B(func2,a,b):
    func2(a,b)


# In[16]:

def mult(a,b):
    print(a*b)


# In[17]:

B(mult,2,3)


# In[18]:

mult(2,3)


# In[69]:

#lambda
def cap_word(words,func):
    for word in words:
        print (func(word))
    


# In[76]:

A = ['hello','hey','how']


# In[74]:

def cap(word):
    return word.capitalize()+'!'


# In[77]:

cap_word(A,cap)


# In[78]:

cap_word(A, lambda word:word.capitalize()+'!')


# In[114]:

def document_it(func):
    def new_func(*arg, **kwargs):
        print('Running func : ',func._name_)
        print('Positional arguments:',args)
        print('keyword argument:',kargs)
        result = func(*args, **kwargs)
        print('result:',result)
        return result
    return new_func


# In[115]:

def add_ints(a,b):
    return a+b


# In[116]:

add_ints(3,5)


# In[117]:

color_add_ints = document_it(add_ints)


# In[118]:

color_add_ints(3,5)


# In[100]:

@document_it
def add_ints(a,b):
    return a + b


# In[101]:

add_ints(3,5)


# In[ ]:



