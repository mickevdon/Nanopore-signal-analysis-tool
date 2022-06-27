# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firste.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.crop_start_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.crop_start_lineEdit.setObjectName("crop_start_lineEdit")
        self.crop_end_lineEdit = QtWidgets.QLineEdit(self.loadFrame)
        self.crop_end_lineEdit.setGeometry(QtCore.QRect(75, 65, 81, 14))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crop_end_lineEdit.setFont(font)
        self.crop_end_lineEdit.setInputMask("")
        self.crop_end_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.win_size_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.win_size_lineEdit.setObjectName("win_size_lineEdit")
        self.pol_order_lineEdit = QtWidgets.QLineEdit(self.baselineFrame)
        self.pol_order_lineEdit.setGeometry(QtCore.QRect(130, 100, 113, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pol_order_lineEdit.setFont(font)
        self.pol_order_lineEdit.setInputMask("")
        self.pol_order_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.gauss_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.multp_std_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.multp_std_lineEdit.setObjectName("multp_std_lineEdit")
        self.sigma_label = QtWidgets.QLabel(self.threshold_groupBox)
        self.sigma_label.setGeometry(QtCore.QRect(220, 20, 16, 16))
        self.sigma_label.setObjectName("sigma_label")
        self.constant_lineEdit = QtWidgets.QLineEdit(self.threshold_groupBox)
        self.constant_lineEdit.setGeometry(QtCore.QRect(150, 40, 61, 16))
        self.constant_lineEdit.setInputMask("")
        self.constant_lineEdit.setText("")
        self.constant_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.single_spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.plot_overlay_parameters_Button = QtWidgets.QPushButton(self.singleEventFrame)
        self.plot_overlay_parameters_Button.setGeometry(QtCore.QRect(230, 270, 21, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plot_overlay_parameters_Button.setFont(font)
        self.plot_overlay_parameters_Button.setObjectName("plot_overlay_parameters_Button")
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
        self.bins_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.bins_lineEdit.setObjectName("bins_lineEdit")
        self.curren_dist_size_lineEdit = QtWidgets.QLineEdit(self.plotting_Frame)
        self.curren_dist_size_lineEdit.setGeometry(QtCore.QRect(155, 460, 95, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.curren_dist_size_lineEdit.setFont(font)
        self.curren_dist_size_lineEdit.setInputMask("")
        self.curren_dist_size_lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.curren_dist_size_lineEdit.setObjectName("curren_dist_size_lineEdit")
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
        self.baseline_construction_parameters_label.setText(_translate("MainWindow", "Baseline construction parameters"))
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
        self.plot_overlay_parameters_Button.setText(_translate("MainWindow", "..."))
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
        self.save_Button.setText(_translate("MainWindow", "Save data"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())