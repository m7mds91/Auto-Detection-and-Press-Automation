# Auto Arrow Detection and Press Automation

This Python script automates arrow key presses by visually detecting highlighted directional arrows within a selected region on the screen. It's particularly useful for gaming automation where directional inputs must be provided based on visual cues.

## Features
- **Real-time Detection:** Uses image processing (OpenCV) to identify highlighted arrows on-screen.
- **Automatic Keypress:** Simulates key presses using DirectInput (`pydirectinput`), ensuring compatibility with most games.
- **User-friendly Setup:** Interactive selection of the detection area.
- **Customizable Sensitivity:** Easily adjustable brightness threshold for accurate detection.

## Installation

Ensure Python 3.7 or higher is installed.

Install dependencies:

```bash
pip install opencv-python numpy mss pydirectinput
```

## Usage

1. **Run the script:**

```bash
python auto_arrow_press.py
```

2. **Select Region:**
   - A screenshot window will appear; select the region containing the arrows by dragging the mouse, then press `ENTER`.

3. **Automation:**
   - The script will continuously detect highlighted arrows and simulate the corresponding arrow keypress automatically.

4. **Stop the script:**
   - Press the `q` key at any time to terminate the script.

## Recommendations
- Run your game in "Borderless Window" or "Windowed" mode.
- Execute the script with administrator privileges for optimal performance.

## Adjustments and Calibration

If detection isn't accurate, run the calibration script provided in the repository to determine optimal brightness thresholds, and adjust this line accordingly:

```python
return mean_brightness > threshold  # Adjust based on calibration results
```

## Contributions

Feel free to fork, enhance, or open pull requests!

