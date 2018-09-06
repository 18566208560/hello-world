# -*- coding: utf-8 -*-

# https://www.whoishostingthis.com/tools/user-agent/

ua_pool = [
    # QQBrowser
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36 '
    'Core/1.47.277.400 QQBrowser/9.4.7658.400',
    # 360极速浏览器
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    # 360安全浏览器
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    # Chrome
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36',
    # Firefox
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    # Opera
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36 '
    'OPR/37.0.2178.32',
    # Safari
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    # 百度浏览器
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.3 '
    'Safari/537.36',
    # 遨游浏览器
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.9.2.1000 Chrome/39.0.2146.0 '
    'Safari/537.36',
    # UC浏览器
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 '
    'UBrowser/5.6.12150.8 Safari/537.36',
    # IE Edge
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 '
    'Safari/537.36 Edge/13.10586',
    # IE 11
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    # IE 10
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    # IE 9
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    # IE 8
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0)',
    # 搜狗浏览器
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE '
    '2.X MetaSr 1.0',
    # 猎豹浏览器
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.154 Safari/537.36 '
    'LBBROWSER',
    # 世界之窗浏览器
    'Mozill/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36 '
    'TheWorld 7',
    # safari 5.1 – MAC
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '
    'Safari/534.50',
    # safari 5.1 – Windows
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    # IE 9.0
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    # IE 8.0
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    # IE 7.0
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    # IE 6.0
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    # Firefox 4.0.1 – MAC,
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    # Firefox 4.0.1 – Windows
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    # Opera 11.11 – MAC
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    # Opera 11.11 – Windows
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    # Chrome 17.0 – MAC
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 '
    'Safari/535.11',
    # Maxthon
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    # Tencent TT
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    # The World 2.x
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    # The World 3.x
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    # sogou 1.x
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR '
    '2.0.50727; SE 2.X MetaSr 1.0)',
    # 360
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    # Avant
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
    # Green Browser
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
]

ua_pool_m = [
    # Android QQ浏览器
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/4.1 Mobile Safari/533.1',
    # 安卓 原生浏览器
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    # 安卓 UC
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) UC AppleWebKit/534.31 (KHTML, '
    'like Gecko) Mobile Safari/534.31',
    # 安卓 Opera
    'Opera/9.80 (Android 4.0.3; Linux; Opera Mobi/ADR-1210241554) Presto/2.11.355 Version/12.10',
    # 三星手机
    'SAMSUNG-SGH-G508E/G508EZCIG2 SHP/VPP/R5 NetFront/3.4 Qtv5.3 SMM-MMS/1.2.0 profile/MIDP-2.0 '
    'configuration/CLDC-1.1',
    # iphone Safari
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) '
    'Version/5.1 Mobile/9B206 Safari/7534.48.3',
    # iphone QQ
    'MQQBrowser/38 (iOS 4; U; CPU like Mac OS X; zh-cn)',
    # iphone UC
    'IUC(U;iOS 5.1.1;Zh-cn;320*480;)/UCWEB8.9.1.271/42/800',
    # 塞班 自带浏览器
    'Nokia5320/04.13 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 '
    ') AppleWebKit/413 (KHTML, like Gecko) Safari/413',
    # 塞班 QQ浏览器
    'Nokia5320(19.01)/SymbianOS/9.1 Series60/3.0',
    # iOS 4.33 – iPhone
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, '
    'like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    # iOS 4.33 – iPod Touch
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, '
    'like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    # iOS 4.33 – iPad
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) '
    'Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    # Android N1
    'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, '
    'like Gecko) Version/4.0 Mobile Safari/533.1',
    # Android QQ
    'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) '
    'AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    # Android Opera
    'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
    # Android Pad Moto Xoom
    'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) '
    'Version/4.0 Safari/534.13',
    # BlackBerry
    'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) '
    'Version/6.0.0.337 Mobile Safari/534.1+',
    # WebOS HP Touchpad
    'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) '
    'wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
    # Nokia N97
    'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 '
    'Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
    # Windows Phone Mango
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
    # UC
    'UCWEB7.0.2.37/28/999',
    # UC standard
    'NOKIA5700/ UCWEB7.0.2.37/28/999',
    # UC Openwave
    'Openwave/ UCWEB7.0.2.37/28/999',
    # UC Opera
    'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
]
