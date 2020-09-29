from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange, Length, Regexp, ValidationError


class NoviZaposlenikForm(FlaskForm):
    ime = StringField('Ime', validators=[DataRequired(), Length(min=2, max=20)])
    prezime = StringField('Prezime', validators=[DataRequired(), Length(min=2, max=20)])
    ukupno_dana = IntegerField('Ukupno dana godišnjeg', validators=[NumberRange(min=0, max=50)])
    submit = SubmitField('Potvrdi unos')
