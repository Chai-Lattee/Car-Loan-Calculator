MONTH_DAYS = 30 

class Car():
    def __init__(self, mpg, principle_cost, repair):
        ''' 
        This function is classifying cars in terms of mpg, principle cost (new car) and annual repair costs based on the car's size 
        '''
        self.mpg = mpg 
        self.principle_cost = principle_cost
        self.repair = repair 

compact = Car(32, 23839, 887)
sedan = Car(31.7, 31758, 887)
hatchback = Car(30, 33795, 1064)
coupe = Car(24, 51770, 1064)
sports = Car(25, 32961, 1200)
luxury = Car(21, 42040, 1064)
wagon = Car(30, 25678, 1064)
large_suv = Car(20, 54520, 1064)
pickup = Car(22, 37895, 1200)

def calculate_fuel_cost(daily_distance, mpg, gas_cost=5.55):
    '''
    This function takes in the user's input of daily miles driven and calculates it with 
    the average cost of premium gas in CA, $5.55  
    To make things simple, I will use the standard 30 days in a month for all calculations 
    '''
    return (daily_distance * 30) / mpg * gas_cost

def calculate_monthly_cost(principle_cost, down_payment, interest_rate=0.0663):
    ''' 
    This function takes the selected car's principle cost and multiplies it with the interest rate of 6.63%
    This function also asks the user if they want to put a down payment
    If yes, 20% of the principle cost will be deducted
    '''
    if down_payment == 'y':
        principle_cost -= principle_cost * 0.20
    monthly_cost = principle_cost * interest_rate
    return round(monthly_cost / MONTH_DAYS , 2)


def calculate_loan_cost(loan_amount, loan_term, interest_rate=0.0663):
# Monthly payment formula: P = [r*PV] / [1 - (1 + r)^-n]
    monthly_interest_rate = interest_rate / 12
    monthly_payment = (monthly_interest_rate * loan_amount) / (1 - (1 + monthly_interest_rate) ** -loan_term)

    total_cost = monthly_payment * loan_term
    total_interest = total_cost - loan_amount

    return monthly_payment, total_cost, total_interest

def selected_loan_term(): 
    '''
    This dictionary stores loan terms in letters.
    a is 12 months, so each consecutive letter is += 12 months. 
    User will select a letter based on the loan term he/she wants. 
    '''
    loan_terms = {
        'a' : 12,
        'b' : 24,
        'c' : 36,
        'd' : 48,
        'e' : 60, 
        'f' : 72 
    }
    selected_key = input("Choose a letter corresponding to the loan term (a, b, c, d, e, f): ").lower()
    # Validate user input 
    while selected_key not in loan_terms:
        print("Invalid choice, Please choose a valid letter.")
        selected_key = input("Choose a letter corresponding to the loan term (a, b, c, d, e, f): ").lower()
    return loan_terms[selected_key]    

def main():
    '''
    This is the main function in which we will calculate the user's 
    - fuel cost per month based on user's daily distance 
    - monthly loan payment
    - total cost of the loan 
    - total interest paid 
    '''
    car_classes = {
        'compact': compact,
        'sedan': sedan,
        'hatchback': hatchback,
        'coupe': coupe,
        'sports': sports,
        'luxury': luxury,
        'wagon': wagon,
        'large suv': large_suv,
        'pickup': pickup
    }
    
 
    selected_car = input("Please pick a car class listed: compact\n sedan\n hatchback \n coupe\n sports\n luxury\n wagon\n large suv\n pickup\n Answer here: ").lower()
    
    if selected_car in car_classes:
        car_data = car_classes[selected_car]
        daily_distance = float(input("How many miles do you drive per day? "))
        fuel_cost = calculate_fuel_cost(daily_distance, car_data.mpg)
        fuel_cost = round(fuel_cost, 2)
        print(f"Your fuel principle cost per month will be ${fuel_cost}")

# Figure out how to get down payment calculated 
        make_down_payment = input("Do you want to make a down payment? (y/n): ").lower()
        down_payment_bool = make_down_payment == 'y'

 # Apply down payment to the principle cost if chosen
        adjusted_principle_cost = car_data.principle_cost * 0.80 if down_payment_bool else car_data.principle_cost

        loan_term = selected_loan_term()
        monthly_payment, total_cost, total_interest = calculate_loan_cost(car_data.principle_cost, loan_term)
        print(f"Your monthly loan payment is ${monthly_payment:.2f}")
        print(f"Total principle cost of the loan is ${total_cost:.2f}")
        print(f"Total interest paid is ${total_interest:.2f}")


        print(f"Your annual repair costs based on the car's size will be ${car_data.repair}")
    else:
        print("Invalid car class.")
main()