#Author:Zuriahn Yun
#Date:2/3/2023
#Description:FLower power game

#So program arguments can be used
import sys
#Attaching program arguments to variables
if len(sys.argv)>1:
    s = sys.argv[1]
    p = sys.argv[2]
    trades = sys.argv[3]
    tradep = sys.argv[4]
else:    
#User input for stargazers and plumeria
    s = int(input("How many stargazer did u pick up"))
    p = int(input("How many plumeria did u pick up"))

#Game prompt
    print("While you are walking through the forest a perfumer aproaches you. She prompts you to trade stargazer lilys and plumeria.")
#How much of each the player wants to trade
    trades = int(input("How many stargazer would you like to trade"))
    tradep = int(input("How many plumeria would you like to trade"))


#Trades to emerald conversions
if trades > s or tradep > p:
    print("The Perfumer gets mad you are asking to trade more than you have and ends the conversation.")
    exit()
elif trades and tradep == 0:
    print("The perfumer gets sad and leaves.")
    exit()
if tradep < 6 and trades < 11:
    e = 2 * trades
elif tradep >6 and trades<11:
    e = 3 * tradep
elif tradep<20 and trades % 24 !=0 and trades % 12==0:
    e = tradep
elif trades % 12 == 0 and trades % 24 !=0 and tradep >= 20:
    e = 4 * tradep
elif trades> 11 and tradep  :
    e = trades *5
else:
    e = 0
    
#How many emeralds are being offered
print("The perfumer offers you", e ,"emeralds.", end="")

#Player input to accept or deny trade
response = input("Do you accept the trade? (y / n )")

#Game response to yes or no
if response == "y":
    print("Player receives", e, "emeralds")
    ws = s - trades 
    wp = p - tradep
    print("Player walks away with",ws,"stargazerlily,", wp, "plumeria and", e,"emeralds.")
elif response == "n":
    print("The perfumer gets sad and leaves")
    exit()
    
        
        

