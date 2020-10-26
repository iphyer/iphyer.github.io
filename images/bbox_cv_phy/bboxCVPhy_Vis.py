import numpy as np

# create array data

predict = np.array([[1,2,2,1],
                   [4.5,2.5,10,0.5],
                   [6,6,8,4], 
                   [6.26,6.26,8.26,4.26]],np.double)

truth = np.array([[1,4,3,3],
                 [1.2,2.2,2.2,1.2],
                [5,2,8,1],
                [6.1,6.1,8.1,4.1],
                [8.1,8.1,11.1,9.1]], np.double)
# Below is to show the layout of the problem
# red represents truth
# blue represents prediction

import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
recList = list()

# Adding red rectangle from predict
for rect in predict:
    recList.append(
        patches.Rectangle(
            (rect[0], rect[3]),
             np.abs(rect[2] - rect[0]),
             np.abs(rect[3] - rect[1]),
             fill=False,
             edgecolor = "red"
        )
    )

# Adding blue rectangle for truth
for rect in truth:
    recList.append(
        patches.Rectangle(
            (rect[0], rect[3]),
             np.abs(rect[2] - rect[0]),
             np.abs(rect[3] - rect[1]),
             fill=False,
             edgecolor = "blue"
        )
    )

# plot the graph
for p in recList:
    ax.add_patch(p)

plt.text(1.15, 10, "red for precition", size=15, color="red" )
plt.text(1.15, 9, "blue for ground truth", size=15, color="blue" )

plt.plot()
plt.show()
fig.savefig('rect2.png', dpi=300, bbox_inches='tight')