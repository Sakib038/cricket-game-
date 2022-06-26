import random

#global variables
replay=False
bdec=""
toss=""
tdec=""
bat1st=False
bowl1st=False
total1=0
total2=0

#number of balls and wickets
def nballs():
    global over
    global wickets
    
    over=6*int(input("\nHow many overs do you want to play?\n"))
    
    wickets=int(input("\nNumber of wickets:"))
    
    tosses()
    
#Batting part    
def batting():
     i=1
     runs=0
     global wickets1,wickets,total1,total2
     wickets1=wickets
     while i < (over+2):
         
         if wickets>0 and i<=over:
             
             if i in [x*6 for x in range(1,over+1)]:
                print("\nLast ball of the over")
            
             y=random.choice([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,6,6])
             x=int(input("\nEnter runs:"))
          
             if x not in [1,2,3,4,5,6]:
                print("Entered value must be within 1-6")
                continue
            
             i+=1 
             if x==y:
               
                wickets1-=1
                print("Wicket!!!")
                print(f"balls:{i-1}")
                print(f"wickets remaining:{wickets1}")
                
                continue
             
             else: 
                runs+=x
                print(f"runs:{runs}")
                print(f"balls:{i-1}")
                print(f"wickets remaining:{wickets1}")
            
             if bat1st==False and runs>total2:
                 print("\nYou have won the match!!!\n")
                 break
                
            
         else:
            total1=runs
            print("\nInnings over")
            print(f"You have scored {total1} runs")
            if bat1st:
                print(f"Opponent needs to score {total1+1} runs in {over} balls")
                print("\nStart of the second innings")
                bowling()
            elif total1==total2:
                print("Match drawn")
            elif total1<total2:
                print("\nGame Over\nYou have lost the match")
            break
    
#Bowling part    
def bowling():
     i=1
     runs=0
     global wickets,wickets2,total2,total1
     wickets2=wickets
     while i < (over+2):
         
         if wickets>0 and i<=over:
             
             if i in [x*6 for x in range(1,over+1)]:
                print("\nLast ball of the over")
            
             y=random.choice([1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,5,6,6,6])
             x=int(input("\nEnter runs:"))
          
             if x not in [1,2,3,4,5,6]:
                print("Entered value must be within 1-6")
                i-=1
                continue
            
             i+=1
             if x==y:
               
                wickets2-=1
                print("Wicket!!!")
                print(f"balls:{i-1}")
                print(f"wickets remaining:{wickets2}")
                continue
             
             else: 
                runs+=y
                print(f"runs:{runs}")
                print(f"balls:{i-1}")
                print(f"wickets remaining:{wickets}")
             
             if bowl1st==False and runs>total1:
                 print("\nGame Over\nYou have lost the match\n")
                 break
                
             
         else:
            total2=runs
            print("\nInnings over")
            print(f"Opponent has scored {total2} runs")
            if bowl1st:
                print("\nStart of the second innings")
                print(f"You need to score {total2+1} runs in {over} balls ")
                batting()
            elif total1==total2:
                print("Match drawn")
            elif total2<total1:
                print("\nYou have won the match")
            break
    
#Toss     
def tosses():
   global bat1st
   global bowl1st
   toss=input("\nUp for the toss\nHead or Tail?\n")
   tdec=random.choice(["head","tail"])

#If player wins the toss    
   if toss.lower()==tdec:
     bdec=input("\nYou have won the toss.\nWhat are you choosing then?\nBowling or Batting?\n")
     
   
     if bdec.lower()=="bowling":
        print("So you have chosen to bowl first.")
        bowl1st=True
        bowling()
     
     elif bdec.lower()=="batting":
        print("So you have chosen to bat first.")
        bat1st=True
        batting()
  
#If player loses the toss
     else:   
        print("\nError. You have to toss again.") 
        tosses()

   elif toss.lower() not in ["head","tail"]:
     print("\nError. You have to toss again.") 
     tosses()
   
   else:
        bdec=random.choices(["bowl","bat"])
        print(f"You have lost the toss.\nOpponent has chosen to {bdec[0]} first")
   
        if bdec[0]=="bat":
            bowl1st=True
            bowling()
       
        else:
            bat1st=True
            batting()
nballs()
