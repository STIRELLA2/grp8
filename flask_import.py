from flask import Flask
app = Flask(__name__) # "__main__"


@app.route('/grp7', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def flask_import():
  return """<html>
 
<body>
<h1>FA595 Midterm<h1><br><br>
<h2>Group 7: Zemin Li, Sherri Putnam, Spencer Tirella</h2>
<b>
<p>Deliverables:<br>

1. Created a flask end point accessible to the entire internet hosted on an AWS machine<br>

2. Able to accept cURL calls on one route and successfully return a 200 status when called<br>

3. Able to accept in a request with a payload including a string and a requested NLP service<br>
&nbsp;&nbsp&nbsp;&nbsp;Our project is capable of returning 2 services for each member of our group<br>
</p>
</body>
  </html>
  """

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)
