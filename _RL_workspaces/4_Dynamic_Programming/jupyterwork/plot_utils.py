import numpy as np
import matplotlib.pyplot as plt


def plot_values(V, shape=(4, 4)):
	# reshape value function
	V = np.reshape(V, shape)
	# plot the state-value function
	fig = plt.figure(figsize=(12, 12))
	ax = fig.add_subplot(111)
	im = ax.imshow(V, cmap='cool')
	for (j, i), label in np.ndenumerate(V):
	    ax.text(i, j, np.round(label, 5), ha='center', va='center', fontsize=14)
	plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
	plt.title('State-Value Function')
	plt.show()