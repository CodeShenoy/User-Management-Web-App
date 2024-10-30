import psycopg2
from flask import Flask, redirect, request, render_template, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host = "localhost",
        database = "user_database",
        user = "postgres",
        password = "manager"
    )
    return conn

@app.route('/test_db_connection')
def test_db_connection():
    try:
        conn = get_db_connection()
        conn.close()
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection error: {e}"

@app.route('/')
def home():
    return render_template('home.html')

# Route to render the HTML form
@app.route('/add_user', methods=['GET', 'POST'])
def add_user_form():
    if request.method == 'POST':
        # Handle form submission logic here
        # e.g., get data from form, add it to the database, etc.
        # After handling, you might redirect or show a success message
        return "User added successfully!"  # or redirect to a different page
    
    # For GET requests, render the add_user form
    return render_template('add_user.html')


# Route to handle form submission
@app.route('/submit_user', methods=['POST'])
def submit_user():
    try:
        # Get form data from the request
        name = request.form['name']
        email = request.form['email']

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert the new user into the 'users' table
        cursor.execute(
            'INSERT INTO users (name, email) VALUES (%s, %s)',
            (name, email)
        )

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        # Return a success message
        return f"User {name} added successfully!"

    except Exception as e:
        return f"Error: {str(e)}"
    
@app.route('/view_users', methods=['GET'])
def view_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('view_users.html', users=users)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/view_users')

if __name__ == '__main__':
    app.run(debug=True)