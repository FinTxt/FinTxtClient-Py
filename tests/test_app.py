from FinTxtClient import FinTxtClient

def test_get_languages():

    client = FinTxtClient()
    langs = client.languages()

    assert langs == ["english","french","german","russian","arabic","total"]
