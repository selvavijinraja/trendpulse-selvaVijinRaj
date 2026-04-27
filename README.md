# TrendPulse Project

TrendPulse is a mini project designed to collect, process, analyze, and visualize trending stories data.  
This repository contains all four tasks, the processed dataset, and visualization outputs.

---

## 📂 Project Structure

trendpulse-<yourname>/
├── task1_data_collection.py      # Collects trending stories data  
├── task2_data_processing.py      # Cleans and processes the collected data  
├── task3_analysis.py             # Performs analysis on processed data  
├── task4_visualization.py        # Creates visualizations and dashboard  
├── data/  
│   └── trends_analysed.csv       # Dataset generated from Task 3  
└── outputs/  
├── chart1_top_stories.png    # Top 10 stories by score  
├── chart2_categories.png     # Stories per category  
├── chart3_scatter.png        # Score vs comments scatter plot  
└── dashboard.png             # Combined dashboard (bonus)  


---

## 🚀 Tasks Overview

### Task 1 — Data Collection
- Collects trending stories from source
- Saves raw data into CSV format

### Task 2 — Data Processing
- Cleans and structures the dataset
- Handles missing values and prepares for analysis

### Task 3 — Analysis
- Performs statistical and categorical analysis
- Generates `data/trends_analysed.csv`

### Task 4 — Visualization
- Creates three charts using Matplotlib:
  - Top 10 stories by score
  - Stories per category
  - Score vs comments scatter plot
- Combines charts into a dashboard

---

## 📊 Outputs
All charts are saved in the `outputs/` folder:
- `chart1_top_stories.png`
- `chart2_categories.png`
- `chart3_scatter.png`
- `dashboard.png`

---

## 🛠️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/trendpulse-<name>.git
   cd trendpulse-<name>

2. Make sure you have Python 3 and required libraries installed:
   ```
    pip install pandas matplotlib seaborn
   
4. Run each task script in order:
   ```
    python task1_data_collection.py
    python task2_data_processing.py
    python task3_analysis.py
    python task4_visualization.py
   
6. Check the outputs/ folder for generated charts.
