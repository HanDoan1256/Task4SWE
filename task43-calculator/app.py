
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f1f5f9;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .calculator {
            background: white;
            width: 340px;
            padding: 28px;
            border-radius: 16px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        }
        h1 { text-align: center; color: #1e293b; }
        p { color: #64748b; text-align: center; }
        input, select, button {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin-top: 12px;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            font-size: 16px;
        }
        button {
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover { background: #1d4ed8; }
        .result {
            margin-top: 20px;
            padding: 14px;
            background: #eff6ff;
            border-radius: 8px;
            text-align: center;
            overflow-wrap: anywhere;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>Web Calculator</h1>
        <p>A simple calculator running in Docker</p>

        <form method="POST">
            <input type="number" step="any" name="num1"
                   placeholder="First number" required
                   value="{{ num1 }}">

            <select name="operation">
                <option value="add" {% if operation == 'add' %}selected{% endif %}>Addition (+)</option>
                <option value="subtract" {% if operation == 'subtract' %}selected{% endif %}>Subtraction (-)</option>
                <option value="multiply" {% if operation == 'multiply' %}selected{% endif %}>Multiplication (×)</option>
                <option value="divide" {% if operation == 'divide' %}selected{% endif %}>Division (÷)</option>
            </select>

            <input type="number" step="any" name="num2"
                   placeholder="Second number" required
                   value="{{ num2 }}">

            <button type="submit">Calculate</button>
        </form>

        {% if result is not none %}
        <div class="result">
            <strong>Result: {{ result }}</strong>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    num1 = ""
    num2 = ""
    operation = "add"

    if request.method == "POST":
        num1 = request.form.get("num1", "")
        num2 = request.form.get("num2", "")
        operation = request.form.get("operation", "add")

        try:
            a = float(num1)
            b = float(num2)

            if operation == "add":
                result = a + b
            elif operation == "subtract":
                result = a - b
            elif operation == "multiply":
                result = a * b
            elif operation == "divide":
                if b == 0:
                    result = "Cannot divide by zero"
                else:
                    result = a / b
            else:
                result = "Invalid operation"

        except ValueError:
            result = "Please enter valid numbers"

    return render_template_string(
        HTML_PAGE,
        result=result,
        num1=num1,
        num2=num2,
        operation=operation
    )

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
