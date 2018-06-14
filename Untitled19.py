
# coding: utf-8

# In[ ]:


win = [('r','s'),('s','p'),('p','r')]
import random
l = ['p','s','r']
for i in range(1,6):
    user= input("Enter r,p,s: ")
    ok = user in l
    if(ok):
        print("data theek hei")
    else:
        print("data galat hei")
        break 
    comp = random.choice(l)
    if user == comp:
        print ("user data=" , user)
        print ("computer data=", comp)
        print("match tie")
    elif (user, comp) in win:
        print ("user data=" , user)
        print ("computer data=", comp)

        print ("user win")
    elif (comp, user) in win:
            print ("user data=" , user)
            print ("computer data=", comp)
            print ("computer win")
    print("=======================\n")
    
    
  

