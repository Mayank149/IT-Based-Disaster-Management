from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Services Route
@app.route('/services')
def services():
    return render_template('services.html')

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you'd typically save this information to a database or send an email
        return redirect('/')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
