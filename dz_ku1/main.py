from zipfile import ZipFile

dirname = ""
with ZipFile('files.zip', 'a') as myzip:
    while True:
        command = input('~' + dirname + '# ')
        if command == 'ls':
            for name in myzip.namelist():
                print(name)
        elif command == "exit":
            exit(0)
        elif command == "uname":
            print("Linux")
        elif command == "pwd":
            if dirname == "":
                print("/root")
            else:
                print("/root/" + dirname)
        elif command.startswith('cd'):
            if len(command) == 2:
                dirname = ""
            else:
                ndir = command.split(" ")[1]
                if ndir in myzip.namelist():
                    dirname = ndir
                else:
                    print("sh: cd: can't cd to " + ndir + ": No such file or directory")
        elif command.startswith('touch '):
            new_file = command.split()[1]
            with myzip.open(new_file, 'w'):
                pass
        else:
            print("Command not found.")
