import os
from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask with PostgreSQL!'

@app.route('/db')
def db():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cur = conn.cursor()
    cur.execute('SELECT version()')
    version = cur.fetchone()
    conn.close()
    return f'Database connected! Version: {version}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)