#encoding:utf-8
#规定文档的编码为utf-8

#代码写于2023/3/18 3时33分

# 从requests中导入get()方法,用于使用get请求
from requests import get 

# 从requests中导入post()方法,用于使用post请求
from requests import post 

# 从os.path中导入exists()方法,用于检查文件夹是否存在
from os.path import exists 

# 从os中导入mkdir()方法,用于创建文件夹
from os import mkdir 

# 从re中导入findall()方法,用于搜索规定格式的内容
from re import findall 


#获取歌单的名字及歌曲id和名字
def id_list(params,encSecKey):
    
    # 歌单链接
    url="https://music.163.com/weapi/v6/playlist/detail?csrf_token=ba31dd997365e18fd7864f87e159200d"
    
    # 歌单的请求头
    headers={
        "cookie":"nts_mail_user=kanwenhao12@163.com:-1:1; _ntes_nuid=894152d37b7e6246282b05c757933750; _ntes_nnid=894152d37b7e6246282b05c757933750,1656768416108; NMTID=00Ouvi8IU9PpjhnKkC4lEZ-b1-fnisAAAGBvxfH6g; WEVNSM=1.0.0; WNMCID=juoyjd.1656768416439.01.0; WM_TID=xi+L33ogy7BBBVEUBBLAA4q6Vm/wjUV8; _ga=GA1.2.336513031.1656826901; _ns=NS1.2.666204652.1656826901; ntes_kaola_ad=1; __snaker__id=UsniXk987sbGB6Hw; YD00000558929251:WM_TID=neoAha40v8VAEBQRUBLRdMULl+hG95Jj; __remember_me=true; NTES_CMT_USER_INFO=486617256|有态度网友0t0j2E|http://cms-bucket.nosdn.127.net/2018/08/13/078ea9f65d954410b62a52ac773875a1.jpeg|false|a2Fud2VuaGFvMTJAMTYzLmNvbQ==; __bid_n=186a8b0117931221df4207; FPTOKEN=kz7kGDqNPTSAvfJe2GizOoy23XuklAFocWipkIm6KA5K9U/j73v1UIqwPK2ftPuWnjoCarSDugbtyviB/cvnpKuqo7PzfQ9cKSY9FXKthI7WYPrVkSm1//V/UQ7MOzUO2rp2yTfGWf5aQWu+rjfB3MUm7KyduVCjC64erbjgIGQicj/LcFSgeaNcSaJ1GI9xxNonMfyWiUOlxeTJm6m8Fj15PiH/1ZfSMbeniSFeFxbqwbKnfTfba4YzggY72Bp9bpc2TWUoTBw4SPM8BxYnWviYkf7wIOMH9hLONkzUSqWIMJHXw2FMCfecEq65jHgxW0xHu8srjVXc4q98DiGzSknTViIgxYeuIDBbHJirE6B4mcHs34uNtzV32YkFUle5DoP2sNANF18yIgauE2oy5qC2KS5YAwhr+ylqPc9W0OFD1mMaPP1Y7js1+ETu4hDQ|qsYursh12YcUAjaHz/Ea1/HIuoxRpRxphUdtnLDrXnw=|10|a466e9f79ccaafa6a5c54e959fcda714; NTES_PASSPORT=77p5H7izo2oECCe0ogpNfdBq70R_DUCD3ch2_1VsTCNfgN.agb3pG9JyBXUYm.DW0mLHvbndZjG.pl0iQ_OE9LjLXrTHFifj5XpSb2s7fKXkbT1ZkOjbVpbR7er3TPiFxQsdpipnDqOEjUwk49OXw0na3AEb8P16ws20YbUqOPRsyyxkVWjJZd3Y3pF5TtyNG; ANTICSRF=efd1c44ecc21e1ec3908ed2a16533ebf; MUSIC_EMAIL_U=889047663c2cf0101e561f2696e9bc471a76b2fa248a2b851d15bf53bcd42dbe59b226928335b3c0993166e004087dd32936171bd29c4b4e49faca7a4a782ca1d1fec5d8e70cd56a85a4bfe96bed3d90090f3ad7c86ad1db; BOX_DISABLE=true; playliststatus=visible; NTES_PC_EMAIL_IP=临沂|山东; JSESSIONID-WYYY=j+b19rRAu7n54snTEXUXthHwjpoMb7HSUtqYdbGW/\MeMB1YYdep3oVsiWagPhj6ar4BdcM1Fg5lA7AUlZ5y+NmnqUVrCT2fvl+j08sjpBR0zXAAl0VQCSIECCAatM4XMGBdd2\q0fMrlCbeTI3F75BewuB90Fz2V\zGpWfJZ7XRJ5lR:1679068747193; _iuqxldmzr_=33; WM_NI=CV2vOp9z+mTvAskQcl/SPIcnC7cdebBNvZQy+XhB+XcLZqCI8GWMIdL6a6bYig2+9jJ8NEcSjWrmgP0ZuNUFS23hN0MNbr9U5oocn6yT9VoWNseE546i6WZGqW+G7IuCVWc=; WM_NIKE=9ca17ae2e6ffcda170e2e6ee87c84390b5afa4e53d989a8ba2c55f829a8eb0c86b8deb9fb9f65aaeeab7a6d92af0fea7c3b92a818afe97ce7cfba6e58ed77e83ada5b2e268ed8da0aae26681e9ad85e86a8292babbd473e988a8a3aa54a1949692c243fc9999aecc7090eaafd7e153abb9feccbc628ae882a6e259aa89be8ee65cf486bbafd84e91eefd89cd3c8f92ae93bc5ff7b1a184ed3ebb8cf7b7ee5d8eadaba6b840f6b7fab8d94db389e5a8b643b79d9ab8e237e2a3; gdxidpyhxdE=UkMB9gJ0WbW5BIbUgmICnsxkxyuaa2rv5\MuZhPNutstd9fJX2Go/8UfwqM6OLaih9qCP3bWrgbREpT8m//7tw2HMotiHdZ1J6ouQprHLqTL/3GhrrOBwrGHBzQRRklH8Bj43OTwokmg37pT24f53l0zHx/nVU\AVvHICJTcnhQzGAqw:1679068209576; YD00000558929251:WM_NI=qacGfPFsarBvAMAVKGQRwOCJGcjb07jA9/HMiy8GXBEgKNEPLjwXyL/NLDigrQQSrwWVhPTQ54BfnaRZTluT393CDxGrIDBWGLJ/WFovbPrn56eQFR7YLkE+j04yJQpiWW4=; YD00000558929251:WM_NIKE=9ca17ae2e6ffcda170e2e6ee95cc62f3ecfa97b452aeeb8bb6c55b929a9e87d45ca3b09bb4f06afb94a79ad82af0fea7c3b92ab3bfada8e55c86adaf93c17e83938fb7ca4d938eb9b0c24285bda683b33daa9ff7d0cb47aba7f8a8db4a87b985afc85c90b6b9b9fc48ed9284a5ec6db28f9fb4f17d958aa8b1d75bf7ec8e87ed6b92869c8df860f1e7fda4c77485ae87a5c15d859486d0d64eadaaaeb1f166f7eaabb2c55af587848cc821aaf0fc9ac95bb4b799b8b737e2a3; NTES_P_UTID=y9BhNdv7VonlQL5KOJkHOVzoSyBkCO0L|1679067317; NTES_SESS=13o9WcHLO2ABXXv3UdiTcMV8b3GU3eK2OcyHoA2EPREGuWdmu57zsxG14EwTqdUf2kw2.t82yIjQcdCbjqnjWiY7gJC60aP85qii6MsO97FPf_sG9wr9c3wT4udaOdygb06gqGCXFixacBWlJQdFKJ7ILk8lfn.XX_8FeMVaNkm_OXz2vcpe978QVN.7bSCa8Amou1Myz9.Gx; S_INFO=1679067317|0|3&80##|kanwenhao12; P_INFO=kanwenhao12@163.com|1679067317|0|music|00&99|shd&1678755494&mail163#shd&371300#10#0#0|&0|mail163|kanwenhao12@163.com; __csrf=ba31dd997365e18fd7864f87e159200d; MUSIC_U=e7ef0ba18c1cb123fc1ffd6de43ade951d15bf53bcd42dbed1cb995c02225668993166e004087dd37524949792d07c044f5f2482650e811fcffde9b69b82d136f25f00679dd015cfd4dbf082a8813684".encode("utf-8").decode("latin1"),
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
        "referer":"https://music.163.com/my/"
        }
    
    # 歌单的表单数据
    data={
        "params":params,
        "encSecKey":encSecKey
        }
    
    # 使用post()方法请求歌单
    response=post(url=url,headers=headers,data=data).text
    
    # 在歌单信息中获取歌单名称作为存放歌曲的文件夹
    path=findall('"name":"(.*?)","coverImgId',response)[0]+"\\"
    
    # 在歌单信息中获取音乐名称及id
    name_and_id=findall('{"name":"(.*?)","id":(\d+),"pst":0,"t":0,"ar":.*?}',response)
    
    #计算歌曲数目
    len_ = len(name_and_id)
    
    # 将文件夹名称、歌曲名称和id、歌曲数目返回
    return path, name_and_id, len_


# 获取跳转地址
def get_url(path,name,id):
    
    # 一个“固定链接”,可用于获取歌曲跳转后的链接
    url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(id)
    
    # 使用get()方法请求“固定链接”,获取跳转后的链接
    r = get(url, allow_redirects=False)
    mp3_url=r.headers['Location']
    
    # 检查跳转后的链接是否为404链接
    # (一)若不是，则开始下载歌曲
    if mp3_url != "http://music.163.com/404":

        # 输出内容"歌曲正在下载"
        print('"{}"正在下载'.format(name))
        
        # 创建.mp3文件
        with open(path+name+'.mp3',mode='wb')as f:

            #使用get()方法获取歌曲的内容    
            music_data=get(url=mp3_url).content
            
            # 将歌曲的内容写入.mp3文件
            f.write(music_data)

            # 退出保存.mp3文件
            f.close()

        # 输出内容"歌曲下载完成"
        print('"{}"下载完成'.format(name))
        
        # 歌曲正常下载,使跳转后链接为404链接的歌曲名称为空
        error_name=''

    # (二)若跳转后的链接为404链接
    elif mp3_url == "http://music.163.com/404":

        # 记录此歌曲名称
        error_name=name

    # 将跳转后链接为404链接的歌曲名称返回
    return error_name
    
    
#启动程序
if __name__=="__main__":

    # 手动数入参数,跳过加密
    params=input("params:")
    encSecKey=input("encSecKey:")

    # 调用id_list()方法并接收id_list()方法返回的文件夹名称、歌曲名称和id、歌曲数目
    path,name_and_id,len_ = id_list(params=params,encSecKey=encSecKey)
    
    # 使用exists()方法检查是否存在名为歌曲名称的文件夹
    # (一)若不存在此文件夹
    if not exists(path=path):
        
        # 创建此文件夹
        mkdir(path=path)

    # (二)若存在此文件夹
    else:
    
        # 跳过
        pass

    # 输出歌曲数量
    print("共{}首歌曲".format(len_))

    # 创建空列表,用于存放跳转后链接为404链接的歌曲名称
    error_list=[]

    # 将歌曲名称与id逐个获取
    for i in name_and_id:

        # 获取歌曲的名称和id
        name,id=i

        # 换行,保持输出内容的整洁性
        print("\n")

        # 调用get_url()方法并接收跳转后链接为404链接的歌曲名称
        error_name=get_url(path=path,name=name,id=id)

        # 判断跳转后链接为404链接的歌曲名称是否为空
        # (一)若跳转后链接为404链接的歌曲名称为空
        if error_name=='':
            
            # 跳过
            pass

        # (二)若跳转后链接为404链接的歌曲名称不为空
        elif error_name != '':

            # 将若跳转后链接为404链接的歌曲名称存入列表
            error_list+=[error_name]
    
    #输出存放跳转后链接为404链接的歌曲名称的列表
    print("有以下{}首歌曲下载失败,它们可能是无版权或黑胶限定\n{}".format(len(error_list),error_list))
