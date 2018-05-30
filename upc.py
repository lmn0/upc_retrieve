import requests
import sys
import pprint
import json
productId = sys.argv[1];
res = requests.get("https://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByProduct&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=ThejassK-ProRetri-PRD-47141958a-32e1cf44&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&productId.@type=UPC&productId="+productId)
json_pretty = pprint.pformat(json.loads(res.text))
json_pretty = json_pretty.replace("u'","'")

print json_pretty
