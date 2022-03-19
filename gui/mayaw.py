from shiboken2 import wrapInstance
from builtins import int

from maya.api import OpenMayaUI
from Qt import QtWidgets


def get_maya_main_window():
    """
    Get maya's window instance

    :return: window instance, maya program window
    """
    main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QMainWindow)


def set_window_pos(child_only=0, x=0, y=0):
    """
    Set window position of maya's widgets

    :param child_only: bool. option to set position only for widgets parented
    to maya main window
    :param x: int. window x position
    :param y: int. window y position
    """
    for child in get_maya_main_window().children():
        if isinstance(child, QtWidgets.QWidget) and child.isWindow():
            # set visible
            if child.isHidden():
                child.setVisible(1)
            child.move(x, y)

    if not child_only:
        tops = QtWidgets.QApplication.topLevelWidgets()
        for top in tops:
            if top.isWindow() and not top.isHidden():
                if top.windowTitle() == get_maya_main_window().windowTitle():
                    continue
                top.move(x, y)