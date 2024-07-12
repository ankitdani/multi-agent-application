from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/home', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission here
        job_role = request.form['job_role']
        years_of_experience = request.form['years_of_experience']
        location = request.form['location']
        return f'Job Role: {job_role}, Years of Experience: {years_of_experience}, Location: {location}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
