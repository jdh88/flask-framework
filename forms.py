from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TickerSymbolForm(Form):
    ticker_symbol = StringField('ticker_symbol', validators=[DataRequired()])
    yesno = BooleanField('yesno', default=False)
