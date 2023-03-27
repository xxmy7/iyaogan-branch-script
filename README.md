# iyaogan支部相关脚本

自用，不太会爬虫，还好iyaogan也比较简单hh

- `iyaogan.py`

​	dang支部信息爬取那个入党积极分子的表

1. `功能`: 用于查询支部所有人的入dang信息并保存进excel

2. `介绍`: 因为信息不太好直接看，此项目用于自用数据统计

---

- `import_applicant.py`

​	平台录入申请书的人的信息，初始化

1. `功能`: 用于将刚交申请书的人的信息通过excel录入

2. `介绍`: 因为只能手动添加，还有个确认框，不太方便，注意这个添加没有检查，需要最后导完检查是否导全了，系统有年龄检查，所以可能存在时间输错了，没插入的情况。
  
2. excel模板的格式如下：
  
  注意时间格式的需要
  
  | 党支部 | 学号          | 姓名 | 时间       |
  | ------ | ------------- | ---- | ---------- |
  | 2      | xxxxxxxxxxxxx | xxx  | 2022-09-22 |
  

---

- `update_information.py`

​	更新新的培养联系人和预备期培养人

1. `功能`: 用于通过excel更新新的培养联系人和预备期培养人

2. `介绍`: 同理，因为只能手动添加，不太方便

3. excel模板的格式如下：
  
  注意时间格式，就是系统可以导出的那个表，把列名合并成一个单元格作为一行。
  
  | 序号 | ID   | 所在党支部 | 团支部 | 学号 | 姓名 | 当前身份 | 递交入党申请时间 | 最近推优通过时间 | 确定积极分子时间 | 党校结业时间 | 培养人1 | 培养人2 | 培养人3 | 培养人4 | 确定发展对象时间 | 预备期培养人1 | 预备期培养人2 | 预备期培养人3 | 预备期培养人4 | 介绍人1 | 介绍人2 | 吸收预备党员时间 | 审批新党员时间 | 转正时间 | 转正审批时间 | 手机 | QQ   | 年级 | 姓名 | 性别 | 民族 | 出生日期 | 籍贯 |
  | ---- | ---- | ---------- | ------ | ---- | ---- | -------- | ---------------- | ---------------- | ---------------- | ------------ | ------- | ------- | ------- | ------- | ---------------- | ------------- | ------------- | ------------- | ------------- | ------- | ------- | ---------------- | -------------- | -------- | ------------ | ---- | ---- | ---- | ---- | ---- | ---- | -------- | ---- |
  | xx   | xx   | 2          | xxxx   |      |      |          |                  |                  |                  |              |         |         |         |         |                  |               |               |               |               |         |         |                  |                |          |              |      |      |      |      |      |      |          |      |

注意保存的excel格式，如果其他格式文件保存为xlsx文件时选择了`Script Open xml电子表格\*.xlsx`，会报错`UserWarning: File contains an invalid specification for Sheet1. This will be removed warn(msg)`，找不到对应的表名，重新另存为`Excel工作簿 \*.xlsx`格式即可。

---

- `update_dangxiao.py`

​	完成党校后，更新党校结业时间，是否优秀结业以及政治面貌

1. `功能`: 用于通过excel更新完成党校后的相关信息

2. `介绍`: 同理，因为只能手动添加，不太方便

3. excel模板的格式如下：

   注意时间格式，可以系统里先导出积极分子里面没完成党校的人的信息，然后挑选出正在上党校的人的信息，然后添加一列是否优秀即是如下的格式了。

| 序号 | ID   | 所在党支部 | 学号 | 姓名 | 当前身份 | 确定积极分子时间 | 是否优秀结业 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1 | xxxx | 本科生第1党支部 | xxxxx | xxx | 入党积极分子(正上党校) | 2022-06-12 | 否 |

