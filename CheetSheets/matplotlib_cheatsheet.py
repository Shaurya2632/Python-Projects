
import matplotlib.pyplot as plt
import numpy as np

# --------------------------------------
# Sample Data
# --------------------------------------
x = np.linspace(0, 10, 100)
y = np.sin(x)
data = np.random.randn(1000)

# --------------------------------------
# Basic Line Plot with All Arguments
# --------------------------------------
plt.figure(figsize=(8, 4))  # Set figure size in inches (width, height)
plt.plot(
    x, y,
    color='blue',              # Line color
    linestyle='--',            # Line style: solid, dashed, etc.
    linewidth=2,              # Width of the line
    marker='o',               # Marker style for points
    markersize=6,             # Size of the markers
    markerfacecolor='red',    # Fill color for markers
    markeredgecolor='black',  # Border color for markers
    alpha=0.8,                # Opacity of the line
    label='sin(x)'            # Label for legend
)
plt.title("Sine Wave Example", fontsize=14)  # Title with font size
plt.xlabel("X Axis", fontsize=12)            # Label for x-axis
plt.ylabel("Y Axis", fontsize=12)            # Label for y-axis
plt.grid(True, linestyle=':', linewidth=0.5) # Show grid with custom style
plt.legend(loc='upper right')                # Show legend in upper right
plt.xlim(0, 10)                               # Set x-axis range
plt.ylim(-1.5, 1.5)                           # Set y-axis range
plt.xticks(np.arange(0, 11, 1))               # Set x-axis ticks
plt.yticks(np.linspace(-1.5, 1.5, 7))         # Set y-axis ticks
plt.axhline(0, color='gray', linestyle='--') # Horizontal reference line
plt.axvline(5, color='gray', linestyle='--') # Vertical reference line
plt.fill_between(x, y, color='skyblue', alpha=0.2)  # Fill area under curve
plt.show()

# --------------------------------------
# Other Plot Types
# --------------------------------------
plt.bar([1, 2, 3], [3, 4, 5], color='skyblue', edgecolor='black', width=0.4)  # Bar chart
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

plt.scatter(x, y, color='green', marker='x', s=50, alpha=0.7, label='scatter')  # Scatter plot
plt.title("Scatter Plot")
plt.legend()
plt.show()

plt.hist(data, bins=30, color='purple', edgecolor='white', alpha=0.7, density=True)  # Histogram
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

plt.boxplot(
    [np.random.rand(10), np.random.rand(10)],
    notch=True,                                  # Notched box
    vert=True,                                   # Vertical box
    patch_artist=True,                           # Fill boxes with color
    boxprops=dict(facecolor='lightblue', color='blue')  # Box style
)
plt.title("Box Plot")
plt.show()

plt.pie(
    [10, 20, 30],
    labels=['A', 'B', 'C'],     # Labels for slices
    autopct='%1.1f%%',          # Percentage display
    startangle=90,              # Rotation angle
    explode=[0, 0.1, 0],        # Slice offset
    shadow=True                 # Add shadow
)
plt.title("Pie Chart")
plt.show()

# --------------------------------------
# Subplots
# --------------------------------------
plt.subplot(2, 1, 1)  # First subplot (2 rows, 1 column, first)
plt.plot(x, y)
plt.title("Top Plot")

plt.subplot(2, 1, 2)  # Second subplot
plt.plot(x, -y, color='orange')
plt.title("Bottom Plot")
plt.tight_layout()  # Adjust spacing
plt.show()

fig, axs = plt.subplots(2, 2, figsize=(10, 6))  # Create 2x2 subplot grid
axs[0, 0].plot(x, y)
axs[0, 0].set_title("Plot 1")
axs[0, 1].scatter(x, y, color='red')
axs[0, 1].set_title("Plot 2")
axs[1, 0].hist(data, bins=20)
axs[1, 0].set_title("Plot 3")
axs[1, 1].bar([1, 2, 3], [3, 2, 5])
axs[1, 1].set_title("Plot 4")
plt.tight_layout()
plt.show()

# --------------------------------------
# Save Plot and Window Customization
# --------------------------------------
plt.plot(x, y)
plt.title("Save This Plot Example")
plt.savefig("sine_wave.png", dpi=300, bbox_inches='tight', transparent=False)  # Save to file
plt.show()

fig = plt.figure()
fig.canvas.manager.set_window_title('My Custom Figure Window')  # Set window title
plt.plot(x, y)
plt.show()

# --------------------------------------
# Summary Table of Functions and Arguments
# --------------------------------------
# Function                          Description
# -------------------------------  --------------------------------------------
# plt.plot()                        Line plot with customization options
# plt.bar()                         Vertical bar chart
# plt.scatter()                     Scatter plot with point styling
# plt.hist()                        Histogram with adjustable bins
# plt.boxplot()                     Box-and-whisker plot
# plt.pie()                         Pie chart with slice customization
# plt.subplot()                     Manual subplot grid placement
# plt.subplots()                    Auto subplot layout with Axes objects
# plt.title()                       Title of the plot
# plt.xlabel(), plt.ylabel()        Axis labels
# plt.legend()                      Legend for labeled items
# plt.grid()                        Toggle and style grid
# plt.savefig()                     Save plot to file
# plt.xlim(), plt.ylim()            Axis range limits
# plt.xticks(), plt.yticks()        Custom tick marks
# plt.axhline(), plt.axvline()      Add reference lines
# plt.fill_between()                Fill under/between curves
# plt.tight_layout()                Avoid subplot overlap
# fig.canvas.manager.set_window_title()  Set custom window title
