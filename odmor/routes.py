from flask import render_template, flash, url_for, redirect
from odmor.forms import NoviZaposlenikForm
from odmor.models import Zaposlenik, Odmor, UkupnoDana
from odmor import app, db


# zaposlenici = [
#     {
#         'rb': 1,
#         'ime': 'Ivan',
#         'prezime': 'Maric',
#         'ukupno_dana': 20,
#         'iskoristeno': 10
#     },
#     {
#         'rb': 2,
#         'ime': 'Josip',
#         'prezime': 'Tokic',
#         'ukupno_dana': 21,
#         'iskoristeno': 11
#     },
#     {
#         'rb': 3,
#         'ime': 'Ante',
#         'prezime': 'Antic',
#         'ukupno_dana': 22,
#         'iskoristeno': 12
#     },
# ]


@app.route('/')
def home():
    zaposlenici = Zaposlenik.query.join(UkupnoDana)
    zaposlenici = db.session.query(Zaposlenik).join(Odmor, Zaposlenik.rb == Odmor.zaposlenik_rb)
    print(zaposlenici)
    return render_template('home.html', zaposlenici=zaposlenici)


@app.route('/novi_zaposlenik', methods=['GET', 'POST'])
def novi_zaposlenik():
    form = NoviZaposlenikForm()
    if form.validate_on_submit():
        flash(f'Uspiješno kreiran zaposlenik: {form.ime.data} {form.prezime.data}', 'success')
        return redirect(url_for('home'))
    return render_template('create_user.html', form=form, title='Novi Zaposlenik')
