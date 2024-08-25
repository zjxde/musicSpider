import re

import requests
import execjs
import json
import requests
import jsonpath
import os

from bs4 import BeautifulSoup

def sort_dict_val(song_dict:dict):
    swapped_dict = {v: k for k, v in song_dict.items()}
    print(swapped_dict)
    # 转换为列表，以便排序
    items = list(swapped_dict.items())

    # 根据值进行排序
    items.sort(key=lambda x: x[0])

    # 将排序后的列表转换回字典
    sorted_dict = dict(items)
    return sorted_dict

def handle_duplicate(song_dict:dict):
    songs = sort_dict_val(song_dict)
    print(songs)
    new_song_names = []
    new_songs = {}
    keys = list(songs.keys())
    new_keys = list(songs.keys())
    index = 0
    for key in keys:
        myindex = 0
        compare_song_name = keys[index]
        if compare_song_name:
            for key in new_keys:
                myindex += 1
                remove_song_name = new_keys[myindex]
                if remove_song_name.count(compare_song_name)>0:
                    if remove_song_name in songs:
                        songs.pop(remove_song_name)
                        keys.remove(remove_song_name)
                if myindex <= len(keys)-1:
                    index += 1
                    break



        #for item in song_dict.
    print(songs)
    return songs


def create_file_if_not_exists(file_path: str) -> None:
    """
    如果文件不存在，则创建一个新的空文件。
    如果文件已经存在，则不做任何操作。
    """
    try:
        with open(file_path, 'x',encoding='utf-8'):
            pass  # 文件被创建，但我们不需要在这里做任何操作
    except FileExistsError:
        print(f"文件 {file_path} 已经存在，不需要创建。")





def create_directory(path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            print(f"Directory '{path}' created successfully.")
        except OSError:
            print(f"Creation of the directory '{path}' failed.")
    else:
        print(f"Directory '{path}' already exists.")




headers = {
    "authority": "music.163.com",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://music.163.com",
    "pragma": "no-cache",
    "referer": "https://music.163.com/search/",
    "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}
cookies = {
    "mail_psc_fingerprint": "05e714a9b1cf5c7e2d861737beecd49e",
    "vjuids": "-be00373d.171976917cb.0.7bd4a9f5d9312",
    "vjlast": "1587383179.1587383179.30",
    "mp_MA-91DF-2127272A00D5_hubble": "%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fsf.163.com%2Fzonghe%2Fsolution%3Fopener%3Dhttps%253A%252F%252Fwww.163yun.com%252F%3Ftag%3DM_zhihu_39907719%22%2C%22updatedTime%22%3A%201653661485937%2C%22sessionStartTime%22%3A%201653661470235%2C%22sendNumClass%22%3A%20%7B%22allNum%22%3A%203%2C%22errSendNum%22%3A%200%7D%2C%22deviceUdid%22%3A%20%22e6eca609ee3383f9c12df00e0cfe7aa50a339ab7%22%2C%22persistedTime%22%3A%201653661470226%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_hover%22%2C%22time%22%3A%201653661485937%7D%2C%22sessionUuid%22%3A%20%222eaf2976fbab92d544f99bed7752bff3c380f41b%22%7D",
    "P_INFO": "zjxdede3@126.com|1701328766|1|mail126|00&99|null&null&null#gud&440100#10#0#0|&0||zjxdede3@126.com",
    "NTES_SESS": "4U5j12AvKOcJ2gXqL2MJBidKdrpMQ3JPLGPmpDYK7UKxCIEACNjlM8Tz6xXLRBcv7xZ0aZn.l725GRuks9rc6SlwEw858XkoY5GuXKzmTPqNBYyzYLJZ8iDBYOh0g_l_bjm9ZjdQVi0DLhJfhKAcWmfb3m50RRHoCVyXJMEn3h7U1lhUe6Xp9n.VX5ookVNxxAlmxxyNlG.C1Jfb0pg8CzAOG",
    "S_INFO": "1720241621|1|#0&60#|zjxdede3@126.com",
    "ANTICSRF": "07574953007cdec91bc8537917cf89e3",
    "hb_MA-93D5-9AD06EA4329A_source": "www.google.com",
    "__root_domain_v": ".163.com",
    "_qddaz": "QD.800823468240823",
    "NMTID": "00OEZlXZVbs9x0JbEjcnjwYaKo93fsAAAGRg2vAKA",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "1e0aa7fb69f4abf15801b6988d7b8566,1724486759694",
    "_ntes_nuid": "1e0aa7fb69f4abf15801b6988d7b8566",
    "WEVNSM": "1.0.0",
    "WNMCID": "ebywkc.1724486763556.01.0",
    "sDeviceId": "YD-f%2F3Zs02HmpREU0BEAEfA1U2V4%2FrOpLg3",
    "__snaker__id": "iMAxyydgcKQjYA6O",
    "gdxidpyhxdE": "h4gCMifTl2pbGfKPE39QK4eWsnNDONI68CG9%2FNVBha3LI1B9i1PLIdxtKbAAQ756Au0dygUZP8E%2Bjz6kkmWpUf1M96BwM6qtyaCIsJplIna6cmyfIeh24bY8sdbzJUWcrKQYsm5fSojxj0RHEW%2FBe6btMI0hKWUCBzUTv%2BjlrEHQGWrH%3A1724488694901",
    "__csrf": "287b3a6e038e1ccc3e7f43c246ea5922",
    "MUSIC_U": "006BB78FF55541CBD0F75C6CCFCFAF1DC3ACCA6AC0DF26CFFD6125184BFA5D707A07A2AC71D46936910EB63E56F440F3D99325B7ECD4092C519C13E604A6231FE78BC86EB38ECEAAB0166E61CBCBDD553070B4D04A2D5024D46AD74994CF0C5FB93C92A8336D4E92B879C75F1F9011811C5CBCFEFDFCA64C253D5828337708E584C530C57379FEDED978CF620F360CEC38F60BE9E5982215E2EB560F9D64BEAE5DBA05EF764C66FD884041807BC9DC9EF7A94DE6180CDEF7D64DE67F6A09CEEB3FF28D031F4A1AB4690C4F25700F11B4AA50B0B677DEBCE638359B2664EE3E34750513F831F02861AFB0A404814E801EA51B17BFC34991344350BDB3BA666D7BC4D5025319014FB0C84159B696CF4BF877EBDC59ECC55D8AAADBE60123329E4C9A51E844023E714CF0511516BC43D3AFE6957429651BBEC41B5AEAC3F3A7F7C140B34FA488CA0A4CCBA144A16EE58A25F6A6764938F4E6C2381602357B32356065",
    "ntes_kaola_ad": "1",
    "playerid": "62513655",
    "ntes_utid": "tid._.tlQqRlvh9NZBEwEUAReCB9EPhF2hQQig._.0",
    "WM_NI": "Ihe6CD%2BOLxU4gvWg6c2jiKyhpnDluKDortVwcyD6WgmOhIyk4xv0Ey%2BsG%2BJVDP5ky0j4MzSA7Os2xB4TG7TKpdm41VzSfvsM3WpbP5GEkS5zqP84sNoJhuTzjuZowLAyajY%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eea2b2508790a0ccee6ef3a88fb6d15e869f8f86d64ffc8b858dd872bc8a99b8d32af0fea7c3b92a8bb8abd7c250e9918499d840a5aa9988b569f2b6a7acfc64b4b28c8df84188b1be95d57da1a78cd7d66daf91a8aafc61f8a8bad1c873e9ad89ccc95e8890fb8cfc3caaec839bd24bf591bdd3fb4af88c89d8d741b4bca3d5b45eba8daa97f247f189c083d33f859ba5b4b872b390f8d5f246ad96a896d772aaab9690f64883a7af8bdc37e2a3",
    "WM_TID": "vyZLNij5HTxFAARFREaDApFbgFmxECGa",
    "JSESSIONID-WYYY": "13qKUst0BUtwvXj4KbGJWrehbc2zpiKvY%2FeniHQgQNtF0%2BaR9Zasgropf9oIlNax9TPR84Snti3iUhtoHQJUmy%2BFHJj%5CI%2BqvZYrcF5hmD4pS%2Bc7nrT0oXBvjqVAkV0NUh%2BUz90m90S0k2cgpxmjYkl6qMvz0n0b%5C5JCbfiPuE1GT%2F3jo%3A1724515238652"
}
url = "https://music.163.com/weapi/cloudsearch/get/web"
singer = '蔡依林'
# 使用例子
#create_file_if_not_exists(singer)
# 使用函数创建文件夹
dir = 'music/'+singer
create_directory(dir)
params = {
    "csrf_token": "287b3a6e038e1ccc3e7f43c246ea5922"
}
offset = 0
show_total = True
limit = 30
d = {"hlpretag":"<span class=\"s-fc7\">","hlposttag":"</span>","#/discover/artist":"","s":singer,"type":"1","offset":offset,"total":show_total,"limit":limit,"csrf_token":"287b3a6e038e1ccc3e7f43c246ea5922"}
aa = "010001"
bb = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
cc = "0CoJUm6Qyw8W8jud"
with open('list.js',encoding='utf-8') as f:
    js_code = f.read()

pp = execjs.compile(js_code).call("get_enc_param",json.dumps(d))
data = {
    "params": pp['encText'],
    "encSecKey": pp['encSecKey']
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
total = jsonpath.jsonpath(response.json(),'$..songCount')[0]
id_list = jsonpath.jsonpath(response.json(),'$..songs[*].id')
name_list = jsonpath.jsonpath(response.json(),'$..songs[*].name')
songlist = dict(zip(id_list, name_list))
mylist = None
while offset <= total:
    offset += limit
    show_total = False
    d = {"hlpretag":"<span class=\"s-fc7\">","hlposttag":"</span>","#/discover/artist":"","s":singer,"type":"1","offset":offset,"total":show_total,"limit":limit,"csrf_token":"287b3a6e038e1ccc3e7f43c246ea5922"}
    pp = execjs.compile(js_code).call("get_enc_param", json.dumps(d))
    data = {
        "params": pp['encText'],
        "encSecKey": pp['encSecKey']
    }
    response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
    new_id_list = jsonpath.jsonpath(response.json(), '$..songs[*].id')
    new_name_list = jsonpath.jsonpath(response.json(), '$..songs[*].name')
    if new_id_list and len(new_id_list)>0:
        id_list.extend(new_id_list)
    if new_name_list and len(new_name_list)>0:
        name_list.extend(new_name_list)
        newsonglist = dict(zip(new_id_list, new_name_list))
        mylist = {**songlist,**newsonglist}
    songlist = mylist
#
print(id_list)
print(name_list)
songlist = mylist
print(songlist)

new_dict = handle_duplicate(songlist)
swapped_dict = {v: k for k, v in new_dict.items()}
print(swapped_dict)
# 转换为列表，以便排序
songlist = swapped_dict



cookies = {
    "mail_psc_fingerprint": "05e714a9b1cf5c7e2d861737beecd49e",
    "vjuids": "-be00373d.171976917cb.0.7bd4a9f5d9312",
    "vjlast": "1587383179.1587383179.30",
    "mp_MA-91DF-2127272A00D5_hubble": "^%^7B^%^22sessionReferrer^%^22^%^3A^%^20^%^22https^%^3A^%^2F^%^2Fsf.163.com^%^2Fzonghe^%^2Fsolution^%^3Fopener^%^3Dhttps^%^253A^%^252F^%^252Fwww.163yun.com^%^252F^%^3Ftag^%^3DM_zhihu_39907719^%^22^%^2C^%^22updatedTime^%^22^%^3A^%^201653661485937^%^2C^%^22sessionStartTime^%^22^%^3A^%^201653661470235^%^2C^%^22sendNumClass^%^22^%^3A^%^20^%^7B^%^22allNum^%^22^%^3A^%^203^%^2C^%^22errSendNum^%^22^%^3A^%^200^%^7D^%^2C^%^22deviceUdid^%^22^%^3A^%^20^%^22e6eca609ee3383f9c12df00e0cfe7aa50a339ab7^%^22^%^2C^%^22persistedTime^%^22^%^3A^%^201653661470226^%^2C^%^22LASTEVENT^%^22^%^3A^%^20^%^7B^%^22eventId^%^22^%^3A^%^20^%^22da_hover^%^22^%^2C^%^22time^%^22^%^3A^%^201653661485937^%^7D^%^2C^%^22sessionUuid^%^22^%^3A^%^20^%^222eaf2976fbab92d544f99bed7752bff3c380f41b^%^22^%^7D",
    "P_INFO": "zjxdede3^@126.com^|1701328766^|1^|mail126^|00&99^|null&null&null^#gud&440100^#10^#0^#0^|&0^|^|zjxdede3^@126.com",
    "NTES_SESS": "4U5j12AvKOcJ2gXqL2MJBidKdrpMQ3JPLGPmpDYK7UKxCIEACNjlM8Tz6xXLRBcv7xZ0aZn.l725GRuks9rc6SlwEw858XkoY5GuXKzmTPqNBYyzYLJZ8iDBYOh0g_l_bjm9ZjdQVi0DLhJfhKAcWmfb3m50RRHoCVyXJMEn3h7U1lhUe6Xp9n.VX5ookVNxxAlmxxyNlG.C1Jfb0pg8CzAOG",
    "S_INFO": "1720241621^|1^|^#0&60^#^|zjxdede3^@126.com",
    "ANTICSRF": "07574953007cdec91bc8537917cf89e3",
    "hb_MA-93D5-9AD06EA4329A_source": "www.google.com",
    "__root_domain_v": ".163.com",
    "_qddaz": "QD.800823468240823",
    "NMTID": "00OEZlXZVbs9x0JbEjcnjwYaKo93fsAAAGRg2vAKA",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "1e0aa7fb69f4abf15801b6988d7b8566,1724486759694",
    "_ntes_nuid": "1e0aa7fb69f4abf15801b6988d7b8566",
    "WEVNSM": "1.0.0",
    "WNMCID": "ebywkc.1724486763556.01.0",
    "sDeviceId": "YD-f^%^2F3Zs02HmpREU0BEAEfA1U2V4^%^2FrOpLg3",
    "__snaker__id": "iMAxyydgcKQjYA6O",
    "gdxidpyhxdE": "h4gCMifTl2pbGfKPE39QK4eWsnNDONI68CG9^%^2FNVBha3LI1B9i1PLIdxtKbAAQ756Au0dygUZP8E^%^2Bjz6kkmWpUf1M96BwM6qtyaCIsJplIna6cmyfIeh24bY8sdbzJUWcrKQYsm5fSojxj0RHEW^%^2FBe6btMI0hKWUCBzUTv^%^2BjlrEHQGWrH^%^3A1724488694901",
    "__csrf": "287b3a6e038e1ccc3e7f43c246ea5922",
    "MUSIC_U": "006BB78FF55541CBD0F75C6CCFCFAF1DC3ACCA6AC0DF26CFFD6125184BFA5D707A07A2AC71D46936910EB63E56F440F3D99325B7ECD4092C519C13E604A6231FE78BC86EB38ECEAAB0166E61CBCBDD553070B4D04A2D5024D46AD74994CF0C5FB93C92A8336D4E92B879C75F1F9011811C5CBCFEFDFCA64C253D5828337708E584C530C57379FEDED978CF620F360CEC38F60BE9E5982215E2EB560F9D64BEAE5DBA05EF764C66FD884041807BC9DC9EF7A94DE6180CDEF7D64DE67F6A09CEEB3FF28D031F4A1AB4690C4F25700F11B4AA50B0B677DEBCE638359B2664EE3E34750513F831F02861AFB0A404814E801EA51B17BFC34991344350BDB3BA666D7BC4D5025319014FB0C84159B696CF4BF877EBDC59ECC55D8AAADBE60123329E4C9A51E844023E714CF0511516BC43D3AFE6957429651BBEC41B5AEAC3F3A7F7C140B34FA488CA0A4CCBA144A16EE58A25F6A6764938F4E6C2381602357B32356065",
    "ntes_kaola_ad": "1",
    "ntes_utid": "tid._.tlQqRlvh9NZBEwEUAReCB9EPhF2hQQig._.0",
    "WM_NI": "Ihe6CD^%^2BOLxU4gvWg6c2jiKyhpnDluKDortVwcyD6WgmOhIyk4xv0Ey^%^2BsG^%^2BJVDP5ky0j4MzSA7Os2xB4TG7TKpdm41VzSfvsM3WpbP5GEkS5zqP84sNoJhuTzjuZowLAyajY^%^3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6eea2b2508790a0ccee6ef3a88fb6d15e869f8f86d64ffc8b858dd872bc8a99b8d32af0fea7c3b92a8bb8abd7c250e9918499d840a5aa9988b569f2b6a7acfc64b4b28c8df84188b1be95d57da1a78cd7d66daf91a8aafc61f8a8bad1c873e9ad89ccc95e8890fb8cfc3caaec839bd24bf591bdd3fb4af88c89d8d741b4bca3d5b45eba8daa97f247f189c083d33f859ba5b4b872b390f8d5f246ad96a896d772aaab9690f64883a7af8bdc37e2a3",
    "WM_TID": "vyZLNij5HTxFAARFREaDApFbgFmxECGa",
    "JSESSIONID-WYYY": "MvOO19^%^2FdSINZT26GVRO1AVkr2T3fCuQom6GfBnb2nEW2NVT5y^%^2BG76OMF1dqoY2hhwpC9tVA3WwhuP^%^2Fk7kkxZ376w2hh3Kk2GNZ^%^2B8Z^%^2BO60IXg3VW5GvmRku89RSdlEBd6YF9TXizoNIMDhukWjvo^%^5CxX5^%^2B6WrCgYZpHWeNdUjeZ4N^%^2F0ebi^%^3A1724521369883",
    "playerid": "28737391"
}

params = {
    "csrf_token": "287b3a6e038e1ccc3e7f43c246ea5922"
}

song_url = 'https://music.163.com/weapi/song/enhance/player/url/v1'
song_data = {"ids":id_list,"level":"standard","encodeType":"aac","csrf_token":"287b3a6e038e1ccc3e7f43c246ea5922"}

pp = execjs.compile(js_code).call("get_enc_param",json.dumps(song_data))
data = {
    "params": pp['encText'],
    "encSecKey": pp['encSecKey']
}
response = requests.post(song_url, headers=headers, cookies=cookies, params=params, data=data)
print("===================")
print(response.content)
urls = jsonpath.jsonpath(response.json(),'$.data[*].url')
ids = jsonpath.jsonpath(response.json(),'$.data[*].id')
for index,url in enumerate(urls):
    id = ids[index]
    if url:
        music_response = requests.get(url, headers=headers).content
        if id in songlist:
            songname = songlist[id].replace("/"," ").replace(" ", "").encode("utf-8").decode()
            str = re.sub('[^\u4e00-\u9fa5]+', '', songname)
            with open(dir+'/%s.mp3' % str, 'wb') as fp:
                fp.write(music_response)
                print('[%s]保存成功！' % songlist[id])
