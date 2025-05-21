# Flask School Classes Example

This is a simple Flask web application to demonstrate how to handle web/API development in Python. The app manages school classes and students, showing how to build multi-page web apps with **Flask**.

## Features
| Page                | Description                                                                                                         |
| ------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Main page           | Lists all classes in a table, showing class size, number of girls/boys, and class average                           |
| Class detail page   | Shows class name, statistics (overall average, by lesson, by sex), and a table of students                          |
| Student detail page | Shows student info (name, surname, date of birth, age, address, sex with icon, class link) and grades for 6 lessons |

## Statistics
- **Overall average**: The mean of all grades for all students in the class.
- **Average by lesson**: For each lesson, the mean grade across all students in the class.
- **Average by sex**: The mean of all grades for boys (♂) and girls (♀) in the class, with icons for clarity.
- **Class list**: The main page shows, for each class, the number of students, number of girls/boys, and the class average.

## Sex (Male/Female)
- Each student has a sex attribute (Male or Female), displayed with a corresponding icon (♂ for male, ♀ for female) in both the student detail and class statistics.
- The number of boys and girls is shown in the class list, and averages are calculated by sex in the statistics.

## Other Useful Features
- **Modern UI**: The app uses a clean, modern style for all tables and buttons.
- **Navigation**: Class and student names are clickable for easy navigation between details.
- **Tooltips**: Lesson names in the student detail page have an info icon with a tooltip showing the lesson description.
- **Data structure**: The app uses Python classes for SchoolClass, Student, and Lesson, making it easy to extend or modify.
- **Randomized data**: Student grades are randomly generated for demonstration, and the sample includes a realistic mix of names, addresses, and sexes.

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
| `static/style.cs`  | Style sheet for modern looks |

## How Flask Works
**Flask** is a lightweight Python web framework that makes it easy to build web applications. Here’s a quick overview:

- **Routing**: Flask uses routes to map URLs to Python functions. Each route (using `@app.route`) defines what should happen when a user visits a specific URL. For example, `/` shows the main page, `/class/<id>` shows a class detail, and `/student/<id>` shows a student detail.
- **Templates**: Flask uses HTML template files (in the `templates/` folder) to display content. The `render_template` function fills these templates with data and sends the result to the browser.
- **Data Connection**: Data (like classes and students) is stored in Python variables or can come from a database. The route functions prepare this data and pass it to the templates, which then display it to the user.
- **Static Files**: CSS and other static files are placed in the `static/` folder and linked in templates for styling.

This structure makes it easy to separate logic (Python code), data, and presentation (HTML/CSS), helping you build clear and maintainable web applications.

## What this example shows:
- How to define routes and render templates in Flask
- How to pass data (classes, students) to templates
- How to use Python functions for logic (age, average)
- How to link between pages using Flask's `url_for`

## Future
Feel free to modify the data or templates to experiment further!
