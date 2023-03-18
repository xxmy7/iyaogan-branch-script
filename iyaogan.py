# -*- coding: utf-8 -*-

# # Author ： whb
# # 开发时间 : 2022/7/27 14:52

import requests
from lxml import etree
import pandas as pd

def get_students() -> list:
    headers = {
        'Cookie':'',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'http://ygxxgcxy.whu.edu.cn/iyaogan/iyaogan_left_menu_student.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    response = requests.get('http://ygxxgcxy.whu.edu.cn/iyaogan/iyaogan_stuser_chaxun/stuser_rudang_chaxun.php',
                            headers=headers, verify=False)
    response.encoding = 'gbk'
    tree = etree.HTML(response.text)
    table = tree.xpath('/html/body/font/table[2]')
    first = True
    students = []
    for tr in table[0].xpath('.//node()[self::tr]'):
        if first:
            first = False
            continue
        else:
            tds = tr.xpath('./node()[self::td]')
            ID2 = tds[1].text
            stNo = tds[4].text
            name = tds[5].text
            students.append({"name": name, "No": stNo, "id": ID2})

    return students


def get_students_rudang(id, stNo):
    headers = {
        'Cookie':'',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://ygxxgcxy.whu.edu.cn',
        'Referer': 'http://ygxxgcxy.whu.edu.cn/iyaogan/iyaogan_stuser_chaxun/stuser_rudang_chaxun.php',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    data = f'ID2={id}&stNo={stNo}&submit=%E4%AF%C0%C0'

    response = requests.post('http://ygxxgcxy.whu.edu.cn/iyaogan/iyaogan_stuser_chaxun/st_jijifenzi_preview.php',
                             headers=headers, data=data, verify=False)
    response.encoding='gbk'
    tree = etree.HTML(response.text)

    # region 基本信息
    No = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[1]/td[1]')[0].text
    ID = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[1]/td[2]')[0].text
    name = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[2]/td[1]')[0].text
    gender = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[2]/td[2]')[0].text
    identity = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[3]/td[1]')[0].text
    branch = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[3]/td[2]')[0].text
    birthday = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[4]/td[1]')[0].text
    nation = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[4]/td[2]')[0].text
    major = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[5]/td[1]')[0].text
    direction = tree.xpath('/html/body/table[3]/tr/td[1]/table/tr[5]/td[2]')[0].text
    # endregion

    # region 思想觉悟
    applydate = tree.xpath('/html/body/table[4]/tr/td/table/tr[1]/td')[0].text
    jijifenzidate = tree.xpath('/html/body/table[4]/tr/td/table/tr[2]/td')[0].text
    if len(tree.xpath('/html/body/table[4]/tr/td/table/tr[2]/td/font')) > 0:
        jijifenzidate += tree.xpath('/html/body/table[4]/tr/td/table/tr[2]/td/font')[0].text
    # endregion

    # region 理论水平
    mayuan_node = tree.xpath('/html/body/table[5]/tr/td/table/tr[1]/td')
    mayuan = mayuan_node[0].text
    if (len(mayuan_node[0].xpath('./node()[self::font]')) > 0):
        mayuan = mayuan_node[0].text + mayuan_node[0].xpath('./node()[self::font]')[0].text

    maogainode = tree.xpath('/html/body/table[5]/tr/td/table/tr[2]/td')
    maogai = maogainode[0].text
    if (len(maogainode[0].xpath('./node()[self::font]')) > 0):
        maogai = maogainode[0].text + maogainode[0].xpath('./node()[self::font]')[0].text

    xigainode = tree.xpath('/html/body/table[5]/tr/td/table/tr[3]/td')
    xigai = xigainode[0].text
    if (len(xigainode[0].xpath('./node()[self::font]')) > 0):
        xigai = xigainode[0].text + xigainode[0].xpath('./node()[self::font]')[0].text

    jindaishi_node = tree.xpath('/html/body/table[5]/tr/td/table/tr[4]/td')
    jindaishi = jindaishi_node[0].text
    if (len(jindaishi_node[0].xpath('./node()[self::font]')) > 0):
        jindaishi = jindaishi_node[0].text + jindaishi_node[0].xpath('./node()[self::font]')[0].text

    sixiu_node = tree.xpath('/html/body/table[5]/tr/td/table/tr[5]/td')
    sixiu = sixiu_node[0].text
    if (len(sixiu_node[0].xpath('./node()[self::font]')) > 0):
        sixiu = sixiu_node[0].text + sixiu_node[0].xpath('./node()[self::font]')[0].text

    xingce_node = tree.xpath('/html/body/table[5]/tr/td/table/tr[6]/td')
    xingce = xingce_node[0].text
    if (len(xingce_node[0].xpath('./node()[self::font]')) > 0):
        xingce = xingce_node[0].text + xingce_node[0].xpath('./node()[self::font]')[0].text

    average_node = tree.xpath('/html/body/table[5]/tr/td/table/tr[7]/td')
    average = average_node[0].text
    if (len(average_node[0].xpath('./node()[self::font]')) > 0):
        average = average_node[0].text + average_node[0].xpath('./node()[self::font]')[0].text

    dangxiao_node = tree.xpath('/html/body/table[5]/tr/td/table/tr[8]/td')
    dangxiao = dangxiao_node[0].text
    if (len(dangxiao_node[0].xpath('./node()[self::font]')) > 0):
        dangxiao = dangxiao_node[0].text + dangxiao_node[0].xpath('./node()[self::font]')[0].text
    # endregion

    # region 学习成绩
    gpa_node = tree.xpath('/html/body/table[6]/tr/td/table/tr[1]/td')
    each_gpa = gpa_node[0].text
    if (len(gpa_node[0].xpath('./node()[self::font]')) > 0):
        each_gpa += gpa_node[0].xpath('./node()[self::font]')[0].text
    gpa_flag = False
    GPA = ""
    for ch in each_gpa:
        if (ch == '>' or ch == '<'):
            gpa_flag = False
        if gpa_flag:
            GPA += ch
        if (ch == '前'):
            gpa_flag = True

    bujige_node = tree.xpath('/html/body/table[6]/tr/td/table/tr[2]/td')
    bujige = bujige_node[0].text
    if (len(bujige_node[0].xpath('./node()[self::font]')) > 0):
        bujige += bujige_node[0].xpath('./node()[self::font]')[0].text

    english = tree.xpath('/html/body/table[6]/tr/td/table/tr[3]/td')[0].text
    # endregion

    # region 宗旨意识
    former_work_node = tree.xpath('/html/body/table[7]/tr/td/table/tr[1]/td')
    former_work = former_work_node[0].text
    if (len(former_work_node[0].xpath('./node()[self::font]')) > 0):
        former_work += former_work_node[0].xpath('./node()[self::font]')[0].text

    present_work_node = tree.xpath('/html/body/table[7]/tr/td/table/tr[2]/td')
    present_work = present_work_node[0].text
    if (len(present_work_node[0].xpath('./node()[self::font]')) > 0):
        present_work += present_work_node[0].xpath('./node()[self::font]')[0].text

    volunteer_node = tree.xpath('/html/body/table[7]/tr/td/table/tr[3]/td')
    volunteer = volunteer_node[0].text
    if (len(volunteer_node[0].xpath('./node()[self::font]')) > 0):
        volunteer += volunteer_node[0].xpath('./node()[self::font]')[0].text

    # endregion

    # region群众基础
    tuiyou_node = tree.xpath('/html/body/table[8]/tr/td/table/tr[1]/td')
    tuiyou = tuiyou_node[0].text
    if (len(tuiyou_node[0].xpath('./node()[self::font]')) > 0):
        tuiyou += tuiyou_node[0].xpath('./node()[self::font]')[0].text
    # endregion

    # region 综合表现
    praise = tree.xpath('/html/body/table[9]/tr/td/table/tr[1]/td')[0].text
    criticism = tree.xpath('/html/body/table[9]/tr/td/table/tr[2]/td')[0].text
    award = tree.xpath('/html/body/table[9]/tr/td/table/tr[3]/td')[0].text
    punishment = tree.xpath('/html/body/table[9]/tr/td/table/tr[4]/td')[0].text

    # endregion

    person = {
        '学号': No,
        'ID': ID,
        '姓名': name,
        '性别': gender,
        '身份': identity,
        '所在团支部': branch,
        '出生日期': birthday,
        '民族': nation,
        '专业': major,
        '方向': direction,
        '申请书递交日期': applydate,
        '确定积极分子日期': jijifenzidate,
        '马原': mayuan,
        '毛概': maogai,
        '习概': xigai,
        '近代史': jindaishi,
        '思修': sixiu,
        '行策': xingce,
        '思政课平均成绩': average,
        '党校培训情况': dangxiao,
        'GPA各学期': each_gpa,
        'GPA': GPA,
        '不及格情况': bujige,
        '英语水平': english,
        '曾任社会工作': former_work,
        '现任社会工作': present_work,
        '参加志愿服务': volunteer,
        '团支部推优赞成率': tuiyou,
        '通报表扬': praise,
        '通报批评': criticism,
        '所获奖励': award,
        '所受处分': punishment
    }

    # 删除空格
    for k in person:
        if person[k] is None:   # 发现有的方向那一栏写的空，而不是未分方向，系统的问题，如果有空值就跳过
            continue
        person[k] = person[k].strip()
        person[k] = "".join(person[k].split())

    return person


if __name__ == '__main__':
    students = get_students()
    print('0查询支部所有人学号done')
    rudang_list = []
    for student in students:
        st = get_students_rudang(id=student['id'], stNo=student['No'])
        rudang_list.append(st)
    print('1查询每个人的数据done')
    df = pd.DataFrame(rudang_list)
    df.index = df.index + 1
    # print(df)
    df.to_excel("./test.xlsx")
    print('2保存数据done')
