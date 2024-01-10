import json
import random
import time

title = """
===========================================================================


███████ ██     ██ ██ ███████ ███████     ██████   █████  ███    ██ ██   ██ 
██      ██     ██ ██ ██      ██          ██   ██ ██   ██ ████   ██ ██  ██  
███████ ██  █  ██ ██ ███████ ███████     ██████  ███████ ██ ██  ██ █████   
     ██ ██ ███ ██ ██      ██      ██     ██   ██ ██   ██ ██  ██ ██ ██  ██  
███████  ███ ███  ██ ███████ ███████     ██████  ██   ██ ██   ████ ██   ██ 
                                                                           
                                                               
===========================================================================
"""


def load_accounts():
    try:
        with open("accounts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=2)


def open_account():
    accounts = load_accounts()

    print("Hello! This is account management section.\nYou will get an interest rate of 2.70% on your savings account.")
    boolean = input("Do you still want to continue (y/n) : ")
    if boolean.lower() == "y":
        boolean = True
    elif boolean.lower() == "n":
        boolean = False
    else:
        boolean = False

    if boolean:
        name = input("Enter account holder's name: ")

        group = input("Are you individidual or HUF (Hindu United Family) : ")
        if group.lower() == "individual":
            group = group
        elif group.lower() == "huf":
            group = "HUF"
        else:
            group = "Unknown"
        while True:
            date_of_birth = input("Enter your Date of Birth (DD/MM/YYYY) : ")
            try:
                if len(date_of_birth) >= 5:
                    if date_of_birth[2] == '/' and date_of_birth[5] == '/':
                        break
                    else:
                        raise ValueError
                else:
                    raise ValueError
            except:
                pass
            print("Please enter in format DDD/MM/YYYY...")

        gender = input("What's your gender (M/F/T) : ")
        if gender.lower() == 'm':
            gender = "Male"
        elif gender.lower() == 'f':
            gender = "Female"
        elif gender.lower() == 't':
            gender = "Transgender"
        else:
            gender = "Unknown"

        status = input("Enter your Status (Minor/Adult) : ")
        if status.lower() == 'minor' or status.lower() == 'm':
            mother_name = input("Enter your Mother's Name : ")
            father_name = input("Enter your Father's Name : ")
            married_status = None
        elif status.lower() == 'adult' or status.lower() == 'a':
            mother_name = None
            father_name = None
            married_status = input("Enter your married status (Married/Unmarried) : ")
        else:
            mother_name = None
            father_name = None
            married_status = None

        nationality = input("Enter your nationality : ")

        while True:
            pan_number = input("Enter your Pan number : ")
            try:
                pan_number = int(pan_number)
                break
            except:
                pass
            print("Please enter an integer...")

        while True:
            aadhar_number = input("Enter your Aadhar number : ")
            try:
                aadhar_number = int(aadhar_number)
                break
            except:
                pass
            print("Please enter an integer...")

        address = input("Enter your Address : ")

        while True:
            pin_code = input("Enter your Pin Code : ")
            try:
                pin_code = int(pin_code)
                break
            except:
                pass
            print("Please enter an integer...")

        while True:
            mobile_number = input("Enter your Mobile number : ")
            try:
                mobile_number = int(mobile_number)
                break
            except:
                pass
            print("Please enter an integer...")

        email = input("Enter your Email address : ")

        security_ques = input("Enter your security question : ")

        security_ans = input("Enter your security answer : ")

        while True:
            balance = input("How much you want to deposit now : ₹")
            try:
                balance = float(balance)
                break
            except:
                pass
            print("please enter a valid amount...")

        print("Please accept the following declaration")
        print("I hereby acknowledge that I have received and read the terms and conditions, agree to comply with the "
              "policies set forth by The Bank, and confirm that the information provided is accurate to the best of my "
              "knowledge.")
        accepted = input("Do you accept the above declaration (y/n) : ")
        if accepted.lower() == "y":
            accepted = True
        elif accepted.lower() == "n":
            accepted = False
        else:
            accepted = False

        if accepted:
            account_number = random.randint(100000000000, 999999999999)
            if account_number in accounts:
                return

            pin = random.randint(1000, 9999)

            accounts[account_number] = {
                "Name": name.capitalize(),
                "PIN": pin,
                "Group": group.capitalize(),
                "Date of Birth": date_of_birth,
                "Gender": gender,
                "Status": status,
                "Mother's name": mother_name,
                "Father's name": father_name,
                "Married Status": married_status,
                "Nationality": nationality.capitalize(),
                "PAN Number": pan_number,
                "Aadhar Number": aadhar_number,
                "Address": address,
                "Pin Code": pin_code,
                "Mobile Number": mobile_number,
                "Email Address": email,
                "Security Question": security_ques,
                "Security Answer": security_ans,
                "Balance": balance
            }
            save_accounts(accounts)

            print("Just give us a second...")
            time.sleep(3)

            print(f'''
    Dear {name.capitalize()},
    
    Congratulations! Your account with The Swiss Bank has been successfully opened. Here are your essential details:
    
    Account Number: {account_number}
    4-Digit PIN: {pin}
    Please remember to keep this information confidential for your security. If you have any questions or need assistance, feel free to reach out.
    
    Thank you for choosing us. We look forward to serving you!
    
    Best regards,
    
    Bank Account Management
    The Swiss Bank
    ''')
        else:
            main()

    else:
        main()


def deposit_money():
    accounts = load_accounts()

    while True:
        account_number = input("Enter account number (or q to quit) : ")
        try:
            if account_number.lower() == 'q':
                main()
                break
            elif account_number in accounts:
                break
            else:
                raise ValueError
        except:
            pass
        print("Please enter correct account number...")

    if account_number.lower() == 'q':
        main()
    else:
        pass

    while True:
        amount = input("Enter the amount to deposit: ₹")
        try:
            amount = float(amount)
            break
        except:
            pass
        print("Enter a valid amount...")

    while True:
        check_pin = input("Enter Your Pin : ")
        try:
            check_pin = int(check_pin)
            break
        except:
            pass
        print("Please enter a valid input...")

    if check_pin == accounts[account_number]['PIN']:
        print("Just give us a second...")
        time.sleep(2)

        accounts[account_number]["Balance"] += amount
        save_accounts(accounts)

        print(f"Deposited ₹{amount} successfully. New balance: ₹{accounts[account_number]['Balance']}")

        main()
    else:
        print("The PIN entered is not correct.")
        main()


def withdraw_money():
    accounts = load_accounts()

    while True:
        account_number = input("Enter account number (or q to quit) : ")
        try:
            if account_number.lower() == 'q':
                main()
                break
            elif account_number in accounts:
                break
            else:
                raise ValueError
        except:
            pass
        print("Please enter correct account number...")

    if account_number.lower() == 'q':
        main()
    else:
        pass

    while True:
        amount = input("Enter the amount to withdraw: ₹")
        try:
            amount = float(amount)
            break
        except:
            pass
        print("Enter a valid amount...")

    while True:
        check_pin = input("Enter Your PIN : ")
        try:
            check_pin = int(check_pin)
            break
        except:
            pass
        print("Please enter a valid input...")

    if check_pin == accounts[account_number]["PIN"]:
        if accounts[account_number]['Balance'] - amount > 200.0:
            print("Just give us a second...")
            time.sleep(2)
            accounts[account_number]["Balance"] -= amount
            save_accounts(accounts)
            print(f"Withdrew ₹{amount} successfully. New balance: ₹{accounts[account_number]['Balance']}")
            main()
        else:
            print("Just give us a second...")
            time.sleep(2)
            print("I'm sorry, but you can't withdraw that much money since it won't maintain the minimum balance(₹200).")
            main()
    else:
        print("The Pin entered is not correct.")
        main()


def check_balance():
    accounts = load_accounts()

    while True:
        account_number = input("Enter account number (or q to quit) : ")
        try:
            if account_number.lower() == 'q':
                main()
                break
            elif account_number in accounts:
                break
            else:
                raise ValueError
        except:
            pass
        print("Please enter correct account number...")

    while True:
        check_pin = input("Enter Your PIN : ")
        try:
            check_pin = int(check_pin)
            break
        except:
            pass
        print("Please enter a valid input...")

    if check_pin == accounts[account_number]["PIN"]:
        print(f"Your Balance is ₹{accounts[account_number]['Balance']}.")
        main()
    else:
        print("The Pin entered is not correct.")
        main()


def fd_enquiry():
    while True:
        amount = input("Enter the amount : ₹")
        try:
            amount = float(amount)
            break
        except:
            pass
        print("Please enter a valid amount.")
    while True:
        time = input("Enter how many years you want to file fixed deposit : ")
        try:
            time = int(time)
            break
        except:
            pass
        print("Please enter an integer.")
    while True:
        age = input("Enter your age : ")
        try:
            age = int(age)
            break
        except:
            pass
        print("Please enter an integer.")
    if 60 <= age <= 80:
        rate_of_interest = 7.50
    else:
        rate_of_interest = 6.50

    maturity_amnt = amount + (amount * time * rate_of_interest) / 100

    print(f"Your maturity amount is ₹{maturity_amnt}.")
    main()


def forgot_details():
    accounts = load_accounts()
    name = input("Enter your name : ").lower()
    if ' ' in name:
        name = name.split()[0]
    else:
        name = name
    print("Just give us a second...")
    time.sleep(3)
    for i in accounts:
        if name in accounts[i]['Name'].lower().split():
            user_answer = input(accounts[i]['Security Question'] + ':')
            if user_answer.lower() == accounts[i]['Security Answer'].lower():
                print(f'''
            Account Number : {i}
            Name : {accounts[i]['Name']}
            PIN : {accounts[i]['PIN']}
            Group : {accounts[i]['Group']}
            Date of Birth : {accounts[i]['Date of Birth']}
            Gender : {accounts[i]['Gender']}
            Status : {accounts[i]['Status']}
            Mother's Name : {accounts[i]["Mother's name"]}
            Father's Name : {accounts[i]["Father's name"]}
            Married Status : {accounts[i]["Married Status"]}
            Nationality : {accounts[i]["Nationality"]}
            PAN Number : {accounts[i]["PAN Number"]}
            Aadhar Number : {accounts[i]["Aadhar Number"]}
            Address : {accounts[i]["Address"]}
            Pin Code : {accounts[i]["Pin Code"]}
            Mobile Number : {accounts[i]["Mobile Number"]}
            Email : {accounts[i]["Email Address"]}
            ''')
                main()
            else:
                print("Your answer does not match.")
                main()
        else:
            continue
    print("Your account does not exist.")
    main()


def main():
    while True:
        print("\nWelcome to The Swiss Bank!")
        print("[1] Open Account")
        print("[2] Deposit Money")
        print("[3] Withdraw Money")
        print("[4] Check Balance")
        print("[5] Fixed Deposit Enquiry")
        print("[6] Forgot Details")
        print("[7] Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            open_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            fd_enquiry()
        elif choice == "6":
            forgot_details()
        elif choice == "7":
            print("\nExiting program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    print(title)
    main()
