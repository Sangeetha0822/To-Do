# To-Do

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


   
