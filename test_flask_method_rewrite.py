from flask import Flask
from flask_method_rewrite import MethodRewrite

app = Flask(__name__)
method_rewrite = MethodRewrite(app)

@app.route('/')
def index():
    return """
    <form action="/?__METHOD_OVERRIDE__=PUT" method='POST'>
        <input type="text" name="testing"/>
        <input type="submit">
    </form>
    """

@app.route('/',methods=['PUT'])
def put():
    return "OK"

if __name__ == "__main__":
    app.debug = True
    app.run()