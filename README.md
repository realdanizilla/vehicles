## Project Objective
The objective of this project is to perform an Exploratory Data Analysis (EDA) on a dataset containing car listings and to build an interactive web application using Streamlit. The web app enables visualization of key metrics like car prices, mileage, and distribution of other attributes to gain insights into the data.

## Project Structure

**Exploratory Data Analysis:**

- Dataset Overview: The dataset contains 51,525 records with 13 columns, including price, model_year, odometer, and other car attributes. Some columns like cylinders, odometer, and is_4wd have missing values that were handled during the analysis.
- Descriptive Statistics: Provided insights into the distribution of prices, model years, mileage (odometer), and listing durations, among others.
- Visualizations: Various charts were created, such as histograms for car prices and scatter plots showing the relationship between price and odometer readings.
Interactive Web Application with Streamlit:

**App Functionality:**
- Users can generate interactive charts such as histograms and scatter plots based on the car listings dataset.
- Includes a feature to display the dataset as a table.
- Provides options to create charts using buttons or checkboxes, offering flexibility in data exploration.

**Visualizations Provided:**
- A histogram visualizing car prices, ranging from $0 to $60,000.
- A scatter plot depicting the relationship between car price and mileage, with an option to include a trendline.

**Tools and Techniques Utilized**
- Python Libraries:
  - pandas: Used for data manipulation, handling missing values, and providing descriptive statistics.
  - plotly-express: Created interactive visualizations such as histograms and scatter plots to explore the dataset.
  - streamlit: Developed a web application for an interactive experience to analyze the car listings dataset.

**EDA Techniques:**

- Data cleaning, handling missing values, and calculating descriptive statistics to understand the dataset's structure.
- Visualization of data distributions and relationships between variables.

**Web Application Development:**
- Built a Streamlit app with interactive elements like buttons and checkboxes to generate visualizations based on user input.

## Specific Results and Outcomes

**Dataset Analysis and Key Findings:**
- **Price Distribution**: The car prices ranged from $0 to around $60,000, with the majority of cars priced below $20,000. The data revealed that there were some extremely low prices, which could indicate potential data entry errors or promotional pricing.
- **Odometer Readings**: Most cars had odometer readings under 150,000 miles, indicating that the dataset predominantly features cars with moderate usage. There were a few high-mileage cars, creating a right-skewed distribution.
- **Year of Manufacture**: Cars in the dataset were manufactured between the years 1900 and 2021, with a concentration around more recent years. The majority of cars were manufactured between 2000 and 2015.

**Visualization Insights:**
- **Price vs. Mileage (Odometer)**: A scatter plot indicated a negative correlation between car price and odometer readings: as the mileage increased, the price generally decreased. However, there were exceptions, with some high-mileage cars priced higher than expected, potentially due to model-specific factors.
- **Model Year vs. Price**: A bar chart showed that more recent cars tend to have higher prices, as expected. The analysis indicated that the average price significantly drops for cars older than 10 years.
- **Price Distribution for Popular Brands**: By filtering car listings by brand, the analysis found that certain brands (e.g., luxury brands) maintained higher average prices even for older models. More budget-friendly brands had prices that depreciated more quickly over time.

**Handling Missing Values and Outliers:**
- **Missing Values**: Columns such as cylinders and is_4wd had missing values. These were either filled with appropriate substitutes (e.g., mode of the column) or excluded from visualizations when necessary.
- **Outlier Detection and Management**: Extreme values in car prices (like cars listed at $0 or extremely high values) were treated as outliers. Their impact on statistical analysis and visualizations was examined, and filters were applied to improve data quality in charts.

**Building Interactive Visualizations:**
- The Streamlit app allowed users to explore the data by generating their own histograms and scatter plots. This interactive approach provided:
- **Filtering Options**: Users could filter based on specific criteria like model year or mileage to see tailored visualizations.
- **Real-time Updates**: Charts updated dynamically based on user input, making it easy to observe how different factors influence car prices and attributes.

**Web App Deployment and User Experience:**
- The app was deployed on Render, allowing users to interact with the car listings data in real-time. It provided a smooth experience for generating plots and understanding the data without requiring any programming knowledge.
- Checkbox controls were added as an alternative to buttons, enhancing the user experience by allowing multiple chart types to be generated seamlessly.


## What I Have Learned From This Project (Skills and Competences)

**Data Analysis Skills:**
- Efficiently handled a real-world dataset with missing values and extracted insights using descriptive statistics and visual exploration.
- Gained experience in creating interactive visualizations to communicate data findings effectively.

**Streamlit Web Development:**
- Developed skills in building an interactive web app to allow users to explore data through visualizations.
- Learned how to integrate data visualization libraries like plotly-express into a web framework.

**Data Visualization:**
- Developed a deeper understanding of how to create and customize different types of charts (e.g., histograms, scatter plots).
- Improved competency in presenting complex data in a user-friendly manner through an interactive interface.

URL for app on render: https://vehicles-pawu.onrender.com
