import re
import requests
import os
def path_name_id(url_):
    headers={
        "cookie":'kg_mid=45c4ed38927807372ce764d929994ef1; kg_dfid=3x7mNe1egszq3tW0DH3ctDDn; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1679101349; ACK_SERVER_10015={"list":[["gzlogin-user.kugou.com"]]}; KuGooRandom=66411679101394945; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1679101433',
        "referer": 'https://www.kugou.com/yy/html/special.html',
        "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41'
    }
    response=requests.get(url=url_,headers=headers).text
    path_=re.findall('<strong>&lt;(.*?)&gt; - 歌曲列表</strong>',response)[0]+"\\"
    name_id_=re.findall('<a title="(.*?)" hidefocus=".*?" href="https://www.kugou.com/mixsong/(.*?).html"',response)
    return path_,name_id_

def play_url(encode_album_audio_id_):
    url="https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19105951296850845607_1679101433039&dfid=3x7mNe1egszq3tW0DH3ctDDn&appid=1014&mid=45c4ed38927807372ce764d929994ef1&platid=4&encode_album_audio_id={}&_=1679101433045".format(encode_album_audio_id_)
    headers={
        'cookie':'kg_mid=45c4ed38927807372ce764d929994ef1; kg_dfid=3x7mNe1egszq3tW0DH3ctDDn; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1679101349; kg_mid_temp=45c4ed38927807372ce764d929994ef1; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1679101433',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41',
        'referer':'https://www.kugou.com/'
    }
    response = requests.get(url=url,headers=headers).text
    text=re.findall('play_url":"(.*?)","authors"',response)[0]
    play_url_=text.replace(r"\/","/")
    return play_url_

def download(path_,name_,play_url_):
    print('开始下载"{}"'.format(name_))
    with open(path_+name_+".mp3",mode='wb')as f:
        response=requests.get(url=play_url_).content
        f.write(response)
        f.close()
    print('下载完成"{}"'.format(name_))
    

if __name__ == "__main__":
    url_=input("歌单链接:\n")
    path_,name_id_=path_name_id(url_=url_)
    if not os.path.exists(path=path_):
        os.mkdir(path=path_)
    elif os.path.exists(path=path_):
        pass
    for i_ in name_id_:
        name_=i_[0]
        id_=i_[1]
        play_url_=play_url(encode_album_audio_id_=id_)
        print("\n")
        download(path_=path_,name_=name_,play_url_=play_url_)
