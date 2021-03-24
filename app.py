from flask import Flask, render_template
from controllers.consultants_controller import consultants_blueprint
from controllers.clients_controller import clients_blueprint
from controllers.assignments_controller import assignments_blueprint
from controllers.stats_controller import stats_blueprint

app = Flask(__name__)

app.register_blueprint(consultants_blueprint)
app.register_blueprint(clients_blueprint)
app.register_blueprint(assignments_blueprint)
app.register_blueprint(stats_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)