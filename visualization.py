import matplotlib.pyplot as plt
import seaborn as sns

# Creating a bar chart for the specified column
def create_bar_chart(df, column):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind="bar", color="skyblue")
    plt.title(f"Bar Chart for {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Creating a scatter plot for specified x and y columns
def create_scatter_plot(df, x_column, y_column):
    if x_column not in df.columns or y_column not in df.columns:
        raise ValueError(f"Columns '{x_column}' or '{y_column}' not found in DataFrame.")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_column, y=y_column)
    plt.title(f"Scatter Plot: {x_column} vs {y_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.tight_layout()
    plt.show()

# Createing a histogram for specified column
def create_histogram(df, column, bins=10):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=bins, color="pink", edgecolor="black")
    plt.title(f"Histogram for {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# Creating a box plot for the column
def create_box_plot(df, column):
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame.")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, y=column)
    plt.title(f"Box Plot for {column}")
    plt.ylabel(column)
    plt.tight_layout()
    plt.show()
