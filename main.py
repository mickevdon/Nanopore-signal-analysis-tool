import matplotlib
matplotlib.use('Qt5Agg')
import cgitb
cgitb.enable(format = 'text')

from ABF_Load import loadABF
from EventDetection import *
from EventPlot import *
import matplotlib.pyplot as plt
from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
plt.rcParams.update({'figure.autolayout': True})
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadFrame = QtWidgets.QFrame(self.centralwidget)
        self.loadFrame.setGeometry(QtCore.QRect(20, 10, 261, 181))
        self.loadFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.loadFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.loadFrame.setLineWidth(2)
        self.loadFrame.setObjectName("loadFrame")
        self.sampling_rate_label = QtWidgets.QLabel(self.loadFrame)
        self.sampling_rate_label.setGeometry(QtCore.QRect(20, 100, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sampling_rate_label.setFont(font)
        self.sampling_rate_label.setObjectName("sampling_rate_label")
        self.signal_lenght_label = QtWidgets.QLabel(self.loadFrame)
        self.signal_lenght_label.setGeometry(QtCore.QRect(20, 120, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.signal_lenght_label.setFont(font)
        self.signal_lenght_label.setObjectName("signal_lenght_label")
        self.abf_id_label = QtWidgets.QLabel(self.loadFrame)
        self.abf_id_label.setGeometry(QtCore.QRect(20, 82, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.abf_id_label.setFont(font)
        self.abf_id_label.setObjectName("abf_id_label")
        self.loadButton = QtWidgets.QPushButton(self.loadFrame)
        self.loadButton.setGeometry(QtCore.QRect(20, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.loadButton.setFont(font)
        self.loadButton.setObjectName("loadButton")
        self.flipButton = QtWidgets.QPushButton(self.loadFrame)
        self.flipButton.setGeometry(QtCore.QRect(20, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.flipButton.setFont(font)
        self.flipButton.setObjectName("flipButton")
        self.crop_dataButton = QtWidgets.QPushButton(self.loadFrame)
        self.crop_dataButton.setGeometry(QtCore.QRect(160, 50, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.crop_dataButton.setFont(font)
        self.crop_dataButton.setObjectName("crop_dataButton")
        self.crop_start_lineEdit = QtWidgets.QLineEdit(self.loadFrame)
        self.crop_start_lineEdit.setGeometry(QtCore.QRect(75, 50, 81, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crop_start_lineEdit.setFont(font)
        self.crop_start_lineEdit.setInputMask("")
        self.crop_start_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.crop_start_lineEdit.setObjectName("crop_start_lineEdit")
        self.crop_end_lineEdit = QtWidgets.QLineEdit(self.loadFrame)
        self.crop_end_lineEdit.setGeometry(QtCore.QRect(75, 65, 81, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crop_end_lineEdit.setFont(font)
        self.crop_end_lineEdit.setInputMask("")
        self.crop_end_lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.crop_end_lineEdit.setObjectName("crop_end_lineEdit")
        self.crop_start_label = QtWidgets.QLabel(self.loadFrame)
        self.crop_start_label.setGeometry(QtCore.QRect(20, 47, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crop_start_label.setFont(font)
        self.crop_start_label.setObjectName("crop_start_label")
        self.crop_end_label = QtWidgets.QLabel(self.loadFrame)
        self.crop_end_label.setGeometry(QtCore.QRect(20, 63, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crop_end_label.setFont(font)
        self.crop_end_label.setObjectName("crop_end_label")
        self.baselineFrame = QtWidgets.QFrame(self.centralwidget)
        self.baselineFrame.setGeometry(QtCore.QRect(20, 200, 261, 221))
        self.baselineFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.baselineFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.baselineFrame.setLineWidth(2)
        self.baselineFrame.setObjectName("baselineFrame")
        self.baseline_construction_parameters_label = QtWidgets.QLabel(self.baselineFrame)
        self.baseline_construction_parameters_label.setGeometry(QtCore.QRect(10, 10, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.baseline_construction_parameters_label.setFont(font)
        self.baseline_construction_parameters_label.setScaledContents(False)
        self.baseline_construction_parameters_label.setOpenExternalLinks(False)
        self.baseline_construction_parameters_label.setObjectName("baseline_construction_parameters_label")
        self.selectbaseline_label = QtWidgets.QLabel(self.baselineFrame)
        self.selectbaseline_label.setGeometry(QtCore.QRect(10, 30, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selectbaseline_label.setFont(font)
        self.selectbaseline_label.setObjectName("selectbaseline_label")
        self.baseline_select_comboBox = QtWidgets.QComboBox(self.baselineFrame)
        self.baseline_select_comboBox.setGeometry(QtCore.QRect(10, 50, 231, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.baseline_select_comboBox.setFont(font)
        self.baseline_select_comboBox.setEditable(False)
        self.baseline_select_comboBox.setObjectName("baseline_select_comboBox")
        self.baseline_select_comboBox.addItem("")
        self.baseline_select_comboBox.addItem("")
        self.baseline_select_comboBox.addItem("")
        self.baseline_select_comboBox.addItem("")
        self.moving_window_label = QtWidgets.QLabel(self.baselineFrame)
        self.moving_window_label.setGeometry(QtCore.QRect(10, 80, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.moving_window_label.setFont(font)
        self.moving_window_label.setObjectName("moving_window_label")
        self.polynomial_order_label = QtWidgets.QLabel(self.baselineFrame)
        self.polynomial_order_label.setGeometry(QtCore.QRect(10, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.polynomial_order_label.setFont(font)
        self.polynomial_order_label.setObjectName("polynomial_order_label")
        self.win_size_lineEdit = QtWidgets.QLineEdit(self.baselineFrame)
        self.win_size_lineEdit.setGeometry(QtCore.QRect(130, 80, 113, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.win_size_lineEdit.setFont(font)
        self.win_size_lineEdit.setInputMask("")
        self.win_size_lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.win_size_lineEdit.setObjectName("win_size_lineEdit")
        self.pol_order_lineEdit = QtWidgets.QLineEdit(self.baselineFrame)
        self.pol_order_lineEdit.setGeometry(QtCore.QRect(130, 100, 113, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pol_order_lineEdit.setFont(font)
        self.pol_order_lineEdit.setInputMask("")
        self.pol_order_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.pol_order_lineEdit.setObjectName("pol_order_lineEdit")
        self.baseline_construction_Button = QtWidgets.QPushButton(self.baselineFrame)
        self.baseline_construction_Button.setGeometry(QtCore.QRect(20, 170, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.baseline_construction_Button.setFont(font)
        self.baseline_construction_Button.setObjectName("baseline_construction_Button")
        self.gaussian_std = QtWidgets.QLabel(self.baselineFrame)
        self.gaussian_std.setGeometry(QtCore.QRect(10, 115, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.gaussian_std.setFont(font)
        self.gaussian_std.setWordWrap(True)
        self.gaussian_std.setObjectName("gaussian_std")
        self.gauss_lineEdit = QtWidgets.QLineEdit(self.baselineFrame)
        self.gauss_lineEdit.setGeometry(QtCore.QRect(130, 120, 113, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gauss_lineEdit.setFont(font)
        self.gauss_lineEdit.setInputMask("")
        self.gauss_lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.gauss_lineEdit.setObjectName("gauss_lineEdit")
        self.thresholdFrame = QtWidgets.QFrame(self.centralwidget)
        self.thresholdFrame.setGeometry(QtCore.QRect(20, 430, 261, 181))
        self.thresholdFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.thresholdFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.thresholdFrame.setLineWidth(2)
        self.thresholdFrame.setObjectName("thresholdFrame")
        self.threshold_parameters_label = QtWidgets.QLabel(self.thresholdFrame)
        self.threshold_parameters_label.setGeometry(QtCore.QRect(10, 10, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.threshold_parameters_label.setFont(font)
        self.threshold_parameters_label.setScaledContents(False)
        self.threshold_parameters_label.setOpenExternalLinks(False)
        self.threshold_parameters_label.setObjectName("threshold_parameters_label")
        self.standard_deviation_label = QtWidgets.QLabel(self.thresholdFrame)
        self.standard_deviation_label.setGeometry(QtCore.QRect(10, 30, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.standard_deviation_label.setFont(font)
        self.standard_deviation_label.setObjectName("standard_deviation_label")
        self.thresholdButton = QtWidgets.QPushButton(self.thresholdFrame)
        self.thresholdButton.setGeometry(QtCore.QRect(20, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.thresholdButton.setFont(font)
        self.thresholdButton.setObjectName("thresholdButton")
        self.threshold_groupBox = QtWidgets.QGroupBox(self.thresholdFrame)
        self.threshold_groupBox.setGeometry(QtCore.QRect(10, 50, 241, 80))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.threshold_groupBox.setFont(font)
        self.threshold_groupBox.setObjectName("threshold_groupBox")
        self.multiple_std_radioButton = QtWidgets.QRadioButton(self.threshold_groupBox)
        self.multiple_std_radioButton.setGeometry(QtCore.QRect(10, 20, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.multiple_std_radioButton.setFont(font)
        self.multiple_std_radioButton.setChecked(True)
        self.multiple_std_radioButton.setObjectName("multiple_std_radioButton")
        self.constant_radioButton = QtWidgets.QRadioButton(self.threshold_groupBox)
        self.constant_radioButton.setGeometry(QtCore.QRect(10, 40, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.constant_radioButton.setFont(font)
        self.constant_radioButton.setObjectName("constant_radioButton")
        self.multp_std_lineEdit = QtWidgets.QLineEdit(self.threshold_groupBox)
        self.multp_std_lineEdit.setGeometry(QtCore.QRect(180, 20, 31, 16))
        self.multp_std_lineEdit.setInputMask("")
        self.multp_std_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.multp_std_lineEdit.setObjectName("multp_std_lineEdit")
        self.sigma_label = QtWidgets.QLabel(self.threshold_groupBox)
        self.sigma_label.setGeometry(QtCore.QRect(220, 20, 16, 16))
        self.sigma_label.setObjectName("sigma_label")
        self.constant_lineEdit = QtWidgets.QLineEdit(self.threshold_groupBox)
        self.constant_lineEdit.setGeometry(QtCore.QRect(150, 40, 61, 16))
        self.constant_lineEdit.setInputMask("")
        self.constant_lineEdit.setText("")
        self.constant_lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.constant_lineEdit.setObjectName("constant_lineEdit")
        self.pa_label = QtWidgets.QLabel(self.threshold_groupBox)
        self.pa_label.setGeometry(QtCore.QRect(220, 40, 16, 16))
        self.pa_label.setObjectName("pa_label")
        self.detectFrame = QtWidgets.QFrame(self.centralwidget)
        self.detectFrame.setGeometry(QtCore.QRect(20, 620, 261, 261))
        self.detectFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.detectFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.detectFrame.setLineWidth(2)
        self.detectFrame.setObjectName("detectFrame")
        self.DetectEventsButton = QtWidgets.QPushButton(self.detectFrame)
        self.DetectEventsButton.setGeometry(QtCore.QRect(20, 10, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.DetectEventsButton.setFont(font)
        self.DetectEventsButton.setObjectName("DetectEventsButton")
        self.results_groupBox = QtWidgets.QGroupBox(self.detectFrame)
        self.results_groupBox.setGeometry(QtCore.QRect(10, 120, 241, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.results_groupBox.setFont(font)
        self.results_groupBox.setObjectName("results_groupBox")
        self.event_count_label = QtWidgets.QLabel(self.results_groupBox)
        self.event_count_label.setGeometry(QtCore.QRect(10, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.event_count_label.setFont(font)
        self.event_count_label.setObjectName("event_count_label")
        self.avg_dwell_time_label = QtWidgets.QLabel(self.results_groupBox)
        self.avg_dwell_time_label.setGeometry(QtCore.QRect(10, 60, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.avg_dwell_time_label.setFont(font)
        self.avg_dwell_time_label.setObjectName("avg_dwell_time_label")
        self.avg_amplitude_label = QtWidgets.QLabel(self.results_groupBox)
        self.avg_amplitude_label.setGeometry(QtCore.QRect(10, 40, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.avg_amplitude_label.setFont(font)
        self.avg_amplitude_label.setObjectName("avg_amplitude_label")
        self.event_detect_parameters_Button = QtWidgets.QPushButton(self.results_groupBox)
        self.event_detect_parameters_Button.setGeometry(QtCore.QRect(10, 90, 221, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.event_detect_parameters_Button.setFont(font)
        self.event_detect_parameters_Button.setObjectName("event_detect_parameters_Button")
        self.plot_Frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.plot_Frame_1.setGeometry(QtCore.QRect(570, 10, 1331, 495))
        self.plot_Frame_1.setFrameShape(QtWidgets.QFrame.Box)
        self.plot_Frame_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plot_Frame_1.setLineWidth(2)
        self.plot_Frame_1.setObjectName("plot_Frame_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.plot_Frame_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1311, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.plot_Frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.plot_Frame_2.setGeometry(QtCore.QRect(570, 510, 1331, 495))
        self.plot_Frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.plot_Frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plot_Frame_2.setLineWidth(2)
        self.plot_Frame_2.setObjectName("plot_Frame_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.plot_Frame_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 1311, 471))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.singleEventFrame = QtWidgets.QFrame(self.centralwidget)
        self.singleEventFrame.setGeometry(QtCore.QRect(290, 510, 271, 311))
        self.singleEventFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.singleEventFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.singleEventFrame.setLineWidth(2)
        self.singleEventFrame.setObjectName("singleEventFrame")
        self.singleEvent_label = QtWidgets.QLabel(self.singleEventFrame)
        self.singleEvent_label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.singleEvent_label.setFont(font)
        self.singleEvent_label.setScaledContents(False)
        self.singleEvent_label.setOpenExternalLinks(False)
        self.singleEvent_label.setObjectName("singleEvent_label")
        self.single_spinBox = QtWidgets.QSpinBox(self.singleEventFrame)
        self.single_spinBox.setGeometry(QtCore.QRect(160, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.single_spinBox.setFont(font)
        self.single_spinBox.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.single_spinBox.setMaximum(0)
        self.single_spinBox.setObjectName("single_spinBox")
        self.single_amplitude_label = QtWidgets.QLabel(self.singleEventFrame)
        self.single_amplitude_label.setGeometry(QtCore.QRect(20, 50, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.single_amplitude_label.setFont(font)
        self.single_amplitude_label.setObjectName("single_amplitude_label")
        self.single_id_label = QtWidgets.QLabel(self.singleEventFrame)
        self.single_id_label.setGeometry(QtCore.QRect(160, 32, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.single_id_label.setFont(font)
        self.single_id_label.setObjectName("single_id_label")
        self.delete_button = QtWidgets.QPushButton(self.singleEventFrame)
        self.delete_button.setGeometry(QtCore.QRect(20, 240, 231, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")
        self.baseline_crossing_groupBox = QtWidgets.QGroupBox(self.singleEventFrame)
        self.baseline_crossing_groupBox.setGeometry(QtCore.QRect(10, 70, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.baseline_crossing_groupBox.setFont(font)
        self.baseline_crossing_groupBox.setObjectName("baseline_crossing_groupBox")
        self.single_dwellTime_label = QtWidgets.QLabel(self.baseline_crossing_groupBox)
        self.single_dwellTime_label.setGeometry(QtCore.QRect(10, 20, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.single_dwellTime_label.setFont(font)
        self.single_dwellTime_label.setObjectName("single_dwellTime_label")
        self.single_riseTime_label = QtWidgets.QLabel(self.baseline_crossing_groupBox)
        self.single_riseTime_label.setGeometry(QtCore.QRect(10, 40, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.single_riseTime_label.setFont(font)
        self.single_riseTime_label.setObjectName("single_riseTime_label")
        self.single_decayTime_label = QtWidgets.QLabel(self.baseline_crossing_groupBox)
        self.single_decayTime_label.setGeometry(QtCore.QRect(10, 60, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.single_decayTime_label.setFont(font)
        self.single_decayTime_label.setObjectName("single_decayTime_label")
        self.FWHM_groupBox = QtWidgets.QGroupBox(self.singleEventFrame)
        self.FWHM_groupBox.setGeometry(QtCore.QRect(10, 150, 241, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FWHM_groupBox.setFont(font)
        self.FWHM_groupBox.setObjectName("FWHM_groupBox")
        self.fwhm_single_dwellTime_label = QtWidgets.QLabel(self.FWHM_groupBox)
        self.fwhm_single_dwellTime_label.setGeometry(QtCore.QRect(10, 20, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fwhm_single_dwellTime_label.setFont(font)
        self.fwhm_single_dwellTime_label.setObjectName("fwhm_single_dwellTime_label")
        self.fwhm_single_riseTime_label = QtWidgets.QLabel(self.FWHM_groupBox)
        self.fwhm_single_riseTime_label.setGeometry(QtCore.QRect(10, 40, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fwhm_single_riseTime_label.setFont(font)
        self.fwhm_single_riseTime_label.setObjectName("fwhm_single_riseTime_label")
        self.fwhm_single_decayTime_label = QtWidgets.QLabel(self.FWHM_groupBox)
        self.fwhm_single_decayTime_label.setGeometry(QtCore.QRect(10, 60, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fwhm_single_decayTime_label.setFont(font)
        self.fwhm_single_decayTime_label.setObjectName("fwhm_single_decayTime_label")
        self.plot_overlay_Button = QtWidgets.QPushButton(self.singleEventFrame)
        self.plot_overlay_Button.setGeometry(QtCore.QRect(20, 270, 205, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plot_overlay_Button.setFont(font)
        self.plot_overlay_Button.setObjectName("plot_overlay_Button")
        self.BaFselect_Button = QtWidgets.QPushButton(self.singleEventFrame)
        self.BaFselect_Button.setGeometry(QtCore.QRect(230, 270, 21, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BaFselect_Button.setFont(font)
        self.BaFselect_Button.setObjectName("BaFselect_Button")
        self.plotting_Frame = QtWidgets.QFrame(self.centralwidget)
        self.plotting_Frame.setGeometry(QtCore.QRect(290, 10, 271, 495))
        self.plotting_Frame.setFrameShape(QtWidgets.QFrame.Box)
        self.plotting_Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.plotting_Frame.setLineWidth(2)
        self.plotting_Frame.setObjectName("plotting_Frame")
        self.plot_raw_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_raw_Button.setGeometry(QtCore.QRect(20, 40, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_raw_Button.setFont(font)
        self.plot_raw_Button.setObjectName("plot_raw_Button")
        self.plot_baseline_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_baseline_Button.setGeometry(QtCore.QRect(20, 90, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_baseline_Button.setFont(font)
        self.plot_baseline_Button.setObjectName("plot_baseline_Button")
        self.plot_threshold_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_threshold_Button.setGeometry(QtCore.QRect(20, 140, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_threshold_Button.setFont(font)
        self.plot_threshold_Button.setObjectName("plot_threshold_Button")
        self.plot_allEvents_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_allEvents_Button.setGeometry(QtCore.QRect(20, 190, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_allEvents_Button.setFont(font)
        self.plot_allEvents_Button.setObjectName("plot_allEvents_Button")
        self.plot_dwVSamp_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_dwVSamp_Button.setGeometry(QtCore.QRect(20, 240, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_dwVSamp_Button.setFont(font)
        self.plot_dwVSamp_Button.setObjectName("plot_dwVSamp_Button")
        self.plot_amp_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_amp_Button.setGeometry(QtCore.QRect(20, 290, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_amp_Button.setFont(font)
        self.plot_amp_Button.setObjectName("plot_amp_Button")
        self.plot_dw_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_dw_Button.setGeometry(QtCore.QRect(20, 340, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_dw_Button.setFont(font)
        self.plot_dw_Button.setObjectName("plot_dw_Button")
        self.plot_riseDec_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_riseDec_Button.setGeometry(QtCore.QRect(20, 390, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_riseDec_Button.setFont(font)
        self.plot_riseDec_Button.setObjectName("plot_riseDec_Button")
        self.plots_label = QtWidgets.QLabel(self.plotting_Frame)
        self.plots_label.setGeometry(QtCore.QRect(120, 10, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plots_label.setFont(font)
        self.plots_label.setScaledContents(False)
        self.plots_label.setOpenExternalLinks(False)
        self.plots_label.setObjectName("plots_label")
        self.plot_current_dist_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.plot_current_dist_Button.setGeometry(QtCore.QRect(20, 440, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plot_current_dist_Button.setFont(font)
        self.plot_current_dist_Button.setObjectName("plot_current_dist_Button")
        self.bins_lineEdit = QtWidgets.QLineEdit(self.plotting_Frame)
        self.bins_lineEdit.setGeometry(QtCore.QRect(155, 440, 95, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bins_lineEdit.setFont(font)
        self.bins_lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.bins_lineEdit.setObjectName("bins_lineEdit")
        self.curren_dist_size_lineEdit = QtWidgets.QLineEdit(self.plotting_Frame)
        self.curren_dist_size_lineEdit.setGeometry(QtCore.QRect(155, 460, 95, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curren_dist_size_lineEdit.setFont(font)
        self.curren_dist_size_lineEdit.setInputMask("")
        self.curren_dist_size_lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.curren_dist_size_lineEdit.setObjectName("curren_dist_size_lineEdit")
        self.Color_select_Button = QtWidgets.QPushButton(self.plotting_Frame)
        self.Color_select_Button.setGeometry(QtCore.QRect(190, 10, 61, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Color_select_Button.setFont(font)
        self.Color_select_Button.setObjectName("Color_select_Button")
        self.saveFrame = QtWidgets.QFrame(self.centralwidget)
        self.saveFrame.setGeometry(QtCore.QRect(20, 890, 261, 121))
        self.saveFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.saveFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.saveFrame.setLineWidth(2)
        self.saveFrame.setObjectName("saveFrame")
        self.save_Button = QtWidgets.QPushButton(self.saveFrame)
        self.save_Button.setGeometry(QtCore.QRect(20, 10, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_Button.setFont(font)
        self.save_Button.setObjectName("save_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #---------------------------------------
        self.initialise_variables(MainWindow)
        self.buttons_functions(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NanoDetect"))
        self.sampling_rate_label.setText(_translate("MainWindow", "Sampling rate:"))
        self.signal_lenght_label.setText(_translate("MainWindow", "Signal lenght:"))
        self.abf_id_label.setText(_translate("MainWindow", "File name:"))
        self.loadButton.setText(_translate("MainWindow", "Load data"))
        self.flipButton.setText(_translate("MainWindow", "Flip"))
        self.crop_dataButton.setText(_translate("MainWindow", "Crop data"))
        self.crop_start_label.setText(_translate("MainWindow", "Start (s):"))
        self.crop_end_label.setText(_translate("MainWindow", "End (s):"))
        self.baseline_construction_parameters_label.setText(
            _translate("MainWindow", "Baseline construction parameters"))
        self.selectbaseline_label.setText(_translate("MainWindow", "Select baseline construction method:"))
        self.baseline_select_comboBox.setItemText(0, _translate("MainWindow", "Moving window average"))
        self.baseline_select_comboBox.setItemText(1, _translate("MainWindow", "Average"))
        self.baseline_select_comboBox.setItemText(2, _translate("MainWindow", "Polynomial fit"))
        self.baseline_select_comboBox.setItemText(3, _translate("MainWindow", "Gaussian smoothing"))
        self.moving_window_label.setText(_translate("MainWindow", "Moving window size (s): "))
        self.polynomial_order_label.setText(_translate("MainWindow", "Polynomial order: "))
        self.win_size_lineEdit.setText(_translate("MainWindow", "1"))
        self.win_size_lineEdit.setPlaceholderText(_translate("MainWindow", "1"))
        self.pol_order_lineEdit.setText(_translate("MainWindow", "2"))
        self.pol_order_lineEdit.setPlaceholderText(_translate("MainWindow", "2"))
        self.baseline_construction_Button.setText(_translate("MainWindow", "Construct baseline"))
        self.gaussian_std.setText(_translate("MainWindow", "Gaussian kernel standard deviation:"))
        self.gauss_lineEdit.setText(_translate("MainWindow", "500"))
        self.gauss_lineEdit.setPlaceholderText(_translate("MainWindow", "1"))
        self.threshold_parameters_label.setText(_translate("MainWindow", "Threshold parameters"))
        self.standard_deviation_label.setText(_translate("MainWindow", "Standard deviation:"))
        self.thresholdButton.setText(_translate("MainWindow", "Set threshold"))
        self.threshold_groupBox.setTitle(_translate("MainWindow", "Threshold value"))
        self.multiple_std_radioButton.setText(_translate("MainWindow", "Multiple of standard deviation"))
        self.constant_radioButton.setText(_translate("MainWindow", "Constant"))
        self.multp_std_lineEdit.setText(_translate("MainWindow", "6"))
        self.multp_std_lineEdit.setPlaceholderText(_translate("MainWindow", "1"))
        self.sigma_label.setText(_translate("MainWindow", "σ"))
        self.constant_lineEdit.setPlaceholderText(_translate("MainWindow", "500"))
        self.pa_label.setText(_translate("MainWindow", "pA"))
        self.DetectEventsButton.setText(_translate("MainWindow", "Detect Translocation Events"))
        self.results_groupBox.setTitle(_translate("MainWindow", "Results"))
        self.event_count_label.setText(_translate("MainWindow", "Event count:"))
        self.avg_dwell_time_label.setText(_translate("MainWindow", "Average dwell time:"))
        self.avg_amplitude_label.setText(_translate("MainWindow", "Average amplitude:"))
        self.event_detect_parameters_Button.setText(_translate("MainWindow", "Parameters"))
        self.singleEvent_label.setText(_translate("MainWindow", "Translocation Event:"))
        self.single_amplitude_label.setText(_translate("MainWindow", "Amplitude:"))
        self.single_id_label.setText(_translate("MainWindow", "ID: 0 - x"))
        self.delete_button.setText(_translate("MainWindow", "Delete Event"))
        self.baseline_crossing_groupBox.setTitle(_translate("MainWindow", "Baseline crossing"))
        self.single_dwellTime_label.setText(_translate("MainWindow", "Dwell time:"))
        self.single_riseTime_label.setText(_translate("MainWindow", "Rise time:"))
        self.single_decayTime_label.setText(_translate("MainWindow", "Decay time:"))
        self.FWHM_groupBox.setTitle(_translate("MainWindow", "FWHM"))
        self.fwhm_single_dwellTime_label.setText(_translate("MainWindow", "Dwell time:"))
        self.fwhm_single_riseTime_label.setText(_translate("MainWindow", "Rise time:"))
        self.fwhm_single_decayTime_label.setText(_translate("MainWindow", "Decay time:"))
        self.plot_overlay_Button.setText(_translate("MainWindow", "Overlay"))
        self.BaFselect_Button.setText(_translate("MainWindow", "..."))
        self.plot_raw_Button.setText(_translate("MainWindow", "Raw data"))
        self.plot_baseline_Button.setText(_translate("MainWindow", "Baseline"))
        self.plot_threshold_Button.setText(_translate("MainWindow", "Threshold"))
        self.plot_allEvents_Button.setText(_translate("MainWindow", "Translocation Events"))
        self.plot_dwVSamp_Button.setText(_translate("MainWindow", "Dwell Time vs Amplitude"))
        self.plot_amp_Button.setText(_translate("MainWindow", "Amplitudes"))
        self.plot_dw_Button.setText(_translate("MainWindow", "Dwell Times"))
        self.plot_riseDec_Button.setText(_translate("MainWindow", "Rise Decay Times"))
        self.plots_label.setText(_translate("MainWindow", "Plots"))
        self.plot_current_dist_Button.setText(_translate("MainWindow", "Current distribution"))
        self.bins_lineEdit.setPlaceholderText(_translate("MainWindow", "auto/nbins"))
        self.curren_dist_size_lineEdit.setPlaceholderText(_translate("MainWindow", "±σ"))
        self.Color_select_Button.setText(_translate("MainWindow", "..."))
        self.save_Button.setText(_translate("MainWindow", "Save data"))

    def initialise_variables(self, MainWindow):
        # Initialise variables ------------------------------
        self.data = []
        self.baseline = []
        self.window_size = 1
        self.threshold = []
        self.EventsList = []
        self.AllEvents = []
        self.raw_data = []
        self.threshold = []
        self.orig_baseline = []
        self.parametersdict = {
            "start_threshold_type": 0,
            "end_threshold_type": 0,
            "start_std": 0,
            "end_std": 0,
            "start_fraction": 0,
            "end_fraction": 0,
            "dt_type": 0
        }
        self.scalebar = {
            "current": 100,
            "time": 10
        }
        self.colors_dict = {
            "current": "#000000",
            "baseline": "#FF0000",
            "threshold": "#FF00FF",
            "marker1": "#00AA00",
            "marker2": "#0000FF",
            "current_dist": "#0000FF",
            "other1": "#00AA00",
            "other2": "#0000FF"
        }
        self.error = {
            "load": False,
            "flip": False,
            "baseline": False,
            "threshold": False,
        }
        self.BaF = 100
        # Plotting -----------------------------------------
        self.figure1 = plt.figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.toolbar1 = NavigationToolbar(self.canvas1, MainWindow)
        self.verticalLayout_1.addWidget(self.toolbar1)
        self.verticalLayout_1.addWidget(self.canvas1)

        self.figure2 = plt.figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.toolbar2 = NavigationToolbar(self.canvas2, MainWindow)
        self.verticalLayout_2.addWidget(self.toolbar2)
        self.verticalLayout_2.addWidget(self.canvas2)

    def buttons_functions(self,MainWindow):
        self.loadButton.clicked.connect(self.loadData)
        self.flipButton.clicked.connect(self.flip_data)
        self.baseline_construction_Button.clicked.connect(self.baselineConstruction)
        self.thresholdButton.clicked.connect(self.setThreshold)
        self.DetectEventsButton.clicked.connect(self.TranslocationEventDetection)
        self.single_spinBox.valueChanged.connect(self.SingleTranslocationEventUpdate)
        self.delete_button.clicked.connect(self.DeleteEvent)
        self.save_Button.clicked.connect(self.SaveData)
        self.crop_dataButton.clicked.connect(self.CropData)
        self.event_detect_parameters_Button.clicked.connect(self.ParamSet)
        self.BaFselect_Button.clicked.connect(self.BaFselect)
        self.Color_select_Button.clicked.connect(self.color_select)

        #Plot buttons
        self.plot_raw_Button.clicked.connect(self.Plot_Raw)
        self.plot_baseline_Button.clicked.connect(self.Plot_Baseline)
        self.plot_threshold_Button.clicked.connect(self.Plot_Threshold)
        self.plot_allEvents_Button.clicked.connect(self.Plot_TranslocationEvents)
        self.plot_dwVSamp_Button.clicked.connect(self.Plot_PeakVSDwTime)
        self.plot_amp_Button.clicked.connect(self.Plot_All_Amplitudes)
        self.plot_dw_Button.clicked.connect(self.Plot_All_DwellTimes)
        self.plot_riseDec_Button.clicked.connect(self.Plot_RiseDecayTimes)
        self.plot_current_dist_Button.clicked.connect(self.Plot_CurrentDistribution)
        self.plot_overlay_Button.clicked.connect(self.Plot_Overlay)

    def show_popup(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        x = msg.exec_()

    def loadData(self):
        self.error["load"] = True
        self.error["flip"] = False
        self.error["baseline"] = False
        self.error["threshold"] = False

        #Clear variables
        self.data = []
        self.baseline = []
        self.window_size = 1
        self.threshold = []
        self.EventsList = []
        self.AllEvents = []
        self.figure1.clear()
        self.canvas1.draw()
        self.figure2.clear()
        self.canvas2.draw()

        # Data input
        self.data = loadABF()
        self.abf_id_label.setText("ABF ID: " + str(self.data['ID']))
        self.abf_id_label.adjustSize()
        self.sampling_rate_label.setText("Sampling rate: " + str(self.data['samplerate']) + " Hz")
        self.sampling_rate_label.adjustSize()
        self.signal_lenght_label.setText("Signal lenght: " + str((len(self.data['i'])-1)/self.data['samplerate']) + "(s)")
        self.signal_lenght_label.adjustSize()
        self.raw_data = self.data.copy()
        self.Plot_Raw()

    def CropData(self):
        crop_start = int(float(self.crop_start_lineEdit.text()) * self.data['samplerate'])
        crop_end = int(float(self.crop_end_lineEdit.text()) * self.data['samplerate'])
        self.data['i'] = self.data['i'][crop_start:crop_end+1]
        self.data['t'] = self.data['t'][crop_start:crop_end + 1]
        self.signal_lenght_label.setText("Signal lenght: " + str((len(self.data['i'])-1) / self.data['samplerate']) + "(s)")
        self.signal_lenght_label.adjustSize()
        self.standard_deviation_label.setText("Standard Deviation: " + str(np.std(self.data['i'])) + "pA")
        self.standard_deviation_label.adjustSize()
        self.raw_data = self.data.copy()
        self.Plot_Raw()

    def flip_data(self):
        if self.error["load"] == True:
            self.data['i'] = flip_x(self.data['i'])
            self.raw_data = self.data.copy()
            self.Plot_Raw()
            self.error["flip"] = not self.error["flip"]
        else:
            self.show_popup("Data not loaded")

    def baselineConstruction(self):
        if self.error["flip"] == True:
            self.baseline_type = self.baseline_select_comboBox.currentIndex()
            self.window_size_s = float(self.win_size_lineEdit.text())
            self.polynomial_order = int(self.pol_order_lineEdit.text())
            self.gauss_std= int(self.gauss_lineEdit.text())
            self.baseline = constructBaseline(self.baseline_type, self.raw_data, self.window_size_s, self.polynomial_order, self.gauss_std)
            self.raw_baseline = self.baseline
            self.Plot_Baseline()
            self.data['i'] = self.raw_data['i'] - self.baseline
            self.baseline = np.full(len(self.data['i']), 0)
            self.error["baseline"] = True
        else:
            self.show_popup("Data not flipped")

    def setThreshold(self):
        if self.error["baseline"] == True:
            if self.multiple_std_radioButton.isChecked():
                self.threshold = self.baseline + (np.std(self.data['i']) * float(self.multp_std_lineEdit.text()))
            else:
                self.threshold = self.baseline + float(self.constant_lineEdit.text())
            self.Plot_Threshold()

            self.standard_deviation_label.setText(
                "Standard Deviation: " + str("{0:.2f}".format(np.std(self.data['i']))) + "pA")
            self.standard_deviation_label.adjustSize()
            self.error["threshold"] = True
        else:
            self.show_popup("Baseline not found")

    def ParamSet(self):
        Dialog = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 366)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 300, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.start_widget = QtWidgets.QWidget(Dialog)
        self.start_widget.setGeometry(QtCore.QRect(30, 10, 381, 101))
        self.start_widget.setObjectName("start_widget")
        self.event_start_label = QtWidgets.QLabel(self.start_widget)
        self.event_start_label.setGeometry(QtCore.QRect(10, 0, 171, 19))
        self.event_start_label.setObjectName("event_start_label")
        self.start_baselineCrossing_radioButton = QtWidgets.QRadioButton(self.start_widget)
        self.start_baselineCrossing_radioButton.setGeometry(QtCore.QRect(10, 20, 181, 23))
        self.start_baselineCrossing_radioButton.setChecked(True)
        self.start_baselineCrossing_radioButton.setObjectName("start_baselineCrossing_radioButton")
        self.start_multiple_radioButton = QtWidgets.QRadioButton(self.start_widget)
        self.start_multiple_radioButton.setGeometry(QtCore.QRect(10, 45, 131, 23))
        self.start_multiple_radioButton.setObjectName("start_multiple_radioButton")
        self.start_fraction_radioButton = QtWidgets.QRadioButton(self.start_widget)
        self.start_fraction_radioButton.setGeometry(QtCore.QRect(10, 70, 191, 23))
        self.start_fraction_radioButton.setObjectName("start_fraction_radioButton")
        self.start_multiple_lineEdit = QtWidgets.QLineEdit(self.start_widget)
        self.start_multiple_lineEdit.setGeometry(QtCore.QRect(140, 47, 113, 17))
        self.start_multiple_lineEdit.setObjectName("start_multiple_lineEdit")
        self.start_fraction_lineEdit = QtWidgets.QLineEdit(self.start_widget)
        self.start_fraction_lineEdit.setGeometry(QtCore.QRect(190, 73, 113, 17))
        self.start_fraction_lineEdit.setObjectName("start_fraction_lineEdit")
        self.end_widget = QtWidgets.QWidget(Dialog)
        self.end_widget.setGeometry(QtCore.QRect(30, 120, 381, 101))
        self.end_widget.setObjectName("end_widget")
        self.event_end_label = QtWidgets.QLabel(self.end_widget)
        self.event_end_label.setGeometry(QtCore.QRect(10, 0, 171, 19))
        self.event_end_label.setObjectName("event_end_label")
        self.end_fraction_lineEdit = QtWidgets.QLineEdit(self.end_widget)
        self.end_fraction_lineEdit.setGeometry(QtCore.QRect(190, 73, 113, 17))
        self.end_fraction_lineEdit.setObjectName("end_fraction_lineEdit")
        self.end_fraction_radioButton = QtWidgets.QRadioButton(self.end_widget)
        self.end_fraction_radioButton.setGeometry(QtCore.QRect(10, 70, 191, 23))
        self.end_fraction_radioButton.setObjectName("end_fraction_radioButton")
        self.end_multiple_radioButton = QtWidgets.QRadioButton(self.end_widget)
        self.end_multiple_radioButton.setGeometry(QtCore.QRect(10, 45, 131, 23))
        self.end_multiple_radioButton.setObjectName("end_multiple_radioButton")
        self.end_multiple_lineEdit = QtWidgets.QLineEdit(self.end_widget)
        self.end_multiple_lineEdit.setGeometry(QtCore.QRect(140, 47, 113, 17))
        self.end_multiple_lineEdit.setObjectName("end_multiple_lineEdit")
        self.end_baselineCrossing_radioButton = QtWidgets.QRadioButton(self.end_widget)
        self.end_baselineCrossing_radioButton.setGeometry(QtCore.QRect(10, 20, 181, 23))
        self.end_baselineCrossing_radioButton.setChecked(True)
        self.end_baselineCrossing_radioButton.setObjectName("end_baselineCrossing_radioButton")
        self.dwelltime_widget = QtWidgets.QWidget(Dialog)
        self.dwelltime_widget.setGeometry(QtCore.QRect(30, 230, 381, 51))
        self.dwelltime_widget.setObjectName("dwelltime_widget")
        self.dwell_time_label = QtWidgets.QLabel(self.dwelltime_widget)
        self.dwell_time_label.setGeometry(QtCore.QRect(10, 0, 171, 19))
        self.dwell_time_label.setObjectName("dwell_time_label")
        self.dwell_baselineCrossing_radioButton = QtWidgets.QRadioButton(self.dwelltime_widget)
        self.dwell_baselineCrossing_radioButton.setGeometry(QtCore.QRect(10, 20, 221, 23))
        self.dwell_baselineCrossing_radioButton.setChecked(True)
        self.dwell_baselineCrossing_radioButton.setObjectName("dwell_baselineCrossing_radioButton")
        self.fwhm_radioButton = QtWidgets.QRadioButton(self.dwelltime_widget)
        self.fwhm_radioButton.setGeometry(QtCore.QRect(260, 20, 131, 23))
        self.fwhm_radioButton.setObjectName("fwhm_radioButton")

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.event_start_label.setText(_translate("Dialog", "Event start threshold:"))
        self.start_baselineCrossing_radioButton.setText(_translate("Dialog", "Baseline crossing"))
        self.start_multiple_radioButton.setText(_translate("Dialog", "Multiple of std"))
        self.start_fraction_radioButton.setText(_translate("Dialog", "Fraction of amplitude"))
        self.event_end_label.setText(_translate("Dialog", "Event end threshold:"))
        self.end_fraction_radioButton.setText(_translate("Dialog", "Fraction of amplitude"))
        self.end_multiple_radioButton.setText(_translate("Dialog", "Multiple of std"))
        self.end_baselineCrossing_radioButton.setText(_translate("Dialog", "Baseline crossing"))
        self.dwell_time_label.setText(_translate("Dialog", "Dwell time:"))
        self.dwell_baselineCrossing_radioButton.setText(_translate("Dialog", "Baseline/Threshold crossing"))
        self.fwhm_radioButton.setText(_translate("Dialog", "FWHM"))

        #--------------------
        self.start_multiple_lineEdit.setText(_translate("Dialog", str(self.parametersdict["start_std"])))
        self.end_multiple_lineEdit.setText(_translate("Dialog", str(self.parametersdict["end_std"])))
        self.start_fraction_lineEdit.setText(_translate("Dialog", str(self.parametersdict["start_fraction"])))
        self.end_fraction_lineEdit.setText(_translate("Dialog", str(self.parametersdict["end_fraction"])))

        if self.parametersdict["start_threshold_type"] == 0:
            self.start_baselineCrossing_radioButton.setChecked(True)
        elif self.parametersdict["start_threshold_type"] == 1:
            self.start_multiple_radioButton.setChecked(True)
        elif self.parametersdict["start_threshold_type"] == 2:
            self.start_fraction_radioButton.setChecked(True)

        if self.parametersdict["end_threshold_type"] == 0:
            self.end_baselineCrossing_radioButton.setChecked(True)
        elif self.parametersdict["end_threshold_type"] == 1:
            self.end_multiple_radioButton.setChecked(True)
        elif self.parametersdict["end_threshold_type"] == 2:
            self.end_fraction_radioButton.setChecked(True)

        if self.parametersdict["dt_type"] == 0:
            self.dwell_baselineCrossing_radioButton.setChecked(True)
        elif self.parametersdict["dt_type"] == 1:
            self.fwhm_radioButton.setChecked(True)

        #--------------------

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.exec()

        if self.start_baselineCrossing_radioButton.isChecked():
            self.parametersdict["start_threshold_type"] = 0
        elif self.start_multiple_radioButton.isChecked():
            self.parametersdict["start_threshold_type"] = 1
            self.parametersdict["start_std"] = float(self.start_multiple_lineEdit.text())
        elif self.start_fraction_radioButton.isChecked():
            self.parametersdict["start_threshold_type"] =2
            self.parametersdict["start_fraction"] = float(self.start_fraction_lineEdit.text())

        if self.end_baselineCrossing_radioButton.isChecked():
            self.parametersdict["end_threshold_type"] = 0
        elif self.end_multiple_radioButton.isChecked():
            self.parametersdict["end_threshold_type"] = 1
            self.parametersdict["end_std"] = float(self.end_multiple_lineEdit.text())
        elif self.end_fraction_radioButton.isChecked():
            self.parametersdict["end_threshold_type"] = 2
            self.parametersdict["end_fraction"] = float(self.end_fraction_lineEdit.text())

        if self.dwell_baselineCrossing_radioButton.isChecked():
            self.parametersdict["dt_type"] = 0
        elif self.fwhm_radioButton.isChecked():
            self.parametersdict["dt_type"] = 1

    def TranslocationEventDetection(self):
        if self.error["threshold"] == True:
            self.EventsList.clear()
            del self.AllEvents
            self.AllEvents = []
            self.EventsList = DetectEvents(self.data, self.threshold, self.parametersdict, self.BaF)
            self.AllEvents = CreateAllTranslocationEventsObject(self.EventsList)
            self.event_count_label.setText("Event count: " + str(len(self.EventsList)))
            self.event_count_label.adjustSize()

            if self.parametersdict['dt_type'] == 0:
                dwellTimes = self.AllEvents.GetAllDwellTimes()
            elif self.parametersdict['dt_type'] == 1:
                dwellTimes = self.AllEvents.GetAllFWHMTimes()

            amplitudes = self.AllEvents.GetAllAmplitudes_pos()
            self.avg_dwell_time_label.setText("Average dwell time: " + str("{0:.2f}".format(np.mean(dwellTimes)*1000000)) + " μs")
            self.avg_dwell_time_label.adjustSize()

            self.avg_amplitude_label.setText("Average amplitude: " + str("{0:.2f}".format(np.mean(amplitudes)) + " pA"))
            self.avg_amplitude_label.adjustSize()


            self.single_spinBox.setMaximum(self.EventsList[-1].number)
            self.single_id_label.setText("ID: 0 -  " + str(self.EventsList[-1].number))
            self.single_id_label.adjustSize()
            self.SingleTranslocationEventUpdate()

            PlotAllEvents(self.figure1, self.canvas1, self.AllEvents, self.data, self.baseline, self.threshold, self.colors_dict)
        else:
            self.show_popup("Threshold not found")

    def SingleTranslocationEventUpdate(self):

        event_num = self.single_spinBox.value()
        self.single_dwellTime_label.setText("Dwell time: " + str("{0:.2f}".format(self.EventsList[event_num].dwellTime*1000000)) + " μs")
        self.single_dwellTime_label.adjustSize()

        self.single_amplitude_label.setText("Amplitude: " + str("{0:.2f}".format(self.EventsList[event_num].peakAmplitude_pos)) + " pA")
        self.single_amplitude_label.adjustSize()

        self.single_riseTime_label.setText("Rise time: " + str("{0:.2f}".format(self.EventsList[event_num].riseTime * 1000000)) + " μs")
        self.single_riseTime_label.adjustSize()

        self.single_decayTime_label.setText("Decay time: " + str("{0:.2f}".format(self.EventsList[event_num].decayTime * 1000000)) + " μs")
        self.single_decayTime_label.adjustSize()

        #---- FWHM
        try:
            self.fwhm_single_dwellTime_label.setText("Dwell time: " + str("{0:.2f}".format(self.EventsList[event_num].FWHM_time * 1000000)) + " μs")
            self.fwhm_single_dwellTime_label.adjustSize()

            self.fwhm_single_riseTime_label.setText("Rise time: " + str("{0:.2f}".format(self.EventsList[event_num].FWHM_riseTime * 1000000)) + " μs")
            self.fwhm_single_riseTime_label.adjustSize()

            self.fwhm_single_decayTime_label.setText("Decay time: " + str("{0:.2f}".format(self.EventsList[event_num].FWHM_decayTime * 1000000)) + " μs")
            self.fwhm_single_decayTime_label.adjustSize()
        except AttributeError:
            self.fwhm_single_dwellTime_label.setText("Dwell time: - μs")
            self.fwhm_single_dwellTime_label.adjustSize()

            self.fwhm_single_riseTime_label.setText("Rise time: - μs")
            self.fwhm_single_riseTime_label.adjustSize()

            self.fwhm_single_decayTime_label.setText("Decay time: - μs")
            self.fwhm_single_decayTime_label.adjustSize()


        PlotEvent(self.figure2, self.canvas2, self.EventsList[event_num], self.colors_dict, self.parametersdict['dt_type'])

    def DeleteEvent(self):
        #Delete Event
        event_num = self.single_spinBox.value()
        del self.EventsList[event_num]
        self.AllEvents.DeleteEvent(event_num)

        for i in range (len(self.EventsList)):
            self.EventsList[i].number = i

        #Update Labels and Plots
        self.event_count_label.setText("Event count: " + str(len(self.EventsList)))
        self.event_count_label.adjustSize()
        if self.parametersdict['dt_type'] == 0:
            dwellTimes = self.AllEvents.GetAllDwellTimes()
        elif self.parametersdict['dt_type'] == 1:
            dwellTimes = self.AllEvents.GetAllFWHMTimes()
        amplitudes = self.AllEvents.GetAllAmplitudes_pos()
        self.avg_dwell_time_label.setText("Average dwell time: " + str("{0:.2f}".format(np.mean(dwellTimes) * 1000000)) + " μs")
        self.avg_dwell_time_label.adjustSize()
        self.avg_amplitude_label.setText("Average amplitude: " + str("{0:.2f}".format(np.mean(amplitudes)) + " pA"))
        self.avg_amplitude_label.adjustSize()
        self.single_spinBox.setMaximum(self.EventsList[-1].number)
        self.single_id_label.setText("ID: 0 -  " + str(self.EventsList[-1].number))
        self.single_id_label.adjustSize()
        self.SingleTranslocationEventUpdate()

        PlotEvent(self.figure2, self.canvas2, self.EventsList[event_num], self.colors_dict, self.parametersdict['dt_type'])
        PlotAllEvents(self.figure1, self.canvas1, self.AllEvents, self.data, self.baseline, self.threshold,self.colors_dict)

    def SaveData(self):
        if self.parametersdict['dt_type'] == 0:
            dwellTimes = self.AllEvents.GetAllDwellTimes()
            riseTimes = self.AllEvents.GetAllRiseTimes()
            decayTimes = self.AllEvents.GetAllDecayTimes()
        elif self.parametersdict['dt_type'] == 1:
            dwellTimes = self.AllEvents.GetAllFWHMTimes()
            riseTimes = self.AllEvents.GetAllFWHM_riseTimes()
            decayTimes = self.AllEvents.GetAllFWHM_decayTimes()
        results = np.array([self.AllEvents.GetAllNumber(),self.AllEvents.GetAllAmplitudes_pos(),dwellTimes,riseTimes,decayTimes]).transpose()
        np.savetxt('results.csv', results,fmt="%i,%1.7f,%1.7f,%1.7f,%1.7f", delimiter=",",header='ID,Amplitude(pA),Dwell_Time(s),Rise_time(s),Decay_time(s)',comments='')

    def BaFselect(self):
        baf, done = QtWidgets.QInputDialog.getInt(None, 'BaF', 'Enter how many data points to plot before and after:')
        self.BaF = baf

    def color_select(self):
        color_convert = lambda color: "background-color: " + str(color) + ";"
        Dialog = QtWidgets.QDialog()
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 366)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 300, 81, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.start_widget = QtWidgets.QWidget(Dialog)
        self.start_widget.setGeometry(QtCore.QRect(20, 10, 411, 281))
        self.start_widget.setObjectName("start_widget")
        self.event_start_label = QtWidgets.QLabel(self.start_widget)
        self.event_start_label.setGeometry(QtCore.QRect(10, 0, 171, 19))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.event_start_label.setFont(font)
        self.event_start_label.setObjectName("event_start_label")
        self.current_label = QtWidgets.QLabel(self.start_widget)
        self.current_label.setGeometry(QtCore.QRect(40, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.current_label.setFont(font)
        self.current_label.setObjectName("current_label")
        self.baseline_label = QtWidgets.QLabel(self.start_widget)
        self.baseline_label.setGeometry(QtCore.QRect(40, 60, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.baseline_label.setFont(font)
        self.baseline_label.setObjectName("baseline_label")
        self.threshold_label = QtWidgets.QLabel(self.start_widget)
        self.threshold_label.setGeometry(QtCore.QRect(40, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.threshold_label.setFont(font)
        self.threshold_label.setObjectName("threshold_label")
        self.marker1_label = QtWidgets.QLabel(self.start_widget)
        self.marker1_label.setGeometry(QtCore.QRect(40, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.marker1_label.setFont(font)
        self.marker1_label.setObjectName("marker1_label")
        self.marker2_label = QtWidgets.QLabel(self.start_widget)
        self.marker2_label.setGeometry(QtCore.QRect(40, 150, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.marker2_label.setFont(font)
        self.marker2_label.setObjectName("marker2_label")
        self.currentdist_label = QtWidgets.QLabel(self.start_widget)
        self.currentdist_label.setGeometry(QtCore.QRect(40, 240, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.currentdist_label.setFont(font)
        self.currentdist_label.setObjectName("currentdist_label")
        self.other1_label = QtWidgets.QLabel(self.start_widget)
        self.other1_label.setGeometry(QtCore.QRect(40, 180, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.other1_label.setFont(font)
        self.other1_label.setObjectName("other1_label")
        self.other2_label = QtWidgets.QLabel(self.start_widget)
        self.other2_label.setGeometry(QtCore.QRect(40, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.other2_label.setFont(font)
        self.other2_label.setObjectName("other2_label")
        self.current_widget = QtWidgets.QWidget(self.start_widget)
        self.current_widget.setGeometry(QtCore.QRect(130, 30, 21, 21))
        self.current_widget.setAutoFillBackground(True)
        self.current_widget.setStyleSheet(color_convert(self.colors_dict['current']))
        self.current_widget.setObjectName("current_widget")
        self.baseline_widget = QtWidgets.QWidget(self.start_widget)
        self.baseline_widget.setGeometry(QtCore.QRect(130, 60, 21, 21))
        self.baseline_widget.setAutoFillBackground(True)
        self.baseline_widget.setStyleSheet(color_convert(self.colors_dict['baseline']))
        self.baseline_widget.setObjectName("baseline_widget")
        self.threshold_widget = QtWidgets.QWidget(self.start_widget)
        self.threshold_widget.setGeometry(QtCore.QRect(130, 90, 21, 21))
        self.threshold_widget.setAutoFillBackground(True)
        self.threshold_widget.setStyleSheet(color_convert(self.colors_dict['threshold']))
        self.threshold_widget.setObjectName("threshold_widget")
        self.marker1_widget = QtWidgets.QWidget(self.start_widget)
        self.marker1_widget.setGeometry(QtCore.QRect(130, 120, 21, 21))
        self.marker1_widget.setAutoFillBackground(True)
        self.marker1_widget.setStyleSheet(color_convert(self.colors_dict['marker1']))
        self.marker1_widget.setObjectName("marker1_widget")
        self.marker2_widget = QtWidgets.QWidget(self.start_widget)
        self.marker2_widget.setGeometry(QtCore.QRect(130, 150, 21, 21))
        self.marker2_widget.setAutoFillBackground(True)
        self.marker2_widget.setStyleSheet(color_convert(self.colors_dict['marker2']))
        self.marker2_widget.setObjectName("marker2_widget")
        self.other1_widget = QtWidgets.QWidget(self.start_widget)
        self.other1_widget.setGeometry(QtCore.QRect(130, 180, 21, 21))
        self.other1_widget.setAutoFillBackground(True)
        self.other1_widget.setStyleSheet(color_convert(self.colors_dict['other1']))
        self.other1_widget.setObjectName("other1_widget")
        self.other2_widget = QtWidgets.QWidget(self.start_widget)
        self.other2_widget.setGeometry(QtCore.QRect(130, 210, 21, 21))
        self.other2_widget.setAutoFillBackground(True)
        self.other2_widget.setStyleSheet(color_convert(self.colors_dict['other2']))
        self.other2_widget.setObjectName("other2_widget")
        self.currentdist_widget = QtWidgets.QWidget(self.start_widget)
        self.currentdist_widget.setGeometry(QtCore.QRect(210, 240, 21, 21))
        self.currentdist_widget.setAutoFillBackground(True)
        self.currentdist_widget.setStyleSheet(color_convert(self.colors_dict['current_dist']))
        self.currentdist_widget.setObjectName("currentdist_widget")
        self.current_pushButton = QtWidgets.QPushButton(self.start_widget)
        self.current_pushButton.setGeometry(QtCore.QRect(160, 30, 75, 23))
        self.current_pushButton.setObjectName("current_pushButton")
        self.baseline_pushButton = QtWidgets.QPushButton(self.start_widget)
        self.baseline_pushButton.setGeometry(QtCore.QRect(160, 60, 75, 23))
        self.baseline_pushButton.setObjectName("baseline_pushButton")
        self.threshold_pushButton = QtWidgets.QPushButton(self.start_widget)
        self.threshold_pushButton.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.threshold_pushButton.setObjectName("threshold_pushButton")
        self.marker1_pushButton = QtWidgets.QPushButton(self.start_widget)
        self.marker1_pushButton.setGeometry(QtCore.QRect(160, 120, 75, 23))
        self.marker1_pushButton.setObjectName("marker1_pushButton")
        self.marker2_pushButton = QtWidgets.QPushButton(self.start_widget)
        self.marker2_pushButton.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.marker2_pushButton.setObjectName("marker2_pushButton")
        self.other1_pushButton = QtWidgets.QPushButton(self.start_widget)
        self.other1_pushButton.setGeometry(QtCore.QRect(160, 180, 75, 23))
        self.other1_pushButton.setObjectName("other1_pushButton")
        self.other2_pushButton = QtWidgets.QPushButton(self.start_widget)
        self.other2_pushButton.setGeometry(QtCore.QRect(160, 210, 75, 23))
        self.other2_pushButton.setObjectName("other2_pushButton")
        self.currentdist_pushButton = QtWidgets.QPushButton(self.start_widget)
        self.currentdist_pushButton.setGeometry(QtCore.QRect(240, 240, 75, 23))
        self.currentdist_pushButton.setObjectName("currentdist_pushButton")

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.event_start_label.setText(_translate("Dialog", "Colour select:"))
        self.current_label.setText(_translate("Dialog", "Current"))
        self.baseline_label.setText(_translate("Dialog", "Baseline"))
        self.threshold_label.setText(_translate("Dialog", "Threshold"))
        self.marker1_label.setText(_translate("Dialog", "Marker 1"))
        self.marker2_label.setText(_translate("Dialog", "Marker 2"))
        self.currentdist_label.setText(_translate("Dialog", "Current Distribution"))
        self.other1_label.setText(_translate("Dialog", "Other 1"))
        self.other2_label.setText(_translate("Dialog", "Other 2"))
        self.current_pushButton.setText(_translate("Dialog", "Select"))
        self.baseline_pushButton.setText(_translate("Dialog", "Select"))
        self.threshold_pushButton.setText(_translate("Dialog", "Select"))
        self.marker1_pushButton.setText(_translate("Dialog", "Select"))
        self.marker2_pushButton.setText(_translate("Dialog", "Select"))
        self.other1_pushButton.setText(_translate("Dialog", "Select"))
        self.other2_pushButton.setText(_translate("Dialog", "Select"))
        self.currentdist_pushButton.setText(_translate("Dialog", "Select"))
        # --------------------

        def current_pressed():
            color = QtWidgets.QColorDialog.getColor()
            self.colors_dict['current'] = color.name()
            self.current_widget.setStyleSheet(color_convert(self.colors_dict['current']))
        self.current_pushButton.clicked.connect(current_pressed)

        def baseline_pressed():
            color = QtWidgets.QColorDialog.getColor()
            self.colors_dict['baseline'] = color.name()
            self.baseline_widget.setStyleSheet(color_convert(self.colors_dict['baseline']))
        self.baseline_pushButton.clicked.connect(baseline_pressed)

        def threshold_pressed():
            color = QtWidgets.QColorDialog.getColor()
            self.colors_dict['threshold'] = color.name()
            self.threshold_widget.setStyleSheet(color_convert(self.colors_dict['threshold']))
        self.threshold_pushButton.clicked.connect(threshold_pressed)

        def marker1_pressed():
            color = QtWidgets.QColorDialog.getColor()
            self.colors_dict['marker1'] = color.name()
            self.marker1_widget.setStyleSheet(color_convert(self.colors_dict['marker1']))
        self.marker1_pushButton.clicked.connect(marker1_pressed)

        def marker2_pressed():
            color = QtWidgets.QColorDialog.getColor()
            self.colors_dict['marker2'] = color.name()
            self.marker2_widget.setStyleSheet(color_convert(self.colors_dict['marker2']))
        self.marker2_pushButton.clicked.connect(marker2_pressed)

        def other1_pressed():
            color = QtWidgets.QColorDialog.getColor()
            self.colors_dict['other1'] = color.name()
            self.other1_widget.setStyleSheet(color_convert(self.colors_dict['other1']))
        self.other1_pushButton.clicked.connect(other1_pressed)

        def other2_pressed():
            color = QtWidgets.QColorDialog.getColor()
            self.colors_dict['other2'] = color.name()
            self.other2_widget.setStyleSheet(color_convert(self.colors_dict['other2']))
        self.other2_pushButton.clicked.connect(other2_pressed)

        def currentdist_pressed():
            color = QtWidgets.QColorDialog.getColor()
            self.colors_dict['current_dist'] = color.name()
            self.currentdist_widget.setStyleSheet(color_convert(self.colors_dict['current_dist']))
        self.currentdist_pushButton.clicked.connect(currentdist_pressed)

        # --------------------

        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.exec()

    def Plot_Raw(self):
        Plot_Raw_Data(self.figure1, self.canvas1, self.data, self.colors_dict)

    def Plot_Baseline(self):
        Plot_Data_Baseline(self.figure1, self.canvas1, self.raw_data, self.raw_baseline, self.baseline_type, self.window_size_s, self.colors_dict)

    def Plot_Threshold(self):
        PlotThreshold(self.figure1, self.canvas1, self.data, self.baseline, self.threshold, self.colors_dict)

    def Plot_TranslocationEvents(self):
        PlotAllEvents(self.figure1, self.canvas1, self.AllEvents, self.data, self.baseline, self.threshold,self.colors_dict)

    def Plot_PeakVSDwTime(self):
        PlotPeakVSDwellTime(self.figure1,self.canvas1, self.AllEvents,self.colors_dict, self.parametersdict['dt_type'])

    def Plot_All_Amplitudes(self):
        PlotAmplitudes(self.figure1,self.canvas1, self.AllEvents, self.colors_dict)

    def Plot_All_DwellTimes(self):
        PlotDwellTimes(self.figure1,self.canvas1, self.AllEvents, self.colors_dict, self.parametersdict['dt_type'])

    def Plot_RiseDecayTimes(self):
        PlotRiseDecayTimes(self.figure1,self.canvas1, self.AllEvents, self.colors_dict, self.parametersdict['dt_type'])

    def Plot_CurrentDistribution(self):
        PlotCurrentDistribution(self.figure1, self.canvas1, self.data['i'], self.bins_lineEdit.text(), self.curren_dist_size_lineEdit.text(), self.colors_dict, self.AllEvents)
        # PlotCurrentDistributionDeleted(self.figure1, self.canvas1, self.data['i'], self.bins_lineEdit.text(),self.curren_dist_size_lineEdit.text(), self.colors_dict, self.AllEvents)

    def Plot_Overlay(self):
        PlotOverlay(self.figure2,self.canvas2, self.AllEvents, self.data['samplerate'], self.scalebar ,self.colors_dict)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
