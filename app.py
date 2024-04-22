from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy admin credentials
ADMIN_ID = "#yourNumber or ID"
ADMIN_PASSWORD = "#Password"

# Dummy data for storing votes
votes = []

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    user_type = request.form['user_type']
    user_id = request.form['id']
    password = request.form['password']

    if user_type == 'admin' and user_id == ADMIN_ID and password == ADMIN_PASSWORD:
        return redirect(url_for('admin_dashboard'))
    elif user_type == 'voter':
        return redirect(url_for('voter_form'))
    else:
        return "Invalid credentials"

@app.route('/voter_form')
def voter_form():
    return render_template('voter_form.html')

@app.route('/vote', methods=['POST'])
def vote():
    name = request.form['name']
    voter_id = request.form['voter_id']
    candidate = request.form['candidate']
    votes.append({'name': name, 'voter_id': voter_id, 'candidate': candidate})
    return "Thanks for voting!"

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html', votes=votes)

@app.route('/results')
def results():
    # Calculate election results
    candidate_votes = {'NARENDRA MODI': 0, 'RAHUL GANDHI': 0, 'NOTA': 0}
    for vote in votes:
        candidate_votes[vote['candidate']] += 1
    return render_template('results.html', results=candidate_votes)

if __name__ == '__main__':
    app.run(debug=True)
