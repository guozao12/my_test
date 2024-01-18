import os
import os.path
import filetype

address_dir = os.path.dirname(__file__)  # 拿到目录名
address_content_old = os.listdir(address_dir)  # 拿到目录中的每个文件名
address_dir_content_new = []  # 待修改的文件名
for adr_file in address_content_old:  # 判断是否为需要更改的文件,并保存到列表中
    adr_whole = os.path.join(address_dir, adr_file)
    if os.path.isdir(adr_whole) or adr_whole.endswith('.py'):
        continue
    if str(filetype.guess(adr_whole).mime).startswith('video'):
        address_dir_content_new.append(adr_whole)

i = 1
# 开始修改
for file_name_old in address_dir_content_new:
    appendix = os.path.splitext(file_name_old)[1]  # 分隔出后缀名
    os.rename(file_name_old, os.path.join(address_dir, f'1（{i}）' + appendix))
    i += 1


