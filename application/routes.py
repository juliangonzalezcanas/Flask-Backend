from app import app

@app.route('/')
def hello():
    return 'Your Flask Server Running'