from platform import system
import os
from datetime import datetime
uname = system()
date_publish = "(Non-Date)"
name_tool = "user1"
if uname == 'Windows':
    clear_code = "cls"
else:
    clear_code = "clear"
try:
    import json
except ImportError:
    os.system("pip install json")
try:
    import lxml
except ImportError:
    os.system("pip install lxml")
try:
    import bs4
except ImportError:
    os.system("pip install bs4")
try:
    import requests
except ImportError:
    os.system("pip install requests")
try:
    import fake_useragent
except ImportError:
    os.system("pip install fake_useragent")
os.system(clear_code)
def start():
    os.system(clear_code)
    logo =  """\033[0;31m
_________              _______  _______  _______ 
\__   __/    |\     /|(  ____ \(  ____ \(  ____ )
   ) (       | )   ( || (    \/| (    \/| (    )|
   | | _____ | |   | || (_____ | (__    | (____)|
   | |(_____)| |   | |(_____  )|  __)   |     __)
   | |       | |   | |      ) || (      | (\ (   
   | |       | (___) |/\____) || (____/\| ) \ \__
   )_(       (_______)\_______)(_______/|/   \__/
                                                
        \033[0;35m Made By TheDark                  
"""
    print(logo)
try:
    import requests, lxml, json
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent
    start()
    run = True
    while run:
        username = str(input("\033[0;33m~ Enter Account Username $\033[1;37m "))
        if username.lower() == 'clear' or username.lower() == 'cls':
            start()
        elif username.__len__() == 0:
            print("\033[1;31m>> Required Field!")
        else:
            BASE_URL = "https://tiktok.com/"
            profile_url = BASE_URL + "@" + username
            ua = UserAgent()
            random_ua = ua.random
            request_headers = {
                'user-agent': random_ua
            }
            html = requests.get(profile_url, headers= request_headers).text
            soup = BeautifulSoup(html, 'lxml')
            user_d = soup.find("script", {"id":"__UNIVERSAL_DATA_FOR_REHYDRATION__", "type":"application/json"})
            user_d = str(user_d).replace("<script id=\"__UNIVERSAL_DATA_FOR_REHYDRATION__\" type=\"application/json\">", '').replace("</script>", '')
            user_d = json.loads(user_d)
            statusMsg = user_d['__DEFAULT_SCOPE__']['webapp.user-detail']['statusMsg']
            if statusMsg == 'ok':
                user_information = user_d['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['user']
                user_stats = user_d['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']['stats']
            else:
                print("\033[1;31m>> Not Found!")
                user_information = False
            if user_information != False:
                nickname = user_information['nickname']
                uniqueId = user_information['uniqueId']
                region = user_information['region']
                isprivate = user_information['privateAccount']
                isbanned = user_information['isEmbedBanned']
                lastnicknameupdate = datetime.fromtimestamp(int(user_information['nickNameModifyTime']))
                followers = user_stats['followerCount']
                followings = user_stats['followingCount']
                hearts = user_stats['heartCount']
                videos = user_stats['videoCount']
                friends = user_stats['friendCount']
                id = user_information['id']
                createtime = datetime.fromtimestamp(int(user_information['createTime']))
                lastuniqueupdate = datetime.fromtimestamp(int(user_information['uniqueIdModifyTime']))
                isverified = user_information['verified']
                language = user_information['language']
                avatar = user_information['avatarMedium']
                
                information = f"""\033[0;32m
>> Nickname > {nickname}
>> Username > {uniqueId}
>> Region > {region}
>> isPrivte > {isprivate}
>> isBanned > {isbanned}
>> Last Nickname Upadate > {lastnicknameupdate}
>> Followers > {followers}
>> Followings > {followings}
>> Friends > {friends}
>> id > {id}
>> Create Account Date > {createtime}
>> Last Username Update > {lastuniqueupdate}
>> isVerified > {isverified}
>> Language > {language}
>> Avatar Link > {avatar}
                """
                print(information)
except KeyboardInterrupt:
    exit()
