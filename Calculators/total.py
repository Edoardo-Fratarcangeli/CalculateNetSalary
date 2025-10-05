from taxes import calculateNetIncome
from expenses import expensesAndSum
import pandas as pd

# solo queste verranno importate con *
__all__ = ['analyze'] 

def analyze(state, income, expenses_list):
    netIncome = calculateNetIncome(state, income)
    expensesTotal_list = expensesAndSum(expenses_list)
    return CreateFinanceDataFrame(state, netIncome, expensesTotal_list)


def CreateFinanceDataFrame(state, net_income, expenses_list):
    """
    Create a printable pandas DataFrame showing state, net income, and expenses.
    expenses_list: list of tuples (name, value), last item should be ("total", total_value)
    """
    # Costruisci il dizionario dei dati
    data = {
        "Category": ["Net Income"] + [name.capitalize() for name, _ in expenses_list],
        "Amount ($)": [net_income] + [value for _, value in expenses_list]
    }

    df = pd.DataFrame(data)
    df.index = [state] * len(df)  # opzionale: ripeti lo stato come indice
    df.index.name = "State"

    return df
