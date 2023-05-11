import requests


def get_contents(browsers, url, reflection="", data=False, headers={}):
    
    reflect_url = url.replace("FUZZ", reflection)
    #Do the petition
    if data:
        print("Getting", reflect_url)
        payload = data.replace("FUZZ", reflection)
        content = requests.post(reflect_url, data=payload, headers=headers).text
        print("Data ----> "+payload)
    else:
        print("Getting "+reflect_url+" with Headless Browser")
        content = browsers.petition(reflect_url, headers)
    
    
    if headers and headers != {}:
        print("Using extra HEADERS:", headers)
    
    
    
    return content