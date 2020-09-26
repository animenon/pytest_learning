import logging
import unittest

from operator import add

from pyspark.sql import SparkSession


# CODE TO BE TESTED
def sample_word_count():
    spark = SparkSession.builder.appName("Python Spark example").getOrCreate()
    test_rdd = spark.sparkContext.parallelize(['cat dog mouse','cat cat dog'], 2)
    return test_rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(add).collect()

def filter_df(df, threshold):
    return df.filter(df[0]<threshold)


#################################################################################################
# A simple comparision of unitest Vs pytest is shown below
################################### UNIT TEST ####################################################
class PySparkTest(unittest.TestCase):
    
    @classmethod
    def suppress_py4j_logging(cls):
        logger = logging.getLogger('py4j')
        logger.setLevel(logging.WARN)

    @classmethod
    def create_testing_pyspark_session(cls):
        return (SparkSession.builder.master('local').appName('my-local-testing-pyspark-context')
                .enableHiveSupport().getOrCreate())
    
    @classmethod
    def setUpClass(cls):
        cls.suppress_py4j_logging()
        cls.spark = cls.create_testing_pyspark_session()

    @classmethod
    def tearDownClass(cls):
        cls.spark.stop()

class SimpleTest(PySparkTest):
    def test_basic(self):
        results = sample_word_count()
        expected_results = [('cat', 3), ('dog', 2), ('mouse', 1)]
        self.assertEqual(set(results), set(expected_results))

    def test_filter_df(self):
       # spark = PySparkTest.create_testing_pyspark_session()
       df = SimpleTest.spark.createDataFrame([(i,) for i in list(range(50))])
       results = [i[0] for i in list(filter_df(df, 10).collect())]
       expected_results = list(range(10))
       self.assertEqual(results, expected_results)


####################################### PYTEST ###################################################
# decorator - to set logging level to Warning
def logger_fix(func):
    def wrapper(*args, **kwargs):
        try:
            # logging.info("started '{0}', parameters : {1} and {2}".format(func.__name__, args, kwargs))
            logger = logging.getLogger('py4j')
            logger.setLevel(logging.WARN)
            return func(*args, **kwargs)
        except Exception as e:
            logging.exception(e)
    return wrapper


# logger level declaration below will serve the purpose but using a decorator as defined above would
# be a better way to do it.

# logger = logging.getLogger('py4j')
# logger.setLevel(logging.WARN)


@logger_fix
def test_basic():
    results = sample_word_count()
    expected_results = [('cat', 1), ('dog', 2), ('mouse', 1)] 
    assert set(results) == set(expected_results)


@logger_fix
def test_filter_df(spark_session):
    df = spark_session.createDataFrame([(i,) for i in list(range(50))])
    results = [i[0] for i in list(filter_df(df, 10).collect())]
    expected_results = list(range(10))
    assert results == expected_results

