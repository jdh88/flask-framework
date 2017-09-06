from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TickerSymbolForm(FlaskForm):
    ticker_symbol = StringField('ticker_symbol', validators=[DataRequired()])
    yesno = BooleanField('yesno', default=False)
