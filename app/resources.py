from app import app

@app.route('/pets/')
def pets():
    return '{"pets":"list"}'

@app.route('/pets/1')
def pet():
    return '{"pets":"1"}'