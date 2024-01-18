import os
import os.path

address_dir = os.path.dirname(__file__)  # 拿到目录名
address_content_old = os.listdir(address_dir)  # 拿到目录中的每个文件名
address_dir_content_new = []  # 待修改的文件名
for adr_file in address_content_old:  # 根据后缀名判断是否为需要更改的文件
    if os.path.splitext(adr_file)[1] == '.mp4':
        adr_new = os.path.join(address_dir, adr_file)  # 组合成rename需要形式的旧路径
        address_dir_content_new.append(adr_new)

i = 1
# 开始修改
for file_name_old in address_dir_content_new:
    os.rename(file_name_old, os.path.join(address_dir, f'1（{i}）.mp4'))
    i += 1


