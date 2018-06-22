
# coding: utf-8

# In[1]:


str = input('请输入字符串: ')
new_str = []   
for i in str:  
    new_str.append(i)  
new_str.reverse()    
print(''.join(new_str)) 


# In[ ]:


str = input('请输入字符串：')  
new_str = list(str)
a = len(str)-1
b = 0
while a > b:  
    new_str[a] , new_str[b] = new_str[b] , new_str[a]
    a -= 1
    b += 1
print(''.join(new_str)) 

