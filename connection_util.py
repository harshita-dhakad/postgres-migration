import psycopg2 as ps
from neo4j import GraphDatabase
from log import logger
from dotenv import load_dotenv
import os


load_dotenv()

def create_postgres_connection():
    username = os.getenv("postgres_username")
    password = os.getenv("postgres_password")
    host = os.getenv("postgres_host")
    connection = ps.connect(f"postgresql://{username}:{password}@{host}/pro?sslmode=require")
    logger.info("connection to postgres is establised")
    return connection


def create_neo4j_connection():


    uri = "neo4j://localhost:7687" 
    username = "neo4j"  
    password = os.getenv('neo4j_password')

    driver = GraphDatabase.driver(uri, auth=(username, password))  
    logger.info("connection to neo4j is established")
    return driver