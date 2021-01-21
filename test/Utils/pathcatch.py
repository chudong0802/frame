#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
'''
@Descripttion:
@version:
@@Company: DCIT-SH
@Author: Jason Wu
@Date: 2020-06-19 22:50:18
@LastEditors: Jason Wu
@LastEditTime: 2020-06-19 23:49:05
'''

import sys
import ftplib
import socket
import datetime
from ftplib import FTP, error_perm
import os
import gzip
import tarfile
import shutil
from time import sleep
import serial
import serial.tools.list_ports
from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
import glob

# def ftppath():
#     tmp_path=os.path.join(base_name, "..", "data")
#     ##查找tmp-开头的文件路径名
#     tmp_dirs=glob.glob(os.path.join(tmp_path,'tmp-*'))
#     ## 获取路径中的文件名
#     ## 可通过os.path.split分割，可避免windows和linux的分隔符不同的问题
#     for tmp_dir in tmp_dirs:
#         file_name=os.path.split(tmp_dir)[-1]



def usp_up():
    cap = {
        "autoGrantPermissions": True,
        "platformName": "android",
        "deviceName": "whatever",
        "appActivity": ".MainActivity",
        "appPackage": "com.example.hyan6.pma_upgrade_app",
        "unicodeKeyboard": True
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', cap)
    sleep(3)
    # size_dict = driver.get_window_size()
    # x = size_dict.get('width')
    # y = size_dict.get('height')
    # x, y = get_size()
    # print(x, y)
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    add_action = MultiAction(driver)
    # 指定操作
    action1.press(x=20, y=1883).wait(1000).move_to(x=20, y=1000).wait(1000).release()
    action2.press(x=60, y=1883).wait(1000).move_to(x=60, y=1000).wait(1000).release()
    add_action.add(action1, action2)
    # 执行操作
    add_action.perform()
    driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button[1]").click()



def ftpconnect(host, port, username, password):
    ftp = FTP()
    ftp.set_debuglevel(0)
    try:
        ftp.connect(host, port)
        ftp.login(username, password)
    except (socket.error, socket.gaierror):
        print("ERROR: cannot connect [{}:{}]".format(host, port))
        return None
    except error_perm:
        print("ERROR: user Authentication failed")
        return None
    except:
        print("ERROR: Unknow")
        return None
    return ftp


# 下载文件，remotepath下载前的ftp的目标地址，localpath下载后的文件存放的本地目录
def downloadfile(ftp, remotepath, localpath, time_db):
    bufsize = 1024
    with open(localpath, 'wb') as fp:
        ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)


# 上传文件
# def uploadfile(ftp, remotepath, localpath):
#     bufsize = 1024
#     with open(localpath, 'rb') as fp:
#         ftp.storbinary('STOR ' + remotepath, fp, bufsize)


# 文件解压，file_name文件存放路径及文件名，imgpath存放路径
def unzip(file_name, imgpath):
    # 获取文件的名称，去掉后缀名
    f_name = file_name.replace(".gz", "")
    # 开始解压gz文件
    g_file = gzip.GzipFile(file_name)
    # 读取解压后的文件，并写入去掉后缀名的同名文件（即得到解压后的文件）
    open(f_name, "wb+").write(g_file.read())
    g_file.close()
    # 开始解压tar文件
    tar = tarfile.open(f_name, 'r')
    tar.extractall(path=imgpath)
    tar.close()

def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(r'/x')[1:]]])


def portlist():
    plist = list(serial.tools.list_ports.comports())

    if len(plist) <= 0:
        print("The Serial port can't find!")
    else:
        plist_0 = list(plist[0])
        serialName = plist_0[0]
        serialFd = serial.Serial(serialName, 115200, timeout=60)
        print("check which port was really used >", serialFd.name)
        return serialFd.name

# def com():
#     ser=serial.Serial()
#     i=1
#     while i<10:
#         name='COM'+str(i)
#         ser.open
#         try:
#             ser.is_open
#             ser = serial.Serial(name)
#             ser.baudrate=9600
#             print(name)
#             return name
#         except serial.serialutil.SerialException:
#             pass
#         i+=1

def readport():
    try:
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        portx = "COM6"

        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = 115200

        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        timex = None

        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)
        print("串口详情参数：", ser)

        # # 十六进制的发送
        # result = ser.write(chr(0x06).encode("utf-8")) # 写数据
        # print("写总字节数：", result)

        # 十六进制的读取
        print(ser.read().hex())  # 读一个字节

        print("----------")
        ser.close()  # 关闭串口

    except Exception as e:
        print("error!", e)


def portwrite(port, bps):
    try:
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        portx = port

        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = bps

        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        timex = 5

        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)

        # 写数据
        result = ser.write("HELLO WORLD".encode("gbk"))
        print("写总字节数：", result)

        ser.close()  # 关闭串口

    except Exception as e:
        print("error!", e)


def portwrite16(port, bps, arg):
    try:
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        portx = port

        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = bps

        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        timex = 10

        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)

        # 写数据
        result = ser.write(arg)
        # print(ser.read(6).hex())
        print("写总字节数：", result)
        if ser.read(6).hex() == '3a0602030106':
            print("Successful")
        else:
            print("Failed")

        ser.close()  # 关闭串口

    except Exception as e:
        print("error!", e)


def portpower16(port, bps, arg):
    try:
        # 端口：CNU； Linux上的/dev /ttyUSB0等； windows上的COM3等
        portx = port

        # 波特率，标准值有：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
        bps = bps

        # 超时设置，None：永远等待操作；
        #         0：立即返回请求结果；
        #        其他：等待超时时间（单位为秒）
        timex = 10

        # 打开串口，并得到串口对象
        ser = serial.Serial(portx, bps, timeout=timex)

        # 写数据
        result = ser.write(arg)
        print("写总字节数：", result)
        print(ser.read(6).hex())
        if ser.read(6).hex() == '3a0602040107':
            print("Successful")
        else:
            print("Failed")

        ser.close()  # 关闭串口

    except Exception as e:
        print("error!", e)



if __name__ == "__main__":
    # config = configparser.ConfigParser()  # 注意大小写
    # config.read(filenames="imgPath.ini")0x17
    # print(config.sections())
    # weekly_path = config.get('path', 'weeklyPath')
    # config.read('config.ini')
    # print(config.get('', 'weeklyPath'))
    # port = portlist()
    port = "/dev/ttyUSB0"
    bps = 115200  # 设定波特率
    usb_power_on = [0x3C, 0x08, 0x01, 0x03, 0x02, 0x01, 0x02, 0x09]
    usb_power_off = [0x3C, 0x08, 0x01, 0x03, 0x02, 0x01, 0x00, 0x07]
    connect_pc = [0x3C, 0x07, 0x01, 0x03, 0x03, 0x12, 0x19]
    connect_usb_2 = [0x3C, 0x07, 0x01, 0x03, 0x01, 0x12, 0x17]
    connect_usb_1 = [0x3C, 0x07, 0x01, 0x03, 0x03, 0x11, 0x18]
    usb_switch_check = [0x3A, 0x06, 0x02, 0x03, 0x01, 0x06]  # 3a0602030106
    power_on = [0x3C, 0x08, 0x01, 0x04, 0x03, 0x02, 0x01, 0x0B]
    power_off = [0x3C, 0x08, 0x01, 0x04, 0x03, 0x02, 0x00, 0x0A]
    power_check = [0x3A, 0x06, 0x02, 0x04, 0x01, 0x07]  # 3a0602040107
    # portwrite16(port, bps, arg=usb_power_off)
    # sleep(2)
    # portwrite16(port, bps, arg=usb_power_on)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_pc)
    # print('J is ready！')
    # sleep(3)
    time = datetime.datetime.now().strftime("%Y-%m-%d")
    local_path = "/home/shileiwu/build/UsbBuild/gin-userdebug-img.tar.gz"
    # remote_path_0 = "/idcm-release/dailybuild/gin-dev/" + time + "-04-13-00/gin-userdebug-img.tar.gz"
    remote_path_0 = "/idcm-release/dailybuild/gin-dev/"
    remote_path_1 = "/idcm-release/dailybuild/gin-dev/" + time + "-04-00-00/gin-userdebug-img.tar.gz"
    # weekly_path = '/idcm-release/verifybuild/gin-dev-20200523/2020-06-03-15-12-49/gin-userdebug-img.tar.gz'
    if os.path.exists(local_path):
        os.remove(local_path)
    ftp = ftpconnect("10.18.34.24", 21, "idcmftp", "Hryt@123")
    remote_path_2= ftp.nlst("/idcm-release/dailybuild/gin-dev/")[-1]
    try:
        downloadfile(ftp, remote_path_2 + '/gin-userdebug-img.tar.gz', local_path,time)
    except ftplib.error_perm:
        downloadfile(ftp, remote_path_2 + '/gin-userdebug-fullbuild-img.tar.gz', local_path,time)
    ftp.quit()
    unzip('/home/shileiwu/build/UsbBuild/gin-userdebug-img.tar.gz', '/home/shileiwu/build/UsbBuild')
    os.system('simg2img /home/shileiwu/build/UsbBuild/system.img /home/shileiwu/build/UsbBuild/la_system.img')
    os.system('simg2img /home/shileiwu/build/UsbBuild/vendor.img /home/shileiwu/build/UsbBuild/la_vendor.img')
    # shutil.copy('/home/shileiwu/build/UsbBuild/la_system.img', '/media/shileiwu/J/UpdatePackage/ARM/la_system.img')
    # shutil.copy('/home/shileiwu/build/UsbBuild/la_vendor.img', '/media/shileiwu/J/UpdatePackage/ARM/la_vendor.img')
    # sleep(10)
    # portwrite16(port, bps, arg=connect_usb_1)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_usb_2)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_usb_1)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_usb_2)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_usb_1)
    # sleep(2)
    # portwrite16(port, bps, arg=connect_usb_2)
    # sleep(2)
    # print('switch to IDCM')
    # usp_up()
    # sleep(2400)



