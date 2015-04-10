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
    #SIZE = {}
    SIZE_CACHE=1024*1024
    DISK_INFO = ""
    DISK_INFO = os.statvfs(device_path)
    DISK_Free = (DISK_INFO.f_bavail * DISK_INFO.f_frsize)
    DISK_Total = (DISK_INFO.f_blocks * DISK_INFO.f_frsize)
    DISK_Use = (DISK_INFO.f_blocks - DISK_INFO.f_bfree) * DISK_INFO.f_frsize
    DISK_Usage = round(float(DISK_Use * 100) / float(DISK_Use + DISK_Free),1)
    DISK_Total = MB_TO_GB(float(DISK_Total)/SIZE_CACHE)
    DISK_Use = MB_TO_GB(float(DISK_Use)/SIZE_CACHE)
    DISK_Free = MB_TO_GB(float(DISK_Free)/SIZE_CACHE)
    return {
        'Total':DISK_Total,
        'Use':DISK_Use,
        'Free':DISK_Free,
        'Usage':[DISK_Usage,'%']
    }
    #return SIZE
def GETDISK():
    """
        获取磁盘名称，磁盘类型。
        返回值：
        1 文件不存在
        0 文件存在，并获取到了信息
    """
    DISK_INFO={}
    if not os.path.exists(DISK_CONF_FILE):
        return 1  
    with open(DISK_CONF_FILE) as f:
        data = f.readlines()
    for x in data:
        data1 = x.split()
        if data1[2].strip() in DIST_TYPE:
            #print data1
            DISK_INFO={}
            #GETDISK_SIZE(data1[1].strip())#,data1[0],data1[2]
    return 0
GETDISK()
