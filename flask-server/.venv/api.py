from flask import Flask

app = Flask(__name__)

@app.route('/api/members')
def summarised_newletters():
    return {"members": ["Members1", "Members2", "Member3"]}

if __name__ == "__main__":
    app.run(debug=True)