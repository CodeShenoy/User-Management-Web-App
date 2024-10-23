import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host = "localhost",
        database = "user_database",
        user = "postgres",
        password = "manager"
    )
    return conn

@app.route('/test_db')
def test_db():
    try:
        # Establish connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Execute a simple query to check the database connection
        cursor.execute('SELECT version();')
        db_version = cursor.fetchone()  # Fetch one result (the version)
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        # Return the database version as the response
        return f"Connected to PostgreSQL! Database version: {db_version}"
    
    except Exception as e:
        # Return an error message if the connection fails
        return f"Error: {str(e)}"

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        # Get user data from the request body (JSON format)
        user_data = request.get_json()
        name = user_data['name']
        email = user_data['email']
        
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
        return jsonify({'message': 'User added successfully!'})
    
    except Exception as e:
        return jsonify({'error': str(e)})