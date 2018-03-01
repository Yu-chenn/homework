
# coding: utf-8

# In[1]:

def unicode_test(value):
    import  unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s",value2="%s"'%(value,name,value2))


# In[2]:

unicode_test('A')


# In[3]:

unicode_test('$')


# In[4]:

unicode_test('\u00a2')


# In[5]:

unicode_test('\u00ac')


# In[6]:

unicode_test('\u2603')


# In[7]:

place='cafe'
place


# In[8]:

place='caf\u00e9'
place


# In[9]:

place='caf\N{LATIN SMALL LETTER E WITH ACUTE}'
place


# In[10]:

u_umlaut='{LATIN SMALL LETTER U WITH DIAERESIS'
u_umlaut


# In[11]:

drink='Gew'+ u_umlaut+'rztramoner'
print('Now I can finally have my',drink,'in a',place)


# In[12]:

snowman='\u2603'


# In[13]:

len(snowman)


# In[14]:

ds=snowman.encode('utf-8')


# In[15]:

len(ds)


# In[16]:

ds


# In[17]:

snowman.encode('ascii','ignore')


# In[18]:

snowman.encode('ascii','replace')


# In[19]:

snowman.encode('ascii','backslashreplace')


# In[20]:

snowman.encode('ascii','xmlcharrefreplace')


# In[21]:

palce='caf\u00e9'
place


# In[22]:

type(place)


# In[23]:

place_bytes=place.encode('utf-8')
place_bytes


# In[24]:

type(place_bytes)


# In[25]:

place2 = place_bytes.decode('utf-8')
place2


# In[26]:

place_bytes = place.encode('utf-8')
place_bytes


# In[27]:

type(place_bytes)


# In[28]:

place2 = place_bytes.decode('utf-8')
place2


# In[29]:

place3=place_bytes.decode('ascii')


# In[ ]:

place4=place_bytes.decode('latin-1')
place4


# In[ ]:

place5=place_bytes.decode('windows-1252')
place5


# In[ ]:

'%s'%7.03


# In[ ]:

'%f'%7.03


# In[ ]:

'%e'%7.03


# In[ ]:

'%g'%7.03


# In[ ]:

actor='Richard Gere'
cat='Chester'
weight=28


# In[ ]:

"My wife's favorite actor is %s" % actor


# In[ ]:

"Our cat %s weighs %s pounds"%(cat, weight)


# In[ ]:

n=42
f=7.03
s='string cheese'


# In[ ]:

'%d %f %s' %(n,f,s)


# In[ ]:

'%10d %10f %10s' %(n,f,s)


# In[ ]:

'%10.4d%10.4f %10.4s' %(n,f,s)


# In[ ]:

'%.4d%.4f %.4s' %(n,f,s)


# In[ ]:

'%*.*d%*.*f %*.*s' %(10,4,n,10,4,f,10,4,s)


# In[ ]:

'{}{}{}'.format(n,f,s)


# In[ ]:

'{2} {0} {1}'.format(f,s,n)


# In[ ]:

'{n} {f} {s}'.format(n=42,f=7.03,s='string cheese')


# In[ ]:

d ={'n':42, 'f':7.03, 's':'string cheese'}


# In[ ]:

'{0:d} {1:f} {2:s}'.format(n,f,s)


# In[ ]:

'{n:d} {f:f} {s:s}'.format(n=42,f=7.03,s='string cheese')


# In[ ]:

'{0:10d} {1:10f} {2:10s}'.format(n,f,s)


# In[ ]:

'{0:>10d} {1:>10f} {2:>10s}'.format(n,f,s)


# In[ ]:

'{0:<10d} {1:<10f} {2:<10s}'.format(n,f,s)


# In[ ]:

'{0:^10d} {1:^10f} {2:^10s}'.format(n,f,s)


# In[ ]:

'{0:!^30s}'.format('BIG SALE')


# In[ ]:

import re
source = 'Young Frankenstein'
m=re.match('You','source')#match從來源的開頭開始
if m: #match回傳一個物件，做這件事來查看有哪些匹配項目
    print(m.group())


# In[ ]:

m=re.match('^You',source)#開始的苗點做同樣的事
if m:
    print(m.group())


# In[ ]:

m=re.match('^Frank',source)#開始的苗點做同樣的事
if m:
    print(m.group())


# In[ ]:

m=re.search('Frank',source)
if m:  #search return an object
    print(m.group())


# In[ ]:

m=re.findall('n',source)
m #findall會回傳一個串列
['n','n','n','n']
print('Found',len(m),'matches')


# In[ ]:

m=re.findall('n',source)
m


# In[ ]:

m=re.findall('n.?',source)
m


# In[ ]:

m=re.split('n',source)
m   #split returns a list


# In[ ]:

m=re.sub('n','?',source)
m   #sub returns a string


# In[ ]:

import string
printable=string.printable
len(printable)


# In[ ]:

printable[0:50]


# In[ ]:

printable[50:]


# In[ ]:

re.findall('\d',printable)


# ### re.findall('\w',printable)

# In[ ]:

re.findall('\s',printable)


# In[ ]:

source='''I wish I may,I wish I might
...Have a dish of fish tonight.'''


# In[ ]:

re.findall('wish',source)


# In[ ]:

re.findall('wish|fish',source)


# In[ ]:

re.findall('fish$',source)


# In[ ]:

re.findall('I wish',source)


# In[ ]:

re.findall('^I wish',source)


# In[ ]:

re.findall('fish tonight.$',source)


# In[ ]:

re.findall('fish tonight\.$',source)


# In[ ]:

re.findall('[wf]ish',source)


# In[ ]:

re.findall('[wsh]+',source)


# In[ ]:

re.findall('I (?=wish)',source)


# In[ ]:

m=re.search(r'(.dish\b).*(\bfish)',source)
m.group()


# In[ ]:

m.groups()


# In[ ]:

blist =[1,2,3,255]
the_bytes=bytes(blist)
the_bytes


# In[ ]:

the_byte_array=bytearray(blist)
the_byte_array


# In[ ]:

the_bytes[1]=127


# In[ ]:

the_byte_array[1]=127
the_byte_array


# In[ ]:

the_bytes=bytes(range(0,256))
the_byte_array=bytearray(range)


# In[ ]:

the_bytes=bytes(range(0,256))
the_byte_array=bytearry(range(0,256))


# In[ ]:

data[16:20]


# In[ ]:

import unicodedata
mystery = '\U0001f4a9'
mystery


# In[ ]:

pop_bytes=mystery.encode('utf-8')
pop_bytes


# In[ ]:

pop_string = pop_bytes.decode('utf-8') 
pop_string


# In[ ]:

pop_string == mystery


# In[ ]:

poem='''My kitty cat likes %s,
        My kitty cat likes %s,
        My kitty cat fell on his %s
        And now thinks he's a %s.
        '''
args=('roast beef','ham','head','clam')
print(poem%args)


# In[ ]:

leeter='''
Dear{salutation} {name},

Thank you for you letter,We are sorry that our{product}{verbed}in your
{room}.Please note that it should never be used in a {room}, especially
near any {animals}.

Send us your receipt and {amount} for shipping and handling.We will send 
you another {product} that, in our tests,is{percent}%less likely to
have{verbed}.

Thanl you for your support.

Sincerely,
 {spokesman}
 {job_title}
 '''


# In[ ]:

response = {
    'salutation':'Colonel'
    'name': 'Hackenbush',
    'product':'duck blind',
    'verbed':'imploded',
    'room':'conservatory',
    'animals':'emus'
    'amount':'$1.38'
    'percent':'1'
    'spokesman':'Edgar Schmeltz'
    'job_title':'Licensed Podiatrist'
    }
print(letter.format(**response))


# In[ ]:

import re
re = r'\bc\w*'
re.findall(pat, mammoth)


# In[ ]:




# In[ ]:



