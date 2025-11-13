# Flood Forecasting for Northeast India

This project focuses on developing a flood forecasting system for Northeast India using satellite data and machine learning.

## Project Structure

```
flood_forecasting_ne_india/
├── data/               # Data storage
│   ├── raw/           # Raw data files
│   └── processed/     # Processed data files
├── notebooks/         # Jupyter notebooks for exploration
└── src/               # Source code
    ├── data/          # Data processing scripts
    ├── models/        # Model training and evaluation
    └── visualization/ # Visualization utilities
```

## Setup

1. Create and activate conda environment:
   ```bash
   conda create -n flood_forecast python=3.10
   conda activate flood_forecast
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up Earth Engine (one-time setup):
   ```bash
   earthengine authenticate
   ```

## Usage

1. Activate the environment:
   ```bash
   conda activate flood_forecast
   ```

2. Start Jupyter Lab:
   ```bash
   jupyter lab
   ```

## Data Sources

- Satellite Imagery: Google Earth Engine
- Rainfall Data: IMD Gridded Data
- Terrain Data: SRTM DEM
- River Gauge Data: CWC (Central Water Commission)

## License

MIT
