from flask import *

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>3-parametriani calculatori</title>
</head>
<body style="font-family: sans-serif; background: #eef;">
  <h2>3-parametriani calculator super cool</h2>
  <form action="/calculate" method="post">
    <input type="number" name="a" placeholder="number 1" required>
    <input type="number" name="b" placeholder="number 2" required>
    <input type="number" name="c" placeholder="number 3" required>
    <select name="op" required>
      <option value="+">+</option>
      <option value="*">*</option>
    </select>
    <button type="submit">calculate</button>
  </form>
  {% if result is not none %}
    <h3>result: {{ result }}</h3>
  {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML, result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['a'])
    b = float(request.form['b'])
    c = float(request.form['c'])
    op = request.form['op']

    if op == '+':
        result = a + b + c
    elif op == '*':
        result = a * b * c
    else:
        result = "error:the only operator available is +  *"

    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(debug=True)
