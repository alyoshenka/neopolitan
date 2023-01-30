"""Demo test"""
from src import demo

def demo_test():
    """Test demo"""
    try:
        demo.main()
    # pylint: disable=broad-except
    except Exception as err:
        assert False, str(err)
