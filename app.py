from flask import Flask, render_template
from controllers.projects_controller import projects_blueprint
from controllers.triages_controller import triages_blueprint
from controllers.risks_controller import risks_blueprint
from controllers.stats_controller import stats_blueprint

app = Flask(__name__)

app.register_blueprint(projects_blueprint)
app.register_blueprint(triages_blueprint)
app.register_blueprint(risks_blueprint)
app.register_blueprint(stats_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)