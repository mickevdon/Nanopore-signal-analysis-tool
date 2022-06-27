import numpy as np
from scipy.ndimage import gaussian_filter1d
def flip_x(input):
   """
      Function used to change the sign of input values.
      -------
      Parameters:
         'input' (ndarray): with ionic current data
      Returns
      -------
      List
          'rsignal' (ndarray): signal with reversed sign
   """
   flipped = -1*input
   return flipped

def constructBaseline(baseline_type, data, window_size_s, polynomial_order, gauss_std):
   """Function used to construct baseline for the signal

   -------
   Parameters:
      'type' (int): A value which defines baseline construction method
         0 - Non-overlapping Moving window average
         1 - Average
         2 - Polynomial fit
         3 - Gaussian Smoothing
      'input' (dict): abf file data
      'window_size_s' (float): window size in seconds
   Returns
   -------
   List
       'baseline' (ndarray): Baseline values
   """
   if baseline_type == 0:  # Moving window average
      window_size = int(window_size_s * data['samplerate'])
      av_arr = np.array(data['i'])
      # https://stackoverflow.com/questions/15956309/averaging-over-every-n-elements-of-a-numpy-array
      av_arr = np.nanmean(np.pad(av_arr.astype(float), (0, ((window_size - av_arr.size % window_size) % window_size)), mode='constant', constant_values=np.NaN).reshape(-1,window_size),axis=1)
      baseline = []
      mod = len(data['i']) % window_size
      if mod ==0: #Moving average
         for i in range(len(av_arr)):
            fill = np.full(window_size, av_arr[i])
            baseline = np.append(baseline, fill)
         return baseline

      elif mod !=0:
         for i in range(len(av_arr)-1):
            fill = np.full(window_size, av_arr[i])
            baseline = np.append(baseline, fill)

         filllast = np.full(len(data['i'])-len(baseline),av_arr[-1])
         baseline = np.append(baseline, filllast)
         return baseline

   if baseline_type == 1:  # Average
      baseline = np.full((1, len(data['i'])), np.average(data['i']))
      return baseline[0]

   if baseline_type == 2:  # Polynomial fit
      p = np.polyfit(data['t'], data['i'], polynomial_order)
      baseline = np.polyval(p, data['t'])
      return baseline

   if baseline_type == 3:  # Gaussian smoothing
      baseline = gaussian_filter1d(data['i'], gauss_std)
      return baseline

   else:
      return -1