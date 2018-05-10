from flask import Flask, render_template
app = Flask(__name__)


shopping_list = ['Milk', 'Eggs']

@app.route('/')
def index():
    return render_template('index.html', items=shopping_list)

if __name__ == '__main__':
    app.run(debug=True)

