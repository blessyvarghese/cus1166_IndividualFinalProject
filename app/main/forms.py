# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField, TimeField
from wtforms.validators import ValidationError, DataRequired, Length


class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo', 'Todo'), ('doing', 'Doing'), ('done', 'Done')])
    submit = SubmitField('submit')


class AppointmentForm(FlaskForm):
    Appointment_title = StringField('Appointment Title: ', validators=[DataRequired()])
    Appointment_date = DateField('Appointment Date: ', validators=[DataRequired()])
    Appointment_time = TimeField('Start Time: ', validators=[DataRequired()])
    Appointment_duration = TimeField('Duration: ', validators=[DataRequired()])
    Appointment_location = StringField('Client Address: ', validators=[DataRequired()])
    Appointment_customer = StringField('Client Name: ', validators=[DataRequired()])
    Appointment_notes = StringField('Notes: ', validators=[DataRequired()])
    submit = SubmitField('Add Appointment')
