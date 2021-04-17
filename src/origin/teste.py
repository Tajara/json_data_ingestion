from pyspark.sql import SparkSession
from pyspark.sql import functions as sf
if __name__ == '__main__':
    spark = SparkSession.builder.appName('abc').getOrCreate()
    #sc.hadoopConfiguration.set("mapreduce.input.fileinputformat.input.dir.recursive", "true")
    json_file = spark.read.json('D:\Projetos\Pismo\input_data\_tmp\*.json')
    json_file.show(10, False)
    json_file.printSchema()
    test = json_file.select('event_id','timestamp','data.id','data.new_status','data.old_status','data.reason').show()





