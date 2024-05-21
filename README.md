# To-do App Documentation

## Abbreviations

1. **to-do** - Short for "to-do list," referring to the list of tasks users need to complete.
1. **txt** - Refers to the file extension for text files, used in "tasks.txt."
1. **GUI** - Graphical User Interface: Although not explicitly mentioned in the documentation, it's a common term referring to visual interfaces like windows and buttons in software.

## Introduction

Todo App is a Python-based command-line application designed to help users manage their to-do lists efficiently. It provides basic functionalities such as adding tasks, marking tasks as complete, deleting tasks, and displaying the current list of tasks. The application is user-friendly and easy to use, making it suitable for personal task management.

## Features

1. **Display Tasks:** Users can view their current list of tasks along with their status (completed or not completed).
1. **Add Task:** Users can add new tasks to their to-do list.
1. **Mark Task as Complete:** Users can mark tasks as complete, indicating that they have been finished.
1. **Delete Task:** Users can delete tasks from their to-do list.
1. **Quit:** Allows users to exit the application.
## Cloning the Repository
To clone the Wordle Game project from GitHub, follow these steps:

1. Open your terminal (Command Prompt, PowerShell, or any other terminal emulator).
1. Navigate to the directory where you want to clone the repository.
1. Run the following command: git clone https://github.com/ROHANDAS2003/todo_app
1. Navigate into the cloned repository directory: cd todo\_app

## File Structure

- **todo\_app.py:** Contains the main code for the Todo App.
- **tasks.txt:** Stores the to-do items. Tasks are saved in this file in a simple text format.
## Dependencies
1. **Built-in Modules**:
- **os**: Not explicitly used in the provided script, but commonly used for file path operations.
- **sys**: Not used in the script but can be useful for exiting the program or handling command-line arguments.
## Running the Program
**Setup**: Place the Python script (todo\_app.py) and the text file (tasks.txt) in the same directory.

**Running the Script**: Execute the Python script todo\_app.py. You can do this by navigating to the directory containing the script in your command line or terminal and then running: python todo\_app.py

1. Upon running the application, users are presented with a menu of options to choose from.
1. Users can select an option by entering the corresponding number.
1. Based on the selected option, users can perform various actions such as adding tasks, marking tasks as complete, deleting tasks, and viewing the current list of tasks.
1. Users can continue interacting with the application until they choose to quit.

## Code Overview

The todo\_app.py file contains the following functions:

1. **display\_tasks():** Reads tasks from tasks.txt and displays them to the user.
1. **add\_task(task):** Adds a new task provided by the user to tasks.txt.
1. **mark\_task\_complete(task\_number):** Marks a specific task as complete by modifying its status in tasks.txt.
1. **delete\_task(task\_number):** Deletes a specific task from tasks.txt.
1. **main():** The main function of the application. It displays the menu options and handles user input to execute the corresponding functions.

## Error Handling

The application includes basic error handling for file operations such as file not found errors. However, further enhancements can be made to handle other potential errors gracefully.

## Future Enhancements

1. **Validation:** Implement input validation to ensure that users provide valid input.
1. **Confirmation:** Add confirmation prompts before performing actions like marking a task as complete or deleting it.
1. **Persistence:** Use a more robust data storage mechanism such as a database for better scalability and flexibility.
1. **User Authentication:** Introduce user authentication for multi-user support.
1. **Priority Management:** Implement task prioritization to help users manage their tasks more effectively.
1. **Deadline Management:** Allow users to set deadlines for tasks and receive reminders for approaching deadlines.
1. **GUI Implementation:** Develop a graphical user interface to enhance the user experience.

## Conclusion

Todo App provides a simple yet effective solution for managing to-do lists. With its intuitive interface and essential features, users can easily organize their tasks and stay productive. The application can be further enhanced with additional features and improvements to cater to a wider range of users and use cases.

