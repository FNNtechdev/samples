import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(4, 8))

# Outer phone body (rounded rectangle)
phone_body = patches.FancyBboxPatch(
    (0.1, 0.05),      # (x, y)
    0.8,              # width
    0.9,              # height
    boxstyle="round,pad=0.02,rounding_size=0.06",
    linewidth=3,
    fill=False
)
ax.add_patch(phone_body)

# Screen area
screen = patches.Rectangle(
    (0.18, 0.18),
    0.64,
    0.64,
    linewidth=2,
    fill=False
)
ax.add_patch(screen)

# Speaker slot
speaker = patches.FancyBboxPatch(
    (0.42, 0.82),
    0.16,
    0.02,
    boxstyle="round,pad=0.01,rounding_size=0.01",
    linewidth=1.5,
    fill=False
)
ax.add_patch(speaker)

# Front camera
camera = patches.Circle((0.7, 0.83), 0.01, linewidth=1.5, fill=False)
ax.add_patch(camera)

# Home button
home_button = patches.Circle((0.5, 0.12), 0.03, linewidth=1.5, fill=False)
ax.add_patch(home_button)

# Volume buttons
vol_up = patches.Rectangle((0.92, 0.65), 0.02, 0.08, linewidth=1.5, fill=False)
vol_down = patches.Rectangle((0.92, 0.45), 0.02, 0.08, linewidth=1.5, fill=False)
ax.add_patch(vol_up)
ax.add_patch(vol_down)

# Power button
power = patches.Rectangle((0.06, 0.55), 0.02, 0.12, linewidth=1.5, fill=False)
ax.add_patch(power)

# App icons on the screen (3×3 grid)
x0, y0 = 0.22, 0.62
for row in range(3):
    for col in range(3):
        ix = x0 + col * 0.18
        iy = y0 - row * 0.18
        icon = patches.Rectangle((ix, iy), 0.12, 0.12, linewidth=1, fill=False)
        ax.add_patch(icon)

# Final styling
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')
plt.title("Simple Phone Drawing", pad=20)

plt.show()
