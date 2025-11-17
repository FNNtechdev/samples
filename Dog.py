# Cartoon dog drawn over 60 seconds using matplotlib animation.
# Paste into a Jupyter notebook and run the cell.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches, animation
from IPython.display import HTML

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-2, 8)
ax.set_ylim(-2, 8)
ax.set_aspect('equal')
ax.axis('off')

def body_patch():
    return patches.Ellipse((3,3), width=5.0, height=3.0, angle=0, fill=True, linewidth=1.5)

def head_patch():
    return patches.Circle((6,4.5), radius=1.0, fill=True, linewidth=1.5)

def ear_patch(side='left'):
    if side=='left':
        return patches.Polygon([[5.2,5.3],[4.6,6.0],[5.6,5.5]], closed=True, linewidth=1.0)
    else:
        return patches.Polygon([[6.8,5.3],[7.4,6.0],[6.4,5.5]], closed=True, linewidth=1.0)

def eye_patch(x=5.7):
    return patches.Circle((x,4.8), radius=0.08, fill=True)

def nose_patch():
    return patches.Circle((6.45,4.25), radius=0.12, fill=True)

def mouth_line():
    return plt.Line2D([6.15,6.6],[3.95,4.05], linewidth=1.5)

def leg_patch(x):
    return patches.FancyBboxPatch((x,0.6), 0.5, 1.2, boxstyle="round,pad=0.05")

def tail_line():
    return plt.Line2D([1.95,0.5],[3.8,5.0], linewidth=2.5)

def collar_patch():
    return patches.Rectangle((5.15,3.8), 0.9, 0.18)

def spot_patch(x, y, w=0.6, h=0.35):
    return patches.Ellipse((x,y), width=w, height=h, angle=20, fill=True, alpha=0.9)

artists = {
    'body': body_patch(),
    'spot1': spot_patch(2.5,3.5,0.9,0.5),
    'spot2': spot_patch(3.8,3.2,0.6,0.4),
    'head': head_patch(),
    'left_ear': ear_patch('left'),
    'right_ear': ear_patch('right'),
    'left_eye': eye_patch(5.7),
    'right_eye': eye_patch(6.2),
    'nose': nose_patch(),
    'mouth': mouth_line(),
    'front_left_leg': leg_patch(4.6),
    'front_right_leg': leg_patch(5.6),
    'back_left_leg': leg_patch(1.8),
    'back_right_leg': leg_patch(2.8),
    'tail': tail_line(),
    'collar': collar_patch()
}

# Colors (simple scheme)
fill_color = '#E6C9A8'  # body
spot_color = '#8B5A2B'  # spots
nose_color = 'black'
collar_color = '#D63E3E'

for k, art in artists.items():
    if isinstance(art, (patches.Ellipse, patches.Circle, patches.Polygon, patches.FancyBboxPatch, patches.Rectangle)):
        if 'spot' in k:
            art.set_facecolor(spot_color)
        elif k == 'nose':
            art.set_facecolor(nose_color)
        elif k == 'collar':
            art.set_facecolor(collar_color)
        else:
            art.set_facecolor(fill_color)
        art.set_edgecolor('black')
    if isinstance(art, plt.Line2D):
        art.set_color('black')

sequence = [
    ('ground', 0, 3),
    ('body', 4, 12),
    ('spot1', 13, 16),
    ('spot2', 17, 20),
    ('back_left_leg', 21, 26),
    ('back_right_leg', 22, 28),
    ('front_left_leg', 29, 34),
    ('front_right_leg', 30, 36),
    ('tail', 37, 42),
    ('head', 43, 50),
    ('left_ear', 45, 52),
    ('right_ear', 46, 53),
    ('left_eye', 51, 55),
    ('right_eye', 52, 56),
    ('nose', 54, 58),
    ('mouth', 56, 59),
    ('collar', 57, 60)
]

ground = plt.Line2D([-1,9],[0.4,0.4], linewidth=2)
ground.set_color('#6B8E23')

def animate(frame):
    ax.clear()
    ax.set_xlim(-2, 8)
    ax.set_ylim(-2, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.add_line(ground)
    ax.text(-1.6,6.8,"Cartoon Dog (drawing over 60 seconds)", fontsize=10, va='top')
    for name, start, end in sequence:
        if start <= frame <= end:
            art = artists.get(name)
            if art is not None:
                if isinstance(art, plt.Line2D):
                    ax.add_line(art)
                else:
                    ax.add_patch(art)
    if 37 <= frame <= 60:
        wag = plt.Line2D([1.95, 0.5 + 0.4*np.sin(frame/3.0)],[3.8,5.0 + 0.2*np.cos(frame/3.0)], linewidth=2)
        ax.add_line(wag)
    remaining = max(0, 60 - frame)
    ax.text(5.2, -1.2, f"Seconds remaining: {remaining}", fontsize=9)
    return []

anim = animation.FuncAnimation(fig, animate, frames=range(0,61), interval=1000, blit=False, repeat=False)

# Display inline (in Jupyter)
HTML(anim.to_jshtml())

# If your environment doesn't render the animation, you can save to a GIF (requires imagemagick or pillow):
# anim.save('dog_60s.gif', writer='pillow', fps=1)
# print("Saved dog_60s.gif")
