from negeng.retry_tools import simple_retry

def test_simple_retry():
    @simple_retry(count=3, sec=0)
    def failing_func():
        raise Exception("This function always fails.")
    
    @simple_retry(count=3, sec=0)
    def passing_func():
        return True

    assert failing_func() is None
    assert passing_func() is True