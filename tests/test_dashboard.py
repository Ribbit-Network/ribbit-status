import requests 

def test_ribbit_dashboard():
    r = requests.get("https://ribbit-network.herokuapp.com/")
    if r.status_code == 200:
        assert True 
    else:
        assert False