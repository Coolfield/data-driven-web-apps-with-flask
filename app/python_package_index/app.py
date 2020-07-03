import flask

from app.python_package_index.infrastructure.view_monifiers import response

app = flask.Flask(__name__)


def get_latest_packages():
    return [
        {'name': 'Flask', 'version': '1.2.3'},
        {'name': 'aws-cli', 'version': '2.4.5'},
        {'name': 'SQLAlchemy', 'version': '3.6.8'}
    ]


@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_packages()
    return {'packages': test_packages}
    # return flask.render_template('home/index.html', packages=test_packages)


@app.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
    # return flask.render_template('home/about.html')


if __name__ == "__main__":
    app.run(debug=True)
