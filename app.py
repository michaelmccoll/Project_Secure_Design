from flask import Flask, render_template
from controllers.consultant_controller import consultants_blueprint
from controllers.client_controller import clients_blueprint
from controllers.assignment_controller import assignments_blueprint

app = Flask(__name__)

app.register_blueprint(consultants_blueprint)
app.register_blueprint(clients_blueprint)
app.register_blueprint(assignments_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)