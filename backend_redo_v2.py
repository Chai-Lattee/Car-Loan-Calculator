MONTH_DAYS = 30 
import time

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
    return (daily_distance * MONTH_DAYS) / mpg * gas_cost

def calculate_loan_cost(loan_amount, loan_term, interest_rate=0.0663):
    monthly_interest_rate = interest_rate / 12
    monthly_payment = (monthly_interest_rate * loan_amount) / (1 - (1 + monthly_interest_rate) ** -loan_term)
    total_cost = monthly_payment * loan_term
    total_interest = total_cost - loan_amount
    return monthly_payment, total_cost, total_interest

def selected_loan_term(): 
    '''
    This function asks user to select a loan term from a key value set
    '''
    loan_terms = {'a': 12, 'b': 24, 'c': 36, 'd': 48, 'e': 60, 'f': 72}
    selected_key = input("Choose a letter corresponding to the loan term (in months)\n(a = 12, b = 24, c = 36, d = 48, e = 60, f = 72): ").lower()
    while selected_key not in loan_terms:
        selected_key = input("Invalid choice. Please choose a valid letter (a, b, c, d, e, f): ").lower()
    return loan_terms[selected_key]    

def calculate_costs_for_car(car_data):
    '''
    This function asks user how many miles he/she drives per day and then calculates it to get fuel cost 
    Also asks user for the down payment option with optional desired amount
    '''
    daily_distance = float(input("How many miles do you drive per day? "))
    fuel_cost = calculate_fuel_cost(daily_distance, car_data.mpg)
    fuel_cost = round(fuel_cost, 2)

    make_down_payment = input("Do you want to make a down payment? (y/n): ").lower()
    if make_down_payment == 'y':
        down_payment_percentage = float(input("Enter the down payment percentage (without the '%' sign): ")) / 100
        down_payment_amount = car_data.principle_cost * down_payment_percentage
    else:
        down_payment_amount = 0

    adjusted_principle_cost = car_data.principle_cost - down_payment_amount

    loan_term = selected_loan_term()
    monthly_payment, total_cost, total_interest = calculate_loan_cost(adjusted_principle_cost, loan_term)

    print(f"Total principle cost of the loan is ${total_cost:.2f}")
    time.sleep(2)
    print(f"Total interest paid is ${total_interest:.2f}")
    time.sleep(2)
    print(f"Your annual repair costs based on the car's size will be ${car_data.repair}.")
    time.sleep(2)
    print(f"Your fuel principle cost per month will be ${fuel_cost:.2f}")
    print(f"Your monthly loan payment is ${monthly_payment:.2f} based on a 6.63% annual interest rate.")
    time.sleep(2)

def main():
    '''
    - This is the main function which contains the car classes
    - This function is encapsulated so that a second car can be entered (at the end of the first car's calculation) if  hte user desires 
    '''
    car_classes = {
        'compact': compact, 'sedan': sedan, 'hatchback': hatchback, 'coupe': coupe,
        'sports': sports, 'luxury': luxury, 'wagon': wagon, 'large suv': large_suv, 'pickup': pickup
    }

    for i in range(2):  # Loop twice for two cars
        selected_car = input(f"Please pick car class #{i+1} listed:\n compact\n sedan\n hatchback\n coupe\n sports\n luxury\n wagon\n large suv\n pickup\n Answer here: ").lower()

        if selected_car in car_classes:
            car_data = car_classes[selected_car]
            print(f"Calculating costs for {selected_car}...")
            calculate_costs_for_car(car_data)
            if i == 0:  # After the first car, ask if the user wants to continue
                continue_choice = input("Do you want to calculate for another car? (y/n): ").lower()
                if continue_choice != 'y':
                    break
        else:
            print("Invalid car class. Please try again.")
            break  # Break the loop if invalid class is selected

if __name__ == "__main__":
    main()