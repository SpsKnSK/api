# Flask School Classes Example

This is a simple Flask web application to demonstrate how to handle web/API development in Python. The app manages school classes and students, showing how to build multi-page web apps with **Flask**.

## Features
| Page                | Description                                                                              |
| ------------------- | ---------------------------------------------------------------------------------------- |
| Main page           | Lists all classes (max 3)                                                                |
| Class detail page   | Shows class name and a table of students (surname, name, age, average grade)             |
| Student detail page | Shows student info (name, surname, date of birth, age, address) and grades for 6 lessons |

## How to Run
1. Open a terminal in the `WebWithFlask` folder.
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Start the Flask app:
   ```powershell
   python app.py
   ```
4. Open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## File Structure
| File/Folder        | Description                  |
| ------------------ | ---------------------------- |
| `app.py`           | Main Flask application       |
| `templates/`       | HTML templates for the pages |
| `requirements.txt` | Python dependencies          |

## What this example shows:
- How to define routes and render templates in Flask
- How to pass data (classes, students) to templates
- How to use Python functions for logic (age, average)
- How to link between pages using Flask's `url_for`

## Future
Feel free to modify the data or templates to experiment further!
