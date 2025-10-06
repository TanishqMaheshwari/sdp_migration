from pyspark import pipelines as sdp
from pyspark.sql import DataFrame, SparkSession

spark = SparkSession.active()

@sdp.materialized_view
def example_python_materialized_view() -> DataFrame:
    return spark.range(10)
