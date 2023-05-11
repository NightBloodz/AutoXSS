from browserutils import *
import json, re, html, argparse, sys
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", type=bool, choices=[True, False], required=False, default=False, help="Outupt verbose" )
parser.add_argument("-t", "--target", type=str, help="Url to attack, the word FUZZ will be replaced with the payloads", required=True)
parser.add_argument("-d", "--data", type=str, help="Data of the petitions, the word FUZZ will be replaced with the payloads", default=False, required=False)
parser.add_argument("-H", "--headers", type=str, help="Use headers with this format 'HEADER:value'", required=False, default=False)
parser.add_argument("--pathstocheck", type=str, help="Paths to check reflections, useful for stored XSS", required=False, default=False)

args = parser.parse_args()

#Check args
verbose = args.verbose
paths2check = args.pathstocheck

data = args.data
if data:
    if "FUZZ" not in data:
        print("Data must contain FUZZ word")
        sys.exit(1)


target = args.target
if "https://" not in target:
    print("The target must have this format 'https://website.com/path/path?things=thing'")
    sys.exit(1)
if not data and "FUZZ" not in target:
    print("Url without POST data must contain FUZZ word")
    sys.exit(1)


if args.headers:
    headers = {}
    for header in args.headers:
        headers[header.split(":")[0]] = header.split(":")[1]
        
        
     





browsers = BrowserPool(10, headers)


if __name__ == "__main__":
    print("Checking reflection on "+target)
    
    #Create the reflect payload
    reflect_url = target.replace("FUZZ", "xxxaaaxxxyyyzzz")
    
    #Do the petition
    if data:
        content = browsers.petition(reflect_url, data=data)
    else:
        content = browsers.petition(reflect_url)
        
    
    
    
    
    
    
    
    
    
    
    
    