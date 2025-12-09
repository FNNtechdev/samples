import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.transforms import Affine2D

fig, ax = plt.subplots(figsize=(8,6))

# Draw book pages (rectangle)
pages = patches.Rectangle((1.0, 2.0), 5.0, 2.8, linewidth=1.8)
ax.add_patch(pages)

# Draw book cover slightly offset above pages (like an open cover)
cover = patches.FancyBboxPatch((0.9, 2.05), 5.3, 2.9, boxstyle="round,pad=0.08,rounding_size=0.12", linewidth=2.0)
ax.add_patch(cover)

# Draw lines representing page divisions (thin horizontal lines)
for i in range(1,6):
    y = 2.3 + i*0.36/1.0
    ax.plot([1.15, 5.8], [y, y], linewidth=0.8)

# Draw book spine (vertical thin lines near left)
for i in range(3):
    x = 1.02 + i*0.06
    ax.plot([x, x], [2.05, 4.85], linewidth=1.1)

# Draw a bookmark (a small triangle at the top edge)
bookmark = patches.Polygon([[4.8, 4.6], [4.95, 4.25], [4.65, 4.25]], closed=True, linewidth=1.2)
ax.add_patch(bookmark)

# Draw a pen: a rotated rectangle (body), a circle for the end, and a triangle nib
pen_body = patches.Rectangle((3.6, 1.0), 3.2, 0.35, linewidth=1.6)
# Rotate the pen about its center
trans = Affine2D().rotate_deg_around(4.2, 1.175, -18) + ax.transData
pen_body.set_transform(trans)
ax.add_patch(pen_body)

# Pen back (circular end)
pen_end = patches.Circle((6.4, 1.0), 0.18, linewidth=1.6)
pen_end.set_transform(trans)
ax.add_patch(pen_end)

# Pen nib (triangle at front)
nib = patches.Polygon([[3.1, 1.05], [3.4, 0.92], [3.25, 1.25]], closed=True, linewidth=1.6)
nib.set_transform(trans)
ax.add_patch(nib)

# Add a little ink line to suggest writing
ax.plot([2.5, 3.0, 3.5], [2.25, 2.15, 1.95], linewidth=1.4)

ax.set_xlim(0.5, 7.2)
ax.set_ylim(0.5, 5.2)
ax.set_aspect('equal')
ax.axis('off')  # hide axes

plt.title("Book and Pen", pad=12)
plt.show()
