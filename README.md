# YOUTUBE-DATA-HARVESTING-AND-WAREHOUSING

This project aims to harvest data from YouTube using Python scripting and store it in a NoSQL (MongoDB) database as a data lake. The harvested data can then be fetched from the MongoDB database and migrated to a SQL (MySQL) database for further analysis. Additionally, MYSQL queries can be executed on the MySQL database to answer specific questions related to the uploaded channel information.

Prerequisites Before running the scripts, make sure you have the following dependencies installed:

* Python
* MongoDB
* MySQL

Configure the MongoDB and MySQL database connection:

Open the youtube.py file and update the MongoDB and MySQL connection details. Make sure you have a MongoDB database and collection created to store the harvested data. Create a MySQL database and tables to store the migrated data.

# Harvest YouTube Data

![image](https://github.com/Vibilishwer/YOUTUBE-DATA-HARVESTING-AND-WAREHOUSING/assets/145904866/a84b528a-7cfa-46b2-bf0f-d8addfeaa8af)

Run the Youtube.py script. Provide the channel ID as user input. The script will fetch the channel data from YouTube using the YouTube Data API and store it in the MongoDB database as a data lake.

# Upload Channel Information

![image](https://github.com/Vibilishwer/YOUTUBE-DATA-HARVESTING-AND-WAREHOUSING/assets/145904866/8a89247e-2228-456b-8892-bddcd21ca81c)

Run the function_upload_fetch.py script. Provide the necessary parameters (e.g., channel ID) as user input. The script will fetch the uploaded channel information from the MongoDB database.

# Migrate Data to MySQL

![image](https://github.com/Vibilishwer/YOUTUBE-DATA-HARVESTING-AND-WAREHOUSING/assets/145904866/d2a0f576-8b20-41a8-9c4d-d4725710e7da)

Run the migrate_to_mysql.py script. The script will migrate the fetched data from the MongoDB database to the MySQL database for further analysis.

# Execute SQL Queries

![image](https://github.com/Vibilishwer/YOUTUBE-DATA-HARVESTING-AND-WAREHOUSING/assets/145904866/5350ca88-5b33-49ae-aba8-e335d9a28c13)

Run the execute_sql_queries.py script. Write SQL queries in the script to answer specific questions related to the uploaded channel information. The script will execute the SQL queries on the MySQL database and display the results
