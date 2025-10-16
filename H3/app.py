from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/profile', methods=['POST'])
def profile():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    sex = request.form['sex']
    status = request.form['status']
    location = request.form['location']
    bio = request.form['bio']
    
    return render_template('profile.html', first_name=first_name, last_name=last_name,
                           sex=sex, status=status, location=location, bio=bio)

if __name__ == '__main__':
    app.run(debug=True)
