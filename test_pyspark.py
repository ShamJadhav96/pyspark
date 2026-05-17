from pyspark.sql import SparkSession
 
spark = SparkSession.builder.appName("TestPySpark").getOrCreate()
 
data = [("Alice", 29), ("Bob", 35)]
 
df = spark.createDataFrame(data, ["Name", "Age"])
 
df.show()
 
spark.stop()