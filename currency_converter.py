import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk


class RealTimeCurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        #convert to USD if not in USD as base currency
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)

        return amount



api = 'https://open.er-api.com/v6/latest/USD'

convert = RealTimeCurrencyConverter(api)

amount = convert.convert('NGN','USD', 137000)

print(amount)

class CurrencyConverterUI():
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter
        self.geometry("500x200")

        self.intro_label = Label(self, text="Welcome to Teal Time Currency Converter", fg='blue', relief = tk.RAISED, borderwidth = 3)
        self.intro_label.config(font=('Courier', 15, 'bold'))

        self.date_label = Label(self, text=f"1 Nigerian Naira equals = {self.currency_converter.convert('NGN','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief=tk.GROOVE, borderwidth=5)

        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=170, y=50)


c = CurrencyConverterUI(convert)