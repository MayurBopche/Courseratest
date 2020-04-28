#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Assignment

class user():        
    def __init__(self,name,book):
        self.book = book
        self.name = name
        if self.name not in self.book:
            name = self.name
            accno = input("Enter your account number:")
            phno = input("Enter your Mobile number:")
            pin = input("Enter your pin number:")
            self.book[name] = [name,accno,phno,pin,0]
            print("User Registered")
        else:
            print("Name already exists")
    def userinfo(self):
        if self.book[self.name] != "Blocked":
            if self.name in self.book.keys():
                print(f"Name:{self.name}")
                print(f"Account number:{self.book[self.name][1]}")
                print(f"Phone Number:{self.book[self.name][2]}")
                print(f"Balance:{self.book[self.name][4]}")
            else:
                print("User doesn't Exists or may have been blocked")
        else:
            print("Account Doesn't exists or is blocked")
    def pinchange(self):
        if self.book[self.name] != "Blocked":
            def pinupdate():
                print("Old Pin Verfied")
                new = input("Enter new pin:")
                self.book[self.name][2] = new
                print("New pin successfully updated")
            print("Portal for pin change")
            old = input("Enter your old pin:")
            for x in range(3):
                if old == self.book[self.name][3]:
                    pinupdate()
                    break
                print(f"Wrong Pin:Attempts left:{2-x}")
                if (2-x) == 0 :
                        self.book[self.name] = "Blocked"
                        print("Account Blocked")
        else:
            print("Account Doesn't exists or is blocked")
        
    def withdraw(self):
        if self.book[self.name] != "Blocked":
            for x in range(3):
                if self.name in self.book.keys():
                    pin = input("Enter pin:")
                    if pin == self.book[self.name][3]:
                        y = int(input("Amount to be drawn:"))
                        self.book[self.name][4] -= y
                        print(f"Current Balance:{self.balance()}")
                        break
                    print(f"Wrong Pin:Attempts left:{2-x}")
                    if (2-x) == 0 :
                        self.book[self.name] = "Blocked"
                        print("Account Blocked")
        else:
            print("Account Doesn't exists or is blocked")
                
    def deposit(self):
        if self.book[self.name] != "Blocked":
            for x in range(3):
                if self.name in self.book.keys():
                    pin = input("Enter pin:")
                    if pin == self.book[self.name][3]:
                        y = int(input("Amount to be deposit:"))
                        self.book[self.name][4] += y
                        print(f"Current Balance:{self.balance()}")
                        break
                    print(f"Wrong Pin:Attempts left:{2-x}")
                    if (2-x) == 0 :
                        self.book[self.name] = "Blocked"
                        print("Account Blocked")
        else:
            print("Account Doesn't exists or is blocked")
    def balance(self):
        if self.book[self.name] != "Blocked":
            return self.book[self.name][4]
        else:
            print("Account Doesn't exists or is blocked")
        
        


    book = {}

    