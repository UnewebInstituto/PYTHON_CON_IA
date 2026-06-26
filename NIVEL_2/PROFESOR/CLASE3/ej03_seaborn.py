# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
<seaborn.axisgrid.FacetGrid object at 0x0000025BF41F2C00>
plt.show()