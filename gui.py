from PyQt5.QtWidgets import QMainWindow
# , QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QPushButton, QTextEdit
# import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.setGeometry(300, 300, 600, 400)
        # self.setWindowTitle("Server Info")

        # Central widget to hold the main layout
        # central_widget = QWidget(self)
        # self.setCentralWidget(central_widget)

        # Main layout with two frames: server info and action buttons
        # main_layout = QVBoxLayout(central_widget)

        # Frame 1: Server Info
        # frame_info = QWidget(self)
        # frame_info_layout = QGridLayout(frame_info)

        # Server Info Labels and Values (Example data, replace with actual server info)
        # server_info_data = {
        #     "Server Name": "My Server",
        #     "IP Address": "192.168.1.1",
        #     "Port": "8080",
        #     "Status": "Running"
        # }

        # row_num = 0
        # for label, value in server_info_data.items():
        #     frame_info_layout.addWidget(QLabel(label), row_num, 0, alignment=0)
        #     frame_info_layout.addWidget(QLabel(value), row_num, 1, alignment=0)
        #     row_num += 1

        # Console Output (Example, replace with your console implementation)
        # console_output = QTextEdit(self)
        # frame_info_layout.addWidget(console_output, row_num, 0, 1, 2)
        #
        # main_layout.addWidget(frame_info)
        #
        # Frame 2: Action Buttons
        # frame_actions = QWidget(self)
        # frame_actions_layout = QVBoxLayout(frame_actions)
        #
        # btn_start = QPushButton("Start", self)
        # btn_start.clicked.connect(self.start_server)
        # frame_actions_layout.addWidget(btn_start)
        #
        # btn_stop = QPushButton("Stop", self)
        # btn_stop.clicked.connect(self.stop_server)
        # frame_actions_layout.addWidget(btn_stop)

        # btn_restart = QPushButton("Restart", self)
        # btn_restart.clicked.connect(self.restart_server)
        # frame_actions_layout.addWidget(btn_restart)

        # main_layout.addWidget(frame_actions)

        self.show()
