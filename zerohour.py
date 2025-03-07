def UstaZeroHour(referer,api):
    import requests
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #yetki alınması gerek. 
    url = "https://usta.prodaft.com/api/threat-stream/v4/brand-protection/referrers"
    payload = { "urls": [referer] }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer "+api
    }
    response = requests.post(url, json=payload, headers=headers,verify=False)
    response=response.json()
    try:
        report=response["errors"][referer][0]
    except:
        report="Hatasız Report edildi."
    return report

print(UstaZeroHour("https://example12345678900sdadssdasdaasdasdasdasdsdasasasssdasdaasdasd.net","apikey"))
