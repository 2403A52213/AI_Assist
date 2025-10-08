# Flask Login App

This project is a simple Flask application that provides a user login functionality. It serves an HTML form for users to input their credentials and prints the username upon successful login.

## Project Structure

```
flask-login-app
├── src
│   ├── static
│   │   └── css
│   │       └── style.css
│   ├── templates
│   │   ├── index.html
│   │   └── login.html
│   ├── app.py
│   └── config.py
├── requirements.txt
└── README.md
```

## Requirements

To run this application, you need to have Python and Flask installed. You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:
   ```
   cd flask-login-app/src
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Features

- User login form
- Displays username upon successful login
- Responsive design with basic CSS styling

## License

This project is licensed under the MIT License.