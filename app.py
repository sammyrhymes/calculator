from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result='')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = eval(expression)
    except:
        result = 'Error'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
