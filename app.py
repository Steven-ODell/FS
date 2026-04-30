from blessed import Terminal
import os
import sys

term = Terminal()
y = 0
# PC DIR = '/home/saoii'
# MAC DIR = '/Users/Steven/Desktop'
baseDir = "/home/saoii"
dirTitle = "HOME"
state = "main"
currentDir = ""
baseFileList = os.listdir(baseDir)

def createDirectoryName():
    print(term.move_y(10) + term.center("|---------------------------------------|"))
    print(term.center(""))
    print(term.center("|---------------------------------------|"))
    name = ""
    while True:
        x = term.width // 2 - len(name) // 2
        print(term.move_xy(x, 11) + " " * 20, end="", flush=True)
        print(term.move_xy(x, 11) + name, end="", flush=True)
        val = term.inkey()
        if val.name == "KEY_ENTER":
            break
        elif val.name == "KEY_BACKSPACE":
            name = name[:-1]
            print(term.move_xy(term.width // 2 - 3, 11) + " " * 20, end="", flush=True)
            print(term.move_xy(term.width // 2 - 3, 11) + name, end="", flush=True)
        elif val.isprintable():
            name += val
    return name

with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    while True:
        if state == "main":
            baseFileList = os.listdir(baseDir)
            y = min(y, len(baseFileList) - 1)
            out = term.home + term.clear
            out += term.bold(dirTitle) + '\n'
            for item in baseFileList:
                out += item + '\n'
            out += term.move(term.height - 1, 0) + 'Press "q" to quit'
            out += term.move(y + 1, 0) + term.reverse_underline(baseFileList[y])
            sys.stdout.write(out)
            sys.stdout.flush()

        if state == "folderOpen":
            if os.path.isdir(currentDir):
                baseFileList = os.listdir(currentDir)
                y = min(y, len(baseFileList) - 1)
                out = term.home + term.clear
                out += term.bold(currentDir) + '\n'
                for item in baseFileList:
                    out += item + '\n'
                out += term.move(term.height - 2, 0) + 'Press "enter" or "l" to open'
                out += term.move(term.height - 1, 0) + 'Press "h" or "b" to go back'
                out += term.move(y + 1, 0) + term.reverse_underline(baseFileList[y])
                sys.stdout.write(out)
                sys.stdout.flush()

        if state == "openFile":
            directory = os.path.dirname(currentDir)
            os.chdir(directory)
            os.system(f"nvim '{currentDir}'")
            currentDir = directory
            sys.stdout.write(term.home + term.clear)
            sys.stdout.flush()
            print(term.hide_cursor)
            state = "folderOpen"
            continue

        if state == "createFolder":
            print(term.clear)
            mkName = createDirectoryName()
            newFolderPath = os.path.join(currentDir, mkName)
            os.mkdir(newFolderPath)
            sys.stdout.write(term.home + term.clear)
            sys.stdout.flush()
            state = "folderOpen"
            continue
        #if state == "deleteFolder":


        key = term.inkey()
        if key.lower() == "q":
            break
        elif key.name == "KEY_DOWN" or key.lower() == "j":
            y = min(len(baseFileList) - 1, y + 1)
        elif key.name == "KEY_UP" or key.lower() == "k":
            y = max(0, y - 1)
        elif key.name == "KEY_ENTER" or key == "\r" or key.lower() == "l":
            selected = os.path.join(currentDir if currentDir else baseDir, baseFileList[y])
            if os.path.isdir(selected):
                currentDir = selected
                y = 0
                state = "folderOpen"
            else:
                currentDir = selected
                state = "openFile"
        elif key.lower() == "b" or key.lower() == "h":
            currentDir = os.path.dirname(currentDir)
            y = 0
            if state == "main":
                break
            if currentDir == baseDir or not currentDir.startswith(baseDir):
                state = "main"
        elif key.lower() == "n":
            state = "createFolder"

