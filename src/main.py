import yfinance as yf
import pandas as pd
from pathlib import Path
import json

statements_dir = Path(__file__).parent.parent/ "Statements"
statements_dir.mkdir(parents=True, exist_ok=True)

ticker = input("Enter company code (e.g. AAPL, CBA.XA): ")

def save_ticker_data(ticker):
    dat = yf.Ticker(ticker)

    balance_sheet = dat.get_balance_sheet()
    cash_flows = dat.get_cash_flow()
    income_statement = dat.get_income_stmt()
    
    financial_data = {
        "balance_sheet": balance_sheet,
        "cash_flows": cash_flows,
        "income_statement": income_statement
    }
    
    for name, data in financial_data.items():
        filepath = statements_dir / f'{ticker}_{name}.json'
        data.to_json(filepath, orient = 'split', compression = 'infer', index = 'true')

def load_ticker_data(ticker):
    filepath = statements_dir / f'{ticker}_balance_sheet.json'
    with open(filepath) as file:
        balance_sheet = json.load(file)
        return balance_sheet
def get_ticker_data():
    return 0

# save_ticker_data(ticker)

bs = load_ticker_data(ticker)

index_list = bs['index']
data_list = bs['data']

retained_earnings_index = index_list.index("RetainedEarnings")
retained_earnings = data_list[retained_earnings_index][0]

print(retained_earnings)
