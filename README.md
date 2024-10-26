# To-Do

#Features
Create Tasks: Add new tasks with a title and optional description.
Edit Tasks: Modify task details if needed.
Delete Tasks: Remove tasks that are no longer relevant.
Mark Tasks: Mark tasks as completed or pending.
Filter Tasks: Filter between all, completed, and pending tasks.
Persistent Storage: Tasks remain saved locally (using localStorage) until cleared.

#Description
Frontend:
Use HTML and CSS to create a user interface.
The UI should have:
An input field to add a new task.
A button to submit the new task.
A list displaying existing tasks with a delete button for each task.
Backend:
Use Python with Flask (or Django) to handle requests.
Create a PostgreSQL database to store tasks.
Each task should have an ID, description, and a status (e.g., completed or not).
Functionality:
When a user submits a new task, it should be added to the database and displayed in the list.
Users should be able to delete a task, which should remove it from the database and the displayed list.
Implement email notifications to inform the user when a new task is created.

#Installation

Prerequisites
Git installed on your system.
Steps to Run the App
Clone the Repository:

bash
Copy code
git clone git@github.com:Sangeetha0822/TO-Do.git
Navigate to the project folder:

bash
Copy code


cd TO-Do
Open the App:
Open index.html in a web browser.


