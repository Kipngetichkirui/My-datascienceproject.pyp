
# import matplotlib.pyplot as plt
import matplotlib.pyp as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample Data - Visitors (in thousands) for different months
months = ["July", "August", "September", "October", "November"]
series_names = ["Searches", "Direct", "Social media"]
data = np.random.randint(20, 100, size=(5, 3))  # Random visitor numbers

# Convert to DataFrame
df = pd.DataFrame(data, columns=series_names, index=months)

# Plot settings
plt.figure(figsize=(8, 6))
df.plot(kind="bar", colormap="viridis", edgecolor="black")

# Labels & Title
plt.xlabel("Months")
plt.ylabel("Visitors (in Thousands)")
plt.title("visitors by web traffic sources")
plt.legend(title="Websites")

# Save the visualization
chart_path = "/mnt/data/visitor_chart.png"
plt.savefig(chart_path)

# Show the chart
plt.show()