from bl.line_notify import SendLineNotify

def test_SendLineNotify():
    assert SendLineNotify("test from stock line notify unit test").index('ok')>0
