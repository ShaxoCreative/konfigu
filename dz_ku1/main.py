import tkinter as tk
from tkinter import scrolledtext
from zipfile import ZipFile

root = tk.Tk()
root.title("Shell Emulator")

dirname = ""
myzip = ZipFile('files.zip', 'a')


def process_command():
    global dirname
    command = entry.get()
    output = ""

    if command == 'ls':
        for name in myzip.namelist():
            output += name + "\n"
    elif command == "exit":
        root.quit()
    elif command == "uname":
        output += "Linux\n"
    elif command == "pwd":
        if dirname == "":
            output += "/root\n"
        else:
            output += "/root/" + dirname + "\n"
    elif command.startswith('cd'):
        if len(command) == 2:
            dirname = ""
        else:
            ndir = command.split(" ")[1]
            if ndir in myzip.namelist():
                dirname = ndir
            else:
                output += "sh: cd: can't cd to " + ndir + ": No such file or directory\n"
    elif command.startswith('touch '):
        new_file = command.split()[1]
        with myzip.open(new_file, 'w'):
            pass
    else:
        output += "Command not found.\n"

    output_text.insert(tk.END, "~" + dirname + "# " + command + "\n" + output)
    entry.delete(0, tk.END)


entry = tk.Entry(root, width=50)
entry.grid(row=0, column=0, padx=10, pady=10)

send_button = tk.Button(root, text="Enter", command=process_command)
send_button.grid(row=0, column=1, padx=10, pady=10)

output_text = scrolledtext.ScrolledText(root, width=70, height=50)
output_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

myzip.close()
