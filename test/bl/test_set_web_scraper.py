from bl.set_web_scraper import GetSetData

def test_getsetdata():
    assert  len(GetSetData(["ptt"])) > 0