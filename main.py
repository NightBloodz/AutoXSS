from utils.browserutils import *
import json, re, html, argparse, sys
from bs4 import BeautifulSoup
from utils.xss_utils import *


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", type=bool, choices=[True, False], required=False, default=False, help="Outupt verbose" )
parser.add_argument("-t", "--target", type=str, help="Url to attack, the word FUZZ will be replaced with the payloads", required=True)
parser.add_argument("-d", "--data", type=str, help="Data of the petitions, the word FUZZ will be replaced with the payloads", default=False, required=False)
parser.add_argument("-H", "--headers", nargs='+', type=str, help="Use headers with this format 'HEADER:value'", required=False, default=False)
parser.add_argument("--pathstocheck", type=str, help="Paths to check reflections, useful for stored XSS", required=False, default=False)
parser.add_argument("--browsers", type=int, help="Number of browsers running simultaneously", required=False, default=1)

args = parser.parse_args()

#Check args
verbose = args.verbose
paths2check = args.pathstocheck
headers = args.headers
max_browsers = args.browsers

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


if headers:
    #Convert headers to dictionary
    headers = {}
    for header in args.headers:
        header = header.split(":")
        headers[header[0]] = header[1]
   
    
        
    
browsers = BrowserPool(max_browsers)

if __name__ == "__main__":
    reflection = "xxxaaaxxxyyyzzz"
    print("Reflection = "+reflection)
    print()
    print()
    
    #Do petition
    content = get_contents(browsers, target, reflection, data, headers)
    
        

            
        
        
    
    
    
    
    
    
    
    
    
    
    
    