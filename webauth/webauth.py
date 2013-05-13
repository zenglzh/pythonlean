import httplib,urllib
username = "zeng***" # Domain user name
password = "***"     # Domain user password
headers = {'Content-Type':'application/x-www-form-urlencoded','Accept':'text/html,application/xml'}
params=urllib.urlencode({'username':username,'password':password,'pwd':password,'secret':'true'})
conn = httplib.HTTPConnection("192.168.255.252:80")
conn.request("POST","/webAuth/",params,headers)
response = conn.getresponse()
print response.status,response.reason # http status code,200 OK 
conn.close()