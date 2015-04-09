#!/usr/bin/env python
# coding=utf-8
import os,sys
DISK_CONF_FILE="/proc/mounts"
DIST_TYPE=['ext2','ext3','ext4','tmpfs']
def GETDISK_SIZE(device_path=""):
    """
    获取磁盘大小,使用率
    变量 device_path 是指定磁盘，如 /dev/sda1 
    字典SIZE 存放获取到得数据
    返回值:
        1 变量为空
        0 变量不为空，获取数据完成
        use% 计算
        int(round(float(used * 100) / float((used + free)))
    """
    if not device_path:
        return 1
    SIZE = {}
    DISK_INFO = ""
    DISK_INFO = os.statvfs("/boot")
    free = (DISK_INFO.f_bavail * DISK_INFO.f_frsize)
    total = (DISK_INFO.f_blocks * DISK_INFO.f_frsize)
    used = (DISK_INFO.f_blocks - DISK_INFO.f_bfree) * DISK_INFO.f_frsize
    usage = int(round(float(used * 100) / float(used + free)))
    return 0
def GETDISK():
    """
        获取磁盘名称，磁盘类型。
        返回值：
        1 文件不存在
        0 文件存在，并获取到了信息
    """
    if not os.path.exists(DISK_CONF_FILE):
        return 1  
    with open(DISK_CONF_FILE) as f:
        data = f.readlines()
    for x in data:
        data1 = x.split()
        if data1[2].strip() in DIST_TYPE:
            print data1[0],data1[2]
    return 0
#GETDISK()
GETDISK_SIZE("/dev/sda1")
