from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

print("Spark temp directory:")
print(spark.sparkContext.getConf().get("spark.local.dir"))

spark.stop()