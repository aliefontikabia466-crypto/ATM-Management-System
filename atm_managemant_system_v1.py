MAX_ATTEMPT=3
STATE_BALANCE=5_4_6.0
permession="admin"
attempt=MAX_ATTEMPT
Balance=STATE_BALANCE
while True:
    USER=input("\nWhat permession did you have ?")
    if USER == permession:
        print(f"{USER} Welcome To:\n============================\n Siera Leone Comercial Bank\n==============================\n"
              "\n1.check balance" 
              "\n2.deposite" 
              "\n3.withdraw"
              "\n4.exit"
              .title())
        user_name= input("\nenter the manu above:".title())
        if user_name.isdigit():
            manue=int(user_name)
            if manue ==1:
                print(f"you have {Balance} in you account")
            else:
             if manue==2:
                 Deposite=input("enter the amout you want to depoait:".title())
                 Deposite=float(Deposite)
                 Deposite=Balance+Deposite
                 print(f"you Blance was Le{Balance}:\nNew Balane is {Deposite}".title())
            if manue ==3:
                Withdrawth=input("\nenter the amont you want to withdrawth:".title())
                Withdrawth1=float(Withdrawth)
                if Withdrawth1>Balance:
                    print("you have insufficent fund".title())
                else:
                    Withdrawth1=Balance -Withdrawth1
                    print(f"you have Withdrawth {Withdrawth} \n and your balance is now {Withdrawth1}".title())

            if manue==4:
                EXIT=input("Are You Sure You Want TO Exit?(y/n)")
                if EXIT =="y":
                  break

    else:
        if attempt>0:
            attempt-=1
            print(f"you have {attempt} attempt left")
        else:
            break