# visualization.py
import matplotlib.pyplot as plt
import geopandas as gpd

def generate_visualization(data, visualization_type):
    """Generate a visualization based on the type provided."""
    if visualization_type == "map":
        # Example: Plot data points on a map
        plot_map(data)
    elif visualization_type == "bar chart":
        # Example: Generate a bar chart
        plot_bar_chart(data)
    elif visualization_type == "scatter plot":
        # Example: Generate a scatter plot
        plot_scatter(data)
    else:
        print("Visualization type not recognized")

def plot_map(data):
    """Generate a basic map plot."""
    # Assuming `data` has 'latitude' and 'longitude' columns
    gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude))
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    ax = world.plot()
    gdf.plot(ax=ax, color="red", markersize=5)
    plt.show()

def plot_bar_chart(data):
    """Generate a basic bar chart."""
    data['some_category'].value_counts().plot(kind='bar')
    plt.show()

def plot_scatter(data):
    """Generate a scatter plot."""
    data.plot(kind='scatter', x='x_column', y='y_column')
    plt.show()
