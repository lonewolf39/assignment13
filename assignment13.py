# Q.1- Get random quotes using the correct endpoints
import requests
resp=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text")
print(resp.content)
