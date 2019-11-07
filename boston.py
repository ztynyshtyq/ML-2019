import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

apl_price = [93.95, 112.15, 104.05, 144.85, 169.49]
ms_price = [39.01, 50.29, 57.05, 69.98, 94.39]
year = [2014, 2015, 2016, 2017, 2018]
fi_1 = plt.figure(1, figsize=(20, 5))
apple_price = fi_1.add_subplot(223)
microsoft_price = fi_1.add_subplot(224)
apple_price.plot(year, apl_price, 'ok')
apple_price.xaxis.set_major_locator(MaxNLocator(integer=True))
microsoft_price.plot(year, ms_price)
plt.xlabel('Year')
plt.ylabel('Stock Price')

plt.show()
