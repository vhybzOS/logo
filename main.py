# main.py
import drawsvg as draw
from petal import draw_single_petal # Import our petal drawing function

# --- Configuration ---
DRAWING_WIDTH = 400
DRAWING_HEIGHT = 400
PETAL_BASE_WIDTH = 50  # Base dimensions for a single petal
PETAL_HEIGHT = 100
PETAL_SCALE = 0.7     # Scale factor to fit petals on the canvas
PETAL_OPACITY = 0.6   # Opacity for blending effect

# Colors (approximated from the image)
COLOR_ORANGE = '#FF8C00' # Dark Orange
COLOR_BLUE = '#0000FF'   # Blue
COLOR_PURPLE = '#8A2BE2' # BlueViolet
COLOR_PINK = '#FF1493'   # DeepPink
BACKGROUND_COLOR = '#f8f8f8' # Light off-white

# Shadow filter (initial simple version)
SHADOW_BLUR_STD_DEV = 5
SHADOW_OFFSET_X = 3
SHADOW_OFFSET_Y = 3
SHADOW_COLOR = 'rgba(0, 0, 0, 0.5)' # Semi-transparent black for shadow color (optional)

# --- Drawing ---
d = draw.Drawing(DRAWING_WIDTH, DRAWING_HEIGHT, origin='center')

# 1. Add background
d.append(draw.Rectangle(
    -DRAWING_WIDTH/2, -DRAWING_HEIGHT/2,
    DRAWING_WIDTH, DRAWING_HEIGHT,
    fill=BACKGROUND_COLOR
))

# 2. Define the base petal shape (will go into <defs>)
# We draw it pointing up (along positive y) with base at (0,0)
base_petal_shape = draw_single_petal(
    base_width=PETAL_BASE_WIDTH,
    height=PETAL_HEIGHT,
    # Optional base styling for the def
    # fill_opacity=PETAL_OPACITY # Opacity applied per Use for blending
)

# Scale down the base shape definition
# This group will contain the scaled petal path in <defs>
scaled_petal_def = draw.Group(transform=f'scale({PETAL_SCALE})')
scaled_petal_def.append(base_petal_shape)


# 3. Define the shadow filter
# This filter will be applied to the elements that should cast a shadow.
# SVG filters are powerful but complex. This is a basic drop shadow.
shadow_filter = draw.Filter(id='petal-shadow')
# Blur the source alpha channel (shape outline)
shadow_filter.append(draw.FilterItem('feGaussianBlur', in='SourceAlpha', stdDev=SHADOW_BLUR_STD_DEV))
# Offset the blurred alpha to create the shadow shape
shadow_filter.append(draw.FilterItem('feOffset', dx=SHADOW_OFFSET_X, dy=SHADOW_OFFSET_Y, result='shadow'))
# Combine the shadow with the original graphic.
# feMergeNode in="shadow" draws the shadow.
# feMergeNode in="SourceGraphic" draws the original shape on top.
merge_nodes = draw.FilterItem('feMerge')
merge_nodes.append(draw.FilterItem('feMergeNode', in='shadow'))
merge_nodes.append(draw.FilterItem('feMergeNode', in='SourceGraphic'))
shadow_filter.append(merge_nodes)

# Add the filter definition to the drawing's defs
d.append_def(shadow_filter)


# 4. Draw the four petals using the scaled definition and transformations
# The rotations position the petals. Petals are colored and made translucent.
# Petal 1: Top-right (rotate 45 deg)
petal1 = draw.Use(
    scaled_petal_def,
    0, 0, # Use origin (0,0) as rotation center
    transform=f'rotate(45)',
    fill=COLOR_ORANGE,
    fill_opacity=PETAL_OPACITY
)
d.append(petal1)

# Petal 2: Top-left (rotate 135 deg)
petal2 = draw.Use(
    scaled_petal_def,
    0, 0,
    transform=f'rotate(135)',
    fill=COLOR_BLUE,
    fill_opacity=PETAL_OPACITY
)
d.append(petal2)

# Petal 3: Bottom-left (rotate 225 deg) - Add shadow
petal3 = draw.Use(
    scaled_petal_def,
    0, 0,
    transform=f'rotate(225)',
    fill=COLOR_PURPLE,
    fill_opacity=PETAL_OPACITY,
    filter='url(#petal-shadow)' # Apply the shadow filter
)
d.append(petal3)

# Petal 4: Bottom-right (rotate 315 deg) - Add shadow
petal4 = draw.Use(
    scaled_petal_def,
    0, 0,
    transform=f'rotate(315)',
    fill=COLOR_PINK,
    fill_opacity=PETAL_OPACITY,
    filter='url(#petal-shadow)' # Apply the shadow filter
)
d.append(petal4)


# --- Output ---
# Save as SVG
d.save_svg('logo_v0_1.svg')
print("Generated logo_v0_1.svg")

# To display in a Jupyter Notebook:
# d.display_inline()
