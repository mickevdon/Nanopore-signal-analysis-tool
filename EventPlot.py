import numpy as np
from matplotlib.lines import Line2D

def Plot_Raw_Data(figure, canvas, data, colors_dict):
    figure.clear()
    ax = figure.add_subplot(111)
    ax.plot(data['t'], data['i'], color = colors_dict['current'],label='Current Trace', linewidth=0.7, zorder=0)
    ax.title.set_text("Raw data")
    ax.legend(loc="upper right")
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Current (pA)')
    canvas.draw()

def Plot_Data_Baseline(figure, canvas, data, baseline, baseline_type, window_size_s, colors_dict):
    if baseline_type == 0:
        title = "Moving Window Average. Window size (s): " + str(window_size_s)
    elif baseline_type == 1:
        title = "Artihmetic average"
    elif baseline_type == 2:
        title = "Polynomial fit"
    elif baseline_type == 3:
        title = "Gaussian smoothing"

    figure.clear()
    ax = figure.add_subplot(111)
    ax.plot(data['t'], data['i'], color= colors_dict['current'],label='Current Trace',linewidth=0.7, zorder=0)
    ax.plot(data['t'], baseline, color =colors_dict['baseline'],label='Baseline',linewidth=1.5, zorder=1)
    ax.title.set_text(title)
    ax.legend(loc="upper right")
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Current (pA)')
    canvas.draw()


def PlotThreshold(figure, canvas, data, baseline, threshold, colors_dict):
    figure.clear()
    ax = figure.add_subplot(111)
    ax.plot(data['t'], data['i'], color= colors_dict['current'], label='Current Trace',linewidth=0.7, zorder=0)
    ax.plot(data['t'], baseline, color =colors_dict['baseline'], label='Baseline', zorder=1)
    ax.plot(data['t'], threshold, color =colors_dict['threshold'], label='6σ Threshold', zorder=2)
    # ax.plot(data['t'], threshold * 0.5, color='b', label='3σ Threshold', zorder=2)
    # ax.plot(data['t'], -1* threshold, color=colors_dict['threshold'], zorder=3)
    ax.title.set_text("Threshold")
    ax.legend(loc="upper right")
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Current (pA)')
    canvas.draw()

def PlotAllEvents(figure, canvas, AllEvents, data, baseline, threshold, colors_dict):
    startPoints = AllEvents.GetAllStartPoints()
    endPoints = AllEvents.GetAllEndPoints()

    figure.clear()
    ax = figure.add_subplot(111)
    ax.plot(data['t'], data['i'], color= colors_dict['current'], label= "Current trace",linewidth=0.7, zorder=0)
    ax.plot(data['t'], baseline, color =colors_dict['baseline'], label='Baseline', zorder=1)
    ax.plot(data['t'], threshold, color =colors_dict['threshold'], label='Threshold', zorder=2)
    ax.scatter(data['t'][startPoints], data['i'][startPoints], color =colors_dict['marker1'], s=15, marker='v',label = "Event start", zorder=4)
    ax.scatter(data['t'][endPoints], data['i'][endPoints], color =colors_dict['marker2'], s=15, marker='v',label = "Event end", zorder=5)
    ax.title.set_text("All Events")
    ax.legend(loc='upper right')
    ax.set_ylabel('Current (pA)')
    ax.set_xlabel('Time (s)')
    canvas.draw()

def PlotEvent(figure, canvas, SingleEvent, colors_dict, type):
    figure.clear()
    ax = figure.add_subplot(111)
    ax.title.set_text("Single Event: " + str(SingleEvent.number))
    ax.plot(SingleEvent.timeStamps_cmb, SingleEvent.currentTrace_cmb, color= colors_dict['current'],label= "Current trace",zorder=0)
    ax.axhline(y=0, color =colors_dict['baseline'], linestyle='-',label = "Baseline", zorder=0)

    if type == 1:
        ax.axhline(y=SingleEvent.peakAmplitude_pos / 2, color=colors_dict['baseline'], linestyle='--', alpha=0.5,label="Half Amplitude", zorder=1)
    ax.scatter(SingleEvent.timeStamps[0],SingleEvent.currentTrace[0], s = 100, color =colors_dict['marker1'], marker='v', label = "Event start", zorder=2)
    ax.scatter(SingleEvent.timeStamps[-1], SingleEvent.currentTrace[-1], s=100, color =colors_dict['marker2'], marker='v', label="Event end",zorder=2)

    ax.legend(loc='upper right')
    ax.set_ylabel('Current (pA)')
    ax.set_xlabel('Time (s)')
    canvas.draw()


def PlotPeakVSDwellTime(figure,canvas, AllEvents, colors_dict,type):
    figure.clear()
    ax = figure.add_subplot(111)
    Amplitudes_pos = AllEvents.GetAllAmplitudes_pos()
    if type == 0:
        DwellTimes = AllEvents.GetAllDwellTimes()
    elif type == 1:
        DwellTimes = AllEvents.GetAllFWHMTimes()
    ax.title.set_text("Peak Amplitude vs Dwell time")
    ax.scatter(DwellTimes, Amplitudes_pos, s= 10, color =colors_dict['other1'], marker='o', zorder=0)
    ax.set_ylabel('Amplitude (pA)')
    ax.set_xlabel('Time (s)')
    canvas.draw()

def PlotAmplitudes(figure,canvas,AllEvents, colors_dict):
    figure.clear()
    ax = figure.add_subplot(111)
    number = AllEvents.GetAllNumber()
    Amplitudes_pos = AllEvents.GetAllAmplitudes_pos()
    Amplitudes_neg = AllEvents.GetAllAmplitudes_neg()
    ax.title.set_text("Amplitudes")
    ax.scatter(number, Amplitudes_pos, color =colors_dict['other1'], s= 10, marker='o', label = 'Positive', zorder=0)
    ax.scatter(number, Amplitudes_neg, color =colors_dict['other2'], s= 10, marker='o', label = 'Negative', zorder=0)
    ax.legend(loc='upper center')
    ax.set_ylabel('Amplitude (pA)')
    ax.set_xlabel('Event number')
    canvas.draw()

def PlotDwellTimes(figure,canvas,AllEvents, colors_dict, type):
    figure.clear()
    ax = figure.add_subplot(111)
    number = AllEvents.GetAllNumber()
    if type == 0:
        DwellTimes = AllEvents.GetAllDwellTimes()
    elif type == 1:
        DwellTimes = AllEvents.GetAllFWHMTimes()
    ax.title.set_text("Dwell Times")
    ax.scatter(number, DwellTimes, color =colors_dict['other1'], s= 10, marker='o', zorder=0)
    ax.set_ylabel('Dwell Time (s)')
    ax.set_xlabel('Event number')
    canvas.draw()

def PlotRiseDecayTimes(figure,canvas,AllEvents, colors_dict,type):
    figure.clear()
    ax = figure.add_subplot(111)
    number = AllEvents.GetAllNumber()
    if type == 0:
        RiseTime = AllEvents.GetAllRiseTimes()
        DecayTime = AllEvents.GetAllDecayTimes()
    elif type == 1:
        RiseTime = AllEvents.GetAllFWHM_riseTimes()
        DecayTime = AllEvents.GetAllFWHM_decayTimes()

    ax.title.set_text("Rise and Decay Times")
    ax.scatter(number, RiseTime, color =colors_dict['other1'],s= 10, marker='o', label = 'RiseTime', zorder=0)
    ax.scatter(number, DecayTime, color =colors_dict['other2'], s= 10, marker='o', label = 'DecayTime', zorder=0)
    ax.legend(loc='upper center')
    ax.set_ylabel('Time(s)')
    ax.set_xlabel('Event number')
    canvas.draw()

def PlotCurrentDistribution(figure,canvas,data,bins,s, colors_dict, AllEvents):
    ticks = []
    labels = []
    mean = np.mean(data)
    std = np.std(data)
    if bins.isdigit():
        bins = int(bins)
    else:
        bins = 'auto'

    if s.isdigit():
        s=int(s)
        p_min = mean - std * s
        p_max = mean + std * s

        for i in range(-1* s,s+1 ):
            if i == 0:
                ticks.append(mean + std * i)
                labels.append(str(i))
            else:
                ticks.append(mean + std * i)
                labels.append(str(i) + "σ")
    else:
        p_min = np.min(data)
        p_max = np.max(data)

    figure.clear()
    ax= figure.add_subplot(111)
    n, bins, patches = ax.hist(data, bins=bins,range=(p_min,p_max), color =colors_dict['current_dist'], density = True)
    ax.title.set_text("Current Distribution")
    ax.set_ylabel('Probability')
    ax.set_xlabel('Standard deviation')
    ax.set_xticks(ticks, labels)
    ax.grid(True)
    canvas.draw()

# def PlotCurrentDistributionDeleted(figure,canvas,data,bins,s, colors_dict, AllEvents):
#
#     ticks = []
#     labels = []
#     mean = np.mean(data)
#     std = np.std(data)
#     if bins.isdigit():
#         bins = int(bins)
#     else:
#         bins = 'auto'
#
#     if s.isdigit():
#         s=int(s)
#         p_min = mean - std * s
#         p_max = mean + std * s
#
#         for i in range(-1* s,s+1 ):
#             if i == 0:
#                 ticks.append(mean + std * i)
#                 labels.append(str(i))
#             else:
#                 ticks.append(mean + std * i)
#                 labels.append(str(i) + "σ")
#     else:
#         p_min = np.min(data)
#         p_max = np.max(data)
#
#     # Try deletion
#     sP = AllEvents.GetAllStartPoints()
#     eP = AllEvents.GetAllEndPoints()
#     i = len(sP) - 1
#     while (i >= 0):
#         data = np.delete(data, np.s_[sP[i]:eP[i]])
#         i = i - 1
#     figure.clear()
#     ax= figure.add_subplot(111)
#     n, bins, patches = ax.hist(data, bins=bins,range=(p_min,p_max), color =colors_dict['current_dist'], density = True)
#     ax.title.set_text("Current Distribution")
#     ax.set_ylabel('Probability')
#     ax.set_xlabel('Standard deviation')
#     ax.set_xticks(ticks, labels)
#     ax.grid(True)
#     canvas.draw()
#     # figure.clear()
#     # ax = figure.add_subplot(111)
#     #
#     # ax.plot(data, color=colors_dict['current'], label='Current Trace', linewidth=0.7, zorder=0)
#     # ax.title.set_text("Raw data")
#     # ax.legend(loc="upper right")
#     # ax.set_xlabel('Time (s)')
#     # ax.set_ylabel('Current (pA)')
#     # canvas.draw()


# class AnchoredHScaleBar(matplotlib.offsetbox.AnchoredOffsetbox):
#     """ size: length of bar in data units
#         extent : height of bar ends in axes units """
#     def __init__(self, size=1, extent = 0.03, label="", loc=2, ax=None,
#                  pad=0.4, borderpad=0.5, ppad = 0, sep=2, prop=None,
#                  frameon=True, linekw={}, **kwargs):
#         if not ax:
#             ax = plt.gca()
#         trans = ax.get_xaxis_transform()
#         size_bar = matplotlib.offsetbox.AuxTransformBox(trans)
#         line = Line2D([0,size],[0,0], **linekw)
#         size_bar.add_artist(line)
#         txt = matplotlib.offsetbox.TextArea(label, minimumdescent=False)
#         self.vpac = matplotlib.offsetbox.VPacker(children=[size_bar,txt], align="center", pad=ppad, sep=sep)
#         matplotlib.offsetbox.AnchoredOffsetbox.__init__(self, loc, pad=pad, borderpad=borderpad, child=self.vpac, prop=prop, frameon=frameon,**kwargs)
#
# class AnchoredVScaleBar(matplotlib.offsetbox.AnchoredOffsetbox):
#     """ size: length of bar in data units
#         extent : height of bar ends in axes units """
#     def __init__(self, size=1, extent = 0.03, label="", loc=2, ax=None,
#                  pad=0.4, borderpad=0.5, ppad = 0, sep=2, prop=None,
#                  frameon=True, linekw={}, **kwargs):
#         if not ax:
#             ax = plt.gca()
#         trans = ax.get_yaxis_transform()
#         size_bar = matplotlib.offsetbox.AuxTransformBox(trans)
#         line = Line2D([0,0],[0,size], **linekw)
#         size_bar.add_artist(line)
#         txt = matplotlib.offsetbox.TextArea(label, minimumdescent=False)
#         self.vpac = matplotlib.offsetbox.VPacker(children=[size_bar,txt], align="left", pad=ppad, sep=sep)
#         matplotlib.offsetbox.AnchoredOffsetbox.__init__(self, loc, pad=pad, borderpad=borderpad, child=self.vpac, prop=prop, frameon=frameon,**kwargs)
#

def PlotOverlay(figure, canvas, AllEvents, samplerate,scalebar, colors_dict):
    traces = AllEvents.GetAllCurrentTraces()

    figure.clear()
    ax = figure.add_subplot(111)
    center = []

    for trace in traces:
        center.append(np.argmax(trace))

    i=0

    for trace in traces:
        diff = 0 - center[i]
        x= np.arange(0, len(trace), 1) + (diff)
        microsec= 1/samplerate * 1000000
        x= x*microsec
        ax.plot(x,trace,color = 'k', alpha = 0.15, linewidth = '1')
        i=i+1

    ax.title.set_text("Event Traces")
    ax.set_ylabel('Current (pA)')
    ax.set_xlabel('Time (s)')
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    ax.legend([Line2D([0], [0], color='k', alpha = 1, linewidth = '1')], ['Overlayed Event Traces'])


    #Scale Bar
    # timescale = scalebar['time'] #μs
    # currentscale = scalebar['current'] # pA
    # obH = AnchoredHScaleBar(size=(timescale/samplerate)*1000000, label=str(timescale) + "μs", loc=2, frameon=False,pad=0.0, sep=4, linekw=dict(color="black"), )
    # obV = AnchoredVScaleBar(size=currentscale, label=str(currentscale) + "pA", loc=2 , frameon=False,pad=0.0, sep=4, linekw=dict(color="black"), )
    # ax.add_artist(obH)
    # ax.add_artist(obV)

    canvas.draw()

