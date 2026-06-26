Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Una API de alto nivel para gráficos estadísticos
# Apply the default theme
sns.set_theme()
# Load an example dataset
tips = sns.load_dataset("tips")
# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
<seaborn.axisgrid.FacetGrid object at 0x0000011E6E7FDEE0>
plt.show()
# Create a visualization
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
<seaborn.axisgrid.FacetGrid object at 0x0000011E6EB1D8B0>
plt.show()
dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)
SyntaxError: multiple statements found while compiling a single statement
dots = sns.load_dataset("dots")
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)
<seaborn.axisgrid.FacetGrid object at 0x0000011E730DAC30>
plt.show()
# Estimación estadística
fmri = sns.load_dataset("fmri")
fmri
     subject  timepoint event    region    signal
0        s13         18  stim  parietal -0.017552
1         s5         14  stim  parietal -0.080883
2        s12         18  stim  parietal -0.081033
3        s11         18  stim  parietal -0.046134
4        s10         18  stim  parietal -0.037970
...      ...        ...   ...       ...       ...
1059      s0          8   cue   frontal  0.018165
1060     s13          7   cue   frontal -0.029130
1061     s12          7   cue   frontal -0.004939
1062     s11          7   cue   frontal -0.025367
1063      s0          0   cue  parietal -0.006899

[1064 rows x 5 columns]
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
)
<seaborn.axisgrid.FacetGrid object at 0x0000011E730D8F50>
plt.show()
tips
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[244 rows x 7 columns]
)
SyntaxError: unmatched ')'
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
<seaborn.axisgrid.FacetGrid object at 0x0000011E72E2E030>
plt.show()
sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")
<seaborn.axisgrid.FacetGrid object at 0x0000011E6D630410>
plt.show()
# Representaciones distributivas
tips
     total_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

[244 rows x 7 columns]
sns.displot(data=tips, x="total_bill", col="time", kde=True)
<seaborn.axisgrid.FacetGrid object at 0x0000011E72E2FC80>
plt.show()
sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)
<seaborn.axisgrid.FacetGrid object at 0x0000011E6EB9AEA0>
plt.show()
# Gráficos para datos categóricos
sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")
<seaborn.axisgrid.FacetGrid object at 0x0000011E702F4A40>
plt.show()
sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)
<seaborn.axisgrid.FacetGrid object at 0x0000011E430B1A60>
plt.show()
sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")
<seaborn.axisgrid.FacetGrid object at 0x0000011E43063F20>
plt.show()
# Perspectivas multivariadas sobre conjuntos de datos complejos
penguins = sns.load_dataset("penguins")
penguins
    species     island  ...  body_mass_g     sex
0    Adelie  Torgersen  ...       3750.0    Male
1    Adelie  Torgersen  ...       3800.0  Female
2    Adelie  Torgersen  ...       3250.0  Female
3    Adelie  Torgersen  ...          NaN     NaN
4    Adelie  Torgersen  ...       3450.0  Female
..      ...        ...  ...          ...     ...
339  Gentoo     Biscoe  ...          NaN     NaN
340  Gentoo     Biscoe  ...       4850.0  Female
341  Gentoo     Biscoe  ...       5750.0    Male
342  Gentoo     Biscoe  ...       5200.0  Female
343  Gentoo     Biscoe  ...       5400.0    Male

[344 rows x 7 columns]
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")
<seaborn.axisgrid.JointGrid object at 0x0000011E430B3A40>
plt.show()
sns.pairplot(data=penguins, hue="species")
<seaborn.axisgrid.PairGrid object at 0x0000011E41EB3890>
plt.show()
# Herramientas de nivel inferior para construir figuras
g = sns.PairGrid(penguins, hue="species", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
<seaborn.axisgrid.PairGrid object at 0x0000011E6E9CB080>
g.map_lower(sns.scatterplot, marker="+")
341  Gentoo     Biscoe  ...       5750.0    Male
SyntaxError: multiple statements found while compiling a single statement
g.map_lower(sns.scatterplot, marker="+")
<seaborn.axisgrid.PairGrid object at 0x0000011E6E9CB080>
g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
<seaborn.axisgrid.PairGrid object at 0x0000011E6E9CB080>
g.add_legend(frameon=True)
<seaborn.axisgrid.PairGrid object at 0x0000011E6E9CB080>
g.add_legend(frameon=True)
<seaborn.axisgrid.PairGrid object at 0x0000011E6E9CB080>
plt.show()
# Valores predeterminados con opiniones definidas y personalización flexible
sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g"
)
<seaborn.axisgrid.FacetGrid object at 0x0000011E42821BE0>
plt.show()
sns.set_theme(style="ticks", font_scale=1.25)
g = sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g",
    palette="crest", marker="x", s=100,
)
g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
<seaborn.axisgrid.FacetGrid object at 0x0000011E730C0830>
g.legend.set_title("Body mass (g)")
g.figure.set_size_inches(6.5, 4.5)
g.ax.margins(.15)
g.despine(trim=True)
<seaborn.axisgrid.FacetGrid object at 0x0000011E730C0830>
plt.show()
