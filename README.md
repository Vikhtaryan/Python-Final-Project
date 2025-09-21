# CORD-19 Data Analysis and Visualization

Analyze and visualize the COVID-19 Open Research Dataset (CORD-19) metadata. This Python project enables data loading, cleaning, exploration, and insightful visualizations of COVID-19 research publications.

---

## Project Overview

This project processes the `metadata.csv` file from the CORD-19 dataset and performs the following:

### Part 1: Data Loading and Basic Exploration
- Download only the `metadata.csv` file from the [CORD-19 dataset](https://github.com/allenai/cord19).
- Load the file into a pandas DataFrame.
- Examine the first few rows and data structure.
- Basic data exploration including DataFrame dimensions, data types of each column.
- Check for missing values in key columns.
- Generate basic statistics for numerical columns.

### Part 2: Data Cleaning and Preparation
- Identify columns with many missing values and drop those exceeding a 50% missing threshold.
- Handle missing values by removing rows missing critical info, like title and publication date.
- Prepare data for analysis by converting date columns to datetime format.
- Extract publication year for time-based analysis.
- Create new columns if needed (e.g., abstract word count).

### Part 3: Data Analysis and Visualization
- Perform basic analysis, such as counting papers by publication year and identifying top journals.
- Compute simple word frequency on paper titles.
- Visualize results through:
  - Line plot for number of publications over time.
  - Bar chart of top publishing journals.
  - Word cloud of frequent words in titles.
  - Bar chart for paper counts by source (if available).
- Save each plot separately as PNG files and display them.

### Part 4: Streamlit Application (Future Work)
- Build an interactive Streamlit app with a simple layout, sliders, dropdowns.
- Display interactive visualizations and data samples.

---

## Setup and Requirements

### Dependencies:


### Download Data:

Download the latest `metadata.csv` from reliable sources:
- [AllenAI CORD-19 GitHub](https://github.com/allenai/cord19)
- [Kaggle CORD-19 dataset](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge)

Place `metadata.csv` in the same directory as the python script or update the path accordingly.


The script performs all cleaning, analysis, and visualization steps. It prints summaries and saves plots:

- `papers_per_year.png`
- `top_journals.png`
- `title_wordcloud.png`
- `papers_by_source.png` (if applicable)

---

## Project Structure


---

## Future Directions

- Develop the Streamlit app for interactive data exploration.
- Incorporate deeper text analysis on abstracts and keywords.
- Automate dataset version tracking and update detection.
- Extend plots and statistics for comprehensive research insights.

---

## License

This project is open-source and free for educational and research use.

---

## Contact

For questions or collaborations, please reach out via:

- Email: victornjoro1368@gmail.com
  

---



