from flask import Flask, render_template, request, jsonify
from calc import salary_breakdown  # Replace 'your_python_module' with the actual module where salary_breakdown is defined

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/net_salary_simulator')
def net_salary_simulator():
    return render_template('net_salary_simulator.html')

@app.route('/calculate-salary', methods=['POST'])
def calculate_salary():
    try:
        # Get salary input from the request
        data = request.get_json()
        salary = float(data['salary'])

        # Call your Python function to calculate the salary breakdown
        result = salary_breakdown(salary)

        # Return the result as JSON
        return jsonify(result)
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
