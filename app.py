from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/version')
def version():
    return jsonify({"version": "1.0.0"})

@app.route('/login', methods=['POST'])
def login():
    return {"message": "login incorrect"}

@app.route('/logout', methods=['POST'])
def logout():
    return {"message": "logged out"}
 
@app.route('/logout', methods=['POST'])
def logout():
    return {"message": "logged out"}
