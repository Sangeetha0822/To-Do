# To-Do

## **Key Features and Overview of the Python Usage (app.py)**  

- **Framework and Tools:** Built with **Flask** for web development and **SQLAlchemy** for database interactions.  
- **Database Configuration:** Uses a **PostgreSQL** database with a `TaskList` table containing fields:  
  - `id` (primary key)  
  - `description`  
  - `priority`  
  - `status` (default: 'Pending')  

### **Task Management Features:**  
- **CRUD Operations:**  
  - **Create:** Add new tasks.  
  - **Read:** Display tasks on the homepage.  
  - **Update:** Edit task details.  
  - **Delete:** Remove tasks from the list.  

- **API for Task Status:**  
  Provides a **JSON-based API** (`/update_status/<id>`) to update the status of tasks (e.g., mark as "Completed").  

### **Email Notifications:**  
- Sends **email alerts** when a new task is added using Gmail's SMTP server.  

### **Flash Messages:**  
- Implements **flash messaging** to notify users about actions like task addition, updates, or errors.  

### **Templates:**  
- Uses **HTML templates** (`index.html` and `update.html`) to display and update tasks on the frontend.  

### **Configuration Settings:**  
- **`SQLALCHEMY_DATABASE_URI`** connects to PostgreSQL.  
- **`SECRET_KEY`** enables flash messaging support.  

### **Error Handling:**  
- Uses `try-except` to handle errors in email sending and display appropriate feedback using flash messages.  

### **Running the Application:**  
- Runs locally on **http://127.0.0.1:5000** with **debug mode enabled** for easier troubleshooting.  



## Features  
- **Create Tasks**: Add new tasks with a  description.  
- **Edit Tasks**: Modify task details if needed.  
- **Delete Tasks**: Remove tasks that are no longer relevant.  
- **Mark Tasks**: Mark tasks as completed , pending or active  
- **Filter Tasks**: Filter between all, completed, and pending tasks.  
- **Persistent Storage**: Tasks remain saved locally (using `localStorage`) until cleared.  

## Description  

### Frontend:  
- **HTML** and **CSS** to create a user interface.  
- The UI  have:  
  - An **input field** to add a new task.  
  - A **button** to submit the new task.  
  - A **list** displaying existing tasks with a delete button for each task.  

### Backend:  
-  **Python** with **Flask**  to handle requests.  
-  A **PostgreSQL database** to store tasks.  
- Each task should :  
  - An **ID**  
  - A **description**  
  - A **status** (e.g., completed or not).  

### Functionality:  
- When a user submits a new task, it is added to the database and displayed in the list.  
- Users  are able to delete a task, which removes it from the database and the displayed list.  
- **email notifications** to inform the user when a new task is created.  

## Installation  

### Prerequisites  
- Git installed on your system.  

### Steps to Run the App  
1. **Clone the Repository:**  
   ```bash
   git clone git@github.com:Sangeetha0822/TO-Do.git

### For Images
Kindly refer the file Scrrenshots of the applications in the repository


   
