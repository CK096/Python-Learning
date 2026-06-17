balance = 1000
pin = "1234"

while True:
    test = 3
    while test > 0:
        user_test = input("Please key in 4 digit Pin:")# getpass.getpass()隐藏密码输入"Please key in 4 digit Pin:")
        if user_test != pin:
            test -= 1
            if test == 0:
                print("Sorry Account Lock")
                exit()
            else:
                print(f"Wrong PIN, you still have {test} chance")
        else:
            print("PIN Number Correct")
            break

    while True:
        try:
            print("1. Check Balance\n"
              "2. Deposit\n"
              "3. Withdraw\n"
              "4. Change PIN \n" 
              "5. Exit")
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        if choice > 5 or choice < 1:
            print("Please enter a valid number")

        elif choice == 1:
            print(f"Balance: {balance}")

        elif choice == 2:
            try:
                deposit = float(input("Deposit Amount: "))
                if deposit <= 0 :
                    print("Deposit Minimum need 0.1")
                    continue

                balance += deposit
                print(f"Balance: {balance}")

            except ValueError:
                print("Please enter a valid number")

        elif choice == 3:
            try:
                ask = input("withdraw have collect RM 1 Fee: (Yes/No)").upper()
                if ask != "YES":
                    continue

                withdraw = float(input("Withdraw Amount: "))

                if withdraw+1 > balance:
                    print("Insufficient balance")
                    continue

                balance -= (withdraw + 1)
                print(f"Balance: {balance}")

            except ValueError:
                print("Please enter a valid number")

        elif choice == 4:
            old = input("Enter current PIN: ")
            if pin != old:
                print("Current PIN is Wrong")
                continue

            new_pin = input("Enter New PIN: ")
            if len(new_pin) != 4 or not new_pin.isdigit():
                print("New PIN must be 4 digit")
                continue
            elif pin == new_pin:
                print("New PIN cant same with old")
                continue

            again_pin = input("Confirm New PIN: ")

            if new_pin != again_pin :
                print("PIN no match")
                continue

            pin = new_pin
            print("PIN changed successfully")
            break # 跳出 ATM 循环，回到登录循环

        elif choice == 5:
            print("Thanks For Visit Bank")
            exit()
