import os
import codecs


def copy_files(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)

                # 判断文件名是否以中文开头
                if ord(full_path.split(os.sep)[-1][0]) > 127:
                    # 读取文件并进行编码转换
                    with codecs.open(full_path, 'r', 'utf-8') as f:
                        content = f.read()
                    with codecs.open(os.path.join(target_folder, file), 'w', 'utf-8') as f:
                        f.write(content)


if __name__ == '__main__':
    source_dir = '../../Laws'
    target_dir = '../source'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    copy_files(source_dir, target_dir)
