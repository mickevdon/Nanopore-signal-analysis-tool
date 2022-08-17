# Nanopore-signal-analysis-tool
Software for nanopore signal analysis with Python based GUI.

![GUI_github](https://user-images.githubusercontent.com/94792865/185167884-b51d70b1-25c1-4b1d-9d1e-83b36e7363be.png)

Features:
- Event detection using amplitude threshold detection algorithm
  - Baseline
    - Non-overlapping dynamic window average
    - Polynomial fit
    - Arithmetic mean
    - Gaussian Smoothing
  - Threshold
    - User defined constant
    - Multiple of standard deviation
- Analysis results
  - Dwell time
     - Baseline crossing/defined threshold
     - FWHM
  - Amplitude
    - Current peak maxima
- Signal crop
- Save results
- Advanced results visualisation

![Main drawio](https://user-images.githubusercontent.com/94792865/185168882-50f6b09c-55ad-4f04-9642-de5fcbeb6041.png)

