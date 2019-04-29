from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# for the stacked widget page buttons
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QAbstractButton

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

    # Fwd/Back buttons on each page
    @Slot(QAbstractButton)
    def on_onPageGrp_buttonClicked(self, button):
        self.stackedWidget.setCurrentIndex(button.property('page'))

    # Button to select each page
    @Slot(QAbstractButton)
    def on_byPageGrp_buttonClicked(self, button):
        self.stackedWidget.setCurrentIndex(button.property('page'))

    # Fwd/Back buttons off the stacked widget
    def on_fwdBtn_released(self):
        lastPage = 2
        currentIndex = self.stackedWidget.currentIndex()
        if currentIndex == lastPage:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(currentIndex + 1)

    def on_backBtn_released(self):
        lastPage = 2
        currentIndex = self.stackedWidget.currentIndex()
        if currentIndex == 0:
            self.stackedWidget.setCurrentIndex(lastPage)
        else:
            self.stackedWidget.setCurrentIndex(currentIndex - 1)



