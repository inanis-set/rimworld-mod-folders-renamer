import os
from xml.dom import minidom

basepath = input('path: ')

def readName(dir):
    try:
        mydoc = minidom.parse(f'{basepath}{dir}/About/About.xml')
    except Exception as ex:
        print('================================================')
        print(ex)
        print(dir)
        return dir
    items = mydoc.getElementsByTagName('name')
    name = items[0].firstChild.data
    return ''.join(char for char in name if char.isalnum())

def renameDir(dir, name):
    olddir = basepath + dir
    newdir = basepath + name
    os.rename(olddir, newdir)

def main():
    print('Processing...')
    with os.scandir(basepath) as dirs:
        for dir in dirs:
            if dir.is_dir():
                name = readName(dir.name)
                renameDir(dir.name, name)

if __name__ == '__main__':
    main()
    print('Done!')