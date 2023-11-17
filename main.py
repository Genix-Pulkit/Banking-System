import json
import random
import  time
import  sys

title = """
================================================================

████████ ██   ██ ███████     ██████   █████  ███    ██ ██   ██ 
   ██    ██   ██ ██          ██   ██ ██   ██ ████   ██ ██  ██  
   ██    ███████ █████       ██████  ███████ ██ ██  ██ █████   
   ██    ██   ██ ██          ██   ██ ██   ██ ██  ██ ██ ██  ██  
   ██    ██   ██ ███████     ██████  ██   ██ ██   ████ ██   ██ 
                                                               
================================================================
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
        if status.lower() == 'minor':
            mother_name = input("Enter your Mother's Name : ")
            father_name = input("Enter your Father's Name : ")
            married_status = None
        elif status.lower() == 'adult':
            mother_name = None
            father_name = None
            married_status = input("Enter your married status (Married/Unmarried) : ")
        else:
            mother_name = None
            father_name = None
            married_status = None

        nationality = input("Enter your nationalty : ")

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

        while True:
            balance = input("How much you want to deposit now : ")
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
                "PIN" : pin,
                "Group" : group,
                "Date of Birth" : date_of_birth,
                "Gender" : gender,
                "Status" : status,
                "Mother's name" : mother_name,
                "Father's name" : father_name,
                "Married Status" : married_status,
                "Nationality" : nationality,
                "PAN Number" : pan_number,
                "Aadhar Number" : aadhar_number,
                "Address" : address,
                "Pin Code" : pin_code,
                "Mobile Number" : mobile_number,
                "Email Address" : email,
                "Balance": balance
            }
            save_accounts(accounts)

            print("Just give us a second...")
            time.sleep(3)

            print(f'''
    Subject: Your New Account is Open!
    
    Dear {name},
    
    Congratulations! Your account with The Bank has been successfully opened. Here are your essential details:
    
    Account Number: {account_number}
    4-Digit PIN: {pin}
    Please remember to keep this information confidential for your security. If you have any questions or need assistance, feel free to reach out.
    
    Thank you for choosing us. We look forward to serving you!
    
    Best regards,
    
    Bank Account Management
    The Bank
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
        print("Please enter valid input...")

    while True:
        amount = input("Enter the amount to deposit: ")
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

        print(f"Deposited {amount} successfully. New balance: {accounts[account_number]['Balance']}")

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
        print("Please enter valid input...")

    while True:
        amount = input("Enter the amount to deposit: ")
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
            print(f"Withdrew {amount} successfully. New balance: {accounts[account_number]['Balance']}")
            main()
        else:
            print("Just give us a second...")
            time.sleep(2)
            print("Sorry but dont have enough funds.")
            main()
    else:
        print("The Pin entered is not correct.")
        main()

def fd_enquiry():
    while True:
        amount = input("Enter the amount : ")
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
    if age >= 60 and age <= 80:
        rate_of_interest = 7.50
    else:
        rate_of_interest = 6.50

    maturity_amnt = (amount * time * rate_of_interest) / 100

    print(f"Your maturity amount is {maturity_amnt}.")
    main()

def forgot_details():
    acconts = load_accounts()
    name = input("Enter your name : ").lower()
    if ' ' in name:
        name = name.split()[0]
    else:
        name = name
    print("Just give us a second...")
    time.sleep(3)
    for i in acconts:
        if name in acconts[i]['Name'].lower().split():
            print(f'''
        Account Number : {i}
        Name : {acconts[i]['Name']}
        PIN : {acconts[i]['PIN']}
        Group : {acconts[i]['Group']}
        Date of Birth : {acconts[i]['Date of Birth']}
        Gender : {acconts[i]['Gender']}
        Status : {acconts[i]['Status']}
        Mother's Name : {acconts[i]["Mother's name"]}
        Father's Name : {acconts[i]["Father's name"]}
        Married Status : {acconts[i]["Married Status"]}
        Nationality : {acconts[i]["Nationality"]}
        PAN Number : {acconts[i]["PAN Number"]}
        Aadhar Number : {acconts[i]["Aadhar Number"]}
        Address : {acconts[i]["Address"]}
        Pin Code : {acconts[i]["Pin Code"]}
        Mobile Number : {acconts[i]["Mobile Number"]}
        Email : {acconts[i]["Email Address"]}
        ''')
            main()
        else:
            continue
    print("Your account does not exist.")
    main()


def main():
    while True:
        print("\nWelcme to the bank!")
        print("[1] Open Account")
        print("[2] Deposit Money")
        print("[3] Withdraw Money")
        print("[4] Fixed Deposit Enquiry")
        print("[5] Forgot Details")
        print("[6] Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            open_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            fd_enquiry()
        elif choice == "5":
            forgot_details()
        elif choice == "6":
            print("Exiting program. Thank you!")
            sys.exit()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    print(title)
    main()
