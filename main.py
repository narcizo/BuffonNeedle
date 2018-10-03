import math, random
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def buffon_needle(ratio=2):
    delta = random.uniform(0, ratio)
    theta = random.uniform(0, math.pi / 2)
    return (delta, theta, delta < math.cos(theta))

def buffon_plot(ratio=2):
    hitlist = [1, 0]
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.set_aspect(1)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    ax1.grid(True, axis='x')
    ax1.set_title("Agulhas de Buffon")

    rpi = ratio * math.pi
    ax2.set_ylim(0, rpi)
    ax2.axhline(y=rpi/2, linewidth=1, color='green')
    ax2.set_xlabel('Agulhas')
    ax2.set_ylabel('Estimativa')
    ax2.grid()
    ax2.set_title("Estimativa de PI")

    def buffon_animation(frame):
        delta, theta, hit = buffon_needle(ratio)
        color = 'r' if hit else 'b'
        doff = delta / ratio
        posx = random.randint(1, 4) * 2
        posy = random.uniform(1, 9)
        flpx = random.choice([-1, 1])
        flpy = random.choice([-1, 1])
        thdx = math.cos(theta) / ratio
        thdy = math.sin(theta) / ratio
        plx1 = posx + (-thdx + doff) * flpx
        plx2 = posx + (thdx + doff) * flpx
        ply1 = posy - thdy * flpy
        ply2 = posy + thdy * flpy
        line = Line2D([plx1, plx2], [ply1, ply2], color=color, alpha=1/3)
        hitlist[0] += hit
        est = frame / hitlist[0]
        err = est - math.pi
        
        if abs(err) < abs(hitlist[1] - math.pi):
            hitlist[1] = est
        scl = 'r' if err < 0 else 'b'
        ax1.add_line(line)
        ax1.set_xlabel("  Atual = {:.8f}\nMelhor = {:.8f}".format(est, hitlist[1]))
        ax2.scatter(frame, est, marker='.', color=scl, alpha=2/3, linewidth=2/3)

    ani = animation.FuncAnimation(fig, buffon_animation, interval=1000/60, blit=False)
    fig.canvas.set_window_title('Simulador Agulha de Buffon')
    plt.show()

buffon_plot()
