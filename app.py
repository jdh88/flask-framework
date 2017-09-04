from flask import Flask, render_template, request, redirect
from flask import flash
from forms import TickerSymbolForm

app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TickerSymbolForm()
    if form.validate_on_submit():
        flash('Company: %s' % (form.ticker_symbol.data))
        #flash('The following data was submitted: \n'
        #      + 'Ticker Symobl: %s' % (form.ticker_symbol.data))
        return redirect('/')
    return render_template('index.html', form=form)

if __name__ == '__main__':
  app.run(port=33507)
