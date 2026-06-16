 
@app.route('/logout', methods=['POST'])
def logout():
    return {"message": "logged out"}
