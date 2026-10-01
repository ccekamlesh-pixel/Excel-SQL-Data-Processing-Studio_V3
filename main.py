"""
Excel SQL Data Processing Studio - Main entry point
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt

from ui.main_window import MainWindow
from utils.logger import setup_logger
from utils.theme import ThemeManager


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Excel SQL Data Processing Studio")
    app.setOrganizationName("DataStudio")
    app.setApplicationVersion("1.0.0")

    logger = setup_logger()
    logger.info("Application started")

    theme_manager = ThemeManager(app)
    theme_manager.apply_theme("light")

    window = MainWindow(theme_manager)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
