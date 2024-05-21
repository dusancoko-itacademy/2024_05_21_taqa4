from quart import Quart, render_template

app = Quart(__name__)

@app.route('/')
async def hello():
    #return {
    #    "first_name": "Peter",
    #    "last_name": "Smith"
    #}
    return await render_template("home.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=50000, debug=True)