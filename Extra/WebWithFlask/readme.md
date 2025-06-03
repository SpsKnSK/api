# Flask School Classes Example

This is a modern Flask web application for managing school classes, students, lessons, and grades. It demonstrates best practices in web/API development, database integration, authentication, and UI/UX design using **Flask** and **SQLite**.

## How to Run
1. Open a terminal in the project folder.
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Initialize the database (only needed once):
   ```powershell
   python createDb.py
   ```
4. Start the Flask app:
   ```powershell
   python app.py
   ```
5. Open your browser and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


## Features
| Page                | Description                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Main page           | Lists all classes in a table, showing class size, number of girls/boys, and class average                             |
| Class detail page   | Shows class name, statistics (overall average, by lesson, by sex), and a table of students                            |
| Student detail page | Shows student info (name, surname, date of birth, age, address, sex with icon, class link) and grades for all lessons |
| Edit student        | Admins can edit student info and grades, with validation and role-based access                                        |
| Login/logout        | Secure login with hashed passwords, role-based access, and session management                                         |

## Database & Data Layer
- **SQLite Database**: All data (students, classes, lessons, grades, users, roles) is stored in a local SQLite database for persistence and easy setup.
- **Database Layer**: The `Db/school_db.py` file contains the `SchoolDB` class, which abstracts all database operations (CRUD, authentication, aggregation, etc.), making the code modular and maintainable.
- **Database Creation**: Use `createDb.py` to initialize the database schema and populate it with demo data. Run it once before starting the app:
  ```powershell
  python createDb.py
  ```
- **Why a DB Layer?**
  - Centralizes all data access logic, making it easier to maintain, test, and extend.
  - Keeps your Flask routes clean and focused on business logic.
  - Allows for easy migration to other databases in the future.

## Authentication & Authorization
- **Login**: Users log in with a username and password. Passwords are securely hashed and checked using industry-standard methods.
- **Session Management**: Flask sessions store the logged-in user's ID and role.
- **Role-based Access**: Decorators (e.g., `@login_required`, `@admin_required`) restrict access to certain routes. Only admins can edit students.
- **How Password Check Works**: On login, the password is hashed and compared to the stored hash in the database. No plain-text passwords are stored.

## Decorators
- `@login_required`: Ensures the user is logged in before accessing a route.
- `@admin_required`: Ensures the user is both logged in and has the 'admin' role.
- These decorators keep your route functions clean and enforce security consistently.

## Light/Dark Theme
- The app supports both light and dark themes for better accessibility and user preference.
- **Switching Themes**: Use the sun/moon icon in the header to toggle between light and dark mode. The preference is saved and persists across sessions.

## Model & Data Structure
- The app uses Python classes (e.g., `Student`, `SchoolClass`, `Lesson`) to represent entities.
- **Why Use Class Instances?**
  - Encapsulates related data and behavior, making code more readable and maintainable.
  - Easier to pass around, extend, and refactor than using raw dictionaries or tuples.
  - Supports methods for computed properties (e.g., age, averages).

## Other Useful Features
- **Modern UI**: Clean, responsive design with consistent button and table styles.
- **Navigation**: Clickable class and student names for easy navigation.
- **Tooltips**: Info icons with tooltips for lesson descriptions.
- **Bulk Data Generation**: Demo data (students, lessons, grades) is generated for realistic testing.
- **Multilanguage Ready**: Instructions and code for adding Flask-Babel for multilanguage support.
## File Structure

```
FlaskApplicationWithCopilot/
├── app.py                # Main Flask application
├── Db/
│   └── school_db.py      # Database access layer
├── Models/
│   └── models.py         # Data model classes
├── createDb.py           # Script to create/populate DB
├── templates/            # HTML templates for the pages
├── static/               # CSS and static assets
├── requirements.txt      # Python dependencies
```

## Suggestions for Future Improvements
1. **User Registration & Management**: Add user registration, password reset, and user management features.
2. **REST API**: Expose data via a RESTful API for integration with other systems or a mobile app.
3. **Advanced Analytics**: Add charts and more detailed statistics (e.g., grade distributions, trends over time).
4. **Notifications**: Email or in-app notifications for grade updates or class announcements.
5. **Parent/Teacher Roles**: Add more user roles (e.g., parent, teacher) with custom dashboards and permissions.
6. **Import/Export**: Allow CSV/Excel import/export of students, grades, and classes.
7. **Unit Tests**: Add automated tests for the database layer and Flask routes.
8. **Deployment**: Add instructions for deploying to cloud platforms (Heroku, Azure, etc.).
9. **Accessibility**: Improve accessibility for users with disabilities (ARIA, keyboard navigation).
10. **Mobile Optimization**: Enhance the UI for mobile and tablet devices.

Feel free to experiment, extend, and adapt this project for your own needs!
