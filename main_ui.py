# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(921, 506)
        icon = QIcon()
        icon.addFile(u":/images/ms_icon.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.newFile_action = QAction(MainWindow)
        self.newFile_action.setObjectName(u"newFile_action")
        self.about_action = QAction(MainWindow)
        self.about_action.setObjectName(u"about_action")
        self.open_action = QAction(MainWindow)
        self.open_action.setObjectName(u"open_action")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.newFile_button = QPushButton(self.centralwidget)
        self.newFile_button.setObjectName(u"newFile_button")

        self.horizontalLayout_4.addWidget(self.newFile_button)

        self.select_button = QPushButton(self.centralwidget)
        self.select_button.setObjectName(u"select_button")

        self.horizontalLayout_4.addWidget(self.select_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_edit = QLineEdit(self.centralwidget)
        self.name_edit.setObjectName(u"name_edit")
        font = QFont()
        font.setPointSize(12)
        self.name_edit.setFont(font)

        self.horizontalLayout.addWidget(self.name_edit)

        self.title_edit = QLineEdit(self.centralwidget)
        self.title_edit.setObjectName(u"title_edit")
        self.title_edit.setFont(font)

        self.horizontalLayout.addWidget(self.title_edit)

        self.department_edit = QLineEdit(self.centralwidget)
        self.department_edit.setObjectName(u"department_edit")
        self.department_edit.setFont(font)

        self.horizontalLayout.addWidget(self.department_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submit_button.sizePolicy().hasHeightForWidth())
        self.submit_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.submit_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.table = QTableWidget(self.centralwidget)
        if (self.table.columnCount() < 4):
            self.table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table.setObjectName(u"table")
        self.table.setColumnCount(4)
        self.table.verticalHeader().setVisible(True)

        self.verticalLayout.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 921, 22))
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.about_action)
        self.menuHelp.addAction(self.actionAbout_Qt)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CSV Tool", None))
        self.newFile_action.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.newFile_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.about_action.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.open_action.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.open_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.newFile_button.setText(QCoreApplication.translate("MainWindow", u"Create New File", None))
        self.select_button.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"name", None))
        self.title_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"title", None))
        self.department_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"department", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Department", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Timestamp", None));
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

