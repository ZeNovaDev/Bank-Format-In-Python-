#amount in bank
#deposit
#withdraw
#quit
def balance_in_bank():
  print(f"Your balance is ${balance:.2f}")


def deposit():
  try:
    user_deposit=float(input("Enter valid amount to deposit: "))
    if user_deposit < 0:
      print("Deposit amount cannot be less than $0")
      return 0
    elif user_deposit>= 0:
      print(f"${user_deposit} has been added to your account ")
      return user_deposit
  except ValueError :
    print("Invalid value")
    


def withdraw():
  try:
    withdraw_amount=float(input("Enter amount to withdraw: "))
    if withdraw_amount>balance:
      print("Insufficient amount")
      return 0
    elif withdraw_amount<0:
      print("withdraw amount cannot be less than $0 ")
      return 0
    elif withdraw_amount>0 and withdraw_amount<= balance:
      print(f"withdrawed ${withdraw_amount} ")
      return withdraw_amount
  except ValueError :
    print("Please enter a valid value! ")


balance = 0
is_running=True

while is_running:
  print("Nepal Rastrya Bank")
  print("1:Check balance")
  print("2:Deposit amount")
  print("3:Withdraw amount")
  print("4:Quit")
  user_choice=input("Enter a valid choice: ")
  if user_choice=="1":
    balance_in_bank()
    continue
    
  elif user_choice=="2":
    deposit_result = deposit()
    balance += deposit_result
    continue
    
  elif user_choice=="3":
    balance = balance - withdraw()
    continue
    
  elif user_choice=="4":
    print("Thanks :) ")
    is_running=False
  else:
    print("Invalid choice:! ")