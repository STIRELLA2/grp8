from flask import Flask
app = Flask(__name__) # "__main__"


@app.route('/grp7', methods=['GET'])
def flask_import():
  return """<html>
  <head>
     <meta charset="utf-8">
   <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>
       Midterm Project 2021F FA 595-WS2</b>
    <title>
  <head>
  
  <body>
  <h1>welcome to group 7's midterm project <h1>
  <br><br><br><br><br/>
  </p>
  
  Tasks<i><br>
  
  1. Be a flask end point accessible to the entire internet hosted on an AWS machine.<br>

  2. Accept cURL calls on one (or more) routes and successfully return something (ideally a 200 or 4XX status but never a 500) when called<br>

  3. Accept in a request with a payload including a string and a requested NLP service. Our project is capable of returning 2 services for each member of our group.<br>
  
    </p>
  
  </body>
  
  </html>
  """
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
