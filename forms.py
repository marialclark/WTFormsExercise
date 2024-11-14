from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    """Renders form to add new adoptee."""
    name = StringField("Pet Name", 
            validators=[InputRequired()])
    
    species = SelectField("Species", 
            choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Porcupine', 'Porcupine')])
    
    photo_url = StringField("Photo URL",
            validators=[Optional(), URL()])
    
    age = IntegerField("Age",
            validators=[Optional(),
            NumberRange(min=0, max=30)])
    
    notes = TextAreaField("Notes",
            validators=[Optional()])
    

class EditPetForm(FlaskForm):
    """Renders form for editing pet information."""
    photo_url = StringField("Photo URL",
                validators=[Optional(), URL()])
    
    notes = TextAreaField("Notes",
             validators=[Optional()]   )
    
    available = BooleanField("Available")
