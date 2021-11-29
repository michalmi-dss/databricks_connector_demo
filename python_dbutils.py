from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils


spark = SparkSession.builder.getOrCreate()
dbutils = DBUtils(spark)

list_fs = dbutils.fs.ls("dbfs:/mnt/")

for path in list_fs:
    print(path.path)