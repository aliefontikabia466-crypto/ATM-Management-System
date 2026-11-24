Account_numbers=[]
Pass_codes=[]
#ACCOUNT_CODE=2005
Starting_balance=[]

ACCOUNT_INFO=[]

Enter_user=input("Enter name:")
print(f"{Enter_user} welcome to:\n============================\natm management_system\n======================================\n".title())
while True:
    print(
        "\n1.Create account"
        "\n2.View account"
        "\n3.Deposit Money"
        "\n4.Withdraw Money"
        "\n5.Check Balance"
        "\n6.Exit"
                                
    )
    Choose_option=input("Choose options:").strip()
    if Choose_option.isdigit():
        Choose_option=int(Choose_option)

        if Choose_option==1:
            Full_name=input("Enter full name:").strip()

            Account_number=input("Enter account number:").strip()
            if Account_number.isdigit():
                  Account_number=int(Account_number)
                  if Account_number not in Account_numbers:
                       Account_numbers.append(Account_number)

                       Pass_code=input("Enter passcode:").strip()
                       if Pass_code.isdigit():
                            Pass_code=int(Pass_code)
                            if Pass_code not in Pass_codes:
                                Pass_codes.append(Pass_code)

                                Start_balance=input("Enter start balance:").strip()
                                if Start_balance.isdigit():
                                    Start_balance=int(Start_balance)
                               #if Start_balance not in Starting_balance:
                                    Starting_balance.append(Start_balance)
                           
                                    STATE_BALANCE=Start_balance
                                  #print("State balance",STATE_BALANCE)
                                    Nested_info=[Full_name,Account_number,Pass_code,STATE_BALANCE]
                                    ACCOUNT_INFO.append(Nested_info)
                               #print(type,ACCOUNT_INFO)
                              # print(f"{ACCOUNT_CODE} this is your account don't share this code with any one")
                                else:
                                   print("invalid input")
                            else:
                               print(f"{Pass_code} alrady inserted")
                       else:
                           print("invalid input")
                      
                  else:
                      print(f"{Account_number} has been used")

            else:
                 print("invalid input")
                  
                    
        if Choose_option ==2:
           Enter_Code=input("Enter account number:")
           if Enter_Code.isdigit():
               Enter_Code=int(Enter_Code)
               # print(Enter_Code)
               # print(type(Enter_Code))
               # print(ACCOUNT_INFO)
               # print(type(ACCOUNT_INFO))
           
               #index=.index(ACCOUNT_INFO)
               for Views in ACCOUNT_INFO:
                  if  Enter_Code == Views[1]:
                                                                   
                     print("\n")
                     print("Name:",Views[0])
                     print("Account_number:",Views[1])
                     print("Pin:",Views[2])
                     print("Balnace:",Views[3])
           else:
              print("account was not found")
              
        if Choose_option==3:
            
           Number_Deposit=input("Enter account number:").strip()
           if Number_Deposit.isdigit():
                Number_Deposit=int(Number_Deposit)
                if Number_Deposit in Account_numbers:
                  for  account in ACCOUNT_INFO:
                    if Number_Deposit == account[1] :
                        print(account[0],"account\n")  
                        break
                  # print("loop finish",account)
                  # print(account[3])

                  Deposit=input("Enter the amount to Deposit:").strip()
                  if Deposit.isdigit():
                     Deposit=int(Deposit)

                     if Deposit > 0:
                       Total_Deposite=Deposit + account[3]

                       account[3]=Total_Deposite
                       print(account)
                       print("your deposit was successful.\nyour new balance is:",Total_Deposite,"le")
                       
                     else:
                       print(f"{Deposit} amount is too low.")
                  else:
                    print("invalid input")

           else:
                print(f"{Number_Deposit} not found.")

       
        if Choose_option ==4:
           Number_Withdraw=input("Enter account number:").strip()
           if Number_Withdraw.isdigit():
              Number_Withdraw = int (Number_Withdraw)

              if Number_Withdraw in Account_numbers:
                 for   withdraw  in ACCOUNT_INFO:                     #print(withdraw[3])
                    if Number_Withdraw == withdraw[1]:
                      print(withdraw[0],"account\n")
                      
                    else:
                       print("account not found")
                       break
                 #print(withdraw)
                 Withdrew_Money=input("Enter the amount you want to withdraw:").strip()
                 if Withdrew_Money.isdigit():
                    Withdrew_Money=int(Withdrew_Money)

                    if Withdrew_Money >  STATE_BALANCE :
                       print("insuficent found")
                    elif Withdrew_Money==0:
                           print(f"{Withdrew_Money} is to low")

                    else:
                      Total_withdraw =  withdraw[3]  - Withdrew_Money
                      withdraw[3]=Total_withdraw
                      print("your withdraw is successful.\nyour new balance is:",Total_withdraw,"le")
                 else:
                   print("invalid input")
              else:("account not found")

           else:
                print("invalid input")

        if Choose_option == 5:
           Check_Blance=input("Enter account number:")
           if Check_Blance.isdigit():
              Check_Blance = int (Check_Blance)
              if Check_Blance in Account_numbers:
                 for  balance in ACCOUNT_INFO:
                  if  Check_Blance == balance[1]:
                    print("your balcnce is",balance[3],"le")
              else:
                 print("account does not exit")

        if Choose_option == 6:
           Exit=input("are you sure want to exit (y/n)").strip().lower()
           if Exit == "y":
              break

    



