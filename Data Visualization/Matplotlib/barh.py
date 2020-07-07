# Horizontal bar chart

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='blue', ecolor='black')
##ax.set_yticks(y_pos)
##ax.set_yticklabels(people)
##ax.invert_yaxis()  # labels read top-to-bottom
##ax.set_xlabel('Performance')
##ax.set_title('How fast do you want to go today?')

plt.show()
##import matplotlib.pyplot as plt
##import numpy as np
##
##np.random.seed(19680801)
##data = np.random.randn(2, 100)
##
##fig, axs = plt.subplots(3, 3, figsize=(5, 5))
##axs[0, 0].hist(data[0])
##axs[1, 0].scatter(data[0], data[1])
##axs[0, 1].plot(data[0], data[1])
##axs[1, 1].hist2d(data[0], data[1])
##a = np.linspace(1,2,20)
##axs[0,2].barh(a[0],[2])
##
##
##plt.show()
