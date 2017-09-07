from flask import Flask, render_template, request, redirect
from flask import flash
from forms import TickerSymbolForm

from stocks import get_dates, get_stock_data, plot_stocks

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TickerSymbolForm()
    script = None
    div = None
    bad_result = None
    if form.validate_on_submit():
        company = form.ticker_symbol.data

        #flash('You entered: %s' % (company))

        dates = get_dates()

        sdata = get_stock_data(company, dates[0], dates[1])
        if sdata.empty:
            bad_result = 'Data for {} not found'.format(company)
        else:
            script, div = plot_stocks(sdata, company)

        #return redirect('/')
    return render_template('index.html', form=form, bad_result=bad_result,
                            script=script, div=div)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
