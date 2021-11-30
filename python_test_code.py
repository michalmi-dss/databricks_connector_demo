# Databricks notebook source
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# test 

databases = spark.sql("""
show databases;
""").collect()

for database in databases:
    if database.databaseName.startswith('ap'):
        print(database.databaseName)
