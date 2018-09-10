import sys, getopt, os
from collections import Counter


def count_word(file):
    list = open(file, 'r', encoding='utf-8').read()
    word_list = []
    end = 0
    for i in range(len(list)):  # 遍历全文
        if list[i].isalpha() and i >= end:  # 词首（字母）
            for j in range(i, len(list)):
                if (list[j].isalpha() == 0) or (j == len(list)-1):  # 词尾（非字母）
                    word_list.append(list[i: j])  # 词
                    end = j
                    break
    word_list.pop(-1)
    for k, v in Counter(word_list).items():
        print('{}: {}'.format(k, v))
    num = len(word_list)
    print('总词数： {}'.format(num))


def count_char(file):
    num = len(open(file, 'r', encoding='ISO-8859-1').read())
    print("文件{}的字符数(包括换行符)为{}".format(file, num))


def count_line(file):
    print('文件{}的行数：'.format(file) +
          str(len(open(file, 'r', encoding='utf-8').readlines())))


def down_find(dir, hz):
    dir_files = os.listdir(dir)  # 路径下的文件列表
    for i in dir_files:  # 生成子目录
        son_path = os.path.join(dir, i)
        if os.path.isdir(son_path):  # 如果是目录，递归操作
            down_find(son_path, hz)
        elif hz in son_path:
            files_list.append(son_path)
    return files_list


def recursion(value):
    op2 = value[0: 2]  # 第二选项串
    hz = args[0]  # 文件后缀参数
    dir = os.getcwd()  # 当前路径
    files = down_find(dir, hz)  # 返回相应后缀文件列表
    print("当前目录下符合后缀{}的文件有： {}".format(hz, files_list))
    for file in files:
        if op2 == "-c":  # 返回字符数
            count_char(file)
        elif op2 == "-w":  # 返回词的数目
            count_word(file)
        elif op2 == "-l":  # 返回行数
            count_line(file)
        elif op2 == '-a':
            more_data(file)


def more_data(value):
    code_line = blank_line = comment_line = 0
    end = -1
    lines = open(value, 'r', encoding='utf-8').readlines()
    for i in range(len(lines)):
        if lines[i].startswith('#') and (i > end):  # 单行注释
            comment_line += 1
        elif len(lines[i].strip()) <= 1:  # 空行
            blank_line += 1
        elif lines[i][0].isalpha() and (i > end):  # 代码行
            code_line += 1
        elif lines[i].startswith('"""') and (i > end):  # 多行注释
            for j in range(i + 1, len(lines)):
                if lines[j].startswith('"""'):
                    comment_line += (j - i + 1)
                    end = j
        elif lines[i].startswith("'''") and (i > end):
            for j in range(i + 1, len(lines)):
                if lines[j].startswith("'''"):
                    comment_line += (j - i + 1)
                    end = j
    print('文件：{}\n代码行：{}\n空行：{}\n注释行：{}\n'.format(value,code_line, blank_line, comment_line))


if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hc:w:l:s:a:")
    files_list = []  # 相应后缀文件列表
    for op, value in opts:  # op为选项串，value为附加参数
        if op == "-c":  # 返回字符数
            count_char(value)
        elif op == "-w":  # 返回词的数目
            count_word(value)
        elif op == "-l":  # 返回行数
            count_line(value)
        elif op == "-s":  # 递归处理目录下符合条件的文件
            recursion(value)
        elif op == "-a":  # 返回代码行，空行，注释行数
            more_data(value)
        elif op == "-h":
            print('-c file  返回文件 file 的字符数\n'
                  '-w file  返回文件 file 的词的数目\n'
                  '-l file  返回文件 file 的行数\n'
                  '-a file  返回空行代码行注释行数\n'
                  '-s -*[后缀]  递归相应后缀文件再执行基本指令')
            sys.exit()
