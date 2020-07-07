import matplotlib.pyplot as plt
# Data Sets 
Group = ['EUL','PES','EFA','EDD','ELDR','EPP','UEN','OTHER']
Seats = [39,200,42,15,67,276,27,66]
explode = (0,0,0,0,0,0.1,0,0)
# Specify the axis
plt.axis('equal')
# Give the Title
plt.title("European Parliment election ,2019")
# Colors Code 
colors = ['red','orangered','forestgreen','lemonchiffon','yellow','navy','royalblue','lightgrey']
plt.pie(x=Seats,colors=colors,autopct='%1.0f%%',explode=explode)
plt.legend(loc="center right", labels=Group)
plt.show()
