import os
import openpyxl
import csv
import sys


class Course:
    def __init__(self):
        self.name = None  # 名称
        self.weekdays = []  # 星期
        self.start_t = []  # 开始节数
        self.end_t = []  # 结束节数
        self.teacher = None  # 老师
        self.location = None  # 地点
        self.week = None  # 周数


print("本程序能将吉林大学新教务系统中的课程信息转化为WakeUp课程表能识别的csv文件。")
print("")
print("请在新教务系统中进行如下操作：")
print("课表查看->教学进度表->导出->导出文件列表,然后将下载到的xlsx文件放在本程序同一目录下，并重命名为1.xlsx")
input("完成后，请按回车键")

workbook = openpyxl.load_workbook("1.xlsx")
sheet = workbook['sheet1']
max_row = sheet.max_row
course_list = []
range_i = 0
for i in range(1, max_row):
    cell = sheet[i + 1]
    course_list.append(Course())
    k = 0
    for j in cell:
        # print(j.value, end=" ")
        if k == 0:  # 周数
            temp_string = ""
            for d in range(len(j.value)):
                if j.value[d] != "周":
                    temp_string = temp_string + j.value[d]
            course_list[range_i].week = temp_string
        elif k == 1:  # 星期
            for d in range(len(j.value)):
                c = j.value[d]
                if c == "一":
                    course_list[range_i].weekdays.append(1)
                elif c == "二":
                    course_list[range_i].weekdays.append(2)
                elif c == "三":
                    course_list[range_i].weekdays.append(3)
                elif c == "四":
                    course_list[range_i].weekdays.append(4)
                elif c == "五":
                    course_list[range_i].weekdays.append(5)
                elif c == "六":
                    course_list[range_i].weekdays.append(6)
                elif c == "日":
                    course_list[range_i].weekdays.append(7)
        elif k == 2:  # 开始节数
            for d in range(len(j.value)):
                c = j.value[d]
                if c.isdigit():
                    if j.value[d + 1].isdigit():
                        course_list[range_i].start_t.append(c + j.value[d + 1])
                    else:
                        if not j.value[d - 1].isdigit():
                            course_list[range_i].start_t.append(c)
        elif k == 3:  # 结束节数
            for d in range(len(j.value)):
                c = j.value[d]
                if c.isdigit():
                    if j.value[d + 1].isdigit():
                        course_list[range_i].end_t.append(c + j.value[d + 1])
                    else:
                        if not j.value[d - 1].isdigit():
                            course_list[range_i].end_t.append(c)
        elif k == 5:  # 名称
            course_list[range_i].name = j.value
        elif k == 9:  # 地点
            course_list[range_i].location = j.value
        elif k == 10:  # 老师
            course_list[range_i].teacher = j.value
        k = k + 1
    range_i = range_i + 1

with open("output.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["课程名称", "星期", "开始节数", "结束节数", "老师", "地点", "周数"])
    for p in course_list:
        for q in p.weekdays:
            for r in range(len(p.start_t)):
                writer.writerow([
                    p.name,
                    q,
                    p.start_t[r],
                    p.end_t[r],
                    p.teacher,
                    p.location,
                    p.week
                ])
        print("已输出：", p.name)
    print("Done.")

print("程序执行完成，好像没有遇到错误")
print("请在当前目录下找到输出文件output.csv，把它发送到你的手机上。")
print("打开WakeUp并进行以下操作")
print("1.右上角...->上课时间 在这里将上课时间调整为新的上课时间")
print("2.右上角下载图标（第二个）->从Excel模板导入->新建课表再导入->勾选'我已仔细阅读以下说明'->选取CSV文件")
print("3.找到并导入刚刚发送的output.csv")
print("4.右上角...->已添课程，对照教务系统逐一检查每门课程的上课节数是否正确，如有错误请手动修改")
print()
input("按回车键退出程序")
