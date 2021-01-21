## IUA(IOV_UI_Auto)：
IUA是基于Python3.6+AppiumService+Seleium Grid+Jenkins构建的UI自动化框架。
IUA用于稳定模块app的UI自动化冒烟测试及回归测试。

###项目进展：
#####•	Setup：
           1.启动项封装（完成）
           2.Android和QNX刷机（未完成，受限于U盘续写权限，需走OA流程）
#####•	PO模式封装（完成）
#####•	公共方法封装
          1.定位方法（完成）
          2.触控方法（完成）
          3.异常处理（完成）
          4.数据清洗（待完成）
#####•	自动化行为（待完成，需要具体Case进行定制）
#####•	报告输出（插件ready，需与Jenkins集成后进一步优化）
###环境：
1.	Python3.x
2.	Appium
3.	Selenium
4.	JDK8+
5.	Android 8.1（API level 27）
6.	node v13+
7.  allure 2