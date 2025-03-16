from requests import get
import functions.info as info
def check() -> str:
    try:
        v=get('https://azkbbys.github.io/getversion/timeToStamp.txt')
    except:
        return '无法连接到更新服务器，请检查网络连接'
    else:
        if(v.status_code==200):
            if(v.text==info.version):
                return '已是最新版本'
            else:
                return '有新版本可用'+v.text
        else:
            return '无法连接到更新服务器，请检查网络连接'
if __name__ == '__main__':
    print(check())
    print(info.version)