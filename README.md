# YOUTUBE-DATA-HARVESTING-AND-WAREHOUSING

This project aims to harvest data from YouTube using Python scripting and store it in a NoSQL (MongoDB) database as a data lake. The harvested data can then be fetched from the MongoDB database and migrated to a SQL (MySQL) database for further analysis. Additionally, MYSQL queries can be executed on the MySQL database to answer specific questions related to the uploaded channel information.

Prerequisites Before running the scripts, make sure you have the following dependencies installed:

* Python
* MongoDB
* MySQL

Configure the MongoDB and MySQL database connection:

Open the youtube.py file and update the MongoDB and MySQL connection details. Make sure you have a MongoDB database and collection created to store the harvested data. Create a MySQL database and tables to store the migrated data.
