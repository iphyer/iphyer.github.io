"""
[This codes show how to read in data and plot parity plot]

"""
# Import libraries

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score

# Font for figure for publishing
font_axis_publish = {
        'color':  'black',
        'weight': 'bold',
        'size': 22,
        }
plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 16

# Read in data
pred_vals = pd.read_csv("pred.csv", header=0, names=['Index','Pred'])
gt_vals = pd.read_csv("gt.csv",header=0, names=['Index','GT'])

# Plot Figures
fignow = plt.figure(figsize=(8,8))

x = gt_vals['GT']
y = pred_vals['Pred']

## find the boundaries of X and Y values
bounds = (min(x.min(), y.min()) - int(0.1 * y.min()), max(x.max(), y.max())+ int(0.1 * y.max()))

# Reset the limits
ax = plt.gca()
ax.set_xlim(bounds)
ax.set_ylim(bounds)
# Ensure the aspect ratio is square
ax.set_aspect("equal", adjustable="box")

plt.plot(x,y,"o", alpha=0.5 ,ms=10, markeredgewidth=0.0)

ax.plot([0, 1], [0, 1], "r-",lw=2 ,transform=ax.transAxes)

# Calculate Statistics of the Parity Plot 
mean_abs_err = np.mean(np.abs(x-y))
rmse = np.sqrt(np.mean((x-y)**2))
rmse_std = rmse / np.std(y)
z = np.polyfit(x,y, 1)
y_hat = np.poly1d(z)(x)

text = f"$\: \: Mean \: Absolute \: Error \: (MAE) = {mean_abs_err:0.3f}$ \n $ Root \: Mean \: Square \: Error \: (RMSE) = {rmse:0.3f}$ \n $ RMSE \: / \: Std(y) = {rmse_std :0.3f}$ \n $R^2 = {r2_score(y,y_hat):0.3f}$"

plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,
     fontsize=14, verticalalignment='top')

# Title and labels 
plt.title("Parity Plot", fontdict=font_axis_publish)
plt.xlabel('Ground Truth', fontdict=font_axis_publish)
plt.ylabel('Prediction', fontdict=font_axis_publish)

# Save the figure into 300 dpi
fignow.savefig("parityplot.png",format = "png",dpi=300,bbox_inches='tight')
