import os,json
import zipfile
from pyspark.sql import SparkSession



spark = SparkSession.builder.appName('abc').getOrCreate()

class LoadFilesModule():

    def read_json():
        json_files = spark.read.json('D:\Projetos\json_data_ingestion\input_data\_tmp\*.json')
        return json_files


    def dict_to_df(json_files):
        df = json_files.select('event_id', 'timestamp', 'data.id', 'data.new_status', 'data.old_status','data.reason')
        return df











