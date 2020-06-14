import flask

app = flask.Flask(__name__)


def get_latest_packages():
    return [
        {'name': 'Flask', 'version': '1.2.3'},
        {'name': 'awscli', 'version': '2.4.5'},
        {'name': 'SQLAlchemy', 'version': '3.6.8'}
    ]


@app.route('/')
def index():
    test_packages = get_latest_packages()
    return flask.render_template('index.html', packages=test_packages)


@app.route('/about')
def about():
    return flask.render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
