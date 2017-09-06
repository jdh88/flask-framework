"""
Helper functions that get stock data and plot it, returning html and javascript code to embedd it
"""

import requests
import calendar
import datetime as dt
import pandas as pd
from bokeh import plotting as bk
from bokeh.embed import components
from bokeh.models import HoverTool

def get_dates():
    """
    Returns the current date and one month ago
    """
    today = dt.date.today()
    lastmonth = today - dt.timedelta(days=calendar.monthrange(today.year, today.month)[1])

    return [str(lastmonth), str(today)]


def get_stock_data(company, start_date_inc, stop_date_inc):
    """
    Gets the stock data for a given company between two dates

    :company: the company ticker name
    :param start_date_inc: the start date of interest (inclusive)
    :param stop_date_inc: the end date of interest (inclusive)

    :return: pandas data table with the stock data
    """

    api_key = 'Bo9P_cJnmf5EsQPp1Bdp'
    desired_cols = 'date,close'

#    ticker = 'FB'
#    start_date_inc = '20170801'
#    end_date_inc = '20170831'

    # format and send the request
    payload = {
        'date.gte': start_date_inc,
        'date.lte': stop_date_inc,
        'ticker': company,
        'qopts.columns': desired_cols,
        'api_key': api_key
    }
    meta_url = r'https://www.quandl.com/api/v3/datatables/WIKI/PRICES'
    r = requests.get(meta_url, params=payload)

    # convert to a pandas dataframe
    df = pd.DataFrame(r.json()['datatable']['data'])
    if not df.empty:
        df.columns = ['date', 'price']
        df['date'] = pd.to_datetime(df['date'])

    return df


def plot_stocks(df, ticker):
    """
    :param df: the pandas data frame with the stock data and datatables
    :param ticker: the name of the company (used in title)

    :return: script and div elements for a bokeh based plot
    """
    title = 'Closing prices for: ' + ticker
    f = bk.figure(title=title, x_axis_type='datetime')
    f.xaxis.axis_label = 'Date'
    f.yaxis.axis_label = 'Closing Price (USD)'

    source = bk.ColumnDataSource(data=dict(
        x = df['date'],
        y = df['price']))

    hover = HoverTool(
        tooltips=[
            ('Date:', '@x{%F}'),
            ('Price:', '@y{($ 0.00 a)}'),
        ],
        formatters={
            'x': 'datetime',
            'y': 'numeral'
        })
    f.add_tools(hover)

    f.line('x', 'y', source=source)

    return components(f)
