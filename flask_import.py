from flask import Flask
app = Flask(__name__) # "__main__"


@app.route('/grp7', methods=['GET'])
def flask_import():
  return """<html>
  <body>
  <h1>welcome to group 7's midterm project <h1>
  </body>
  </html>
  """

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
