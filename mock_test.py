from unittest.mock import MagicMock

class ProductionClass():
    """ Some Class with code """
    def __init__(self):
        print("In Prod Class")

    def query_result(self, a, b):
        """ Connect to DB, run a select and return result. """
        return "Result from DB"

def func():
    """ some function """
    pass


def test_query_result():
    """ testing with mock """
    thing = ProductionClass()
    thing.query_result = MagicMock(return_value=3, side_effect=func())
    rv = thing.query_result(3, 4, 5)
    assert rv==3
    thing.query_result.assert_called_with(3, 4, 5)

