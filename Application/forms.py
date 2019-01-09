from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class UserInput(FlaskForm):
    address = StringField("address")
    bed = IntegerField("number of bed(s)")
    bath = IntegerField("number of bath(s)")
    sf = IntegerField("square feet")
    free_rent = IntegerField("month(s) of free rent")
    washer_dryer = StringField("washer & dryer?")
    walk_in_closet = StringField("walk-in closet?")
    hardwood_vinyl_floor = StringField("hardwood/vinyl floor?")
    submit = SubmitField()
