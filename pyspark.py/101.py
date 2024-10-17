from pyspark.sql import SparkSession

# Initialize a Spark session
spark = SparkSession.builder.appName("example").getOrCreate()

# Create a DataFrame
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Perform some operations
df.show()
df.filter(df.Age > 30).show()