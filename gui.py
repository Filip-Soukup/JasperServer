import tkinter as tk
from server import Server
# import sys


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.frameConsole = tk.Frame(self, padx=10, pady=10)
        self.frameButtons = tk.Frame(self, padx=10, pady=10)
        self.console = tk.Text(self, padx=10, pady=10)
        self.frameConsole.grid(column=0, row=0)
        self.frameButtons.grid(column=1, row=0)
        self.console.grid(column=0, columnspan=2, row=1)

        self.info = {
            "name": {
                "label": tk.Label(self.frameConsole, text="Server name:", anchor="e", justify="right"),
                "display": tk.Label(self.frameConsole, text="None", anchor="w", justify="left")
            },
            "ip": {
                "label": tk.Label(self.frameConsole, text="IP address:", anchor="e", justify="right"),
                "display": tk.Label(self.frameConsole, text="None", anchor="w", justify="left")
            },
            "access": {
                "label": tk.Label(self.frameConsole, text="Accessibility:", anchor="e", justify="right"),
                "display": tk.Label(self.frameConsole, text="inactive", anchor="w", justify="left")
            },
            "status": {
                "label": tk.Label(self.frameConsole, text="Status:", anchor="e", justify="right"),
                "display": tk.Label(self.frameConsole, text="Stopped", anchor="w", justify="left")
            },
            "user_count": {
                "label": tk.Label(self.frameConsole, text="Users:", anchor="e", justify="right"),
                "display": tk.Label(self.frameConsole, text="0", anchor="w", justify="left")
            },
        }

        self.buttons = {
            "setup": tk.Button(self.frameButtons, text="Setup", width=20),
            "start": tk.Button(self.frameButtons, text="Start", width=20),
            "stop": tk.Button(self.frameButtons, text="Stop", width=20),
            "restart": tk.Button(self.frameButtons, text="Restart", width=20),
        }

        keysInfo = list(self.info.keys())
        for x in keysInfo:
            pos = keysInfo.index(x)
            self.info[x]["label"].grid(sticky="e", column=0, row=pos)
            self.info[x]["display"].grid(sticky="w", column=1, row=pos)

        self.buttons["setup"].grid(column=0, row=0, sticky="se")
        self.buttons["start"].grid(column=1, row=0, sticky="sw")
        self.buttons["stop"].grid(column=0, row=1, sticky="ne")
        self.buttons["restart"].grid(column=1, row=1, sticky="nw")

        self.mainloop()

    def write_console(self, message):
        self.console.insert("end", message)