from flask import render_template, redirect, url_for
from app.main import bp
from app import db
from app.main.forms import TaskForm, AppointmentForm
from app.models import Task, Appointments


# Main route of the applicaitons.
@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template("main/index.html")


#
#  Route for viewing and adding new tasks.
@bp.route('/todolist', methods=['GET', 'POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_task = Task()
        new_task.task_desc = form.task_desc.data
        new_task.task_status = form.task_status_completed.data

        db.session.add(new_task)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.todolist'))

    todo_list = db.session.query(Task).all()

    return render_template("main/todolist.html", todo_list=todo_list, form=form)


#
# Route for removing a task
@bp.route('/todolist/remove/<int:task_id>', methods=['GET', 'POST'])
def remove_task(task_id):
    # Query database, remove items
    Task.query.filter(Task.task_id == task_id).delete()
    db.session.commit()

    return redirect(url_for('main.todolist'))


#
# Route for editing a task

@bp.route('/todolist/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_task = Task.query.filter_by(task_id=task_id).first_or_404()
        current_task.task_desc = form.task_desc.data
        current_task.task_status = form.task_status_completed.data

        db.session.add(current_task)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.todolist'))

    # get task for the database.
    current_task = Task.query.filter_by(task_id=task_id).first_or_404()

    # update the form model in order to populate the html form.
    form.task_desc.data = current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/todolist_edit_view.html", form=form, task_id=task_id)


@bp.route('/AddAppointment', methods=['GET', 'POST'])
def AddAppointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        new_Appointment = Appointments()
        new_Appointment.Appointment_title = form.Appointment_title.data
        new_Appointment.Appointment_date = form.Appointment_date.data
        new_Appointment.Appointment_time = form.Appointment_time.data
        new_Appointment.Appointment_duration = form.Appointment_duration.data
        new_Appointment.Appointment_location = form.Appointment_location.data
        new_Appointment.Appointment_Customer = form.Appointment_customer.data
        new_Appointment.Appointment_notes = form.Appointment_notes.data
        print("WENT THROUGH")
        db.session.add(new_Appointment)
        db.session.commit()
        return redirect(url_for('main.AddAppointment'))

    Appointments_added = db.session.query(Appointments).all()

    return render_template("AddAppointment.html", Appointments_added=Appointments_added, form=form)
