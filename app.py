from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {
        'title': 'Hello World!',
        'message': 'Super secret messages'
    }
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    input_data = request.form['inputData']
    return f'You entered: {input_data}'

if __name__ == '__main__':
    app.run(debug=True)