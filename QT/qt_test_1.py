import sys  # 导入系统库
# 动态显示需要的线程库
import threading
import time

# 挂件所需要的库
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *  # 导入pyqt的相关文件
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import test_1  # 导入我们的ui文件

# 初始化挂件
hear_figure, hear_figure_x = plt.subplots()
canvas = FigureCanvas(hear_figure)


def dynamic_update_figure_data(data=[i for i in range(1000)], sleep=0.01):
    global hear_figure, hear_figure_x
    global thread_hear_flag, hear_pause_flag

    # 数据宽度
    data_length = len(data)
    # 缓存区
    data_cache = [0] * data_length
    # 由于本次绘图不再更新坐标轴，所以必须指明高度
    hear_figure_x.set_ylim([0, max(data)])
    # 首次绘制
    line_sin, = hear_figure_x.plot(data_cache)
    while 1:
        # 判断是否已经全部显示完
        if not data:
            break
        # 舍去第一个数据
        data_cache.pop(0)
        # 把数据添加到缓存的最后一个数据
        data_cache.append(data.pop(0))
        # 重新显示缓存区数据
        line_sin.set_ydata(data_cache)
        canvas.draw()
        time.sleep(sleep)


def start_draw():
    # 不能用.run()，不然会阻塞运行，不能动态显示
    draw_thread = threading.Thread(target=dynamic_update_figure_data, args=())
    draw_thread.start()


if __name__ == "__main__":
    # 创建应用程序
    app = QApplication(sys.argv)
    # 创建主界面
    main_window = QMainWindow()
    ui = test_1.Ui_MainWindow()
    # 进行主界面的继承
    ui.setupUi(main_window)
    ui.gridLayout.addWidget(canvas)
    ui.pushButton.clicked.connect(start_draw)

    # 主界面的展示
    main_window.show()
    # 等待关闭
    sys.exit(app.exec())
