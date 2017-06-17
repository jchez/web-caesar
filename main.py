from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            text-area {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/change" method="post">
            <label for="rot">
                Rotate by: 
                <input type="text" name="rot" value="0"/>
            </label>
            <textarea name="text">
            </textarea>
            <input type="submit" value ="Submit Query"/>
        </form>
    </body>
</html> 
"""

@app.route("/change", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    rotation2 = int(rotation)
    characters = request.form['text']
    final = rotate_string(characters, rotation2)
    content = "<h1>" + final + "</h1>"
    return content


@app.route("/")
def index():
    content = form
    return content

app.run()