from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .appName("PySpark Test") \
    .getOrCreate()
spark.range(5).show()
spark.stop()