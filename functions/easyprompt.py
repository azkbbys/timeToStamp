from time import strftime, localtime
def info(text:str, name:str='timeToStamp'):
    print('['+name+']','['+strftime("%H:%M:%S", localtime())+']','[\033[32mINFO\033[0m]',text,'')
def warn(text:str, name:str='timeToStamp'):
    print('['+name+']','['+strftime("%H:%M:%S", localtime())+']','[\033[33mWARN\033[0m]',text,'')
def error(text:str, name:str='timeToStamp'):
    print('['+name+']','['+strftime("%H:%M:%S", localtime())+']','[\033[31mERROR\033[0m]',text,'')
