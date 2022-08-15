import requests,json,string,random

#
# this works for any public account , i will post a version for the private accounts . 
#

url = "https://www.instagram.com/tv/ChRyLjMouC0/?utm_source=ig_web_copy_link"#any instagram post url

if "?" in url:
    url=url.split("?")[0] + "?__a=1&__d=dis"
else:
    if url[-1] != "/":
        url = url + "/"
    url = url + "?__a=1&__d=dis"
    print(url)

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',"cookie":"csrftoken="+"".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32))+";"}

req = requests.request("GET",url=url,headers=headers)

DLurl = json.loads(req.text)["graphql"]["shortcode_media"]["video_url"]

downloadReq = requests.get(DLurl ,stream=True )
with open('instaPostTest.mp4','wb') as f:
    f.write(downloadReq.content)
    f.flush()
