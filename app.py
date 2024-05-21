from quart import Quart, render_template
from dotenv import load_dotenv
import mysql.connector as mysql
import os 

load_dotenv()

app = Quart(__name__)

@app.route('/')
async def hello():
    #return {
    #    "first_name": "Peter",
    #    "last_name": "Smith"
    #}
    return await render_template("home.html")

@app.route('/users')
def get_users():
    connection = mysql.connect(host=os.getenv('HOST'),
                               port=os.getenv('PORT'),
                               user=os.getenv('USER'),
                               password=os.getenv('PASSWORD'),
                               database=os.getenv('DATABASE'))
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    users = [row for row in cursor.fetchall()]
    cursor.close()
    connection.close()
    return users

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=50000, debug=True)