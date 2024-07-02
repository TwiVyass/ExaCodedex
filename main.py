from flask import Flask, request, render_template
from exa_py import Exa

app = Flask(__name__)
exa = Exa('15941d40-c085-492b-92e4-d404aa8832ff')


@app.route('/', methods=['GET', 'POST'])
def search():
    results = []
    if request.method == 'POST':
        query = request.form['query']
        response = exa.search(
            query,
            num_results=10,
            include_domains=['https://www.instagram.com/'],
        )
        results = response.results

    return render_template('search.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
