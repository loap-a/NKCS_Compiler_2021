### 南开大学软件学院编译原理-课程实验 ###
- 自己动手做一个简易的c语言编译器
- 使用了flex和yacc作为辅助工具
- 实现功能:
    - 最普通的c程序能运行
    - 一维数组
    - 函数调用(包括递归)
    - 编译成mips汇编码

#### 核心文件简述 ####
- flexx.l:词法分析
- yaccc.y:语法分析
- Tree.cpp:语法树
- InterCode.cpp、Praser.cpp:中间代码生成
- TransToAssemble.py:汇编代码生成
#### 环境要求 ####
- win10 (推荐)
- 编辑器: 推荐使用vscode(运行项目不要使用vscode内置终端, 使用cmder或cmd)
- 最新版本的flex和bison 
- 转汇编需要python

#### 运行 ####
- windows系统直接在命令行中输入
```
makefile.bat
```
中间代码会写入InterCode.txt
生成的MPIS汇编代码会写入Assemble.asm
- 汇编代码使用MARS(http://courses.missouristate.edu/kenvollmar/mars/)即可编译运行



