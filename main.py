from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <label for="rot">
                Rotate by: 
                <input type="text" name="rot" value="0"/>
            </label>
            <textarea type="text" name="text">{0}</textarea>
            <input type="submit" value ="Submit"/>
        </form>
    </body>
</html> 
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    rotation_num = int(rotation)
    characters = request.form['text']
    final = rotate_string(characters, rotation_num)
    return form.format(final)


@app.route("/")
def index():
    return form.format("")
app.run()