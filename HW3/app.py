from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/profile', methods=['POST'])
def profile():
    name = request.form['name']
    username = request.form['username']
    bio = request.form['bio']
    hobbies = request.form['hobbies']
    favorite_color = request.form['favorite_color']
    return render_template('profile.html',
                           name=name,
                           username=username,
                           bio=bio,
                           hobbies=hobbies,
                           favorite_color=favorite_color)

if __name__ == '__main__':
    app.run(debug=True)
