from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("LocalTest") \
    .master("local[*]") \
    .getOrCreate()

data = [("Shyam", 25), ("Ram", 30)]
df = spark.createDataFrame(data, ["Name", "Age"])

df.show()