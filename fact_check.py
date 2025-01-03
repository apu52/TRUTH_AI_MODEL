import requests

def fact_check(query):
    api_url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": query,
        "key": "your_google_api_key"
    }
    
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None


fact_check_results = fact_check("COVID-19 vaccine safety")
print(fact_check_results)
