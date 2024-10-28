import psycopg2
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host = "localhost",
        database = "user_database",
        user = "postgres",
        password = "manager"
    )
    return conn

# Route to render the HTML form
@app.route('/add_user', methods=['GET'])
def add_user_form():
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

if __name__ == '__main__':
    app.run(debug=True)