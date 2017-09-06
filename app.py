from flask import Flask, render_template, request, redirect
from flask import flash
from forms import TickerSymbolForm

from stocks import get_stock_data, plot_stocks

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TickerSymbolForm()
    script = None
    div = None
    if form.validate_on_submit():
        company = form.ticker_symbol.data

        flash('You entered: %s' % (company))

        sdata = get_stock_data(company, '20170801', '20170831')
        script, div = plot_stocks(sdata, company)

        #return redirect('/')
    return render_template('index.html', form=form, script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)
