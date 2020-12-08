from src import db


class CalibrationModel(db.Model):
    __tablename__ = 'CalibrationModel'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    model = db.Column(db.String(255))
    customer = db.Column(db.String(255))

    type_a = db.Column(db.Integer())
    a_highValue = db.Column(db.Float())
    a_hvPlus = db.Column(db.Float())
    a_hvMin = db.Column(db.Float())
    a_lowValue = db.Column(db.Float())
    a_lvPlus = db.Column(db.Float())
    a_lvMin = db.Column(db.Float())

    type_b = db.Column(db.Integer())
    b_highValue = db.Column(db.Float())
    b_hvPlus = db.Column(db.Float())
    b_hvMin = db.Column(db.Float())
    b_lowValue = db.Column(db.Float())
    b_lvPlus = db.Column(db.Float())
    b_lvMin = db.Column(db.Float())

    # def __init__(self, name, model, customer, highValue, hvPlus, hvMin, lowValue, lvPlus, lvMin):
    #     self.name = name
    #     self.model = model
    #     self.customer = customer
    #     self.highValue = highValue
    #     self.hvPlus = hvPlus
    #     self.hvMin = hvMin
    #     self.lowValue = lowValue
    #     self.lvPlus = lvPlus
    #     self.lvMin = lvMin

    # def __repr__(self, name):
    #      return "<CalibrationModel(title='%s')>" % self.name
