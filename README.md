<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>Finance Tracker</h1>
    <p>Finance Tracker is a web application for tracking financial transactions, managing budgets, and gaining spending insights. Built with Django (backend) and React (frontend).</p>
    <h2>Features</h2>
    <ul>
        <li>User authentication</li>
        <li>Add, edit, delete transactions</li>
        <li>Categorize transactions</li>
        <li>Visualize spending with charts</li>
        <li>Set and track budgets</li>
        <li>Export data to CSV</li>
    </ul>  
    <h2>Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Django, Django REST Framework</li>
        <li><strong>Frontend:</strong> React, Redux, Axios, Chart.js</li>
        <li><strong>Database:</strong> PostgreSQL</li>
        <li><strong>Authentication:</strong> JWT</li>
        <li><strong>Styling:</strong> CSS, Bootstrap</li>
    </ul> 
    <h2>Getting Started</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
        <li>Node.js</li>
        <li>npm or yarn</li>
        <li>PostgreSQL</li>
    </ul>
    <h3>Setup</h3>
    <p>Clone the repo:</p>
    <code>
        git clone https://github.com/yourusername/finance-tracker.git<br>
        cd finance-tracker
    </code> 
    <h4>Backend:</h4>
    <code>
        python3 -m venv env<br>
        source env/bin/activate<br>
        pip install -r requirements.txt<br>
        # Set up PostgreSQL and update settings.py<br>
        python manage.py migrate<br>
        python manage.py createsuperuser<br>
        python manage.py runserver
    </code>    
    <h4>Frontend:</h4>
    <code>
        cd frontend<br>
        npm install<br>
        npm start
    </code>
    <h2>Running the Project</h2>
    <ul>
        <li><strong>Frontend:</strong> <a href="http://localhost:3000" target="_blank">http://localhost:3000</a></li>
        <li><strong>Backend API:</strong> <a href="http://localhost:8000" target="_blank">http://localhost:8000</a></li>
    </ul>
</body>
</html>
