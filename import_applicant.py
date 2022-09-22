# Author ： whb
# 开发时间 : 2022/9/21 15:57

import requests
import pandas as pd
import urllib
import datetime


def import_applicant_from_excel(file_name):
    """
    通过excel导入递交入党申请书的同学的数据
    因为系统时间的设置只能设最近，所以先填当天的时间，导入数据，后面再改
    :param file_name: 导入的excel文件路径，需要按模板,第一行列名，分别为党支部(2)，学号，姓名，时间(yyyy-mm-dd)
    :return:
    """
    df = pd.read_excel(file_name)  # 默认读取sheet = 0的

    students = []

    for row in df.index.values:
        students.append({
            "zhibuhao": df.iloc[row, 0],
            "stNo": str(df.iloc[row, 1]),
            "name": str(df.iloc[row, 2]),
            "zhengzhimianmao": "仅递交申请书",
            "shenqingshijian": datetime.date.today(),  # 先填当天时间
            "submit": "保存备案"
        })

    print(f"文件 {file_name} 共有 {len(students)} 数据：")
    print(students)
    print("============================")
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42',
    }

    i = 1
    for student in students:
        data = urllib.parse.urlencode(student, encoding='gb2312')
        print(f'{i} : {student["name"]}的请求表单数据： {data}')
        # 返回好像是个页面，错误似乎只会在页面提示，这里没做判断，后面得自己检查是否导入完毕（是否有学号和名字错误导致没输进去的情况）
        response = requests.post('http://ygxxgcxy.whu.edu.cn/rssims/rssims_st_dangtuan/st_dijiaoshenqingshu_dengji.php',
                                 headers=headers, data=data, verify=False)
        print(response)
        i += 1


def update_applicant_time(file_name):
    """
    修改数据的申请书时间
    :param file_name: 导入的excel文件路径，需要按模板,第一行列名，分别为党支部(2)，学号，姓名，时间(yyyy-mm-dd)
    :return:
    """
    df = pd.read_excel(file_name, keep_default_na=False)  # 默认读取sheet = 0的,将空的地方读取为空字符而不是NAN

    students = []

    # 这里的数据都是本科生，所以直接搞的本科生第几党支部，新录入的没啥数据，只需要几个参数，其他的需要填完整，不然会全部置空了
    for row in df.index.values:
        students.append({
            "stNo": str(df.iloc[row, 1]),
            "name": str(df.iloc[row, 2]),
            "dangzhibu": f'本科生第{df.iloc[row, 0]}党支部',
            "zhengzhimianmao": "仅递交申请书",
            "shenqingshijian": str(df.iloc[row, 3])
        })

    print(f"文件 {file_name} 共有 {len(students)} 数据：")
    print(students)
    print("============================")
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': '',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42',
    }

    i = 1
    for student in students:
        data = urllib.parse.urlencode(student, encoding='gb2312')
        print(f'{i} : {student["name"]}的请求表单数据： {data}')
        # 修改信息的页面
        response = requests.post('http://ygxxgcxy.whu.edu.cn/rssims/rssims_st_dangtuan/st_rudang_edit_save.php',
                                 headers=headers, data=data, verify=False)
        print(response)
        i += 1


if __name__ == '__main__':
    file_name = r"C:\Users\A\Desktop\导入模板.xlsx"
    import_applicant_from_excel(file_name)
    print("导入新数据完成\n")
    update_applicant_time(file_name)
    print("修改申请书时间完成")
