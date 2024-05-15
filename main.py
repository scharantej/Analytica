
# main.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research', methods=['GET', 'POST'])
def research():
    if request.method == 'POST':
        query = request.form['query']
        topic = request.form['topic']
        result_type = request.form['result_type']
        return redirect(url_for('results', query=query, topic=topic, result_type=result_type))
    return render_template('research.html')

@app.route('/results')
def results():
    query = request.args.get('query')
    topic = request.args.get('topic')
    result_type = request.args.get('result_type')
    return render_template('results.html', query=query, topic=topic, result_type=result_type)

if __name__ == '__main__':
    app.run()
