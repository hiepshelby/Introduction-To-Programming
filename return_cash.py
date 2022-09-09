def main():
    APPLES_PRICE_PER_KG = 20
    
    apples_weight = float(input("Enter weight (kg): "))
    customer_give = float(input("Customer give: "))

    total_price = calc_total_price(APPLES_PRICE_PER_KG, apples_weight)
    money_return = calc_money_return(customer_give, total_price)

    print("Total money: " + str(total_price))
    print("-----------")

    exchange_money_return(customer_give, total_price, money_return)

def calc_total_price(APPLES_PRICE_PER_KG, apples_weight):
    return apples_weight * APPLES_PRICE_PER_KG

def calc_money_return(customer_give, total_price):
    if customer_give < total_price:
        return -1
    return customer_give - total_price

def exchange_money_return(customer_give, total_price, money_return):
    if money_return == -1:
        customer_have_to_pay_more = total_price - customer_give
        print("Not enough money, customer have to pay more: " + str(customer_have_to_pay_more))
    elif money_return == customer_give:
        print("Enough money")
    else:
        print("You have to pay for customer: " + str(money_return))
        print_money_info(money_return)

def print_money_info(money_return):
    left_over_1 = money_return % 500
    count_500 = (money_return - left_over_1) / 500
    if count_500 != 0:
        print("So to 500: " + str(count_500))

    left_over_2 = left_over_1 % 200
    count_200 = (left_over_1 - left_over_2) / 200
    if count_200 != 0:
        print("So to 200: " + str(count_200))

    left_over_3 = left_over_2 % 100
    count_100 = (left_over_2 - left_over_3) / 100
    if count_100 != 0:
        print("So to 100: " + str(count_100))

    left_over_4 = left_over_3 % 50
    count_50 = (left_over_3 - left_over_4) / 50
    if count_50 != 0:
        print("So to 50: " + str(count_50))

    left_over_5 = left_over_4 % 20
    count_20 = (left_over_4 - left_over_5) / 20
    if count_20 != 0:
        print("So to 20: " + str(count_20))

    left_over_6 = left_over_5 % 10
    count_10 = (left_over_5 - left_over_6) / 10
    if count_10 != 0:
        print("So to 10: " + str(count_10))

    left_over_7 = left_over_6 % 5
    count_5 = (left_over_6 - left_over_7) / 5
    if count_5 != 0:
        print("So to 5: " + str(count_5))

    left_over_8 = left_over_7 % 2
    count_2 = (left_over_7 - left_over_8) / 2
    if count_2 != 0:
        print("So to 2: " + str(count_2))

    count_1 = left_over_8
    if count_1 != 0:
        print("So to 1: " + str(count_1))

main()