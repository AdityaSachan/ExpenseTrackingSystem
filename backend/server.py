from fastapi import FastAPI
from datetime import date
import db_helper

app=FastAPI()

@app.get('/expenses/{expense_date}')
def get_expenses(expense_date : date):
    return {expense_date}