# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Door.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(281, 353)
        MainWindow.setMinimumSize(QtCore.QSize(281, 353))
        MainWindow.setMaximumSize(QtCore.QSize(281, 353))
        MainWindow.setStyleSheet(_fromUtf8("* {\n"
"    border-color: #2b2b2b;\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(76, 76, 76, 255), stop:0.502347 rgba(42, 41, 42, 255), stop:1 rgba(76, 76, 76, 255));\n"
"    alternate-background-color: #3c3f41;\n"
"}\n"
"\n"
"QFrame {\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    color: #bbbbbb;\n"
"    background-color: #3c3f41;\n"
"    border: none;\n"
"    border-top: 1px solid #2b2b2b;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbbbbb;\n"
"}\n"
"QDialog QScrollArea {\n"
"    border-top: none;\n"
"    border: none;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: #2b2b2b;\n"
"    border: none;\n"
"    color: #bbbbbb;\n"
"    selection-background-color: #2f65ca;\n"
"}\n"
"\n"
"QGraphicsView {\n"
"    background-color: #3c3f41;\n"
"    border-color: #2b2b2b;\n"
"    color: #bbbbbb;\n"
"}\n"
"\n"
"QMainWindow,\n"
"QAbstractItemView,\n"
"QTreeView::branch,\n"
"QTabBar::tab,\n"
"QTreeWidget,\n"
"QToolBox,\n"
"QQuickWidget,\n"
"QMdiArea {\n"
"    color: #bbbbbb;\n"
"    background: #3c3f41;\n"
"    font-size: 13px;\n"
"    border-color: #2b2b2b;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbbbbb;\n"
"    alternate-background-color: #3c3f41;\n"
"}\n"
"QAbstractItemView {\n"
"    border: none;\n"
"    border-top: 1px solid #2b2b2b;\n"
"}\n"
"QAbstractItemView,\n"
"QTreeView * {\n"
"    background: #3c3f41;\n"
"    background-color: #3c3f41;\n"
"    font-size: 13px;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbbbbb;\n"
"    alternate-background-color: #3c3f41;\n"
"}\n"
"QDialog QAbstractItemView {\n"
"    border: 1px solid #2b2b2b;\n"
"}\n"
"\n"
"QListView,\n"
"QListWidget,\n"
"QTableView,\n"
"QColumnView,\n"
"QDockWidget,\n"
"QMessageBox,\n"
"QSlider {\n"
"    border-color: #2b2b2b;\n"
"    background: #313335;\n"
"    color: #bbb;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbb;\n"
"}\n"
"\n"
"QScrollBar {\n"
"    border: none;\n"
"    background: #3c3f41;\n"
"    height: 12px;\n"
"    width: 12px;\n"
"    margin: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    padding: 1px 0 1px;\n"
"}\n"
"QScrollBar:vertical {\n"
"    padding: 0 1px 0 1px;\n"
"}\n"
"QScrollBar::handle {\n"
"    background: #545454;\n"
"    min-width: 10px;\n"
"    min-height: 10px;\n"
"    border: 1px solid #555555;\n"
"    border-radius: 1px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    min-width: 40px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5c5c5c, stop:1 #515151);\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    min-height: 40px;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #5c5c5c, stop:1 #515151);\n"
"}\n"
"QScrollBar::handle:horizontal:hover,\n"
"QScrollBar::handle:horizontal:focus {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6f6f6f, stop:1 #646464);\n"
"}\n"
"QScrollBar::handle:vertical:hover,\n"
"QScrollBar::handle:vertical:focus {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #6f6f6f, stop:1 #646464);\n"
"}\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    background: none;\n"
"    border: none;\n"
"}\n"
"QScrollBar::add-page,\n"
"QScrollBar::sub-page {\n"
"    background: none;\n"
"}\n"
"\n"
"QTreeView::branch:open:adjoins-item:has-children {\n"
"    background: transparent url(images/arrow-bottom.png) center center no-repeat;\n"
"    margin: 0;\n"
"}\n"
"QTreeView::branch:closed:adjoins-item:has-children {\n"
"    background: transparent url(images/arrow-left.png) center center no-repeat;\n"
"    margin: 0;\n"
"}\n"
"QAbstractItemView::item:selected {\n"
"    color: #bbbbbb;\n"
"    background-color: #2f65ca;\n"
"    outline: none;\n"
"}\n"
"QAbstractItemView::branch:open:selected,\n"
"QAbstractItemView::branch:closed:selected,\n"
"QAbstractItemView::branch:open:adjoins-item:selected,\n"
"QAbstractItemView::branch:closed:adjoins-item:selected,\n"
"QAbstractItemView::branch:open:adjoins-item:has-children:selected,\n"
"QAbstractItemView::branch:closed:adjoins-item:has-children:selected {\n"
"    background-color: #2f65ca;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QDialog, QDialogButtonBox {\n"
"    background-color: #3c3f41;\n"
"    border-color: #323232;\n"
"    color: #bbbbbb;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid #2b2b2b;\n"
"    border-radius: 0;\n"
"    font-size: 13px;\n"
"    color: #bbb;\n"
"    padding: 0 12px;\n"
"    background-color: #3c3f41;\n"
"    border-left: none;\n"
"    height: 22px;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    font: normal;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #444);\n"
"}\n"
"QTabBar::close-button {\n"
"    image: url(images/close.png);\n"
"    subcontrol-position: right;\n"
"}\n"
"QTabBar::close-button:hover {\n"
"    image: url(images/close-hover.png);\n"
"}\n"
"\n"
"QTabWidget, QTabWidget::tab-bar {\n"
"    border-color: #292b2d;\n"
"}\n"
"QDialog QTabBar {\n"
"    border: 1px solid #292b2d;\n"
"    height: 26px;\n"
"}\n"
"QDialog QTabBar::tab:selected {\n"
"    margin: 1px 0 -1px 1px;\n"
"    border: 1px solid #666;\n"
"    border-bottom: 0;\n"
"    border-radius: 0;\n"
"    font-size: 13px;\n"
"    color: #bbb;\n"
"    height: 21px;\n"
"    padding: 1px 12px 3px;\n"
"    font: normal;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #535353, stop:1 #444);\n"
"}\n"
"QDialog QTabBar::tab:!selected {\n"
"    margin: 0 -1px 0 0;\n"
"    border: 1px solid #292b2d;\n"
"    border-bottom: 0;\n"
"    border-radius: 0;\n"
"    font-size: 13px;\n"
"    color: #bbb;\n"
"    height: 24px;\n"
"    padding: 0 12px 1px;\n"
"    background-color: #3c3f41;\n"
"}\n"
"\n"
"QDialog QTabBar::tab:last:!selected {\n"
"    margin-right: 0;\n"
"}\n"
"QDialog QTabBar::tab:last:selected {\n"
"    margin-right: 1px;\n"
"}\n"
"\n"
"QDialog QTabWidget::tab-bar {\n"
"    left: 10px;\n"
"    height: 26px;\n"
"    border: 1px solid #292b2d;\n"
"    border-bottom: none;\n"
"}\n"
"QDialog QTabWidget::pane {\n"
"    border: 1px solid #292b2d;\n"
"    background-color: #3c3f41;\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #444, stop:0.03 #3c3f41, stop:0.05 #3c3f41, stop:1 #3c3f41);\n"
"}\n"
"\n"
"QLabel {\n"
"background-color:qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 0), stop:0.479904 rgba(255, 0, 0, 0), stop:0.518868 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0));\n"
"    color: #bbbbbb;\n"
"}\n"
"QLabel:disabled {\n"
"    color: #777777;\n"
"}\n"
"\n"
"QToolButton {\n"
"    color: #eeeeee;\n"
"}\n"
"QToolButton:disabled {\n"
"    color: #777777;\n"
"}\n"
"\n"
"QPushButton,\n"
"QDialog QToolButton,\n"
"QDialog QToolButton:hover {\n"
"    border-radius: 2px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    \n"
"    font: 75 16pt \"URW Palladio L\";\n"
"    color: #bbb;\n"
"    border: 1px solid #5e5f60;\n"
"    background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(76, 76, 76, 255), stop:0.502347 rgba(42, 41, 42, 255), stop:1 rgba(76, 76, 76, 255));\n"
"}\n"
"QPushButton {\n"
"    padding: 0 10px 2px;\n"
"    min-width: 60px;\n"
"    height: 22px;\n"
"}\n"
"QDialog QToolButton,\n"
"QDialog QToolButton:hover {\n"
"    padding: 0;\n"
"    min-width: 30px;\n"
"    height: 21px;\n"
"}\n"
"QDialog QToolButton[popupMode=\"1\"] {\n"
"    padding-right: 20px;\n"
"}\n"
"QDialog QToolButton::menu-button {\n"
"    border-left: 1px solid #5e5f60;\n"
"    width: 20px;\n"
"}\n"
"QPushButton:pressed,\n"
"QDialog QToolButton:pressed {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #44494b, stop:1 #525759);\n"
"}\n"
"QPushButton:default {\n"
"    border: 1px solid #575d65;\n"
"    color: #bbb;\n"
"    font: 75 12pt \"URW Palladio L\";\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #344a65, stop:1 #263549);\n"
"}\n"
"QPushButton:default:pressed {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #263549, stop:1 #344a65);\n"
"}\n"
"QPushButton:focus,\n"
"QPushButton:default:focus,\n"
"QDialog QToolButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid #3b72ab;\n"
"}\n"
"QToolButton::menu-arrow {\n"
"    image: url(images/arrow-down.png);\n"
"}\n"
"QPushButton::menu-indicator,\n"
"QPushButton::menu-indicator:pressed {\n"
"    position: absolute;\n"
"    background: url(images/arrow-down.png) center center no-repeat;\n"
"    width: 20px;\n"
"    height: 24px;\n"
"    top: 0;\n"
"    right: 0;\n"
"    border-left: 1px solid #5e5f60;\n"
"}\n"
"QPushButton:disabled,\n"
"QDialog QToolButton:disabled,\n"
"QPushButton::menu-indicator:disabled,\n"
"QDialog QToolButton::menu-button:disabled {\n"
"    border-color: #595a5a;\n"
"    color: #777777;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid #333333;\n"
"   background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(76, 76, 76, 255), stop:0.502347 rgba(42, 41, 42, 255), stop:1 rgba(76, 76, 76, 255));\n"
"    padding-top: 5px;\n"
"    margin-top: 10px;\n"
"    outline: none;\n"
"    spacing: 0px;\n"
"}\n"
"QGroupBox::title {\n"
"    color: #bbb;\n"
"    font-size: 14px;\n"
"    position: absolute;\n"
"    top: -9px;\n"
"    left: 7px;\n"
"    padding: 0 1px;\n"
"}\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"    color: #777777;\n"
"}\n"
"QCheckBox::indicator,\n"
"QGroupBox::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"QGroupBox::indicator {\n"
"    margin-left: 2px;\n"
"}\n"
"QCheckBox::indicator:unchecked,\n"
"QCheckBox::indicator:unchecked:hover,\n"
"QGroupBox::indicator:unchecked,\n"
"QGroupBox::indicator:unchecked:hover {\n"
"    image: url(images/checkbox_unchecked.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:focus,\n"
"QCheckBox::indicator:unchecked:pressed,\n"
"QGroupBox::indicator:unchecked:focus,\n"
"QGroupBox::indicator:unchecked:pressed {\n"
"    image: url(images/checkbox_unchecked_focus.png);\n"
"}\n"
"QCheckBox::indicator:checked,\n"
"QCheckBox::indicator:checked:hover,\n"
"QGroupBox::indicator:checked,\n"
"QGroupBox::indicator:checked:hover {\n"
"    image: url(images/checkbox_checked.png);\n"
"}\n"
"QCheckBox::indicator:checked:focus,\n"
"QCheckBox::indicator:checked:pressed,\n"
"QGroupBox::indicator:checked:focus,\n"
"QGroupBox::indicator:checked:pressed {\n"
"    image: url(images/checkbox_checked_focus.png);\n"
"}\n"
"QCheckBox::indicator:indeterminate,\n"
"QCheckBox::indicator:indeterminate:hover,\n"
"QCheckBox::indicator:indeterminate:pressed,\n"
"QCheckBox::indicator:checked:disabled,\n"
"QGroupBox::indicator:indeterminate,\n"
"QGroupBox::indicator:indeterminate:hover,\n"
"QGroupBox::indicator:indeterminate:pressed,\n"
"QGroupBox::indicator:checked:disabled {\n"
"    image: url(images/checkbox_checked_disabled.png);\n"
"}\n"
"QCheckBox::indicator:unchecked:disabled,\n"
"QGroupBox::indicator:unchecked:disabled {\n"
"    image: url(images/checkbox_unchecked_disabled.png);\n"
"}\n"
"\n"
"QRadioButton {\n"
"    spacing: 5px;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    margin-bottom: 2px;\n"
"}\n"
"QRadioButton:disabled {\n"
"    color: #777777;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 21px;\n"
"    height: 21px;\n"
"}\n"
"QRadioButton::indicator:unchecked,\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(images/radio_unchecked.png);\n"
"}\n"
"QRadioButton::indicator:unchecked:focus,\n"
"QRadioButton::indicator:unchecked:pressed {\n"
"    image: url(images/radio_unchecked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked,\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(images/radio_checked.png);\n"
"}\n"
"QRadioButton::indicator:checked:focus,\n"
"QRadioButton::indicato::menu-arrowr:checked:pressed {\n"
"    image: url(images/radio_checked_focus.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:indeterminate,\n"
"QRadioButton::indicator:indeterminate:hover,\n"
"QRadioButton::indicator:indeterminate:pressed,\n"
"QRadioButton::indicator:checked:disabled {\n"
"    image: url(images/radio_checked.png);\n"
"}\n"
"QRadioButton::indicator:unchecked:disabled {\n"
"    image: url(images/radio_unchecked.png);\n"
"}\n"
"\n"
"QAbstractTextEdit,\n"
"QTextEdit,\n"
"QAbstractLineEdit,\n"
"QLineEdit {\n"
"    background-color: #45494a;\n"
"    border: 1px solid #646464;\n"
"    outline: none;\n"
"    color: #bbb;\n"
"    border-radius: 0;\n"
"    min-width: 60px;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbb;\n"
"    padding: 0 4px;\n"
"}\n"
"QLineEdit {\n"
"    height: 24px;\n"
"}\n"
"QAbstractLineEdit:focus,\n"
"QTextEdit:focus,\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border: 1px solid #3b72ab;\n"
"}\n"
"QAbstractLineEdit:disabled,\n"
"QTextEdit:disabled,\n"
"QTextEdit:disabled:focus,\n"
"QLineEdit:disabled,\n"
"QLineEdit:disabled:focus,\n"
"QLineEdit:read-only,\n"
"QLineEdit:read-only:focus {\n"
"    border: 1px solid #4f4f4f;\n"
"    color: #777777;\n"
"}\n"
"\n"
"QAbstractSpinBox,\n"
"QSpinBox {\n"
"    padding-right: 20px;\n"
"    border: 1px solid #646464;\n"
"    background-color: #45494a;\n"
"    color: #bbb;\n"
"    border-radius: 0;\n"
"    height: 24px;\n"
"    min-width: 30px;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbb;\n"
"    padding-left: 4px;\n"
"}\n"
"QAbstractSpinBox:focus,\n"
"QSpinBox:focus {\n"
"    outline: none;\n"
"    border: 1px solid #3b72ab;\n"
"}\n"
"QAbstractSpinBox::up-button,\n"
"QSpinBox::up-button {\n"
"    padding-top: 2px;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    height: 10px;\n"
"    border: 0;\n"
"    border-left: 1px solid #646464;\n"
"}\n"
"QAbstractSpinBox::up-button:pressed,\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: #3c3f41;\n"
"}\n"
"QAbstractSpinBox::up-arrow,\n"
"QSpinBox::up-arrow {\n"
"    image: url(images/arrow-up.png);\n"
"    width: 8px;\n"
"    height: 6px;\n"
"}\n"
"QAbstractSpinBox::up-arrow:disabled,\n"
"QAbstractSpinBox::up-arrow:off,\n"
"QSpinBox::up-arrow:disabled,\n"
"QSpinBox::up-arrow:off {\n"
"    image: url(images/arrow-up-disabled.png);\n"
"}\n"
"QAbstractSpinBox::down-button,\n"
"QSpinBox::down-button {\n"
"    padding-bottom: 2px;\n"
"    subcontrol-position: bottom right;\n"
"    width: 20px;\n"
"    height: 10px;\n"
"    border: 0;\n"
"    border-left: 1px solid #646464;\n"
"}\n"
"QAbstractSpinBox::down-button:pressed,\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: #3c3f41;\n"
"}\n"
"QAbstractSpinBox::down-arrow,\n"
"QSpinBox::down-arrow {\n"
"    image: url(images/arrow-down.png);\n"
"    width: 8px;\n"
"    height: 6px;\n"
"}\n"
"QAbstractSpinBox::down-arrow:disabled,\n"
"QAbstractSpinBox::down-arrow:off,\n"
"QSpinBox::down-arrow:disabled,\n"
"QSpinBox::down-arrow:off {\n"
"    image: url(images/arrow-down-disabled.png);\n"
"}\n"
"QAbstractSpinBox:disabled,\n"
"QAbstractSpinBox:disabled:focus,\n"
"QAbstractSpinBox::up-button:disabled,\n"
"QAbstractSpinBox::down-button:disabled,\n"
"QSpinBox:disabled,\n"
"QSpinBox:disabled:focus,\n"
"QSpinBox::up-button:disabled,\n"
"QSpinBox::down-button:disabled {\n"
"    border-color: #4f4f4f;\n"
"    color: #777777;\n"
"}\n"
"\n"
"QComboBox {\n"
"    padding-right: 20px;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #646464;\n"
"    background-color: #45494a;\n"
"    color: #bbb;\n"
"    height: 24px;\n"
"    min-width: 30px;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbb;\n"
"    border-radius: 0;\n"
"}\n"
"QComboBox:focus {\n"
"    outline: none;\n"
"    border: 1px solid #3b72ab;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #646464;\n"
"    border-radius: 0;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(images/arrow-down.png);\n"
"}\n"
"QComboBox:disabled,\n"
"QComboBox::drop-down:disabled {\n"
"    border-color: #4f4f4f;\n"
"    color: #777777;\n"
"}\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(images/arrow-down-disabled.png);\n"
"}\n"
"QComboBox::drop-down:no-frame,\n"
"QComboBox::drop-down:no-frame::disabled {\n"
"    border-color: transparent;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"QMenuBar {\n"
"    background: #3c3f41;\n"
"    padding: 0;\n"
"}\n"
"QMenuBar::item {\n"
"    spacing: 3px;\n"
"    padding: 1px 4px;\n"
"    color: #bbb;\n"
"    background: #3c3f41;\n"
"}\n"
"QMenuBar::item:selected {\n"
"    background: #2f65ca;\n"
"}\n"
"QMenuBar::item:pressed,\n"
"QMenuBar::item:hover {\n"
"    background: #2d2d2d;\n"
"}\n"
"\n"
"QMenu,\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #3c3f41;\n"
"    padding: 0;\n"
"    border: 1px solid #2d2d2d;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbb;\n"
"}\n"
"QComboBox QAbstractItemView::item {\n"
"    background-color: #3c3f41;\n"
"    color: #bbb;\n"
"    padding: 2px 5px;\n"
"}\n"
"QMenu::item {\n"
"    padding: 3px 10px 3px 27px;\n"
"    color: #bbb;\n"
"}\n"
"QMenu::item:selected:!disabled,\n"
"QComboBox QAbstractItemView::item:selected:!disabled,\n"
"QComboBox QAbstractItemView::item:focus:!disabled {\n"
"    background: #2f65ca;\n"
"    outline: none;\n"
"}\n"
"QMenu::icon,\n"
"QComboBox QAbstractItemView::icon {\n"
"    position: absolute;\n"
"    top: 1px;\n"
"    right: 1px;\n"
"    bottom: 1px;\n"
"    left: 6px;\n"
"}\n"
"QMenu::item:disabled,\n"
"QComboBox QAbstractItemView::item:disabled {\n"
"    color: #666;\n"
"}\n"
"QMenu::icon:checked,\n"
"QComboBox QAbstractItemView::icon:checked {\n"
"    background: white;\n"
"    border: 1px inset gray;\n"
"}\n"
"QMenu::separator,\n"
"QComboBox QAbstractItemView::separator {\n"
"    height: 1px;\n"
"    background: #2d2d2d;\n"
"    margin: 2px 0;\n"
"}\n"
"QMenu::indicator,\n"
"QComboBox QAbstractItemView::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"QMenu::indicator:non-exclusive:unchecked,\n"
"QMenu::indicator:non-exclusive:unchecked:selected,\n"
"QMenu::indicator:exclusive:unchecked,\n"
"QMenu::indicator:exclusive:unchecked:selected,\n"
"QComboBox QAbstractItemView::indicator:non-exclusive:unchecked,\n"
"QComboBox QAbstractItemView::indicator:non-exclusive:unchecked:selected,\n"
"QComboBox QAbstractItemView::indicator:exclusive:unchecked,\n"
"QComboBox QAbstractItemView::indicator:exclusive:unchecked:selected {\n"
"    image: none;\n"
"}\n"
"QMenu::indicator:non-exclusive:checked,\n"
"QMenu::indicator:non-exclusive:checked:selected,\n"
"QMenu::indicator:exclusive:checked,\n"
"QMenu::indicator:exclusive:checked:selected,\n"
"QComboBox QAbstractItemView::indicator:non-exclusive:checked,\n"
"QComboBox QAbstractItemView::indicator:non-exclusive:checked:selected,\n"
"QComboBox QAbstractItemView::indicator:exclusive:checked,\n"
"QComboBox QAbstractItemView::indicator:exclusive:checked:selected {\n"
"    image: url(images/checked.png);\n"
"    position: absolute;\n"
"    top: 3px;\n"
"    left: 7px;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    border: none;\n"
"    border-bottom: 1px solid #292b2d;\n"
"    background-color: #3c3f41;\n"
"    color: #bbb;\n"
"    border-radius: 0;\n"
"    min-width: 30px;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbb;\n"
"}\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    border-right: 1px solid #292b2d;\n"
"    background-color: #3c3f41;\n"
"    color: #bbb;\n"
"    border-radius: 0;\n"
"    height: 24px;\n"
"    min-width: 30px;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #bbb;\n"
"}\n"
"QHeaderView::section:disabled {\n"
"    color: #777777;\n"
"}\n"
"QHeaderView::section:last {\n"
"    border: none;\n"
"}\n"
"QHeaderView::section:checked {\n"
"    background-color: #2f65ca;\n"
"}\n"
"QHeaderView::down-arrow {\n"
"    image: url(images/arrow-up.png);\n"
"}\n"
"QHeaderView::up-arrow {\n"
"    image: url(images/arrow-down.png);\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid #646464;\n"
"    background-color: #45494a;\n"
"    border-radius: 2px;\n"
"    color: #bbb;\n"
"    height: 24px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #2f65ca;\n"
"    width: 20px;\n"
"}\n"
"\n"
"QToolTip {\n"
"    background-color: #3c3f41;\n"
"    border: 1px solid #2d2d2d;\n"
"    color: #bbb;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border: none;\n"
"    color: #888;\n"
"    background: #3c3f41;\n"
"    font-size: 11px;\n"
"}\n"
"\n"
"QStatusBar {\n"
"    border-top: 1px solid #27292a;\n"
"    background: #3c3f41;\n"
"    color: #bbb;\n"
"}\n"
"\n"
"QStatusBar QLineEdit, QStatusBar QLineEdit:focus {\n"
"    background: #e5e5e5;\n"
"    border: 1px solid #e5e5e5;\n"
"    border-radius: 2px;\n"
"    color: #333;\n"
"    font-size: 11px;\n"
"    padding: 0;\n"
"    selection-background-color: #2f65ca;\n"
"    selection-color: #ffffff;\n"
"}"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(99, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(250, 220))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/1499123092_door.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(99, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(82, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Open", None))

import dooricons_rc
