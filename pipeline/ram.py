spark = sparkSession.builder.appName("RAMDAS").getOrCreate()
ramdasschema = "ramdasschema"
cust_details = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/ramdasschema") \

    .option("dbtable", "cust_details") \
    .option("user", "root") \
    .option("password", "root") \
    .load()
cust_details.show()
