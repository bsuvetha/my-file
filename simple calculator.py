#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install flask')


# In[7]:


from flask import Flask, request, jsonify
from werkzeug.serving import run_simple
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Simple Calculator</h1>
    <form action="/calculate" method="post">
        <input type="text" name="num1" placeholder="First Number">
        <select name="operation">
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
            <option value="divide">Divide</option>
        </select>
        <input type="text" name="num2" placeholder="Second Number">
        <button type="submit">Calculate</button>
    </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error! Division by zero.'
    else:
        result = 'Invalid operation'
    
    return jsonify(result=result)

# Function to run Flask app
def run_flask():
    run_simple('localhost', 5000, app)

# Run Flask app in a separate thread
thread = threading.Thread(target=run_flask)
thread.start()


# In[ ]:




