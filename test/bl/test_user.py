from bl.user import Authenticate

def test_Authenticate():
    assert not Authenticate('a','b')  