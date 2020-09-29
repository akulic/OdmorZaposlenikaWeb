from odmor import db


class Zaposlenik(db.Model):
    rb = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(20), nullable=False)
    prezime = db.Column(db.String(20), nullable=False)
    godisnji = db.relationship('Odmor', backref='zaposlenik', lazy=True)
    br_dana = db.relationship('UkupnoDana', backref='zaposlenik', lazy=True)

    def __repr__(self):
        return f"Zaposlenik('{self.ime}', '{self.prezime}')"


class Odmor(db.Model):
    rb = db.Column(db.Integer, primary_key=True)
    zaposlenik_rb = db.Column(db.Integer, db.ForeignKey('zaposlenik.rb'), nullable=False)
    datum = db.Column(db.String(12), nullable=False)
    godina = db.Column(db.Integer, nullable=False)
    napomena = db.Column(db.Text)
    __table_args__ = (db.UniqueConstraint('zaposlenik_rb', 'datum', name='unq_zap_odmor'),)

    def __repr__(self):
        return f"Odmor('{self.zaposlenik_rb}', '{self.datum}', '{self.godina}')"


class UkupnoDana(db.Model):
    rb = db.Column(db.Integer, primary_key=True)
    zaposlenik_rb = db.Column(db.Integer, db.ForeignKey('zaposlenik.rb'), nullable=False)
    godina = db.Column(db.Integer, nullable=False)
    br_dana = db.Column(db.Integer, default=0)
    __table_args__ = (db.UniqueConstraint('zaposlenik_rb', 'godina', name='unq_zap_godina'),)

    def __repr__(self):
        return f"UkupnoDana('{self.zaposlenik_rb}', '{self.godina}', '{self.br_dana}')"
