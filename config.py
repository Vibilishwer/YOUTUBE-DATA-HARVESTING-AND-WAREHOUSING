from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from sqlalchemy import create_engine
import pymongo
import mysql.connector

#=======================GOOGLE API KEY=================================
api_key = 'copy your API from youtube'
youtube = build('youtube', 'v3', developerKey=api_key)
channel_id = "UCmyKnNRH0wH-r8I-ceP-dsg"


#======================MONGODB CONNECTION==============================
client = pymongo.MongoClient("mongodb+srv://YourUserName:Password@cluster0.eefu6ud.mongodb.net/")
database = client["youtube"]
collection = database["channel_information"]

#=====================SQLALCHEMY FOR SEND AS DATAFRAME================
engine = create_engine('mysql+mysqlconnector://root:YOUR PASSWORD@localhost/mydatabase')


#=====================MYSQL - PYTHON CONNECTION=======================
mydb = mysql.connector.connect(
  host="localhost",
  user="ROOT",
  password ="YOUR PASSWORD",
  database="mydatabase"
)
mycursor = mydb.cursor()
