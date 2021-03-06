from flask import Flask, request, render_template, redirect, url_for
import os
import robot

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return run_tests()
    return render_template('home.html')

@app.route('/log.html', methods=['GET'])
def log():
    return open('assets/reports/log.html').read()

@app.route('/report.html', methods=['GET'])
def report():
    return open('assets/reports/report.html').read()

def run_tests():
    log_file = open('assets/reports/log.html', 'w')
    robot.run('assets/tests/tests.robot', stdout=log_file, outputdir='assets/reports')
    return redirect(url_for('log'), code=302)

@app.route('/screenshots')
def get_screenshots():
    pictures = []
    for file in os.listdir('assets/reports'):
        if file.endswith('.png'):
            link = '/screenshots/' + file
            pictures.append(link)
    return render_template('screenshots.html', pictures=pictures)

@app.route('/screenshots/<screenshot>')
def get_screenshot(screenshot):
    return open('assets/reports/{screenshot}'.format(screenshot=screenshot)).read()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)