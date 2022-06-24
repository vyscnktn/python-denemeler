import matplotlib.pyplot as plt
import seaborn as sns

def random(start):
    a = 211
    b = 1663
    c = 7875
    start = (start*a+b) % c
    return float(start)/float(c)


liste = [random(i) for i in range(100)]


sns.scatterplot(data=liste);
sns.lineplot(data=liste);
plt.show(block=True)

random(1000000000000)
