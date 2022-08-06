# JLUCourseHelper
## 概要
JLU近期更换了新的教务系统，WakeUp课程表的自动导入教务功能随之失效。本程序为WakeUp课程表app更新前的一个过渡。

## 程序下载
**Windows版本**

Windows版本下载：[奶牛快传](https://cowtransfer.com/s/31d435c1665b47)

Windows版本下载后可直接打开，无需Python环境和依赖。

**MacOS版本**

MacOS用户请直接克隆本项目，然后使用python执行JLUCourseHelper.py

```
python3 JLUCourseHelper.py
```
本程序使用openpyxl来处理xlsx文件，因此在运行前需安装依赖
```
pip3 install openpyxl
```

## 使用

打开新教务系统并进入“我的课表”，然后点击“教学进度表”
![](https://tva1.sinaimg.cn/large/e6c9d24egy1h4x6gyf29aj217i0t8dm6.jpg)

点击“导出”，然后点击“导出文件列表”

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h4x6gyr0laj210o0u0jvw.jpg)
点击此处的下载按钮，即可得到xlsx文件

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h4x6gy49vuj20py08qaam.jpg)

把xlsx文件重命名为1.xlsx，并和JLUCourseHelper.exe放在同一目录下

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h4x6gxwmw1j21ir0u0goy.jpg)

执行脚本：

Windows系统：双击运行JLUCourseHelper.exe

MacOS系统：在终端下打开此目录，然后执行
```
python3 JLUCourseHelper.py
```
脚本正常运行时，你应该会看到如下画面：
![](https://tva1.sinaimg.cn/large/e6c9d24egy1h4x6gxhcwrj21j40twaj4.jpg)

此时，当前目录下会出现output.csv文件，利用自己的方法把它发送到手机上。

## WakeUp APP操作

由于吉林大学本学期开始使用新的时间表，请先将WakeUp课程表中的时间表修改成正确的时间（如下图所示）

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h4xa9nsk6fj20u01chdi8.jpg)

随后回到主界面，点击右上角第二个“下载按钮”，并选择“从Excel模板导入”，然后选择“新建课表再导入”

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h4x6h9dxzgj20u01sxte2.jpg)
随后点击“选取CSV文件”，找到文件并导入即可

## 检查
利用此程序导入的课表很有可能会出现错误，因此导入后一定要手动检查课程是否导入正确。

点击右上角...->已添课程，对照教务系统逐一检查每门课程的上课节数是否正确，如有错误请手动修改。
