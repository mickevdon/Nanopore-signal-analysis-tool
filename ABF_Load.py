import pyabf
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def getfilepath():
   Tk().withdraw() #keep root window from appearing
   filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
   return filename

def loadABF():
   """Function used to import abf data.
   It loads .abf file and returns relevant information

   Returns:
   dict:
       'i' (ndarray):  current trace
       't' (ndarray):  timestamps
       'samplerate' (float): sampling frequency
       'filename' (string): full path to the data file
       'ID' (string): abf ID
   """
   datafilename = getfilepath()
   abf = pyabf.ABF(datafilename)
   abfID = (abf.abfID)
   output = {'i': abf.getAllYs(0),'t': abf.getAllXs(0), 'samplerate': abf.dataRate, 'filename': datafilename, 'ID': abfID}
   return output

