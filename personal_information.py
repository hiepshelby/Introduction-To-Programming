import datetime

def main():
    METER_TO_FEET = 3.281
    firstname, lastname, yearborn, height_meter = ask_personal_info()
    fullname, age, height_feet = convert_personal_info(firstname, lastname, yearborn, height_meter, METER_TO_FEET)
    is_male = ask_yes_no("Are you male (yes/no): ")
    is_vietnamese = ask_yes_no("Are you Vietnamese (yes/no): ")
    print_personal_info(fullname, age, height_feet, is_vietnamese)
    print_height_personal_info(height_feet, is_male)

def ask_personal_info():
    print("Ask Info:")
    print("----------")
    firstname = input("Your firstname: ")
    lastname = input("Your lastname: ")
    yearborn = int(input("When you were born: "))
    height_meter = float(input("Your height (meter): "))
    return firstname, lastname, yearborn, height_meter

def ask_yes_no(promt):
    while True:
        answer = input(promt)
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            continue

def convert_personal_info(firstname, lastname, yearborn, height_meter, METER_TO_FEET):
    now = datetime.datetime.now()
    CURRENT_YEAR = now.year
    fullname = firstname + " " + lastname
    age = CURRENT_YEAR - yearborn
    height_feet = height_meter * METER_TO_FEET
    height_feet = round(height_feet,1)
    return fullname, age, height_feet

def print_personal_info(fullname, age, height_feet, is_vietnamese):
    now = datetime.datetime.now()
    CURRENT_YEAR = now.year
    print("\nReturn Infor: ")
    print("----------")
    print("Your fullname: " + fullname)
    print("Your age: " + str(age) + " year old in " + str(CURRENT_YEAR))
    print("Your height feet: " + str(height_feet))
    if is_vietnamese == True:
        print("Your national: Viet Name")
    else:
        print("Your national: other coutries")
    
def print_height_personal_info(height_feet, is_male):
    if is_male == True:
        if height_feet > 6.5:
            print("You are", end = " ")
            for i in range(11):
                print("very", end = " ")
            print("tall as a man")
        elif height_feet > 6:
            print("You are tall as a man")
        elif height_feet < 5.5:
            print("You are", end = " ")
            for i in range(11):
                print("very", end = " ")
            print("short as a man")
        else:
            print("You are short as a man")
    elif is_male == False:
        if height_feet > 6:
            print("You are", end = " ")
            for i in range(11):
                print("very", end = " ")
            print("tall as a girl")
        elif height_feet > 5.7:
            print("You are tall as a girl")
        elif height_feet < 5:
            print("You are")
            for i in range(11):
                print("very",end = " ")
            print("short as a girl")
        else:
            print("You are short as a girl")

main()