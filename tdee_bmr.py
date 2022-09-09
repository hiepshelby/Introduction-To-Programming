def main():
    CURRENT_YEAR = 2022

    gender,yearborn,h_centimet,w_kg,activity_level = body_inform()
    h_centimet,w_kg,age,activity_level,yearborn = exchange_body_inform(CURRENT_YEAR,yearborn,h_centimet,w_kg,activity_level)
    bmr_male,bmr_female = bmr(h_centimet,w_kg,age,gender)
    calc_tdee_nam,calc_tdee_nu = tdee(bmr_male,bmr_female,activity_level,gender)
    print_inform(gender,h_centimet,w_kg,bmr_male,bmr_female,calc_tdee_nam,calc_tdee_nu)

def body_inform():
    print("\nGet information: ")
    print("----------")

    while True:
        gender = input("Your gender (male/female): ")
        if gender == "male" or gender == "female":
            break

    yearborn = input("What year were you born: ")
    h_centimet = input("Your height (cm): ")
    w_kg = input("Yout weight (kg): ")

    print("\nChoose your activity level: ")
    print("----------")
    print("Little Activity (no exercise): 1.2")
    print("Light Activity (exercise 1 - 3 days per week): 1.375")
    print("Moderate Activity (exercise 3 - 5 days per week): 1.55")
    print("Strong Activity (exercise 6 - 7 days per week): 1.725")
    print("Very Strong Activity (exercise 2 times per day): 1.9")
    
    print("----------")
    activity_level = input("Choose your activity level (enter only number): ")
    return gender,yearborn,h_centimet,w_kg,activity_level

def exchange_body_inform(CURRENT_YEAR,yearborn,h_centimet,w_kg,activity_level):
    yearborn = int(yearborn)
    h_centimet = float(h_centimet)
    w_kg = float(w_kg)
    activity_level = float(activity_level)

    age = CURRENT_YEAR - yearborn

    return h_centimet,w_kg,age,activity_level,yearborn

def bmr(h_centimet,w_kg,age,gender):
        bmr_male = 10 * w_kg + 6.25 * h_centimet - 5 * age + 5
        bmr_female = 10 * w_kg + 6.25 * h_centimet - 5 * age - 161

        bmr_male = round(bmr_male,2)
        bmr_female = round(bmr_female,2)

        return bmr_male,bmr_female
    
def tdee(bmr_male,bmr_female,activity_level,gender):
        TDEE_nam = bmr_male * activity_level
        TDEE_nu = bmr_female * activity_level

        TDEE_nam = round(TDEE_nam,2)
        TDEE_nu = round(TDEE_nu,2)

        return TDEE_nam,TDEE_nu
        
def print_inform(gender,h_centimet,w_kg,bmr_male,bmr_female,calc_tdee_nam,calc_tdee_nu):
    print("\nRusult Information: ")
    print("----------")
    print("Your gender: " + gender)
    print("Your height (cm): " + str(h_centimet))
    print("Your weight (kg): " + str(w_kg))
    
    if gender == "male":
        print("Your BMR: " + str(bmr_male)) 
    else:
        print("Your BMR: " + str(bmr_female)) 
    
    if gender == "male":
        print("Your TDEE: " + str(calc_tdee_nam))
    else:
        print("Your TDEE: " + str(calc_tdee_nu))

main()