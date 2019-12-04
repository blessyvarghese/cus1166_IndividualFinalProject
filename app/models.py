# from flask import url_for
from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))


class Appointments(db.Model):
    Appointment_id = db.Column(db.Integer, primary_key=True)
    Appointment_title = db.Column(db.String(100), index=True)
    Appointment_date = db.Column(db.Date, index=True)
    Appointment_time = db.Column(db.Time, index=True)
    Appointment_duration = db.Column(db.Time, index=True)
    Appointment_location = db.Column(db.String(150), index=True)
    Appointment_Customer = db.Column(db.String(20), index=True)
    Appointment_notes = db.Column(db.String(140), index=True)

    def __repr__(self):
        return '<Appointments {}'.format(
            self.Appointment_title.Appointment_date.Appointment_time.Appointment_duration.Appointment_location.
                Appointment_Customer.Appointment_notes)
