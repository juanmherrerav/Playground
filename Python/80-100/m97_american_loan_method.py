import m96_french_loan_method as fin
import pandas as pd

def american_loan(capital, interest, time):
    pending_capital = capital
    period_list = []
    columns = ["Period", 'Amortized Capital', 'Paid interest', 'Pending capital']
    for i in range(1, time+1):
        paid_interest = fin.get_paid_interest(pending_capital, interest)
        if i == time :
            amortized_capital = capital
        else:
            amortized_capital = 0
        pending_capital = pending_capital - amortized_capital
        period_list.append([i, round(amortized_capital, 2), round(paid_interest, 2), round(pending_capital, 2)])
    loan = pd.DataFrame(period_list, columns=columns)
    loan.set_index( 'Period', inplace=True)
    return loan


if __name__ == '__main__':
    result_box = american_loan(1200, 5, 10)
    print(result_box)
    print("*"*80)
    result_box = fin.french_loan(1200, 5, 10)
    print(result_box)
