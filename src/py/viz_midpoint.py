"""Visualize the Midpoint integration method."""

import matplotlib.pyplot as plt
import numpy as np

def viz_midpoint(f, x_points):

    def midpoint(x_points, f, samples_per_interval=31):
        # Compute element by element in case f does not work with array x
        x = []
        y = []
        y_exact = []
        for i in range(len(x_points)-1):
            mid = 0.5*(x_points[i] + x_points[i+1])
            yi = f(mid)
            dx = (x_points[i+1] - x_points[i])/float(samples_per_interval-1)
            for j in range(samples_per_interval):
                xi = x_points[i] + j*dx
                x.append(xi)
                y.append(yi)
                y_exact.append(f(xi))
        return np.array(x), np.array(y), np.array(y_exact)

    def midpoint_geometry(x_points, f):
        x = []
        y = []
        for i in range(len(x_points)-1):
            x.append(x_points[i])
            y.append(0)
            mid = 0.5*(x_points[i] + x_points[i+1])
            fmid = f(mid)
            x.append(x_points[i])
            y.append(fmid)
            x.append(x_points[i+1])
            y.append(fmid)
            x.append(x_points[i+1])
            y.append(0)
        return np.array(x), np.array(y)

    x, y, y_e = midpoint(x_points, f, 31)
    bx, by = midpoint_geometry(x_points, f)
    plt.plot(x, y_e, 'k-', linewidth=3)
    #plt.fill_between(x, y, y_e)
    #plt.plot(bx, by, 'r-')
    plt.fill(bx, by, 'r--')
    plt.savefig('tmp_midpoint.pdf'); plt.savefig('tmp_midpoint.png')
    plt.show()

if __name__ == '__main__':
    def v(t):
        return 3*t**2*np.exp(t**3)

    x_points = np.array([0, 0.2, 0.6, 0.8, 1.0])
    viz_midpoint(v, x_points)
