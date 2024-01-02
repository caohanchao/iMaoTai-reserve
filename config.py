import os

'''
*********** 商品配置 ***********
'''
ITEM_MAP = {
    "10213": "53%vol 500ml贵州茅台酒（癸卯兔年）",
    "10214": "53%vol 375ml×2贵州茅台酒（癸卯兔年）",
    "10056": "53%vol 500ml茅台1935",
    "2478": "53%vol 500ml贵州茅台酒（珍品）"
}

ITEM_CODES = ['10213', '10214']   # 需要预约的商品(默认只预约2个赚钱的茅子)

'''
*********** 消息推送配置 ***********
push plus 微信推送,具体使用参考  https://www.pushplus.plus
如没有配置则不推送消息
为了安全,这里使用的环境配置.git里面请自行百度如何添加secrets.pycharm也可以自主添加.如果你实在不会,就直接用明文吧（O.o）
'''
PUSH_TOKEN = "4380ca3baba64edc99bbc5999f38f7da"
# os.environ.get("")


'''
*********** 地图配置 ***********
获取地点信息,这里用的高德api,需要自己去高德开发者平台申请自己的key
'''
AMAP_KEY = "f57d5d4860a8684ef467d560d42fff91"
#os.environ.get("f57d5d4860a8684ef467d560d42fff91")


'''
*********** 个人账户认证配置 ***********
个人用户 credentials 路径
不配置,使用默认路径,在项目目录中;如果需要配置,你自己应该也会配置路径
例如： CREDENTIALS_PATH = './myConfig/credentials'
'''
CREDENTIALS_PATH = './myConfig/credentials'


'''
*********** 个人加解密密钥 ***********
为了解决credentials中手机号和token都暴露的问题,采用AES私钥加密,保障账号安全.
这里采用ECB,没有采用CBC.如果是固定iv,那加一层也没多大意义;如果是不固定iv,那每次添加账号判重的时候都认为不一样,除非你每次再把配置全部反解密,去校验去重,得不偿失.
key用了SHA-256转化,所以这里可以配置任意字符串,不用遵守AES算法要求密钥长度必须是16、24或32字节
如果不会配置环境变量(建议学习)、不care安全性、非开源运行,你可以在这里明文指定,eg:PRIVATE_AES_KEY = '666666'
ps:本来是写了判断是否配置密钥，可以自由选择明文保存的方式。但是还是为了安全性，限制了必须使用AES加密。哪怕是明文密钥。
'''
PRIVATE_AES_KEY = "314159"
#os.environ.get("666666")


'''
*********** 预约规则配置 ************
因为目前支持代提的还是少,所以建议默认预约最近的门店
'''
_RULES = {
    'MIN_DISTANCE': 0,   # 预约你的位置最近的门店
    'MAX_SALES': 1,      # 预约本市出货量最大的门店
}
RESERVE_RULE = 0         # 在这里配置你的规则，只能选择其中一个
