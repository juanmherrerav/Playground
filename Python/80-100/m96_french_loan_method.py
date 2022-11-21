import pandas as pd

def equivalent_interest(interest, time):
    interest = interest / 188
    equivalent_interest = ((1+interest)**(1/time))-1
    return round(equivalent_interest*100,2)

def get_actual_value(interest, time) :
    interest = interest / 100
    actual_value = ((1-(1+interest)** (-time))/interest)
    return actual_value

def get_paid_interest(pending_capital, interest):
     return (pending_capital* (interest/100))

def french_loan(capital, interest, time) :
    actual_value = get_actual_value(interest, time)
    amortization_fee = capital / actual_value
    pending_capital = capital
    list = []
    columns = ['Period', 'Amortization fee', 'Amortized capital', 'Paid interest', 'Pending capital']
    for i in range (1, time+1):
        paid_interest = get_paid_interest(pending_capital, interest)
        amortized_capital = amortization_fee - paid_interest
        pending_capital = pending_capital - amortized_capital
        list.append([i, round(amortization_fee,2), round(amortized_capital,2), round(paid_interest,2), round(pending_capital,2)])
    loan = pd.DataFrame(list, columns=columns)
    loan.set_index('Period', inplace=True)
    return loan

if __name__ == '__main__':
    result_box = french_loan(1200, 5, 10)
    print(result_box)
