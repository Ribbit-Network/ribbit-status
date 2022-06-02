import requests 

def test_ribbit_website():
    r = requests.get("https://www.ribbitnetwork.org/")
    if r.status_code == 200:
        assert True 
    else:
        assert False