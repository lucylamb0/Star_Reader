import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

def record(x_position, y_position, z_position,
           x_velocity, y_velocity, z_velocity,
           x_acceleration, y_acceleration, z_acceleration):
    return {
        "position": {
            "x": x_position,
            "y": y_position,
            "z": z_position
        },
        "velocity": {
            "x": x_velocity,
            "y": y_velocity,
            "z": z_velocity
        },
        "acceleration": {
            "x": x_acceleration,
            "y": y_acceleration,
            "z": z_acceleration
        }
    }


# import the data from the csv file
def import_data(filename):
    star_records_star_1 = []
    star_records_star_2 = []
    with open(filename, 'r') as csvfile:
        data = np.genfromtxt(filename, delimiter=',', skip_header=1)

        for line in data:
            if 1 == line[0]:
                star_records_star_1.append(
                    record(line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]))
            elif 2 == line[0]:
                star_records_star_2.append(
                    record(line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]))
    return {
        "star_1": star_records_star_1,
        "star_2": star_records_star_2
    }

style.use('fivethirtyeight')

# get the data
star_records = import_data("2Stars.test.dump.txt")
# make a list of just x positions for star 1
x_positions_star_1 = [record["position"]["x"] for record in star_records["star_1"]]
# make a list of just y positions for star 1
y_positions_star_1 = [record["position"]["y"] for record in star_records["star_1"]]
# make a list of just x positions for star 2
x_positions_star_2 = [record["position"]["x"] for record in star_records["star_2"]]
# make a list of just y positions for star 2
y_positions_star_2 = [record["position"]["y"] for record in star_records["star_2"]]

# make a list of just x positions for star 1
x_velocity_star_1 = [record["velocity"]["x"] for record in star_records["star_1"]]
# make a list of just y positions for star 1
y_velocity_star_1 = [record["velocity"]["y"] for record in star_records["star_1"]]
# make a list of just x positions for star 2
x_velocity_star_2 = [record["velocity"]["x"] for record in star_records["star_2"]]
# make a list of just y positions for star 2
y_velocity_star_2 = [record["velocity"]["y"] for record in star_records["star_2"]]

# delete the last 90% of the data to save time in saving the animation
# x_positions_star_1 = x_positions_star_1[:int(len(x_positions_star_1) * 0.99)]
# y_positions_star_1 = y_positions_star_1[:int(len(y_positions_star_1) * 0.99)]
# x_positions_star_2 = x_positions_star_2[:int(len(x_positions_star_2) * 0.99)]
# y_positions_star_2 = y_positions_star_2[:int(len(y_positions_star_2) * 0.99)]

fig, ax = plt.subplots()
ax.set_xlim(-0.2e-7, 0.2e-7)
ax.set_ylim(-0.2e-7, 0.2e-7)
# add gridlines
ax.grid(visible=True, which='major', color='#666666', linestyle='-')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# annotate the plot with frame number
def annotate_frame(frame_number):
    plt.text(0.1e-7, 0.1e-7, "Frame: " + str(frame_number))


line, = ax.plot([], [], 'o', lw=2, markevery=[-1])
line2, = ax.plot([], [], 'o', lw=2, )


def init():
    line.set_data([], [])
    line2.set_data([], [])

    return line, line2


def animate(i):
    # i += 22000
    x = x_positions_star_1[i:i+10]
    y = y_positions_star_1[i:i+10]
    x2 = x_positions_star_2[i:i+10]
    y2 = y_positions_star_2[i:i+10]
    line.set_data(x, y)
    line2.set_data(x2, y2)
    if i % 100 == 0:
        # ax.savefig("frames/frame_" + str(i) + ".png")
        print("Frame: " + str(i))
        print("Remaining: " + str(len(x_positions_star_1) - i))
    # plt.text(x2[0], y2[0], "Star 2")
    # plt.text(x2[0], y2[0] - 100, x_velocity_star_2[i])
    # plt.text(x2[0], y2[0] - 200, y_velocity_star_2[i])
    return line, line2



ani = animation.FuncAnimation(fig, animate, frames=range(0, len(x_positions_star_1)) , init_func=init, interval=10,
                              blit=True)

# ani.save('animation.gif', fps=30, writer='imagemagick')

plt.show()

# fig, ax = plt.subplots()
# ax.set_xlim(-10, 1000)
# ax.set_ylim(-1.2e-5, 1.2e-5)
# # add gridlines
# ax.grid(b=True, which='major', color='#666666', linestyle='-')
# ax.minorticks_on()
# ax.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
#
# line, = ax.plot([], [], 'o', lw=2, markevery=[-1])
# line2, = ax.plot([], [], 'o', lw=2, )
#
# def animate(i):
#     i += 1800
#     x = range(0, i)
#     y = x_velocity_star_2[0:i]
#
#     x2 = range(0, i)
#     y2 = y_velocity_star_2[0:i]
#
#     line.set_data(x, y)
#     line2.set_data(x2, y2)
#     return line, line2
#
# ani = animation.FuncAnimation(fig, animate, frames=range(0, len(x_velocity_star_1)), interval=5,
#                                 blit=True)
#
# plt.show()


