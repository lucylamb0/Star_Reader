import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

class Stars:
    def __init__(self, star_id):
        self.star_id = star_id
        self.x_list = []
        self.y_list = []
        self.z_list = []
        self.x_vel_list = []
        self.y_vel_list = []
        self.z_vel_list = []
        self.x_acc_list = []
        self.y_acc_list = []
        self.z_acc_list = []


def record(accel_id, x_position, y_position, z_position,
           x_velocity, y_velocity, z_velocity,
           x_acceleration, y_acceleration, z_acceleration):
    return {
        "accel_id": {accel_id},
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

def dict_accel_id(accel_id, x, y, z):
    return{
        accel_id: {
            "x": x,
            "y": y,
            "z": z
        }
    }



# import the data from the csv file
def import_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        stars = []
        skip = False
        for line in lines[1:]:
            line = line.split(',')
            for star in stars:
                if star.star_id == line[0]:
                    skip = True
                    continue
            if skip:
                skip = False
                continue
            star = Stars(line[0])
            stars.append(star)

        for star in stars:
            for line in lines[1:]:
                line = line.split(',')
                if line[0] == star.star_id:
                    star.x_list.append(float(line[2]))
                    star.y_list.append(float(line[3]))
                    star.z_list.append(float(line[4]))
                    star.x_vel_list.append(float(line[5]))
                    star.y_vel_list.append(float(line[6]))
                    star.z_vel_list.append(float(line[7]))
                    star.x_acc_list.append(float(line[8]))
                    star.y_acc_list.append(float(line[9]))
                    star.z_acc_list.append(float(line[10]))
    return stars


stars = import_data("Stars_gaussian.test.dump.csv")
star_array = np.zeros((len(stars), 3), dtype=float)
for i in range(len(stars)):
    star_array[i][0] = stars[i].x_list[0]
    star_array[i][1] = stars[i].y_list[0]
    star_array[i][2] = stars[i].z_list[0]


style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# set the limits of the graph
limitsx = (-8, 8)
limitsy = (-8, 8)
limitsz = (-8, 8)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


def update(frame):
    global limitsx
    global limitsy
    global limitsz
    ax.clear()
    ax.scatter(star_array[:, 0], star_array[:, 1], star_array[:, 2])
    ax.set_xlim3d(limitsx)
    ax.set_ylim3d(limitsy)
    ax.set_zlim3d(limitsz)
    for i in range(len(stars)):

        star_array[i][0] = stars[i].x_list[frame]
        star_array[i][1] = stars[i].y_list[frame]
        star_array[i][2] = stars[i].z_list[frame]



ani = animation.FuncAnimation(fig, update, interval=10, frames=len(stars[0].x_list))
plt.show()


# plot in 3d star dict accel_id
# def plot_3d(x_positions, y_positions, z_positions):
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')
#     ax.scatter(x_positions, y_positions, z_positions)
#     ax.set_xlabel('X Label')
#     ax.set_ylabel('Y Label')
#     ax.set_zlabel('Z Label')
#     plt.show()


# plot_3d(import_data("Gaussian_Stars.csv"))
# animate_3d(import_data("Gaussian_Stars.csv"))

# # get the data
# star_records = import_data("Stars.test.dump.txt")
# # make a list of just x positions for star 1
# x_positions_star_1 = [record["position"]["x"] for record in star_records["star_1"]]
# # make a list of just y positions for star 1
# y_positions_star_1 = [record["position"]["y"] for record in star_records["star_1"]]
# # make a list of just x positions for star 2
# x_positions_star_2 = [record["position"]["x"] for record in star_records["star_2"]]
# # make a list of just y positions for star 2
# y_positions_star_2 = [record["position"]["y"] for record in star_records["star_2"]]
#
# # make a list of just x positions for star 1
# x_velocity_star_1 = [record["velocity"]["x"] for record in star_records["star_1"]]
# # make a list of just y positions for star 1
# y_velocity_star_1 = [record["velocity"]["y"] for record in star_records["star_1"]]
# # make a list of just x positions for star 2
# x_velocity_star_2 = [record["velocity"]["x"] for record in star_records["star_2"]]
# # make a list of just y positions for star 2
# y_velocity_star_2 = [record["velocity"]["y"] for record in star_records["star_2"]]

# delete the last 90% of the data to save time in saving the animation
# x_positions_star_1 = x_positions_star_1[:int(len(x_positions_star_1) * 0.99)]
# y_positions_star_1 = y_positions_star_1[:int(len(y_positions_star_1) * 0.99)]
# x_positions_star_2 = x_positions_star_2[:int(len(x_positions_star_2) * 0.99)]
# y_positions_star_2 = y_positions_star_2[:int(len(y_positions_star_2) * 0.99)]

# make the plot without the animation






# fig, ax = plt.subplots()
# ax.set_xlim(-0.2e-7, 0.2e-7)
# ax.set_ylim(-0.2e-7, 0.2e-7)
# # add gridlines
# ax.grid(visible=True, which='major', color='#666666', linestyle='-')
# ax.minorticks_on()
# ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# # annotate the plot with frame number
# def annotate_frame(frame_number):
#     plt.text(0.1e-7, 0.1e-7, "Frame: " + str(frame_number))
#
#
# line, = ax.plot([], [], 'o', lw=2, markevery=[-1])
# line2, = ax.plot([], [], 'o', lw=2, )
#
#
# def init():
#     line.set_data([], [])
#     line2.set_data([], [])
#
#     return line, line2


# def animate(i):
#     # i += 22000
#     x = x_positions_star_1[i:i+10]
#     y = y_positions_star_1[i:i+10]
#     x2 = x_positions_star_2[i:i+10]
#     y2 = y_positions_star_2[i:i+10]
#     line.set_data(x, y)
#     line2.set_data(x2, y2)
#     if i % 100 == 0:
#         # ax.savefig("frames/frame_" + str(i) + ".png")
#         print("Frame: " + str(i))
#         print("Remaining: " + str(len(x_positions_star_1) - i))
#     # plt.text(x2[0], y2[0], "Star 2")
#     # plt.text(x2[0], y2[0] - 100, x_velocity_star_2[i])
#     # plt.text(x2[0], y2[0] - 200, y_velocity_star_2[i])
#     return line, line2
#
#
#
# ani = animation.FuncAnimation(fig, animate, frames=range(0, len(x_positions_star_1)) , init_func=init, interval=10,
#                               blit=True)

# ani.save('animation.gif', fps=30, writer='imagemagick')

# plt.show()

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


