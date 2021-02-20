# short_scripts
一些直接拿来即用的python脚本

### files_operations.py
  直接放到文件夹下面执行命令`python ./files_operations.py`更多用法可以执行可以加`-h`参数查看帮助，下面是主要的两种用法：
  1、`-r "test%02d.jpg .*.jpg"` 可以将文件夹下的所有jpg文件进行重命名，格式为`test%02d.jpg`。这种语法是来自于python格式化字符串%的一种。由于需要编号排序，所以必须用%d格式化符号；
  2、`-R "x y"`可以将文件夹下文件名称中的x替换为y；
