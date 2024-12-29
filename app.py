#Python code for numerical integration

import math
import time
from flask import Flask, jsonify, request

# Create Flask app
app = Flask(__name__)


# Define the function to integrate
def f(x):
    return abs(math.sin(x))

# Numerical integration using the rectangular method
def numerical_integration(lower, upper, N):
    step_size = (upper - lower) / N
    total_area = 0
    
    for i in range(N):
        # Compute the height of the rectangle
        x = lower + i * step_size
        height = f(x)
        # Add the area of the rectangle to the total
        total_area += height * step_size
    
    return total_area

# Main code
@app.route('/)
def integrate():
    lower = 0
    upper = 3.14  
    N =1000  
    result = numerical_integration(lower, upper, N)
    return jsonify({"lower": lower, "upper": upper, "N": N, "result": result})


if __name__ == "__main__":
    app.run(port=5000)
