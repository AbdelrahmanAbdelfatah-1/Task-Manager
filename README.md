# 📝 Command-Line Task Manager

This is a command-line Task Manager application built in Python. The primary objective is to provide an organized and user-friendly tool for managing tasks, helping users track their responsibilities and deadlines effectively.

---

## 🚀 Key Features

The application provides a main menu that allows users to perform the following actions:
* **Add a Task:** Create a new task.
* **Delete a Task:** Remove an existing task.
* **Show List of Tasks:** View all current tasks.
* **Update Due Date:** Change the due date for a specific task.
* **Mark Task as Completed:** Update a task's status to "completed".
* **Quit:** Exit the application.

---

## 💻 Core Concepts: OOP & Design

This project is built using Object-Oriented Programming (OOP) principles, specifically **Inheritance** and **Polymorphism**.

The application is structured around four main classes:

1.  **`Task` (Base Class)**
    * This is the parent class for all task types.
    * It holds the core attributes for every task: **title**, **description**, **due date**, and **status** (e.g., "incomplete", "completed", "in progress").

2.  **`WorkTask` (Child Class)**
    * Inherits from `Task`.
    * Includes an additional **`task priority`** attribute.
    * Contains a method that returns its specific task type.

3.  **`PersonalTask` (Child Class)**
    * Inherits from `Task`.
    * Includes an additional **`task category`** attribute (e.g., "family", "sports").
    * Contains a method that returns its specific task type.

4.  **`TaskManager` (Handler Class)**
    * This class manages all the logic for creating, updating, viewing, and deleting tasks.

---

## ⚙️ Additional Features

* **Error Handling:** The application correctly handles at least two types of errors using **exceptions** (e.g., invalid user input, task not found).
* **Data Persistence (Bonus):** All tasks are stored in a **JSON file** to ensure data is saved even after the application is closed.

---

## 🛠️ Technologies Used
* **🐍 Python**
* **📄 JSON** (for data storage)

---
