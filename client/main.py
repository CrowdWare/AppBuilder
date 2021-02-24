#############################################################################
# Copyright (C) 2021 CrowdWare
#
# This file is part of AppBuilder.
#
#  AppBuilder is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  AppBuilder is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with AppBuilder.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

import sys
from widgets.mainwindow import MainWindow
from widgets.app import App
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtCore import Qt, QCoreApplication, QSettings
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont
from PyQt5.QtQml import qmlRegisterType
from dulwich import porcelain #needed for the github plugin and pyinstaller
import main_rc


if __name__ == "__main__":
    QCoreApplication.setApplicationName("AppBuilder")
    QCoreApplication.setApplicationVersion("1.0.0")
    QCoreApplication.setOrganizationName("CrowdWare")

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))
    app.setStyleSheet("QPushButton:hover { color: #45bbe6 }")

    qmlRegisterType(App, 'AppBuilder', 2, 0, 'App')
    #qmlRegisterType(Content, 'FlatSiteBuilder', 2, 0, 'Content')
    #qmlRegisterType(Menus, 'FlatSiteBuilder', 2, 0, 'Menus')
    #qmlRegisterType(Menu, 'FlatSiteBuilder', 2, 0, 'Menu')
    #qmlRegisterType(Menuitem, 'FlatSiteBuilder', 2, 0, 'Menuitem')
    #qmlRegisterType(Section, 'FlatSiteBuilder', 2, 0, 'Section')
    #qmlRegisterType(Row, 'FlatSiteBuilder', 2, 0, 'Row')
    #qmlRegisterType(Column, 'FlatSiteBuilder', 2, 0, 'Column')

    font = QFont("Sans Serif", 15) #15 on mac, 11 on Linux
    app.setFont(font)

    p = app.palette()
    p.setColor(QPalette.Window, QColor(53, 53, 53))
    p.setColor(QPalette.WindowText, Qt.white)
    p.setColor(QPalette.Base, QColor(64, 66, 68))
    p.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    p.setColor(QPalette.ToolTipBase, Qt.white)
    p.setColor(QPalette.ToolTipText, Qt.black)
    p.setColor(QPalette.Text, Qt.white)
    p.setColor(QPalette.Button, QColor(53, 53, 53))
    p.setColor(QPalette.ButtonText, Qt.white)
    p.setColor(QPalette.BrightText, Qt.red)
    p.setColor(QPalette.Highlight, QColor("#45bbe6"))
    p.setColor(QPalette.HighlightedText, Qt.black)
    p.setColor(QPalette.Disabled, QPalette.Text, Qt.darkGray)
    p.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.darkGray)
    p.setColor(QPalette.Link, QColor("#bbb"))
    app.setPalette(p)
    app.setWindowIcon(QIcon(":/images/logo.svg"))        
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
