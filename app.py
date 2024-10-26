
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2001@localhost/tasklist'
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for flash messages
db = SQLAlchemy(app)

# Database Model
class TaskList(db.Model):
    __tablename__ = 'tasklist'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(400))
    priority = db.Column(db.String(40))
    status = db.Column(db.String(40), default='Pending')

    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

# Create the database tables
with app.app_context():
    db.create_all()

# Index route to display tasks
@app.route("/")
def index():
    tasks = TaskList.query.all()
    return render_template("index.html", tasks=tasks)

# Submit route with email notification
@app.route("/submit", methods=["POST"])
def submit():
    description = request.form["description"]
    priority = request.form["priority"]

    # Create and add new task
    task = TaskList(description, priority)
    db.session.add(task)
    db.session.commit()

    # Send email notification
    try:
        send_email(description)
        flash("Task added successfully and email sent!", "success")
    except Exception as e:
        flash(f"Task added but email failed: {str(e)}", "danger")

    return redirect(url_for('index'))

# Route to edit a task
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    task = TaskList.query.get_or_404(id)
    if request.method == "POST":
        task.description = request.form["description"]
        task.priority = request.form["priority"]
        db.session.commit()
        flash("Task updated successfully!", "info")
        return redirect(url_for('index'))
    return render_template("update.html", task=task)

# Route to delete a task
@app.route("/delete/<int:id>")
def delete(id):
    task = TaskList.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    flash("Task deleted successfully!", "warning")
    return redirect(url_for('index'))

# Update task status via JSON request
@app.route("/update_status/<int:id>", methods=["POST"])
def update_status(id):
    data = request.get_json()
    if not data or "status" not in data:
        return jsonify({"success": False}), 400
    
    task = TaskList.query.get_or_404(id)
    task.status = data["status"]
    db.session.commit()
    return jsonify({"success": True})

# Email configuration
EMAIL_ADDRESS = 'hemapandit2001@gmail.com'  # Replace with your email
EMAIL_PASSWORD = 'hgku zlqa ssrh vdun'  # Replace with your password
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Email sending function
def send_email(task_description):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS  # Can be modified to the intended recipient
    msg['Subject'] = 'New Task Added'

    # Email body
    body = f"A new task has been added: {task_description}"
    msg.attach(MIMEText(body, 'plain'))

    # Send email using SMTP
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print("Email sent successfully!")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
