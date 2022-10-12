
import random as rnd
from datetime import date, datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()
import plotly.graph_objects as go
from avaiable_tickers import avaiable_tickers
import matplotlib.image as mpimg
from PIL import Image
#from mpl_finance import candlestick_ohlc
#import matplotlib.dates as mpl_dates

class Index:
    ind = 0
    my_colors = ['red','green','darkblue','black','lime','indigo']
    random_ticker = rnd.choice(avaiable_tickers)
    number_of_other_tickers = 2
    number_of_past_months = 24
    end_date = datetime.now()
    start_date = datetime.now()
    df = pdr.get_data_yahoo(random_ticker,  start="2010-01-01", end="2022-04-30")
    all_tickers = [] 
    px = 1/plt.rcParams['figure.dpi']  # pixel in inches

    fig, ax = plt.subplots(figsize=(1200*px, 600*px))
    plt.suptitle('Which stock is it?',fontsize='large',
                                    fontweight='bold',
                                    style='italic',
                                    family='monospace')

    plt.title(' -  '.join(avaiable_tickers),fontweight='bold')
    plt.xlabel('years')
    plt.ylabel('stock price $')

    fig.subplots_adjust(bottom=0.25)
    l, = ax.plot(df['Adj Close'], lw=2)
    # l = candlestick_ohlc(ax, df.values, width=0.6,
    #              colorup='green', colordown='red', alpha=0.8)

    axnext = fig.add_axes([0.81, 0.05, 0.07, 0.075])
    axconfirm = fig.add_axes([0.61, 0.05, 0.1, 0.075])
    
    def __init__(self) -> None:
        
        button_next = Button(self.axnext, 'next')
        button_next.on_clicked(self.next)

        # button_change_colors = Button(axcolors, 'change color')
        # button_change_colors.on_clicked(callback.change_color)

        button_confirm = Button(self.axconfirm, 'show')
        button_confirm.on_clicked(self.confirm)
        plt.show()


    def generate_random_ticker(self):
        return rnd.choice(avaiable_tickers)

    def generate_other_tickers(self):
        self.unvalid_tickers = [0 for i in range(self.number_of_other_tickers)]
        for i in range(self.number_of_other_tickers):
            unvalid_ticker = rnd.choice(avaiable_tickers)
            while unvalid_ticker == self.random_ticker or unvalid_ticker in self.unvalid_tickers:
                unvalid_ticker = rnd.choice(avaiable_tickers)
            self.unvalid_tickers[i] = unvalid_ticker
         
    def get_all_tickers(self):
        self.random_ticker = self.generate_random_ticker()
        self.all_tickers += [self.random_ticker]
        self.all_tickers = str(rnd.sample(self.all_tickers,len(self.all_tickers)))
        return self.all_tickers, self.random_ticker 

    # def change_color(self, event):
    #     self.ind += 1
    #     if self.ind > len(self.my_colors)-1:
    #         self.ind = 0
    #     self.l.set_ydata(self.df['Adj Close'])
    #     self.l.set_color(color=self.my_colors[abs(self.ind)])
    #     plt.draw()

    def next(self, event):
        self.random_ticker = rnd.choice(avaiable_tickers)
        self.df = pdr.get_data_yahoo(self.random_ticker, start="2010-01-01", end="2022-04-30")
        self.l.set_xdata(self.df.index)
        self.l.set_ydata(self.df['Adj Close'])
        # self.l.set_ydata(        candlestick_ohlc(ax, df.values, width=0.6,
        #          colorup='green', colordown='red', alpha=0.8))


        self.ax.set_ylim(min(self.df['Adj Close']),max(self.df['Adj Close']))       
        plt.draw()    

    def confirm(self, event):
        img = Image.open(f'./images/{self.random_ticker}.png')
        img.show()

callback = Index()
# axcolors = fig.add_axes([0.61, 0.05, 0.09, 0.075])
