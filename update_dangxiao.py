# 更新党校结业时间
import pprint

import requests
import pandas as pd
import urllib
from lxml import etree


def get_student_rudang_information(student_num):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # Requests sorts cookies= alphabetically
        'Cookie': '',
        'Origin': 'http://ygxxgcxy.whu.edu.cn',
        'Referer': 'http://ygxxgcxy.whu.edu.cn/rssims/rssims_st_dangtuan/st_rudang_edit.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42',
    }

    data = f'xuehao={student_num}&xingming=&Submit=%B2%E9%D1%AF%D0%E8%D2%AA%D0%DE%B8%C4%B5%C4%D1%A7%C9%FA'

    response = requests.post('http://ygxxgcxy.whu.edu.cn/rssims/rssims_st_dangtuan/st_rudang_edit.php', headers=headers,
                             data=data, verify=False)
    response.encoding = 'gbk'
    tree = etree.HTML(response.text)

    stNo = tree.xpath('/html/body/form[2]/table[1]/tr[2]/td[1]/a')[0].text
    name = tree.xpath('/html/body/form[2]/table[1]/tr[2]/td[2]/input/@value')[0]
    dangzhibu = tree.xpath('/html/body/form[2]/table[1]/tr[2]/td[3]/select/option[1]')[0].text
    zhengzhimianmao = tree.xpath('/html/body/form[2]/table[1]/tr[2]/td[4]/select/option[1]')[0].text
    shenqingshijian = tree.xpath('/html/body/form[2]/table[1]/tr[5]/td[1]/input/@value')[0]
    quedingjijifenzishijian = tree.xpath('/html/body/form[2]/table[1]/tr[5]/td[2]/input/@value')[0]
    peiyangren1 = tree.xpath('/html/body/form[2]/table[1]/tr[5]/td[3]/input/@value')[0]
    peiyangren2 = tree.xpath('/html/body/form[2]/table[1]/tr[5]/td[4]/input/@value')[0]
    peiyangren3 = tree.xpath('/html/body/form[2]/table[1]/tr[5]/td[5]/input/@value')[0]
    peiyangren4 = tree.xpath('/html/body/form[2]/table[1]/tr[5]/td[6]/input/@value')[0]
    beizhu1 = tree.xpath('/html/body/form[2]/table[1]/tr[5]/td[7]/input/@value')[0]
    shangdangxiaoshijian = tree.xpath('/html/body/form[2]/table[1]/tr[8]/td[1]/input/@value')[0]
    dangxiaohegeshijian = tree.xpath('/html/body/form[2]/table[1]/tr[8]/td[2]/input/@value')[0]
    ifyouxiujieye = tree.xpath('/html/body/form[2]/table[1]/tr[8]/td[3]/select/option[1]')[0].text
    if ifyouxiujieye == None:  # 如果没上过党校这块是None，得置空，不然传参是None的字符串，请求最后会返回失败
        ifyouxiujieye = ''
    quedingfazhanduixiangshijian = tree.xpath('/html/body/form[2]/table[1]/tr[8]/td[4]/input/@value')[0]
    jieshaoren1 = tree.xpath('/html/body/form[2]/table[1]/tr[8]/td[5]/input/@value')[0]
    jieshaoren2 = tree.xpath('/html/body/form[2]/table[1]/tr[8]/td[6]/input/@value')[0]
    beizhu2 = tree.xpath('/html/body/form[2]/table[1]/tr[8]/td[7]/input/@value')[0]
    xishouyubeidangyuanshijian = tree.xpath('/html/body/form[2]/table[1]/tr[11]/td[1]/input/@value')[0]
    zhiyuanshubianhao = tree.xpath('/html/body/form[2]/table[1]/tr[11]/td[2]/input/@value')[0]
    peiyanglianxiren1 = tree.xpath('/html/body/form[2]/table[1]/tr[11]/td[3]/input/@value')[0]
    peiyanglianxiren2 = tree.xpath('/html/body/form[2]/table[1]/tr[11]/td[4]/input/@value')[0]
    peiyanglianxiren3 = tree.xpath('/html/body/form[2]/table[1]/tr[11]/td[5]/input/@value')[0]
    peiyanglianxiren4 = tree.xpath('/html/body/form[2]/table[1]/tr[11]/td[6]/input/@value')[0]
    zhuanzhengshijian = tree.xpath('/html/body/form[2]/table[1]/tr[11]/td[7]/input/@value')[0]
    beizhu3 = tree.xpath('/html/body/form[2]/table[1]/tr[11]/td[8]/input/@value')[0]

    student = {
        "stNo": stNo,
        "name": name,
        "dangzhibu": dangzhibu,
        "zhengzhimianmao": zhengzhimianmao,
        "shenqingshijian": shenqingshijian,
        "quedingjijifenzishijian": quedingjijifenzishijian,
        "peiyangren1": peiyangren1,
        "peiyangren2": peiyangren2,
        "peiyangren3": peiyangren3,
        "peiyangren4": peiyangren4,
        "beizhu1": beizhu1,
        "shangdangxiaoshijian": shangdangxiaoshijian,
        "dangxiaohegeshijian": dangxiaohegeshijian,
        "ifyouxiujieye": ifyouxiujieye,
        "quedingfazhanduixiangshijian": quedingfazhanduixiangshijian,
        "jieshaoren1": jieshaoren1,
        "jieshaoren2": jieshaoren2,
        "beizhu2": beizhu2,
        "xishouyubeidangyuanshijian": xishouyubeidangyuanshijian,
        "zhiyuanshubianhao": zhiyuanshubianhao,
        "peiyanglianxiren1": peiyanglianxiren1,
        "peiyanglianxiren2": peiyanglianxiren2,
        "peiyanglianxiren3": peiyanglianxiren3,
        "peiyanglianxiren4": peiyanglianxiren4,
        "zhuanzhengshijian": zhuanzhengshijian,
        "beizhu3": beizhu3,
        # "xuehao": stNo,
        # "xingming": name,
        # "EDIT": "确认修改"
    }

    return student


def update_dangxiao(file_name, sheet_name):
    """
    修改一项的时间
    :param file_name: 导入的excel文件路径，需要按模板
    :return:
    """
    df = pd.read_excel(file_name, sheet_name=sheet_name, keep_default_na=False)
    # , date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))

    students = []

    # 这里的数据都是本科生，所以直接搞的本科生第几党支部，新录入的没啥数据，只需要几个参数，其他的需要填完整，不然会全部置空了
    for row in df.index.values:
        stNo = df.iloc[row, 3]
        student = get_student_rudang_information(stNo)
        # 修改时间
        student['dangxiaohegeshijian'] = "2022-11-15"
        excellent = df.iloc[row, 7]
        student['zhengzhimianmao'] = '入党积极分子(党校优秀结业)' if excellent == '是' else '入党积极分子(党校合格结业)'
        student['ifyouxiujieye'] = excellent
        pprint.pprint(student)
        students.append(student)

    print(f"文件 {file_name} 共有 {len(students)} 数据：")
    print(students)
    print("============================")
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # Requests sorts cookies= alphabetically
        'Cookie': '',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    i = 1
    for student in students:
        data = urllib.parse.urlencode(student, encoding='gbk')
        print(f'{i} : {student["name"]}的请求表单数据： {data}')
        # 修改信息的页面
        response = requests.post('http://ygxxgcxy.whu.edu.cn/rssims/rssims_st_dangtuan/st_rudang_edit_save.php',
                                 headers=headers, data=data, verify=False)
        print("返回结果: ")
        print(response.text)
        i += 1


if __name__ == '__main__':
    file_name = r"C:\Users\Hongbo\Desktop\党校结业时间.xlsx"
    sheet_name = 'Sheet1'
    update_dangxiao(file_name, sheet_name)
    print("修改完成")
