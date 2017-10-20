# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manger.ui'
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
        MainWindow.resize(807, 633)
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
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setMinimumSize(QtCore.QSize(88, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_9 = QtGui.QWidget()
        self.page_9.setObjectName(_fromUtf8("page_9"))
        self.gridLayout_3 = QtGui.QGridLayout(self.page_9)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.page_9)
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        self.label.setStyleSheet(_fromUtf8("font: 75 25pt \"URW Palladio L\";\n"
"color:rgb(156, 161, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(17, 76, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(175, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 2, 0, 1, 1)
        self.groupBox_11 = QtGui.QGroupBox(self.page_9)
        self.groupBox_11.setMinimumSize(QtCore.QSize(350, 340))
        self.groupBox_11.setMaximumSize(QtCore.QSize(350, 340))
        self.groupBox_11.setStyleSheet(_fromUtf8(""))
        self.groupBox_11.setTitle(_fromUtf8(""))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridLayout_37 = QtGui.QGridLayout(self.groupBox_11)
        self.gridLayout_37.setObjectName(_fromUtf8("gridLayout_37"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_7 = QtGui.QLabel(self.groupBox_11)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_13.addWidget(self.label_7)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.gridLayout_37.addLayout(self.horizontalLayout_13, 3, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(156, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_37.addItem(spacerItem5, 0, 2, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.UserpassLog_2 = QtGui.QLineEdit(self.groupBox_11)
        self.UserpassLog_2.setEchoMode(QtGui.QLineEdit.Password)
        self.UserpassLog_2.setObjectName(_fromUtf8("UserpassLog_2"))
        self.horizontalLayout_14.addWidget(self.UserpassLog_2)
        self.gridLayout_37.addLayout(self.horizontalLayout_14, 4, 0, 1, 3)
        self.label_5 = QtGui.QLabel(self.groupBox_11)
        self.label_5.setMinimumSize(QtCore.QSize(110, 121))
        self.label_5.setMaximumSize(QtCore.QSize(110, 120))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/manager-312603_1280.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_37.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridLayout_38 = QtGui.QGridLayout()
        self.gridLayout_38.setObjectName(_fromUtf8("gridLayout_38"))
        self.UserNameLog_2 = QtGui.QLineEdit(self.groupBox_11)
        self.UserNameLog_2.setObjectName(_fromUtf8("UserNameLog_2"))
        self.gridLayout_38.addWidget(self.UserNameLog_2, 0, 0, 1, 1)
        self.gridLayout_37.addLayout(self.gridLayout_38, 2, 0, 1, 3)
        self.gridLayout_39 = QtGui.QGridLayout()
        self.gridLayout_39.setObjectName(_fromUtf8("gridLayout_39"))
        spacerItem6 = QtGui.QSpacerItem(13, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_39.addItem(spacerItem6, 0, 2, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_39.addItem(spacerItem7, 0, 0, 1, 1)
        self.LogBtn_2 = QtGui.QPushButton(self.groupBox_11)
        self.LogBtn_2.setMinimumSize(QtCore.QSize(82, 30))
        self.LogBtn_2.setStyleSheet(_fromUtf8("color:rgb(85, 170, 255)"))
        self.LogBtn_2.setObjectName(_fromUtf8("LogBtn_2"))
        self.gridLayout_39.addWidget(self.LogBtn_2, 0, 1, 1, 1)
        self.gridLayout_37.addLayout(self.gridLayout_39, 6, 0, 1, 3)
        spacerItem8 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_37.addItem(spacerItem8, 5, 1, 1, 1)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_11)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_8.addWidget(self.label_9)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem9)
        self.gridLayout_37.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_11, 2, 1, 2, 1)
        spacerItem10 = QtGui.QSpacerItem(174, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem10, 3, 2, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(17, 75, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem11, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_9)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_5 = QtGui.QGridLayout(self.page)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        spacerItem12 = QtGui.QSpacerItem(45, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem12, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.pushButton_3 = QtGui.QPushButton(self.page)
        self.pushButton_3.setMinimumSize(QtCore.QSize(200, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/Add group.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem14)
        self.pushButton_2 = QtGui.QPushButton(self.page)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 150))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/Delete group.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(44, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem16, 0, 2, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem17)
        self.label_4 = QtGui.QLabel(self.page)
        self.label_4.setMaximumSize(QtCore.QSize(400, 300))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/1.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 3, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(45, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem19, 0, 4, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_8 = QtGui.QWidget()
        self.page_8.setObjectName(_fromUtf8("page_8"))
        self.gridLayout_2 = QtGui.QGridLayout(self.page_8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem20)
        self.label_2 = QtGui.QLabel(self.page_8)
        self.label_2.setMinimumSize(QtCore.QSize(300, 0))
        self.label_2.setStyleSheet(_fromUtf8("font: 75 25pt \"URW Palladio L\";\n"
"color:rgb(156, 161, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem21 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem21)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        spacerItem22 = QtGui.QSpacerItem(20, 167, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem22, 1, 1, 1, 1)
        self.groupBox_9 = QtGui.QGroupBox(self.page_8)
        self.groupBox_9.setMinimumSize(QtCore.QSize(350, 380))
        self.groupBox_9.setMaximumSize(QtCore.QSize(350, 380))
        self.groupBox_9.setStyleSheet(_fromUtf8(""))
        self.groupBox_9.setTitle(_fromUtf8(""))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.gridLayout_34 = QtGui.QGridLayout(self.groupBox_9)
        self.gridLayout_34.setObjectName(_fromUtf8("gridLayout_34"))
        self.label_30 = QtGui.QLabel(self.groupBox_9)
        self.label_30.setMinimumSize(QtCore.QSize(120, 120))
        self.label_30.setMaximumSize(QtCore.QSize(120, 110))
        self.label_30.setText(_fromUtf8(""))
        self.label_30.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/Add group.png")))
        self.label_30.setScaledContents(True)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.gridLayout_34.addWidget(self.label_30, 0, 0, 1, 1)
        spacerItem23 = QtGui.QSpacerItem(156, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_34.addItem(spacerItem23, 0, 1, 1, 1)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_33 = QtGui.QLabel(self.groupBox_9)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_17.addWidget(self.label_33)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem24)
        self.gridLayout_34.addLayout(self.horizontalLayout_17, 1, 0, 1, 2)
        self.UserNameLog_3 = QtGui.QLineEdit(self.groupBox_9)
        self.UserNameLog_3.setObjectName(_fromUtf8("UserNameLog_3"))
        self.gridLayout_34.addWidget(self.UserNameLog_3, 2, 0, 1, 2)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_10 = QtGui.QLabel(self.groupBox_9)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_15.addWidget(self.label_10)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem25)
        self.gridLayout_34.addLayout(self.horizontalLayout_15, 3, 0, 1, 2)
        self.UserpassLog_3 = QtGui.QLineEdit(self.groupBox_9)
        self.UserpassLog_3.setEchoMode(QtGui.QLineEdit.Password)
        self.UserpassLog_3.setObjectName(_fromUtf8("UserpassLog_3"))
        self.gridLayout_34.addWidget(self.UserpassLog_3, 4, 0, 1, 2)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_34 = QtGui.QLabel(self.groupBox_9)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.horizontalLayout_18.addWidget(self.label_34)
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem26)
        self.gridLayout_34.addLayout(self.horizontalLayout_18, 5, 0, 1, 2)
        self.UserpassLog_4 = QtGui.QLineEdit(self.groupBox_9)
        self.UserpassLog_4.setEchoMode(QtGui.QLineEdit.Password)
        self.UserpassLog_4.setObjectName(_fromUtf8("UserpassLog_4"))
        self.gridLayout_34.addWidget(self.UserpassLog_4, 6, 0, 1, 2)
        self.gridLayout_41 = QtGui.QGridLayout()
        self.gridLayout_41.setObjectName(_fromUtf8("gridLayout_41"))
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_41.addItem(spacerItem27, 0, 0, 1, 1)
        self.LogBtn_3 = QtGui.QPushButton(self.groupBox_9)
        self.LogBtn_3.setMinimumSize(QtCore.QSize(82, 30))
        self.LogBtn_3.setStyleSheet(_fromUtf8("color:rgb(31, 170, 31)"))
        self.LogBtn_3.setObjectName(_fromUtf8("LogBtn_3"))
        self.gridLayout_41.addWidget(self.LogBtn_3, 0, 2, 1, 1)
        spacerItem28 = QtGui.QSpacerItem(13, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_41.addItem(spacerItem28, 0, 3, 1, 1)
        self.pushButton = QtGui.QPushButton(self.groupBox_9)
        self.pushButton.setMinimumSize(QtCore.QSize(82, 30))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_41.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_34.addLayout(self.gridLayout_41, 7, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_9, 2, 1, 2, 1)
        spacerItem29 = QtGui.QSpacerItem(285, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem29, 2, 2, 1, 1)
        spacerItem30 = QtGui.QSpacerItem(285, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem30, 3, 0, 1, 1)
        spacerItem31 = QtGui.QSpacerItem(20, 166, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem31, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_8)
        self.page_10 = QtGui.QWidget()
        self.page_10.setObjectName(_fromUtf8("page_10"))
        self.gridLayout_4 = QtGui.QGridLayout(self.page_10)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem32 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem32)
        self.label_3 = QtGui.QLabel(self.page_10)
        self.label_3.setMinimumSize(QtCore.QSize(300, 0))
        self.label_3.setStyleSheet(_fromUtf8("font: 75 25pt \"URW Palladio L\";\n"
"color:rgb(156, 161, 255);\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem33 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem33)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 4)
        spacerItem34 = QtGui.QSpacerItem(20, 23, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem34, 1, 2, 1, 1)
        self.groupBox_10 = QtGui.QGroupBox(self.page_10)
        self.groupBox_10.setMinimumSize(QtCore.QSize(350, 340))
        self.groupBox_10.setMaximumSize(QtCore.QSize(350, 340))
        self.groupBox_10.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(76, 76, 76, 255), stop:0.502347 rgba(42, 41, 42, 255), stop:1 rgba(76, 76, 76, 255));"))
        self.groupBox_10.setTitle(_fromUtf8(""))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.gridLayout_42 = QtGui.QGridLayout(self.groupBox_10)
        self.gridLayout_42.setObjectName(_fromUtf8("gridLayout_42"))
        self.label_41 = QtGui.QLabel(self.groupBox_10)
        self.label_41.setMinimumSize(QtCore.QSize(120, 121))
        self.label_41.setMaximumSize(QtCore.QSize(120, 120))
        self.label_41.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(76, 76, 76, 0), stop:0.5 rgba(42, 41, 42, 0), stop:1 rgba(76, 76, 76, 0))"))
        self.label_41.setText(_fromUtf8(""))
        self.label_41.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/Icons/Delete group.png")))
        self.label_41.setScaledContents(True)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_42.addWidget(self.label_41, 0, 0, 1, 1)
        spacerItem35 = QtGui.QSpacerItem(156, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_42.addItem(spacerItem35, 0, 2, 1, 1)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_42 = QtGui.QLabel(self.groupBox_10)
        self.label_42.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0.502347 rgba(42, 41, 42, 0), stop:1 rgba(76, 76, 76, 0))"))
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.horizontalLayout_20.addWidget(self.label_42)
        spacerItem36 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem36)
        self.gridLayout_42.addLayout(self.horizontalLayout_20, 1, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.groupBox_10)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_42.addWidget(self.comboBox, 2, 0, 1, 3)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_40 = QtGui.QLabel(self.groupBox_10)
        self.label_40.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(76, 76, 76, 0), stop:0.5 rgba(42, 41, 42, 0), stop:1 rgba(76, 76, 76, 0))"))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.horizontalLayout_16.addWidget(self.label_40)
        spacerItem37 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem37)
        self.gridLayout_42.addLayout(self.horizontalLayout_16, 3, 0, 1, 1)
        self.UserpassLog_5 = QtGui.QLineEdit(self.groupBox_10)
        self.UserpassLog_5.setEchoMode(QtGui.QLineEdit.Password)
        self.UserpassLog_5.setObjectName(_fromUtf8("UserpassLog_5"))
        self.gridLayout_42.addWidget(self.UserpassLog_5, 4, 0, 1, 3)
        spacerItem38 = QtGui.QSpacerItem(20, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_42.addItem(spacerItem38, 5, 1, 1, 1)
        self.gridLayout_44 = QtGui.QGridLayout()
        self.gridLayout_44.setObjectName(_fromUtf8("gridLayout_44"))
        self.SignBtn_2 = QtGui.QPushButton(self.groupBox_10)
        self.SignBtn_2.setMinimumSize(QtCore.QSize(82, 30))
        self.SignBtn_2.setStyleSheet(_fromUtf8("color:rgb(255, 92, 51);\n"
"background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255));"))
        self.SignBtn_2.setObjectName(_fromUtf8("SignBtn_2"))
        self.gridLayout_44.addWidget(self.SignBtn_2, 0, 2, 1, 1)
        self.LogBtn_4 = QtGui.QPushButton(self.groupBox_10)
        self.LogBtn_4.setMinimumSize(QtCore.QSize(82, 30))
        self.LogBtn_4.setStyleSheet(_fromUtf8("background-color:qlineargradient(spread:pad, x1:0.600329, y1:1, x2:0.600939, y2:0, stop:0 rgba(97, 97, 97, 255), stop:0.502347 rgba(65, 63, 65, 255), stop:1 rgba(95, 95, 95, 255))"))
        self.LogBtn_4.setObjectName(_fromUtf8("LogBtn_4"))
        self.gridLayout_44.addWidget(self.LogBtn_4, 0, 1, 1, 1)
        spacerItem39 = QtGui.QSpacerItem(13, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_44.addItem(spacerItem39, 0, 3, 1, 1)
        spacerItem40 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_44.addItem(spacerItem40, 0, 0, 1, 1)
        self.gridLayout_42.addLayout(self.gridLayout_44, 6, 0, 1, 3)
        self.gridLayout_4.addWidget(self.groupBox_10, 2, 1, 2, 2)
        spacerItem41 = QtGui.QSpacerItem(172, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem41, 2, 3, 1, 1)
        spacerItem42 = QtGui.QSpacerItem(173, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem42, 3, 0, 1, 1)
        spacerItem43 = QtGui.QSpacerItem(20, 22, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem43, 4, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_10)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Log in Page", None))
        self.label_7.setText(_translate("MainWindow", "Password :", None))
        self.LogBtn_2.setText(_translate("MainWindow", "Log In", None))
        self.label_9.setText(_translate("MainWindow", "Name :", None))
        self.pushButton_3.setText(_translate("MainWindow", "Add User", None))
        self.pushButton_2.setText(_translate("MainWindow", "Delete User", None))
        self.label_2.setText(_translate("MainWindow", "Add user Page", None))
        self.label_33.setText(_translate("MainWindow", "Name :", None))
        self.label_10.setText(_translate("MainWindow", "Password :", None))
        self.label_34.setText(_translate("MainWindow", "Confirm password:", None))
        self.LogBtn_3.setText(_translate("MainWindow", "Save", None))
        self.pushButton.setText(_translate("MainWindow", "Cancel", None))
        self.label_3.setText(_translate("MainWindow", "Delete user Page", None))
        self.label_42.setText(_translate("MainWindow", "Name :", None))
        self.label_40.setText(_translate("MainWindow", "Master password :", None))
        self.SignBtn_2.setText(_translate("MainWindow", "Delete", None))
        self.LogBtn_4.setText(_translate("MainWindow", "Cancel", None))

import icons_rc
