# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Hotel.ui'
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
        MainWindow.resize(753, 675)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        MainWindow.setFont(font)
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
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_84 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_84.setObjectName(_fromUtf8("gridLayout_84"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(735, 440))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_36 = QtGui.QGridLayout(self.page)
        self.gridLayout_36.setObjectName(_fromUtf8("gridLayout_36"))
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setObjectName(_fromUtf8("horizontalLayout_40"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem)
        self.label_93 = QtGui.QLabel(self.page)
        self.label_93.setMinimumSize(QtCore.QSize(300, 0))
        self.label_93.setStyleSheet(_fromUtf8("font: 75 25pt \"URW Palladio L\";\n"
"color:rgb(156, 161, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.label_93.setAlignment(QtCore.Qt.AlignCenter)
        self.label_93.setObjectName(_fromUtf8("label_93"))
        self.horizontalLayout_40.addWidget(self.label_93)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem1)
        self.gridLayout_36.addLayout(self.horizontalLayout_40, 0, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(20, 76, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_36.addItem(spacerItem2, 1, 1, 1, 1)
        self.groupBox_8 = QtGui.QGroupBox(self.page)
        self.groupBox_8.setMinimumSize(QtCore.QSize(350, 340))
        self.groupBox_8.setMaximumSize(QtCore.QSize(350, 340))
        self.groupBox_8.setStyleSheet(_fromUtf8(""))
        self.groupBox_8.setTitle(_fromUtf8(""))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridLayout_33 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_33.setObjectName(_fromUtf8("gridLayout_33"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_6 = QtGui.QLabel(self.groupBox_8)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_11.addWidget(self.label_6)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.gridLayout_33.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(156, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_33.addItem(spacerItem4, 0, 2, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.UserpassLog = QtGui.QLineEdit(self.groupBox_8)
        self.UserpassLog.setEchoMode(QtGui.QLineEdit.Password)
        self.UserpassLog.setObjectName(_fromUtf8("UserpassLog"))
        self.horizontalLayout_12.addWidget(self.UserpassLog)
        self.gridLayout_33.addLayout(self.horizontalLayout_12, 4, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.groupBox_8)
        self.label_2.setMinimumSize(QtCore.QSize(130, 121))
        self.label_2.setMaximumSize(QtCore.QSize(130, 120))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/user-login.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_33.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_31 = QtGui.QGridLayout()
        self.gridLayout_31.setObjectName(_fromUtf8("gridLayout_31"))
        self.UserNameLog = QtGui.QLineEdit(self.groupBox_8)
        self.UserNameLog.setObjectName(_fromUtf8("UserNameLog"))
        self.gridLayout_31.addWidget(self.UserNameLog, 0, 0, 1, 1)
        self.gridLayout_33.addLayout(self.gridLayout_31, 2, 0, 1, 3)
        self.gridLayout_30 = QtGui.QGridLayout()
        self.gridLayout_30.setObjectName(_fromUtf8("gridLayout_30"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem5, 0, 0, 1, 1)
        self.LogBtn = QtGui.QPushButton(self.groupBox_8)
        self.LogBtn.setMinimumSize(QtCore.QSize(82, 30))
        self.LogBtn.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255)"))
        self.LogBtn.setObjectName(_fromUtf8("LogBtn"))
        self.gridLayout_30.addWidget(self.LogBtn, 0, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(13, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem6, 0, 2, 1, 1)
        self.gridLayout_33.addLayout(self.gridLayout_30, 6, 0, 1, 3)
        spacerItem7 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_33.addItem(spacerItem7, 5, 1, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_4 = QtGui.QLabel(self.groupBox_8)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.gridLayout_33.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout_36.addWidget(self.groupBox_8, 2, 1, 2, 1)
        spacerItem9 = QtGui.QSpacerItem(174, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_36.addItem(spacerItem9, 2, 2, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(175, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_36.addItem(spacerItem10, 3, 0, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_36.addItem(spacerItem11, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.label_43 = QtGui.QLabel(self.page_2)
        self.label_43.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet(_fromUtf8("font: 75 25pt \"URW Palladio L\";\n"
"color:rgb(156, 161, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.horizontalLayout_4.addWidget(self.label_43)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_35 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_35.setContentsMargins(-1, 30, -1, 30)
        self.gridLayout_35.setVerticalSpacing(30)
        self.gridLayout_35.setObjectName(_fromUtf8("gridLayout_35"))
        self.DispBTN = QtGui.QPushButton(self.groupBox_2)
        self.DispBTN.setMinimumSize(QtCore.QSize(82, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.DispBTN.setFont(font)
        self.DispBTN.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255)"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/if_computer__desktop__monitor__technology__screen__television__display_2317714.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DispBTN.setIcon(icon)
        self.DispBTN.setObjectName(_fromUtf8("DispBTN"))
        self.gridLayout_35.addWidget(self.DispBTN, 1, 0, 1, 1)
        self.AddBTN = QtGui.QPushButton(self.groupBox_2)
        self.AddBTN.setMinimumSize(QtCore.QSize(82, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.AddBTN.setFont(font)
        self.AddBTN.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255)"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/if_icon-81-document-add_314445.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AddBTN.setIcon(icon1)
        self.AddBTN.setObjectName(_fromUtf8("AddBTN"))
        self.gridLayout_35.addWidget(self.AddBTN, 0, 0, 1, 1)
        self.EditBTN = QtGui.QPushButton(self.groupBox_2)
        self.EditBTN.setMinimumSize(QtCore.QSize(82, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.EditBTN.setFont(font)
        self.EditBTN.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255)"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/if_icon-32-clipboard-edit_314288.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EditBTN.setIcon(icon2)
        self.EditBTN.setObjectName(_fromUtf8("EditBTN"))
        self.gridLayout_35.addWidget(self.EditBTN, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.groupBox_12 = QtGui.QGroupBox(self.page_2)
        self.groupBox_12.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.gridLayout_45 = QtGui.QGridLayout(self.groupBox_12)
        self.gridLayout_45.setContentsMargins(-1, 20, -1, 30)
        self.gridLayout_45.setVerticalSpacing(50)
        self.gridLayout_45.setObjectName(_fromUtf8("gridLayout_45"))
        self.LogOutBTN = QtGui.QPushButton(self.groupBox_12)
        self.LogOutBTN.setMinimumSize(QtCore.QSize(82, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.LogOutBTN.setFont(font)
        self.LogOutBTN.setStyleSheet(_fromUtf8("color:rgb(255, 92, 51)"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/power-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LogOutBTN.setIcon(icon3)
        self.LogOutBTN.setFlat(False)
        self.LogOutBTN.setObjectName(_fromUtf8("LogOutBTN"))
        self.gridLayout_45.addWidget(self.LogOutBTN, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_12)
        self.pushButton.setMinimumSize(QtCore.QSize(82, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255);\n"
"font: 75 15pt \"URW Palladio L\";"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/ff5c491e7e1f33dcd3756831d7ca2d72.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_45.addWidget(self.pushButton, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_12)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        spacerItem17 = QtGui.QSpacerItem(13, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.label_8 = QtGui.QLabel(self.page_2)
        self.label_8.setMaximumSize(QtCore.QSize(700, 16777215))
        self.label_8.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(76, 76, 76, 0), stop:0.5 rgba(42, 41, 42, 0), stop:0.995283 rgba(76, 76, 76, 0))"))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/Hotel-HD-wallpapers.jpg")))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem18 = QtGui.QSpacerItem(37, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem18)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 1)
        self.horizontalLayout_8.setStretch(4, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem19, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.gridLayout_82 = QtGui.QGridLayout(self.page_3)
        self.gridLayout_82.setObjectName(_fromUtf8("gridLayout_82"))
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setObjectName(_fromUtf8("horizontalLayout_39"))
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem20)
        self.label_45 = QtGui.QLabel(self.page_3)
        self.label_45.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet(_fromUtf8("font: 75 25pt \"URW Palladio L\";\n"
"color:rgb(156, 161, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.label_45.setAlignment(QtCore.Qt.AlignCenter)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.horizontalLayout_39.addWidget(self.label_45)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem21)
        self.gridLayout_82.addLayout(self.horizontalLayout_39, 0, 0, 1, 1)
        self.groupBox_26 = QtGui.QGroupBox(self.page_3)
        self.groupBox_26.setTitle(_fromUtf8(""))
        self.groupBox_26.setObjectName(_fromUtf8("groupBox_26"))
        self.gridLayout_83 = QtGui.QGridLayout(self.groupBox_26)
        self.gridLayout_83.setObjectName(_fromUtf8("gridLayout_83"))
        self.groupBox_25 = QtGui.QGroupBox(self.groupBox_26)
        self.groupBox_25.setStyleSheet(_fromUtf8("border:1px solid rgb(58, 58, 58)"))
        self.groupBox_25.setObjectName(_fromUtf8("groupBox_25"))
        self.gridLayout_80 = QtGui.QGridLayout(self.groupBox_25)
        self.gridLayout_80.setObjectName(_fromUtf8("gridLayout_80"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem22)
        self.ShootBtN = QtGui.QPushButton(self.groupBox_25)
        self.ShootBtN.setMinimumSize(QtCore.QSize(82, 30))
        self.ShootBtN.setObjectName(_fromUtf8("ShootBtN"))
        self.horizontalLayout.addWidget(self.ShootBtN)
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem23)
        self.gridLayout_80.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.CameraLB = QtGui.QLabel(self.groupBox_25)
        self.CameraLB.setMinimumSize(QtCore.QSize(405, 170))
        self.CameraLB.setMaximumSize(QtCore.QSize(500, 650))
        self.CameraLB.setStyleSheet(_fromUtf8(""))
        self.CameraLB.setText(_fromUtf8(""))
        self.CameraLB.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/person-icon-1675.png")))
        self.CameraLB.setScaledContents(True)
        self.CameraLB.setObjectName(_fromUtf8("CameraLB"))
        self.gridLayout_80.addWidget(self.CameraLB, 0, 1, 1, 1)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_80.addItem(spacerItem24, 0, 0, 1, 1)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_80.addItem(spacerItem25, 0, 2, 1, 1)
        self.gridLayout_83.addWidget(self.groupBox_25, 0, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.groupBox_26)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_7.addWidget(self.label_7)
        self.timeEdit_2 = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit_2.setMinimumSize(QtCore.QSize(56, 0))
        self.timeEdit_2.setMaximumSize(QtCore.QSize(116, 16777215))
        self.timeEdit_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEdit_2.setObjectName(_fromUtf8("timeEdit_2"))
        self.horizontalLayout_7.addWidget(self.timeEdit_2)
        spacerItem26 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem26)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.calendarWidget = QtGui.QCalendarWidget(self.groupBox)
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.gridLayout_3.addWidget(self.calendarWidget, 8, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_10.addWidget(self.label_16)
        self.dateEdit_2 = QtGui.QDateEdit(self.groupBox)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(56, 0))
        self.dateEdit_2.setMaximumSize(QtCore.QSize(116, 16777215))
        self.dateEdit_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayout_10.addWidget(self.dateEdit_2)
        spacerItem27 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem27)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.timeEdit = QtGui.QTimeEdit(self.groupBox)
        self.timeEdit.setMinimumSize(QtCore.QSize(56, 0))
        self.timeEdit.setMaximumSize(QtCore.QSize(116, 16777215))
        self.timeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeEdit.setObjectName(_fromUtf8("timeEdit"))
        self.horizontalLayout_5.addWidget(self.timeEdit)
        spacerItem28 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem28)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_5.addWidget(self.label_13)
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_5.addWidget(self.label_14)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_5.addWidget(self.label_11)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_5.addWidget(self.label_12)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.RoomCB = QtGui.QComboBox(self.groupBox)
        self.RoomCB.setMinimumSize(QtCore.QSize(56, 0))
        self.RoomCB.setObjectName(_fromUtf8("RoomCB"))
        self.RoomCB.addItem(_fromUtf8(""))
        self.RoomCB.addItem(_fromUtf8(""))
        self.RoomCB.addItem(_fromUtf8(""))
        self.verticalLayout_6.addWidget(self.RoomCB)
        self.PersonCB = QtGui.QComboBox(self.groupBox)
        self.PersonCB.setObjectName(_fromUtf8("PersonCB"))
        self.PersonCB.addItem(_fromUtf8(""))
        self.PersonCB.addItem(_fromUtf8(""))
        self.verticalLayout_6.addWidget(self.PersonCB)
        self.REGNAME = QtGui.QLineEdit(self.groupBox)
        self.REGNAME.setObjectName(_fromUtf8("REGNAME"))
        self.verticalLayout_6.addWidget(self.REGNAME)
        self.REGNID = QtGui.QLineEdit(self.groupBox)
        self.REGNID.setObjectName(_fromUtf8("REGNID"))
        self.verticalLayout_6.addWidget(self.REGNID)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_9.addWidget(self.label_15)
        self.dateEdit = QtGui.QDateEdit(self.groupBox)
        self.dateEdit.setMinimumSize(QtCore.QSize(56, 0))
        self.dateEdit.setMaximumSize(QtCore.QSize(116, 16777215))
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_9.addWidget(self.dateEdit)
        spacerItem29 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem29)
        self.gridLayout_3.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 4, 0, 1, 1)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout_3.addWidget(self.line_3, 7, 0, 1, 1)
        self.gridLayout_83.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem30 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_83.addItem(spacerItem30, 0, 1, 1, 1)
        self.gridLayout_82.addWidget(self.groupBox_26, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem31 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem31)
        self.pushButton_10 = QtGui.QPushButton(self.page_3)
        self.pushButton_10.setMinimumSize(QtCore.QSize(82, 30))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_9 = QtGui.QPushButton(self.page_3)
        self.pushButton_9.setMinimumSize(QtCore.QSize(82, 30))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.gridLayout_82.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_6 = QtGui.QWidget()
        self.page_6.setObjectName(_fromUtf8("page_6"))
        self.gridLayout_18 = QtGui.QGridLayout(self.page_6)
        self.gridLayout_18.setObjectName(_fromUtf8("gridLayout_18"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem32 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem32)
        self.label_47 = QtGui.QLabel(self.page_6)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(_fromUtf8("font: 75 25pt \"URW Palladio L\";\n"
"color:rgb(156, 161, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.horizontalLayout_14.addWidget(self.label_47)
        spacerItem33 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem33)
        self.gridLayout_18.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)
        self.groupBox_6 = QtGui.QGroupBox(self.page_6)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 120))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout_13 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_13.setObjectName(_fromUtf8("gridLayout_13"))
        spacerItem34 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem34, 0, 0, 1, 1)
        self.gridLayout_19 = QtGui.QGridLayout()
        self.gridLayout_19.setObjectName(_fromUtf8("gridLayout_19"))
        self.gridLayout_20 = QtGui.QGridLayout()
        self.gridLayout_20.setObjectName(_fromUtf8("gridLayout_20"))
        self.label_25 = QtGui.QLabel(self.groupBox_6)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_20.addWidget(self.label_25, 1, 0, 1, 1)
        self.label_26 = QtGui.QLabel(self.groupBox_6)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout_20.addWidget(self.label_26, 0, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_20, 0, 0, 1, 1)
        self.gridLayout_21 = QtGui.QGridLayout()
        self.gridLayout_21.setObjectName(_fromUtf8("gridLayout_21"))
        self.comboBox_5 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.comboBox_5.addItem(_fromUtf8(""))
        self.gridLayout_21.addWidget(self.comboBox_5, 0, 0, 1, 1)
        self.comboBox_6 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_6.setObjectName(_fromUtf8("comboBox_6"))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.comboBox_6.addItem(_fromUtf8(""))
        self.gridLayout_21.addWidget(self.comboBox_6, 1, 0, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_21, 0, 1, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_19, 1, 0, 1, 1)
        spacerItem35 = QtGui.QSpacerItem(510, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem35, 1, 1, 1, 1)
        spacerItem36 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem36, 2, 0, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.groupBox_7 = QtGui.QGroupBox(self.page_6)
        self.groupBox_7.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridLayout_22 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_22.setObjectName(_fromUtf8("gridLayout_22"))
        spacerItem37 = QtGui.QSpacerItem(31, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem37, 1, 3, 1, 1)
        spacerItem38 = QtGui.QSpacerItem(20, 4, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem38, 0, 0, 1, 1)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_26 = QtGui.QGridLayout()
        self.gridLayout_26.setObjectName(_fromUtf8("gridLayout_26"))
        self.gridLayout_27 = QtGui.QGridLayout()
        self.gridLayout_27.setObjectName(_fromUtf8("gridLayout_27"))
        self.label_31 = QtGui.QLabel(self.groupBox_7)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout_27.addWidget(self.label_31, 0, 0, 1, 1)
        self.label_32 = QtGui.QLabel(self.groupBox_7)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.gridLayout_27.addWidget(self.label_32, 1, 0, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_27, 0, 0, 1, 1)
        self.gridLayout_28 = QtGui.QGridLayout()
        self.gridLayout_28.setObjectName(_fromUtf8("gridLayout_28"))
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.gridLayout_28.addWidget(self.lineEdit_15, 0, 0, 1, 1)
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.gridLayout_28.addWidget(self.lineEdit_16, 1, 0, 1, 1)
        self.gridLayout_26.addLayout(self.gridLayout_28, 0, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_26)
        spacerItem39 = QtGui.QSpacerItem(28, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem39)
        self.gridLayout_22.addLayout(self.verticalLayout_4, 1, 2, 1, 1)
        self.gridLayout_23 = QtGui.QGridLayout()
        self.gridLayout_23.setObjectName(_fromUtf8("gridLayout_23"))
        self.gridLayout_25 = QtGui.QGridLayout()
        self.gridLayout_25.setObjectName(_fromUtf8("gridLayout_25"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.gridLayout_25.addWidget(self.lineEdit_7, 0, 0, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.gridLayout_25.addWidget(self.lineEdit_8, 1, 0, 1, 1)
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.gridLayout_25.addWidget(self.lineEdit_14, 2, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_25, 0, 1, 1, 1)
        self.gridLayout_24 = QtGui.QGridLayout()
        self.gridLayout_24.setObjectName(_fromUtf8("gridLayout_24"))
        self.label_27 = QtGui.QLabel(self.groupBox_7)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_24.addWidget(self.label_27, 2, 0, 1, 1)
        self.label_28 = QtGui.QLabel(self.groupBox_7)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_24.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_29 = QtGui.QLabel(self.groupBox_7)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_24.addWidget(self.label_29, 0, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_24, 0, 0, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_23, 1, 0, 1, 1)
        spacerItem40 = QtGui.QSpacerItem(32, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem40, 1, 1, 1, 1)
        spacerItem41 = QtGui.QSpacerItem(20, 32, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_22.addItem(spacerItem41, 2, 1, 1, 1)
        self.gridLayout_18.addWidget(self.groupBox_7, 2, 0, 1, 1)
        spacerItem42 = QtGui.QSpacerItem(20, 121, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem42, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem43 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem43)
        self.pushButton_14 = QtGui.QPushButton(self.page_6)
        self.pushButton_14.setMinimumSize(QtCore.QSize(82, 30))
        self.pushButton_14.setMaximumSize(QtCore.QSize(88, 16777215))
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.horizontalLayout_3.addWidget(self.pushButton_14)
        self.pushButton_15 = QtGui.QPushButton(self.page_6)
        self.pushButton_15.setMinimumSize(QtCore.QSize(82, 30))
        self.pushButton_15.setMaximumSize(QtCore.QSize(88, 16777215))
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.horizontalLayout_3.addWidget(self.pushButton_15)
        self.gridLayout_18.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtGui.QWidget()
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.tabWidget = QtGui.QTabWidget(self.page_7)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 771, 411))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label_44 = QtGui.QLabel(self.page_7)
        self.label_44.setGeometry(QtCore.QRect(290, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(_fromUtf8("font: 75 25pt \"URW Palladio L\";\n"
"color:rgb(198, 198, 198)"))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.stackedWidget.addWidget(self.page_7)
        self.gridLayout_84.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.groupBox_27 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_27.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.groupBox_27.setTitle(_fromUtf8(""))
        self.groupBox_27.setObjectName(_fromUtf8("groupBox_27"))
        self.gridLayout_17 = QtGui.QGridLayout(self.groupBox_27)
        self.gridLayout_17.setMargin(0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(_fromUtf8("gridLayout_17"))
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_3 = QtGui.QLabel(self.groupBox_27)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("URW Palladio L"))
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(88, 124, 255);\n"
"font: 75 26pt \"URW Palladio L\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_6.addWidget(self.label_3, 0, 2, 1, 1)
        spacerItem44 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem44, 0, 3, 1, 1)
        spacerItem45 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem45, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_27)
        self.label.setMaximumSize(QtCore.QSize(240, 100))
        self.label.setAutoFillBackground(False)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/1.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_17.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        self.gridLayout_84.addWidget(self.groupBox_27, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Home", None))
        self.label_93.setText(_translate("MainWindow", "Log in page", None))
        self.label_6.setText(_translate("MainWindow", "Password :", None))
        self.LogBtn.setText(_translate("MainWindow", "Log In", None))
        self.label_4.setText(_translate("MainWindow", "Name :", None))
        self.label_43.setText(_translate("MainWindow", "Main menu", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Resident section", None))
        self.DispBTN.setText(_translate("MainWindow", "View", None))
        self.AddBTN.setText(_translate("MainWindow", "Add", None))
        self.EditBTN.setText(_translate("MainWindow", "Update", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "Settings", None))
        self.LogOutBTN.setText(_translate("MainWindow", "Log out", None))
        self.pushButton.setText(_translate("MainWindow", "Hotel assistant", None))
        self.label_45.setText(_translate("MainWindow", "Registration Page", None))
        self.groupBox_25.setTitle(_translate("MainWindow", "Camera", None))
        self.ShootBtN.setText(_translate("MainWindow", "Shoot", None))
        self.groupBox.setTitle(_translate("MainWindow", "Resident Data", None))
        self.label_7.setText(_translate("MainWindow", "Ending time  ", None))
        self.label_16.setText(_translate("MainWindow", "Ending date  ", None))
        self.label_5.setText(_translate("MainWindow", "Starting time", None))
        self.label_13.setText(_translate("MainWindow", "Room", None))
        self.label_14.setText(_translate("MainWindow", "Pesron", None))
        self.label_11.setText(_translate("MainWindow", "Name", None))
        self.label_12.setText(_translate("MainWindow", "NID", None))
        self.RoomCB.setItemText(0, _translate("MainWindow", "Room One", None))
        self.RoomCB.setItemText(1, _translate("MainWindow", "Room Two", None))
        self.RoomCB.setItemText(2, _translate("MainWindow", "Room Three", None))
        self.PersonCB.setItemText(0, _translate("MainWindow", "One", None))
        self.PersonCB.setItemText(1, _translate("MainWindow", "Two", None))
        self.label_15.setText(_translate("MainWindow", "Starting date", None))
        self.pushButton_10.setText(_translate("MainWindow", "Cancel", None))
        self.pushButton_9.setText(_translate("MainWindow", "Save", None))
        self.label_47.setText(_translate("MainWindow", "Updating Data Page", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Room & Person", None))
        self.label_25.setText(_translate("MainWindow", "Person", None))
        self.label_26.setText(_translate("MainWindow", "Room", None))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Room One", None))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Room Two", None))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Room Three", None))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "One", None))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "two", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Person Details", None))
        self.label_31.setText(_translate("MainWindow", "NID", None))
        self.label_32.setText(_translate("MainWindow", "Ending Date", None))
        self.label_27.setText(_translate("MainWindow", "Duration", None))
        self.label_28.setText(_translate("MainWindow", "Starting Date", None))
        self.label_29.setText(_translate("MainWindow", "Name:", None))
        self.pushButton_14.setText(_translate("MainWindow", "Cancel", None))
        self.pushButton_15.setText(_translate("MainWindow", "update", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.label_44.setText(_translate("MainWindow", "View Page", None))
        self.label_3.setText(_translate("MainWindow", "Hotel Registration System", None))

import icons_rc
