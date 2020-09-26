# pytest_learning

This is a repo with few code snippets to start off on unit tests in python using [pytest](https://docs.pytest.org/en/stable/)

- `simple_test` - Simple pytest samples
- `mock_test` - Use of mocks for unit testing
- `spark_test` - A  simple starter for unit testing pyspark code (unittest vs pytest using `spark_session` fixture from `pytest_spark`)

Python version used 3.7 and Java version 8 is to be used (as its the highest Java version currently supported by pyspark).

Pytest configurations are in `pytest.ini`.
The same file is used to configure spark session for [PySpark](https://spark.apache.org/) unit-testing using [pytest-spark](https://pypi.org/project/pytest-spark/)
