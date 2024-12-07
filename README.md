Database Viewer with Flask and React
This project is a web application that allows users to select a table and a column from a MySQL database, and view the data for the selected column. It uses Flask as the backend to interact with the database and React for the frontend.

Features
Fetch the list of tables from a MySQL database.
Select a table and view its column names.
Select a column and fetch the first 10 records from the selected column.
Full-stack implementation with Flask (Python) and React (JavaScript).
Cross-Origin Resource Sharing (CORS) enabled to allow communication between the frontend and backend.
Technologies Used
Backend: Flask (Python), MySQL, Flask-MySQLdb, Flask-CORS
Frontend: React, Fetch API
Database: MySQL (example database: sakila)
Environment Variables: .env file for MySQL connection settings
Setup
Backend Setup (Flask)
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/backend
Create a virtual environment and activate it:

For Windows:

bash
Copy code
python -m venv venv
venv\Scripts\activate
For Mac/Linux:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the environment variables by creating a .env file in the root directory and adding the following:

env
Copy code
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your-password
MYSQL_DB=sakila
Replace your-password with your MySQL root password.

Run the Flask app:

bash
Copy code
python app.py
The backend will be running on http://localhost:5000.

Frontend Setup (React)
Navigate to the frontend directory:

bash
Copy code
cd frontend
Install the dependencies:

bash
Copy code
npm install
Start the React development server:

bash
Copy code
npm start
The React app will be running on http://localhost:3000.

MySQL Database Setup
Ensure you have MySQL installed on your machine. If not, you can download and install it from MySQL's official site.

Create a MySQL database (for example, sakila) and import the sample database if you want to use it. The sakila database can be downloaded from MySQL Sample Databases.

Make sure the database credentials in the .env file match your MySQL setup.

Running the Application
Start the backend (Flask) server by running the Flask app.
Start the frontend (React) development server by running npm start.
Open your browser and go to http://localhost:3000 to interact with the application.
Usage
Once the app loads, select a table from the dropdown.
After selecting the table, the available columns for that table will appear in a second dropdown.
Select a column and click the "Show Data" button.
The first 10 records of the selected column will be displayed below.
Folder Structure
bash
Copy code
/your-repo-name
├── /backend
│   ├── app.py              # Flask backend
│   ├── requirements.txt    # Python dependencies
│   └── .env                # Environment variables for MySQL
│
├── /frontend
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── First.jsx       # Component for selecting table and column
│   │   └── index.js        # React entry point
│   ├── package.json        # React project dependencies
│   └── .env                # Environment variables for React (if any)
│
└── README.md               # Project documentation (this file)
Troubleshooting
CORS Issues: If you encounter CORS issues, ensure that Flask-CORS is installed and properly configured in the backend.
MySQL Connection Errors: Double-check your MySQL credentials in the .env file and ensure the database is running.
Missing Dependencies: If you see errors related to missing dependencies, run pip install -r requirements.txt in the backend or npm install in the frontend directory.
Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
