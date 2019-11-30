# import numpy as np
# import matplotlib.pyplot as plt

# men_means, men_std, = (936.30, 1.99, 1.83, 2.00, 137.84), (0.09, 0.09, 0.09, 0.09, 0.09)
# women_means, women_std = (239, 1, 1, 6, 8), (0, 0, 0, 0, 0)

# ind = np.arange(len(men_means))  # the x locations for the groups
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
#                 color='SkyBlue', label='Average Time (s)')
# rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
#                 color='IndianRed', label='Average Cost (¢)')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Time and Cost')
# ax.set_xlabel('Cryptocurrencies')
# ax.set_title('Further Average Raw Data')
# ax.set_xticks(ind)
# ax.set_xticklabels(('Bitcoin', 'Tron', 'Dash', 'Litecoin', 'Ethereum'))
# ax.legend()


# def autolabel(rects, xpos='center'):
#     """
#     Attach a text label above each bar in *rects*, displaying its height.

#     *xpos* indicates which side to place the text w.r.t. the center of
#     the bar. It can be one of the following {'center', 'right', 'left'}.
#     """

#     xpos = xpos.lower()  # normalize the case of the parameter
#     ha = {'center': 'center', 'right': 'left', 'left': 'right'}
#     offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
#                 '{}'.format(height), ha=ha[xpos], va='bottom')


# autolabel(rects1, "left")
# autolabel(rects2, "right")

# plt.show()

"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data = {'Bitcoin': 0.198, 'Litecoin': 0.015, 'Ethereum': 0.01, 'Dash': 0.00076, 'Tron': 0.0000018}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1)
axs.bar(names, values)
fig.suptitle('Categorical Plotting')

plt.show()
"""