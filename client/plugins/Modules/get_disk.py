#!/usr/bin/env python
# coding=utf-8
import os,sys
DISK_CONF_FILE="/proc/mounts"
DIST_TYPE=['ext2','ext3','ext4','tmpfs']
def MB_TO_GB(SIZE=0):
    """
    MB转GB 函数
    """
    if SIZE >= 1024: 
        return [round(SIZE / 1024,1),'GB']
    return [round(SIZE,1),'MB']
def GETDISK_SIZE(device_path=""):
    """
    获取磁盘大小,使用率
    变量 device_path 是指定磁盘，如 /dev/sda1 
    字典SIZE 存放获取到得数据
    返回值:
        1 变量为空
         变量不为空，获取数据完成
        use% 计算
        int(round(float(used * 100) / float((used + free)))
    """
    if not device_path:
        return 'error'
    SIZE_CACHE=1024*1024
    DISK_INFO = ""
    try:
        DISK_INFO = os.statvfs(device_path)
    except OSError,e:
        return "Error:%s" % e
    DISK_Free = (DISK_INFO.f_bavail * DISK_INFO.f_frsize)
    DISK_Total = (DISK_INFO.f_blocks * DISK_INFO.f_frsize)
    DISK_Use = (DISK_INFO.f_blocks - DISK_INFO.f_bfree) * DISK_INFO.f_frsize
    DISK_Usage = round(float(DISK_Use * 100) / float(DISK_Use + DISK_Free),1)
    DISK_Total = MB_TO_GB(float(DISK_Total)/SIZE_CACHE)
    DISK_Use = MB_TO_GB(float(DISK_Use)/SIZE_CACHE)
    DISK_Free = MB_TO_GB(float(DISK_Free)/SIZE_CACHE)
    DISK_IO_Total = DISK_INFO.f_files
    DISK_IO_Use =  DISK_INFO.f_files - DISK_INFO.f_ffree 
    DISK_IO_Free = DISK_INFO.f_ffree
    DISK_IO_Usage = round(float(DISK_IO_Use) / float(DISK_IO_Total) * 100,1)
    TMP_DISK = ({
        'DISK_Total':DISK_Total,
        'DISK_Use':DISK_Use,
        'DISK_Free':DISK_Free,
        'DISK_Usage':[DISK_Usage,'%']}
    ,{
        'DISK_IO_Total':DISK_IO_Total,
        'DISK_IO_Use':DISK_IO_Use,
        'DISK_IO_Free':DISK_IO_Free,
        'DISK_IO_Usage':DISK_IO_Usage
    })
    return TMP_DISK
def GETDISK():
    """
        获取磁盘名称，磁盘类型。
        返回值：
        1 文件不存在
        0 文件存在，并获取到了信息
    """
    DISK_INFO=[]
    if not os.path.exists(DISK_CONF_FILE):
        return 1  
    with open(DISK_CONF_FILE) as f:
        data = f.readlines()
    for x in data:
        data1 = x.split()
        if  data1[2].strip() in DIST_TYPE:
            DISK_INFO.append(tuple(data1[0:4]))
    return  DISK_INFO
def CHECK_DISK(device="aaa"):
    """
    0  正常
    1  未知
    2  警告
    3  危险

    """
    if not device:
        return "Error: is Device"
    partition = GETDISK()
    #print GETDISK_SIZE(partition[1])
    DISK_STATUS = {}
    for x in partition:
        DISK_Usage1 = GETDISK_SIZE(x[1])[0]
        DISK_Usage = DISK_Usage1['DISK_Usage']
        DISK_IO_Usage1 = GETDISK_SIZE(x[1])[1]
        DISK_IO_Usage = DISK_IO_Usage1['DISK_IO_Usage']
        if DISK_Usage[0] > 90 and DISK_Usage[0] < 100:  #DISK_IO_Usage > 90 and DISK_IO_Usage < 100:
            DISK_STATUS[x[0]]={
                'info':'space use 90%',
                'status':2,
                'disk_size':DISK_Usage1,
                'disk_io':DISK_IO_Usage1
            }
        elif DISK_Usage[0] >= 100: #or DISK_IO_Usage >= 100:
            DISK_STATUS[x[0]]={
                'info':'space use 100%',
                'status':3,
                'disk_size':DISK_Usage1,
                'disk_io':DISK_IO_Usage1
            }
        else:
            DISK_STATUS[x[0]]={
                'info':'space use OK',
                'status':0,
                'disk_size':DISK_Usage1,
                'disk_io':DISK_IO_Usage1
            }
    return DISK_STATUS
            #return 2
        #elif DISK_Usage[0] >= 100 or DISK_IO_Usage >= 100:
        #    return 3
        #else:
        #    return 0
    #a = GETDISK_SIZE('/')
#print 
print CHECK_DISK()
#sys.exit(CHECK_STATUS)
#GETDISK('/dev/sda1','ext4')
#print GETDISK_SIZE('/')
