from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Route to render index.html
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    id = request.form['id']
    name = request.form['name']
    
    # Run your Python application script
    command = ['python', 'main.py', id, name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    return render_template('index.html', output=output.decode())

if __name__ == '__main__':
    app.run(debug=True)