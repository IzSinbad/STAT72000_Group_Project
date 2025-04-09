# Music Success Analysis Project

## Overview

This project analyzes cross-platform music success patterns using the "Most Streamed Spotify Songs 2024" dataset. The analysis examines how songs perform across different streaming platforms, the impact of playlists on streaming numbers, temporal trends in music popularity, and the relationship between explicit content and streaming performance.

## Project Structure

The analysis is divided into 5 Jupyter notebooks, each focusing on a specific aspect of the analysis:

1. **Data Loading and Cleaning** (`1_Data_Loading_Cleaning.ipynb`)
   - Loads the dataset and performs initial data cleaning
   - Converts string-formatted numbers with commas to numeric values
   - Extracts month and year from release dates
   - Creates derived metrics like platform ratios

2. **Statistical Analysis** (`2_Statistical_Analysis.ipynb`)
   - Calculates basic statistics for key metrics
   - Computes correlations between platforms
   - Performs hypothesis testing for explicit vs non-explicit tracks
   - Analyzes optimal release timing

3. **Platform Comparisons** (`3_Platform_Comparisons.ipynb`)
   - Compares performance across different streaming platforms
   - Analyzes time series patterns in music popularity
   - Visualizes cross-platform performance of top tracks

4. **Artist and Playlist Analysis** (`4_Artist_Playlist_Analysis.ipynb`)
   - Analyzes top artists by streaming numbers
   - Examines cross-platform artist presence
   - Investigates the impact of playlist inclusion on streaming performance

5. **Explicit Content Analysis and Conclusion** (`5_Explicit_Content_Analysis.ipynb`)
   - Analyzes the relationship between explicit content and streaming performance
   - Identifies factors that predict track success
   - Provides a comprehensive conclusion for the project

## Running the Analysis

### Prerequisites

- Python 3.6 or higher
- Jupyter Notebook
- Required Python libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - plotly
  - scipy
  - statsmodels
  - scikit-learn

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/IzSinbad/STAT72000_Group_Project.git
   cd STAT72000_Group_Project
   ```

2. Install the required Python libraries:
   ```
   pip install pandas numpy matplotlib seaborn plotly scipy statsmodels scikit-learn jupyter
   ```

### Running the Notebooks

#### Option 1: Run All Notebooks Automatically

Use the provided Python script to run all notebooks in sequence:

```
python run_all_notebooks.py
```

This script will:
- Execute each notebook in order
- Display progress and any errors
- Provide a summary of execution results

#### Option 2: Run Individual Notebooks

Open and run each notebook individually in Jupyter:

```
jupyter notebook
```

Then navigate to and open each notebook in the browser interface.

### Dataset

The analysis uses the "Most Streamed Spotify Songs 2024" dataset, which should be located at:
```
C:\Users\Adilf\Downloads\Most Streamed Spotify Songs 2024.csv (1)\Most Streamed Spotify Songs 2024.csv
```

If your dataset is in a different location, you'll need to update the file path in the first notebook.

## Key Findings

1. **Cross-Platform Success Correlation**
   - Success on one platform generally correlates with success on others, but the strength varies
   - Spotify and YouTube show the strongest correlation, suggesting similar audience preferences
   - TikTok success has a moderate correlation with other platforms, indicating it may have a somewhat distinct audience

2. **Playlist Impact**
   - Playlist inclusion has a significant positive impact on streaming numbers
   - Each additional playlist inclusion is associated with an increase in streams
   - Tracks in 40K+ playlists show dramatically higher average streams than those in fewer playlists

3. **Release Timing**
   - Certain months show higher average streaming performance
   - Releases in Q4 (Oct-Dec) tend to perform better on average
   - This may be related to holiday season listening patterns and year-end playlist curation

4. **Cross-Platform Artist Presence**
   - Top artists maintain strong presence across multiple platforms
   - The most successful artists show balanced performance rather than dominance on a single platform
   - Platform-specific strategies may be important for maximizing cross-platform success

5. **Explicit vs. Non-Explicit Content**
   - Explicit tracks generally perform differently than non-explicit tracks
   - The performance gap varies by platform, with some showing stronger differences than others
   - The distribution of explicit vs. non-explicit content varies across genres and artists

6. **Success Predictors**
   - Spotify playlist count and popularity are the strongest predictors of overall track success
   - YouTube views also significantly contribute to predicting track success
   - Release timing and explicit content have smaller but still measurable effects

## Contributors

- STAT72000 Group Project Team
