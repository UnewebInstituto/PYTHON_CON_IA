a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
print(a)
[ 2  1  5  7  4  6  8 14 10  9 18 20 22]
import matplotlib.pyplot as plt
plt.plot(a)
[<matplotlib.lines.Line2D object at 0x0000023CB4CFBD10>]
plt.show()
x = np.linspace(0, 5, 20)
y = np.linspace(0, 10, 20)
plt.plot(x, y, 'purple') # line
[<matplotlib.lines.Line2D object at 0x0000023CB60AEF60>]
plt.plot(x, y, 'o')      # dots
[<matplotlib.lines.Line2D object at 0x0000023CB60AF170>]
plt.show()
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
X = np.arange(-5, 5, 0.15)
Y = np.arange(-5, 5, 0.15)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
<mpl_toolkits.mplot3d.art3d.Poly3DCollection object at 0x0000023CB60EACF0>
plt.show()
