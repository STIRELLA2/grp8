from flask import Flask
app = Flask(__name__) # "__main__"


@app.route('/grp7', methods=['GET'])
def flask_import():
  return """<html>
  
<head>
<title>FA595 Midterm</title>
</head>
<body>
<h1>Group 7: Joseph Chionchio, Ashley-Marie Fontes, Sherri Putnam, Gloria Rumao</h1>
<b>
<p>Deliverables<b><b>

1. Created a flask end point accessible to the entire internet hosted on an AWS machine<b>

2. Able to accept cURL calls on one route and successfully return a 200 status when called<b>

3. Able to accept in a request with a payload including a string and a requested NLP service<b> 
   Our project is of returning 2 services for each member of our group<b>
</p>
</body>
  </html>
  """

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
