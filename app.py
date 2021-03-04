from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "POC by Ahmed Ismail (<a href=https://bugcrowd.com/AhmedOzil10>https://bugcrowd.com/AhmedOzil10</a>)"
