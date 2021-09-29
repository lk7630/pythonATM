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

    pass
if __name__=="__main__":
    u1=Card(123,4312,100)
    u2=Card(456,2314,1000)
    atm=ATM({},453)
    print("master",atm.master_passcode)
    atm.card_list={u1,u2}

    #driver code
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
    print("Please choose: ")
    selection=int(input("1."))
