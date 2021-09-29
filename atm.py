#!/usr/bin/python3
class Card():
    def __init__(self,number=None,pin=None,amount=None):
        self.number=number
        self.pin=pin
        self.amount=amount

    def __str__(self):
        return (f'card number: {self.number}\n\
pin number : {self.pin}\n\
amount     : {self.amount}')

class ATM():
    def __init__(self,card_list={},master_passcode=000):
        self.card_list=card_list
        self.master_passcode=master_passcode
        self.current_user_index=-1

    def unlock(self, number):
        print("master pass",self.master_passcode)
        if number==self.master_passcode:
            return True
        return False

    def verify_card(self,card_number):
        for card in self.card_list:
            if card_number==card.number:
                return True
        return False

    def verify(self,card_number,pin_number):
        for card in self.card_list:
            if card_number==card.number and pin_number==card.pin:
                self.current_user_index=self.card_list.index(card)
                return True
        return False

    def __str__(self):
        return_string=""
        for card in self.card_list:
            return_string+=(card.__str__() +"\n")
        return return_string

    def __repr__(self):
        return (str(self.card_list))

def master_unlock(atm):
    passcode_pass=False
    while not passcode_pass:
        passcode=int(input("Please type in master passcode:"))
        passcode_pass=atm.unlock(passcode)
    exit()

def deposit(atm):
    amount=int(input("Please insert(type) money: "))
    atm.card_list[atm.current_user_index].amount+=amount
    print("your current balance is: ",atm.card_list[atm.current_user_index].amount)

def withdraw(atm):
    amount=int(input("Please choose(type) the amount to withdraw: "))
    print("Preference:")
    print("1. Mostly 100s\n2. Mostly 50s\n3. Mostly 20s\n4. 100s and 50s")
    selection=int(input("Please select: "))
    currency=[100,50,20,10,5,1]

def greedy(amount,currency,type):
    index=currency.index(type)
    remaining=amount
    return_dict={}
    quantity=0
    for i in range(index,len(currency)):
        if remaining>0:
            quantity=amount//currency[index]
            remaining=amount%currency[index]
            return_dict[currency[index]]=quantity
        if remaining==0:
            break
    return return_dict


if __name__=="__main__":
    u1=Card(123,4312,100)
    u2=Card(456,2314,1000)
    atm=ATM({},453)
    print("master",atm.master_passcode)
    atm.card_list=[u1,u2]

    count=0
    print('WELCOME TO ATM')
    while(count<3):
        card_number=int(input("Please swipe(type) card: "))
        if(atm.verify_card(card_number)):
            break
        else:
            print("card number is invalid, please try again!")
            count+=1
    if count==3:
        print('your card is locked, please contact customer service at xxx-xxx-xxxx')
        master_unlock(atm)
    count=0
    while count<3:
        pin_number=input("Please type in pin number: ")
        if len(pin_number)==4 and pin_number.isnumeric():
            pin_number=int(pin_number)
            if atm.verify(card_number,pin_number):
                print("pin number accepted")
                break
            else:
                print("wrong pin please try again")
                count+=1
        else:
            print ("pin is 4 digit, please try again")
            count+=1
    if count==3:
        print('your card is locked, please contact customer service at xxx-xxx-xxxx')
        master_unlock(atm)
    print("your current balance is: ",atm.card_list[atm.current_user_index].amount)
    print("Please choose: ")
    selection=int(input("1. Deposit\n2. Withdraw\n3. Cancel(eject card)\n"))
    if selection==3:
        exit()
    elif selection==1:
        deposit(atm)
    elif selection==2:
        withdraw()
