from Functions import *
class SingleEvent:
    """
    Translocation event class

    Attributes
    ----------
    number (int): translocation event id (number)
    eventStart(int): event start index
    eventEnd(int): event end index
    samplerate(int): samplerate
    currentTrace(ndarray): event current values
    dwellTime(ndarray): event timestamps
    riseTime(float): event rising time
    decayTime(float): event decay time
    traceBefore (ndarray) : current trace before event used for plotting and resistive peak detection
    traceAfter (ndarray) : current trace after event used for plotting
    timeStampsBefore (ndarray) : timestamps before event used for plotting and resistive peak detection
    timeStampsAfter (ndarray) : timestamps after event used for plotting
    currentTrace_cmb (ndarray) : current trace before/after event
    timeStamps_cmb (ndarray) : timestamps before/after event
    peakAmplitude_neg (float): negative peak amplitude
    FWHM_sP (int): FWHM start index
    FWHM_eP (int): FWHM end index
    FWHM_time (float): FWHM dwell time
    FWHM_riseTime (float): FWHM rise time
    FWHM_decayTime (float): FWHM decay time
    """
    def __init__(self, number):
        self.number = number

    def CreateEvent(self, eventStart, eventEnd, samplerate, current_trace,timestamps):
        self.eventStart = eventStart
        self.eventEnd = eventEnd
        self.samplerate = samplerate
        self.currentTrace = current_trace
        self.dwellTime = len(current_trace)/samplerate
        self.peakAmplitude_pos = max(self.currentTrace)
        self.timeStamps = timestamps
        self.riseTime = np.argmax(self.currentTrace) / self.samplerate
        self.decayTime = self.dwellTime - self.riseTime
        self.FWHF_dwellTime()

    def BeforeAndAfter(self,traceBefore, traceAfter, traceBefore_t, traceAfter_t, peakAmplitude_n):
        self.traceBefore = traceBefore
        self.traceAfter = traceAfter
        self.timeStampsBefore = traceBefore_t
        self.timeStampsAfter = traceAfter_t
        self.currentTrace_cmb = [*self.traceBefore, *self.currentTrace, *self.traceAfter]
        self.timeStamps_cmb = [*self.timeStampsBefore, *self.timeStamps, *self.timeStampsAfter]
        self.peakAmplitude_neg = peakAmplitude_n

    def FWHF_dwellTime(self): #recalculate
        half_amp = np.max(self.currentTrace) / 2
        Pabove = np.where(self.currentTrace > half_amp, 1, 0)
        difference = np.diff(Pabove)
        self.FWHM_sP = np.where(difference == 1)[0]  # Returns a list of indices where the conditions have been met.
        self.FWHM_eP = np.where(difference == -1)[0]  # Returns a list of indices where the conditions have been met.
        try:
            self.FWHM_time = float(self.FWHM_eP[-1] - self.FWHM_sP[0])/ self.samplerate
            self.FWHM_riseTime = (np.argmax(self.currentTrace) - self.FWHM_sP[0]) / self.samplerate
            self.FWHM_decayTime = (self.FWHM_eP[-1] - np.argmax(self.currentTrace)) / self.samplerate
        except:
            IndexError



class AllEvents:
    """"
    Class used to represent all the events.

    Attributes
    ----------
    events (list): list of translocation events

    """
    def __init__(self):
        self.events = []

    def AddEvent(self, Event):
        if isinstance(Event,AllEvents):
            if len(self.events) == 0:
                self.events = Event.events
            else:
                self.events.extend(Event.events)
        elif isinstance(Event,list):
            self.events.extend(Event)
        else:
            self.events.append(Event)

    def DeleteEvent(self, event_number):
        del self.events[event_number]

    def GetAllNumber(self):
        Number = [event.number for event in self.events]
        return Number

    def GetAllAmplitudes_pos(self):
        Amplitudes=[event.peakAmplitude_pos for event in self.events]
        return Amplitudes

    def GetAllAmplitudes_neg(self):
        Amplitudes=[event.peakAmplitude_neg for event in self.events]
        return Amplitudes

    def GetAllDwellTimes(self):
        DwellTimes = [event.dwellTime for event in self.events]
        return DwellTimes

    def GetAllStartPoints(self):
        StartPoints = [event.eventStart for event in self.events]
        return StartPoints

    def GetAllEndPoints(self):
        EndPoints = [event.eventEnd for event in self.events]
        return EndPoints

    def GetAllRiseTimes(self):
        RiseTimes = [event.riseTime for event in self.events]
        return RiseTimes

    def GetAllDecayTimes(self):
        DecayTimes = [event.decayTime for event in self.events]
        return DecayTimes

    def GetAllFWHMTimes(self):
        FWHMTimes = [event.FWHM_time for event in self.events]
        return FWHMTimes

    def GetAllFWHM_riseTimes(self):
        FWHMTimes = [event.FWHM_riseTime for event in self.events]
        return FWHMTimes

    def GetAllFWHM_decayTimes(self):
        FWHMTimes = [event.FWHM_decayTime for event in self.events]
        return FWHMTimes

    def GetAllCurrentTraces(self):
        Traces = [event.currentTrace for event in self.events]
        return Traces