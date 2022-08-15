import requests,json,string,random

url = "https://www.instagram.com/p/Cgz5TJcI6fI6aKbKNrjJFpV9L51lcCAMXME4Dk0/"

session_id = "" #session-id of an account that follow the post account
user_id = session_id.split("%")[0] # session-id starts with the user id so here i split it and use it for the cookies

if "?" in url:                                #
    url=url.split("?")[0] + "?__a=1&__d=dis"  #
else:                                         # edit the url to get the post json .
    if url[-1] != "/":                        #   by adding  (?__a=1&__d=dis) to the end of the url we will get the json .
        url = url + "/"                       #        
    url = url + "?__a=1&__d=dis"              #

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

req = requests.request("GET",
                       url=url,
                       headers=headers,
                       cookies={
                         "sessionid":f"{session_id}",
                         "ds_user_id":f"{user_id}",
                         "csrftoken":"".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32)) # generate a random csrftoken .
                       }
                      )

DLurl = json.loads(req.text)["items"][0]["video_versions"][0]["url"] # extracting the original video url from post json .

downloadReq = requests.get(DLurl ,stream=True ) # loading the bytes of the video from the url we got .

with open('instaPostTest.mp4','wb') as f: # saving the video from the variable we saved the bytes in .
    f.write(downloadReq.content)
    f.flush()
