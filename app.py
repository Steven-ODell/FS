from blessed import Terminal
import os

term = Terminal()
y = 0
baseDir = '/Users/Steven/Desktop'
dirTitle = "Base Search"
infolder = False
state = "main"
currentDir = ""

with term.fullscreen(), term.cbreak(), term.hidden_cursor():
    while True:
        if state == "main":
            print(term.clear)
            infolder = False
            print(term.bold(dirTitle))
            baseFileList = os.listdir('/Users/Steven/Desktop')

            for _, item in enumerate(baseFileList):
                print(item)

            print(term.move(term.height - 1, 0) + 'Press "q" or "h" to quit')
            print(term.move(y + 1, 0) + term.reverse_underline(baseFileList[y]))

        if state == "folderOpen":
            print(term.clear)
            infolder = True
            print(term.bold(currentDir))

            if os.path.isdir(currentDir):
                baseFileList = os.listdir(currentDir)
                for _, item in enumerate(baseFileList):
                    print(item)
            else:
                state = "openFile"
            print(term.move(term.height - 2, 0) + 'Press "enter" or "l" to open folder or file(nvim)')
            print(term.move(term.height - 1, 0) + 'Press "b" or "h" to go back')
            print(term.move(y + 1, 0) + term.reverse_underline(baseFileList[y]))

        if state == "openFile":
            print(term.clear)
            os.system(f"nvim {os.path.join(baseDir,baseFileList[y])}")
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
                directory = os.path.dirname(selected)
                os.chdir(directory)
                os.system(f"nvim '{selected}'")
                print(term.hide_cursor)
        elif key.lower() == "b" or key.lower() == "h":
            currentDir = os.path.dirname(currentDir)
            y = 0
            if state == "main":
                break
            if currentDir == baseDir or not currentDir.startswith(baseDir):
                state = "main"





