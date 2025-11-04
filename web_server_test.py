from flask import Flask, send_from_directory

app = Flask(__name__)

# Define the path to serve static files from
STATIC_PATH = './'

@app.route('/')
def serve_static_index():
    return send_from_directory(STATIC_PATH, "index.html")

# Route to serve static files from any incoming route
@app.route('/<path:filename>')
def serve_static(filename):
    print(filename)
    if filename == "":
        return send_from_directory(STATIC_PATH, "index.html")
    elif filename.endswith(".js") or filename.endswith(".css"):
        return send_from_directory(STATIC_PATH, filename)
    else:
        return send_from_directory(STATIC_PATH, "index.html")


if __name__ == '__main__':
    app.run(debug=True)
