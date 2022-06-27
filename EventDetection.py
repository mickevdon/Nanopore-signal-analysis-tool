
from Functions import *
import EventClasses as EC

def DetectEvents(data, threshold, parameters , BaF):
    """Function used to detect translocation events
    Main function of the software routine. Uses amplitude threshold detection approach to detect events.

   Args:
      'data' (dict): dictionary with .abf file data
      'threshold' (ndarray): numpy array with threshold values
      'parameters' (dict): dictionary with selected detection parameters

   Returns:
        list: containing all of the single translocation event objects
   """
    # Defining return threshold (by default its baseline i.e. =0). This is Return threshold.
    thresholdStart = 0  # Baseline start
    if parameters["start_threshold_type"] == 1:
        thresholdStart = np.std(data['i']) * parameters['start_std']

    thresholdEnd = 0  # Baseline start
    if parameters["end_threshold_type"] == 1:
        thresholdEnd = np.std(data['i']) * parameters['end_std']

    #Find points above threshold
    above = np.where(data['i']>threshold ,1 ,0) #Return list with 1 - above threshold/ 0 - below threshold
    difference = np.diff(above)
    #Find all start and end points
    startP = np.where(difference == 1)[0] #Returns a list of indices where the conditions have been met.
    endP = np.where(difference == -1)[0] #Returns a list of indices where the conditions have been met.
    #Error fixing related. Event start/end at the beginning/end of the current trace
    if startP[0] == 0:
        startP = np.delete(startP, 0)
        endP = np.delete(endP, 0)
    if endP[-1] == len(data['i'])-1:
        startP = np.delete(startP,-1)
        endP = np.delete(endP, -1)

    if len(endP) != len(startP):
        if endP[0] < startP[0]:
            endP = np.delete(endP, 0)
        elif endP[-1] < startP[-1]:
            startP = np.delete(startP , -1)

    #Amplitude-threshold detection algorithm
    eventCount = len(endP)
    for i in range(eventCount):
        s = startP[i]
        while data['i'][s] > thresholdStart and s>0: #Find real start point by tracing back from threshold
            s = s - 1
        startP[i] = s
        e = endP[i]  # Find real end point and trace back
        while data['i'][e] > thresholdEnd:
            e = e + 1
            try:
                if e > startP[i + 1]:  # Trace back and delete other points met
                    startP[i + 1] = 0
                    endP[i] = 0
                    e = 0
                    break
            except:
                IndexError
                break
        endP[i] = e

    startP = startP[startP != 0]  # Clear points
    endP = endP[endP != 0]  # Clear points

    # Fixing first event return to baseline
    if endP[0] < startP[0]:
        endP = np.delete(endP, 0)

    #Fix last event return to baseline
    if data['i'][endP[-1]] > thresholdEnd:
        while (data['i'][endP[-1]] > thresholdEnd and endP[-1]!= len(data['i'])-1):
            endP[-1] = endP[-1] + 1
        if endP[-1]== len(data['i'])-1:
            startP = np.delete(startP, -1)
            endP = np.delete(endP, -1)

    eventCount = len(endP)

    # Recalculate dwell times if fraction of amplitude
    th_amp = []
    if parameters["start_threshold_type"] == 2 or parameters["end_threshold_type"] == 2:
        for j in range(eventCount):
            th_amp.append(np.max(data['i'][startP[j]:endP[j]]))

    if parameters["start_threshold_type"] == 2:
        for j in range(eventCount):
            threshold[j] = th_amp[j] * parameters['start_fraction']
            while data['i'][startP[j]] < threshold[j]:
                startP[j] = startP[j] + 1

    if parameters["end_threshold_type"] == 2:
        for j in range(eventCount):
            threshold[j] = th_amp[j] * parameters['end_fraction']
            while data['i'][endP[j]] < threshold[j]:
                endP[j] = endP[j] - 1

    AllEvents = []
    peakAmplitude_n = []
    l = []
    # Get negative amplitude calculation i.e. negative peaks
    for i in range(eventCount):
        if (startP[i] - endP[i-1] < BaF):
            l.append(startP[i] - endP[i-1])
        else:
            l.append(BaF)
    if (startP[0] < BaF):
        l[0] = startP[0]
    else:
        l[0] = BaF

    #Create transolaction event objects
    for i in range(eventCount):
        current_trace = data['i'][startP[i]:endP[i]+1]
        timestamps = data['t'][startP[i]:endP[i]+1]
        #Get Current Trace before and after
        if (startP[0] > BaF):
            traceBefore = data['i'][startP[i]-BaF:startP[i]]
        else:
            traceBefore = data['i'][0:startP[i]]

        if (endP[-1] < (len(data['i'])-1 - BaF)):
            traceAfter = data['i'][endP[i]+1:endP[i]+BaF+1]
        else:
            traceAfter = data['i'][endP[i]+1:len(data['i'])-1]

        #Get TimeStamps Trace before and after
        if (startP[0] > BaF):
            traceBefore_t = data['t'][startP[i]-BaF:startP[i]]
        else:
            traceBefore_t = data['t'][0:startP[i]]

        if (endP[-1] < (len(data['t'])-1 - BaF)):
            traceAfter_t = data['t'][endP[i]+1:endP[i]+BaF+1]
        else:
            traceAfter_t = data['t'][endP[i]+1:len(data['i'])-1]

        if l[i]!= 0:
            peakAmplitude_n = (np.min(data['i'][startP[i]-l[i]:startP[i]]))
        else:
            peakAmplitude_n = data['i'][startP[i]]

        newEvent = EC.SingleEvent(i)
        newEvent.CreateEvent(startP[i], endP[i], data['samplerate'], current_trace, timestamps)
        newEvent.BeforeAndAfter(traceBefore, traceAfter, traceBefore_t, traceAfter_t, peakAmplitude_n)
        AllEvents.append(newEvent)
    return (AllEvents)


def CreateAllTranslocationEventsObject(SingleEventList):
    """Funtion to create an object caintaining all of the translocation events objects

    Args:
        SingleEventList (object): single translocation event object

    Returns:
        class: returns EventClasses.AllEvents object
    """
    All = EC.AllEvents()
    for event in SingleEventList:
            All.AddEvent(event)
    return All



