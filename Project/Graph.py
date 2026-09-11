import os
import matplotlib.pyplot as plt
import numpy as np

folder_path = "."
file_name_gravity = "Gravity.csv"
file_name_barometer = "Barometer.csv"
file_name_attitude = "Orientation.csv"
file_name_gyroscope = "Gyroscope.csv"

fullpath_gravity = os.path.join(folder_path, file_name_gravity)
fullpath_barometer = os.path.join(folder_path, file_name_barometer)
fullpath_attitude = os.path.join(folder_path, file_name_attitude)
fullpath_gyroscope = os.path.join(folder_path, file_name_gyroscope)

data_gravity = np.loadtxt(fullpath_gravity, delimiter=",", skiprows=1)
data_barometer = np.loadtxt(fullpath_barometer, delimiter=",", skiprows=1)
data_attitude = np.loadtxt(fullpath_attitude, delimiter=",", skiprows=1)
data_gyroscope = np.loadtxt(fullpath_gyroscope, delimiter=",", skiprows=1)

time_gravity = data_gravity[:, 0]
ax_gravity = data_gravity[:, 1]
ay_gravity = data_gravity[:, 2]
az_gravity = data_gravity[:, 3]

time_barometer = data_barometer[:, 0]
ax_barometer = data_barometer[:, 1]

time_attitude = data_attitude[:, 0]
ax_attitude = data_attitude[:, 6]
ay_attitude = data_attitude[:, 7]
az_attitude = data_attitude[:, 8]

time_gyroscope = data_gyroscope[:, 0]
ax_gyroscope = data_gyroscope[:, 1]
ay_gyroscope = data_gyroscope[:, 2]
az_gyroscope = data_gyroscope[:, 3]


def plot_graph(
    x, y, z, time, title, xlabel, ylabel, xlegend, ylegend, zlegend):

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8), sharex=True)


    ax1.plot(time, x, color="crimson", label=xlegend)
    ax1.set_title(title)
    ax1.set_ylabel(ylabel)
    ax1.grid(True)
    ax1.legend()


    ax2.plot(time, y, color="green", label=ylegend)
    ax2.set_ylabel(ylabel)
    ax2.grid(True)
    ax2.legend()


    ax3.plot(time, z, color="blue", label=zlegend)
    ax3.set_xlabel(xlabel)
    ax3.set_ylabel(ylabel)
    ax3.grid(True)
    ax3.legend()

    plt.tight_layout()



plot_graph(
    ax_gravity,
    ay_gravity,
    az_gravity,
    time_gravity,
    "Acceleration Data",
    "Time (s)",
    "Acceleration (m/s²)",
    "X",
    "Y",
    "Z",
)
plot_graph(ax_barometer, np.zeros_like(ax_barometer), np.zeros_like(ax_barometer), time_barometer, 'Barometric Data', 'Time (s)', 'Pressure (hPa)', 'Pressure', '', '')
plot_graph(ax_attitude, ay_attitude, az_attitude, time_attitude, 'Orientation Data', 'Time (s)', 'Orientation (degrees)', 'Yaw', 'Pitch', 'Roll')
plot_graph(ax_gyroscope, ay_gyroscope, az_gyroscope, time_gyroscope, 'Angular Velocity Data', 'Time (s)', 'Angular Velocity (rad/s)', 'X', 'Y', 'Z')

plt.show()