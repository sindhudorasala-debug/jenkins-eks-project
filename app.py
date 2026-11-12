from flask import Flask, render_template, jsonify

app = Flask(_name_)

movies = [
    {
        "name": "RRR",
        "genre": "Action",
        "year": 2022,
        "description": "An action-packed Indian epic."
    },
    {
        "name": "Baahubali",
        "genre": "Fantasy",
        "year": 2015,
        "description": "A legendary kingdom and its epic story."
    },
    {
        "name": "Pushpa",
        "genre": "Action",
        "year": 2021,
        "description": "A story of ambition and determination."
    },
    {
        "name": "Arjun Reddy",
        "genre": "Drama",
        "year": 2017,
        "description": "An emotional romantic drama."
    },
    {
        "name": "Mahanati",
        "genre": "Biography",
        "year": 2018,
          "description": "A beautiful cinematic biography."
    },
    {
        "name": "Eega",
        "genre": "Fantasy",
        "year": 2012,
        "description": "A unique fantasy revenge story."
    }
]


@app.route('/')
def home():
    return render_template('index.html', movies=movies)


@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "application": "CineWorld Movie Website"
    }), 200


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
