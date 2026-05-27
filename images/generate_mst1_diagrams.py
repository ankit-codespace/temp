import os
import math
import random
from PIL import Image, ImageDraw, ImageFont

# Ensure output directory exists
os.makedirs("images", exist_ok=True)

# Helper function to add a hand-drawn sketch effect by adding multiple slightly jittered lines
def draw_sketch_line(draw, x1, y1, x2, y2, fill="black", width=2):
    # Number of strokes for a sketchy overlay look
    strokes = 2
    for _ in range(strokes):
        # Add random minor offset for hand-drawn look
        j_x1 = x1 + random.uniform(-1.0, 1.0)
        j_y1 = y1 + random.uniform(-1.0, 1.0)
        j_x2 = x2 + random.uniform(-1.0, 1.0)
        j_y2 = y2 + random.uniform(-1.0, 1.0)
        draw.line([j_x1, j_y1, j_x2, j_y2], fill=fill, width=int(width))

# Helper to draw a sketchy circle
def draw_sketch_circle(draw, cx, cy, r, fill=None, outline="black", width=2):
    strokes = 2
    for _ in range(strokes):
        j_cx = cx + random.uniform(-1.0, 1.0)
        j_cy = cy + random.uniform(-1.0, 1.0)
        j_r = r + random.uniform(-0.5, 0.5)
        bbox = [j_cx - j_r, j_cy - j_r, j_cx + j_r, j_cy + j_r]
        draw.ellipse(bbox, fill=fill, outline=outline, width=int(width))

# Draw a sketchy zig-zag resistor
def draw_sketch_resistor(draw, x, y, dx, dy, orientation="horizontal", fill="black", width=2):
    # dx, dy is the total length vector of the resistor
    if orientation == "horizontal":
        segments = [
            (x, y),
            (x + dx*0.2, y),
            (x + dx*0.25, y - 8),
            (x + dx*0.35, y + 8),
            (x + dx*0.45, y - 8),
            (x + dx*0.55, y + 8),
            (x + dx*0.65, y - 8),
            (x + dx*0.75, y + 8),
            (x + dx*0.8, y),
            (x + dx, y)
        ]
    else: # vertical
        segments = [
            (x, y),
            (x, y + dy*0.2),
            (x - 8, y + dy*0.25),
            (x + 8, y + dy*0.35),
            (x - 8, y + dy*0.45),
            (x + 8, y + dy*0.55),
            (x - 8, y + dy*0.65),
            (x + 8, y + dy*0.75),
            (x, y + dy*0.8),
            (x, y + dy)
        ]
    
    for i in range(len(segments) - 1):
        draw_sketch_line(draw, segments[i][0], segments[i][1], segments[i+1][0], segments[i+1][1], fill=fill, width=width)

# Draw a sketchy capacitor
def draw_sketch_capacitor(draw, x, y, size=16, orientation="horizontal", fill="black", width=2):
    if orientation == "horizontal":
        # Draw plates (vertical bars)
        draw_sketch_line(draw, x - 4, y - size, x - 4, y + size, fill=fill, width=width+1)
        draw_sketch_line(draw, x + 4, y - size, x + 4, y + size, fill=fill, width=width+1)
        # Draw connecting wires
        draw_sketch_line(draw, x - 20, y, x - 4, y, fill=fill, width=width)
        draw_sketch_line(draw, x + 4, y, x + 20, y, fill=fill, width=width)
    else: # vertical
        # Draw plates (horizontal bars)
        draw_sketch_line(draw, x - size, y - 4, x + size, y - 4, fill=fill, width=width+1)
        draw_sketch_line(draw, x - size, y + 4, x + size, y + 4, fill=fill, width=width+1)
        # Draw connecting wires
        draw_sketch_line(draw, x, y - 20, x, y - 4, fill=fill, width=width)
        draw_sketch_line(draw, x, y + 4, x, y + 20, fill=fill, width=width)

# Draw a sketchy inductor (coils)
def draw_sketch_inductor(draw, x, y, dx, dy, orientation="horizontal", fill="black", width=2):
    if orientation == "horizontal":
        # Draw leading line
        draw_sketch_line(draw, x, y, x + dx*0.2, y, fill=fill, width=width)
        # Draw 4 loops
        start_x = x + dx*0.2
        loop_w = (dx*0.6) / 4
        for i in range(4):
            cx = start_x + i * loop_w + loop_w/2
            cy = y
            # Semicircular arc for inductor coil
            bbox = [start_x + i * loop_w, y - 10, start_x + (i + 1) * loop_w, y + 10]
            draw.arc(bbox, 180, 360, fill=fill, width=int(width))
            # Minor looping line back
            if i < 3:
                draw_sketch_line(draw, start_x + (i+1)*loop_w, y, start_x + (i+1)*loop_w - 2, y, fill=fill, width=width)
        # Draw tail line
        draw_sketch_line(draw, start_x + dx*0.6, y, x + dx, y, fill=fill, width=width)
    else: # vertical
        # Draw leading line
        draw_sketch_line(draw, x, y, x, y + dy*0.2, fill=fill, width=width)
        start_y = y + dy*0.2
        loop_h = (dy*0.6) / 4
        for i in range(4):
            bbox = [x - 10, start_y + i*loop_h, x + 10, start_y + (i+1)*loop_h]
            draw.arc(bbox, 270, 90, fill=fill, width=int(width))
        # Draw tail line
        draw_sketch_line(draw, x, start_y + dy*0.6, x, y + dy, fill=fill, width=width)

# Draw a sketchy AC source symbol
def draw_sketch_ac_source(draw, cx, cy, r, fill="black", width=2):
    draw_sketch_circle(draw, cx, cy, r, fill=None, outline=fill, width=width)
    # Inside sine wave
    points = []
    for x in range(cx - r + 4, cx + r - 4):
        t = (x - (cx - r + 4)) / (2 * r - 8)
        y = cy - int(6 * math.sin(2 * math.pi * t))
        points.append((x, y))
    for i in range(len(points) - 1):
        draw_sketch_line(draw, points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill=fill, width=width)

# Draw a sketchy DC source symbol
def draw_sketch_dc_source(draw, cx, cy, r, fill="black", width=2):
    draw_sketch_circle(draw, cx, cy, r, fill=None, outline=fill, width=width)
    # draw plus and minus
    draw_sketch_line(draw, cx - r/3, cy, cx + r/3, cy, fill=fill, width=width) # horizontal center
    draw_sketch_line(draw, cx, cy - r/4, cx, cy + r/4, fill=fill, width=width) # plus vertical
    
    # minus slightly below
    draw_sketch_line(draw, cx - r/3, cy + r/2, cx + r/3, cy + r/2, fill=fill, width=width)

# Draw a sketchy current source symbol
def draw_sketch_current_source(draw, cx, cy, r, orientation="vertical", fill="black", width=2):
    draw_sketch_circle(draw, cx, cy, r, fill=None, outline=fill, width=width)
    # draw arrow
    if orientation == "vertical":
        draw_sketch_line(draw, cx, cy - r*0.6, cx, cy + r*0.6, fill="red", width=width)
        # arrow head pointing UP
        draw_sketch_line(draw, cx, cy - r*0.6, cx - 4, cy - r*0.2, fill="red", width=width)
        draw_sketch_line(draw, cx, cy - r*0.6, cx + 4, cy - r*0.2, fill="red", width=width)
    else: # horizontal
        draw_sketch_line(draw, cx - r*0.6, cx + r*0.6, cy, cy, fill="red", width=width)
        draw_sketch_line(draw, cx + r*0.6, cy, cx + r*0.2, cy - 4, fill="red", width=width)
        draw_sketch_line(draw, cx + r*0.6, cy, cx + r*0.2, cy + 4, fill="red", width=width)

# Simple custom hand-drawn font rendering (uses default if TTF not found)
try:
    font_large = ImageFont.truetype("arial.ttf", 15)
    font_medium = ImageFont.truetype("arial.ttf", 11)
    font_small = ImageFont.truetype("arial.ttf", 9)
except IOError:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_small = ImageFont.load_default()

# ----------------- 1. RL Series Circuit -----------------
# size: 320 x 200
img1 = Image.new("RGB", (320, 200), "white")
draw1 = ImageDraw.Draw(img1)

# RL Circuit Diagram (Left)
# AC Source on left, R top, L right
draw_sketch_ac_source(draw1, 40, 100, 16, fill="blue")
draw1.text((32, 120), "V", fill="blue", font=font_large)

# Loop wiring
draw_sketch_line(draw1, 40, 84, 40, 50)
draw_sketch_line(draw1, 40, 116, 40, 150)
draw_sketch_line(draw1, 40, 150, 140, 150)

# Resistor R
draw_sketch_resistor(draw1, 40, 50, 60, 0, orientation="horizontal", fill="black")
draw1.text((65, 30), "R", fill="black", font=font_large)

draw_sketch_line(draw1, 100, 50, 140, 50)

# Inductor L
draw_sketch_inductor(draw1, 140, 50, 0, 100, orientation="vertical", fill="green")
draw1.text((155, 90), "L (XL)", fill="green", font=font_large)

# RL Phasor Diagram (Right)
# Origin at (210, 150)
ox, oy = 210, 150
# VR along horizontal (right, length 60)
draw_sketch_line(draw1, ox, oy, ox + 65, oy, fill="black", width=3)
# arrow head for VR
draw_sketch_line(draw1, ox + 65, oy, ox + 60, oy - 3, fill="black", width=2)
draw_sketch_line(draw1, ox + 65, oy, ox + 60, oy + 3, fill="black", width=2)

# VL vertical (up, length 50)
draw_sketch_line(draw1, ox, oy, ox, oy - 55, fill="green", width=3)
# arrow head for VL
draw_sketch_line(draw1, ox, oy - 55, ox - 3, oy - 50, fill="green", width=2)
draw_sketch_line(draw1, ox, oy - 55, ox + 3, oy - 50, fill="green", width=2)

# V resultant (hypotenuse)
draw_sketch_line(draw1, ox, oy, ox + 65, oy - 55, fill="blue", width=3)
# arrow head for V
draw_sketch_line(draw1, ox + 65, oy - 55, ox + 58, oy - 54, fill="blue", width=2)
draw_sketch_line(draw1, ox + 65, oy - 55, ox + 62, oy - 47, fill="blue", width=2)

# Labels
draw1.text((ox + 30, oy + 5), "VR = IR (in-phase)", fill="black", font=font_medium)
draw1.text((ox - 55, oy - 50), "VL = IXL", fill="green", font=font_medium)
draw1.text((ox + 40, oy - 45), "V = IZ", fill="blue", font=font_medium)
draw1.text((ox + 70, oy - 5), "I (Ref)", fill="red", font=font_medium)

# Phase Angle Arc
draw1.arc([ox - 15, oy - 15, ox + 15, oy + 15], 320, 360, fill="red", width=1)
draw1.text((ox + 18, oy - 13), "φ", fill="red", font=font_medium)

img1.save("images/rl_circuit_solved.png")

# ----------------- 2. Sinusoidal Graph -----------------
# size: 320 x 200
img2 = Image.new("RGB", (320, 200), "white")
draw2 = ImageDraw.Draw(img2)

# Axes
draw_sketch_line(draw2, 40, 100, 280, 100, fill="black", width=2) # X axis (time)
draw_sketch_line(draw2, 40, 20, 40, 180, fill="black", width=2)   # Y axis (voltage)
draw_sketch_line(draw2, 280, 100, 275, 96, fill="black", width=2) # arrow x
draw_sketch_line(draw2, 280, 100, 275, 104, fill="black", width=2)
draw_sketch_line(draw2, 40, 20, 36, 25, fill="black", width=2) # arrow y
draw_sketch_line(draw2, 40, 20, 44, 25, fill="black", width=2)

# Labels
draw2.text((25, 10), "Voltage v(t)", fill="black", font=font_large)
draw2.text((275, 108), "t (ms)", fill="black", font=font_medium)
draw2.text((28, 104), "0", fill="black", font=font_medium)

# Grid/Dashed lines for peak (+20V) and trough (-20V)
draw_sketch_line(draw2, 40, 45, 260, 45, fill="grey", width=1)
draw_sketch_line(draw2, 40, 155, 260, 155, fill="grey", width=1)
draw2.text((10, 38), "+20 V", fill="blue", font=font_medium)
draw2.text((10, 148), "-20 V", fill="blue", font=font_medium)

# Draw Sine Wave
# Cycle: 0 to 20ms over width (40 to 240, total 200px)
# f = 50Hz -> T = 20ms
sine_points = []
start_x, end_x = 40, 240
for x in range(start_x, end_x + 1):
    t = (x - start_x) / (end_x - start_x) # 0 to 1
    y = 100 - 55 * math.sin(2 * math.pi * t) # peak amplitude 55px
    sine_points.append((x, y))

for i in range(len(sine_points) - 1):
    draw_sketch_line(draw2, sine_points[i][0], sine_points[i][1], sine_points[i+1][0], sine_points[i+1][1], fill="red", width=3)

# Key points vertical lines
# Peak at 5ms (x = 40 + 50 = 90)
draw_sketch_line(draw2, 90, 45, 90, 100, fill="grey", width=1)
draw2.text((85, 104), "5", fill="black", font=font_small)

# Zero crossing at 10ms (x = 140)
draw2.text((135, 104), "10", fill="black", font=font_small)

# Trough at 15ms (x = 190)
draw_sketch_line(draw2, 190, 155, 190, 100, fill="grey", width=1)
draw2.text((185, 104), "15", fill="black", font=font_small)

# End of cycle at 20ms (x = 240)
draw_sketch_line(draw2, 240, 100, 240, 120, fill="blue", width=1)
draw2.text((230, 104), "20", fill="black", font=font_small)
draw2.text((220, 125), "T = 20ms", fill="blue", font=font_medium)

# Peak to Peak dimension
draw_sketch_line(draw2, 260, 45, 260, 155, fill="green", width=1)
draw_sketch_line(draw2, 256, 45, 264, 45, fill="green", width=1)
draw_sketch_line(draw2, 256, 155, 264, 155, fill="green", width=1)
draw2.text((263, 90), "Vp-p = 40V", fill="green", font=font_medium)

img2.save("images/sinusoidal_graph_solved.png")

# ----------------- 3. RC Series Circuit -----------------
# size: 320 x 200
img3 = Image.new("RGB", (320, 200), "white")
draw3 = ImageDraw.Draw(img3)

# RC Circuit Diagram (Left)
# AC Source on left, R top, C right
draw_sketch_ac_source(draw3, 40, 100, 16, fill="blue")
draw3.text((32, 120), "V", fill="blue", font=font_large)

# Loop wiring
draw_sketch_line(draw3, 40, 84, 40, 50)
draw_sketch_line(draw3, 40, 116, 40, 150)
draw_sketch_line(draw3, 40, 150, 140, 150)

# Resistor R
draw_sketch_resistor(draw3, 40, 50, 60, 0, orientation="horizontal", fill="black")
draw3.text((65, 30), "R", fill="black", font=font_large)
draw_sketch_line(draw3, 100, 50, 140, 50)

# Capacitor C
draw_sketch_capacitor(draw3, 140, 100, size=16, orientation="horizontal", fill="orange")
draw3.text((155, 90), "C (XC)", fill="orange", font=font_large)

# RC Phasor Diagram (Right)
# Origin at (210, 60)
ox, oy = 210, 60
# VR along horizontal (right, length 60)
draw_sketch_line(draw3, ox, oy, ox + 65, oy, fill="black", width=3)
# arrow head
draw_sketch_line(draw3, ox + 65, oy, ox + 60, oy - 3, fill="black", width=2)
draw_sketch_line(draw3, ox + 65, oy, ox + 60, oy + 3, fill="black", width=2)

# VC vertical (down, length 50)
draw_sketch_line(draw3, ox, oy, ox, oy + 55, fill="orange", width=3)
# arrow head
draw_sketch_line(draw3, ox, oy + 55, ox - 3, oy + 50, fill="orange", width=2)
draw_sketch_line(draw3, ox, oy + 55, ox + 3, oy + 50, fill="orange", width=2)

# V resultant
draw_sketch_line(draw3, ox, oy, ox + 65, oy + 55, fill="blue", width=3)
# arrow head
draw_sketch_line(draw3, ox + 65, oy + 55, ox + 58, oy + 54, fill="blue", width=2)
draw_sketch_line(draw3, ox + 65, oy + 55, ox + 62, oy + 47, fill="blue", width=2)

# Labels
draw3.text((ox + 30, oy - 15), "VR = IR", fill="black", font=font_medium)
draw3.text((ox - 55, oy + 45), "VC = IXC", fill="orange", font=font_medium)
draw3.text((ox + 40, oy + 40), "V = IZ", fill="blue", font=font_medium)
draw3.text((ox + 70, oy - 5), "I (Ref)", fill="red", font=font_medium)

# Phase Angle Arc
draw3.arc([ox - 15, oy - 15, ox + 15, oy + 15], 0, 40, fill="red", width=1)
draw3.text((ox + 18, oy + 10), "φ", fill="red", font=font_medium)

img3.save("images/rc_circuit_solved.png")

# ----------------- 4. Superposition Circuit -----------------
# size: 320 x 200
img4 = Image.new("RGB", (320, 200), "white")
draw4 = ImageDraw.Draw(img4)

# Left DC voltage source 20V
draw_sketch_dc_source(draw4, 40, 100, 16, fill="blue")
draw4.text((12, 90), "+", fill="blue", font=font_large)
draw4.text((12, 110), "-", fill="blue", font=font_large)
draw4.text((32, 120), "20V", fill="blue", font=font_medium)

# Connections & Nodes
draw_sketch_line(draw4, 40, 84, 40, 50)
draw_sketch_line(draw4, 40, 116, 40, 150)
draw_sketch_line(draw4, 40, 150, 260, 150) # bottom ground wire

# Resistor 5 ohm top left
draw_sketch_resistor(draw4, 40, 50, 70, 0, orientation="horizontal", fill="black")
draw4.text((70, 32), "5 Ω", fill="black", font=font_medium)
draw_sketch_line(draw4, 110, 50, 140, 50)

# Middle Junction Node
draw_sketch_circle(draw4, 140, 50, 3, fill="black", outline="black")
draw4.text((135, 38), "V2", fill="red", font=font_medium)

# Resistor 10 ohm middle vertical
draw_sketch_resistor(draw4, 140, 50, 0, 70, orientation="vertical", fill="black")
draw4.text((115, 80), "10 Ω", fill="black", font=font_medium)
draw_sketch_line(draw4, 140, 120, 140, 150)

# Resistor 10 ohm top right horizontal
draw_sketch_resistor(draw4, 140, 50, 70, 0, orientation="horizontal", fill="black")
draw4.text((170, 32), "10 Ω", fill="black", font=font_medium)
draw_sketch_line(draw4, 210, 50, 240, 50)

# Right Junction Node
draw_sketch_circle(draw4, 240, 50, 3, fill="black", outline="black")
draw4.text((235, 38), "V3", fill="red", font=font_medium)

# Resistor 20 ohm right vertical (Load)
draw_sketch_resistor(draw4, 240, 50, 0, 70, orientation="vertical", fill="green", width=3)
draw4.text((250, 80), "20 Ω", fill="green", font=font_large)
draw_sketch_line(draw4, 240, 120, 240, 150)

# Current Source 4A on extreme right
draw_sketch_line(draw4, 240, 50, 290, 50)
draw_sketch_line(draw4, 290, 50, 290, 84)
draw_sketch_current_source(draw4, 290, 100, 16, orientation="vertical", fill="red")
draw4.text((282, 120), "4A", fill="red", font=font_medium)
draw_sketch_line(draw4, 290, 116, 290, 150)
draw_sketch_line(draw4, 240, 150, 290, 150)

# Ground symbol
draw_sketch_line(draw4, 140, 150, 140, 160)
draw_sketch_line(draw4, 130, 160, 150, 160)
draw_sketch_line(draw4, 134, 164, 146, 164)
draw_sketch_line(draw4, 138, 168, 142, 168)

img4.save("images/superposition_circuit_solved.png")

# ----------------- 5. KCL & KVL -----------------
# size: 320 x 200
img5 = Image.new("RGB", (320, 200), "white")
draw5 = ImageDraw.Draw(img5)

# Left Side: KCL Junction
# Center node at (75, 100)
ncx, ncy = 70, 95
draw_sketch_circle(draw5, ncx, ncy, 4, fill="black", outline="black")

# Entering current 1 (left-down)
draw_sketch_line(draw5, ncx - 45, ncy - 35, ncx, ncy, fill="black", width=2)
# arrow pointing into node
draw_sketch_line(draw5, ncx - 20, ncy - 15, ncx - 15, ncy - 20, fill="black")
draw_sketch_line(draw5, ncx - 20, ncy - 15, ncx - 22, ncy - 8, fill="black")
draw5.text((ncx - 48, ncy - 48), "I1", fill="black", font=font_large)

# Entering current 2 (top)
draw_sketch_line(draw5, ncx, ncy - 50, ncx, ncy, fill="blue", width=2)
# arrow pointing into node
draw_sketch_line(draw5, ncx, ncy - 20, ncx - 4, ncy - 26, fill="blue")
draw_sketch_line(draw5, ncx, ncy - 20, ncx + 4, ncy - 26, fill="blue")
draw5.text((ncx - 18, ncy - 55), "I2", fill="blue", font=font_large)

# Leaving current 3 (right-down)
draw_sketch_line(draw5, ncx, ncy, ncx + 50, ncy + 30, fill="red", width=2)
# arrow pointing away
draw_sketch_line(draw5, ncx + 30, ncy + 18, ncx + 22, ncy + 20, fill="red")
draw_sketch_line(draw5, ncx + 30, ncy + 18, ncx + 28, ncy + 12, fill="red")
draw5.text((ncx + 40, ncy + 35), "I3", fill="red", font=font_large)

draw2.text((10, 10), "KCL Node", fill="black", font=font_medium)
draw5.text((25, 145), "I1 + I2 = I3", fill="black", font=font_large)
draw5.text((15, 165), "Conservation of Charge", fill="grey", font=font_medium)

# Right Side: KVL Loop
# Loop coordinates: top left (180, 50), width 100, height 80
lx, ly = 180, 50
lw, lh = 90, 80

# Source on left
draw_sketch_dc_source(draw5, lx, ly + lh/2, 14, fill="blue")
draw5.text((lx - 25, ly + lh/2 - 10), "V", fill="blue", font=font_large)

# Loop wiring
draw_sketch_line(draw5, lx, ly + lh/2 - 14, lx, ly)
draw_sketch_line(draw5, lx, ly + lh/2 + 14, lx, ly + lh)
draw_sketch_line(draw5, lx, ly + lh, lx + lw, ly + lh)

# Resistor R1 (top)
draw_sketch_resistor(draw5, lx, ly, lw, 0, orientation="horizontal", fill="black")
draw5.text((lx + lw/2 - 5, ly - 20), "R1", fill="black", font=font_large)

# Resistor R2 (right vertical)
draw_sketch_resistor(draw5, lx + lw, ly, 0, lh, orientation="vertical", fill="green")
draw5.text((lx + lw + 12, ly + lh/2 - 10), "R2", fill="green", font=font_large)

# Clockwise Loop Arrow
draw5.arc([lx + 25, ly + 20, lx + lw - 25, ly + lh - 20], 0, 270, fill="red", width=1)
# arrow head
draw_sketch_line(draw5, lx + lw - 25, ly + lh/2, lx + lw - 29, ly + lh/2 - 4, fill="red")
draw_sketch_line(draw5, lx + lw - 25, ly + lh/2, lx + lw - 21, ly + lh/2 - 4, fill="red")
draw5.text((lx + lw/2 - 5, ly + lh/2 - 10), "I", fill="red", font=font_large)

draw5.text((170, 145), "V - IR1 - IR2 = 0", fill="black", font=font_large)
draw5.text((165, 165), "Conservation of Energy", fill="grey", font=font_medium)

# Partition Line
draw_sketch_line(draw5, 150, 20, 150, 180, fill="grey", width=1)

img5.save("images/kcl_kvl_solved.png")

# ----------------- 6. Norton Equivalent -----------------
# size: 320 x 200
img6 = Image.new("RGB", (320, 200), "white")
draw6 = ImageDraw.Draw(img6)

# Left Side: Original Circuit
# 12V source on left
draw_sketch_dc_source(draw6, 30, 90, 14, fill="blue")
draw6.text((22, 110), "12V", fill="blue", font=font_medium)

# Wiring
draw_sketch_line(draw6, 30, 76, 30, 50)
draw_sketch_line(draw6, 30, 104, 30, 130)
draw_sketch_line(draw6, 30, 130, 150, 130)

# 3 ohm top left
draw_sketch_resistor(draw6, 30, 50, 50, 0, orientation="horizontal", fill="black")
draw6.text((45, 32), "3 Ω", fill="black", font=font_medium)
draw_sketch_line(draw6, 80, 50, 90, 50)

# middle junction node
draw_sketch_circle(draw6, 90, 50, 2, fill="black", outline="black")

# 6 ohm middle vertical
draw_sketch_resistor(draw6, 90, 50, 0, 80, orientation="vertical", fill="black")
draw6.text((70, 80), "6 Ω", fill="black", font=font_medium)
draw_sketch_line(draw6, 90, 130, 90, 130)

# 3 ohm top right
draw_sketch_resistor(draw6, 90, 50, 50, 0, orientation="horizontal", fill="black")
draw6.text((105, 32), "3 Ω", fill="black", font=font_medium)
draw_sketch_line(draw6, 140, 50, 150, 50)

# load terminals A & B
draw_sketch_circle(draw6, 150, 50, 3, fill="black", outline="black")
draw_sketch_circle(draw6, 150, 130, 3, fill="black", outline="black")
draw6.text((155, 42), "A", fill="black", font=font_large)
draw6.text((155, 122), "B", fill="black", font=font_large)

# Load Resistor RL = 1.5 ohm
draw_sketch_resistor(draw6, 150, 50, 0, 80, orientation="vertical", fill="green", width=3)
draw6.text((162, 80), "RL = 1.5 Ω", fill="green", font=font_medium)

# Right Side: Norton Equivalent
# Current source IN = 1.6A pointing UP on left
draw_sketch_current_source(draw6, 210, 90, 14, orientation="vertical", fill="red")
draw6.text((200, 110), "IN = 1.6A", fill="red", font=font_medium)

# Wiring
draw_sketch_line(draw6, 210, 76, 210, 50)
draw_sketch_line(draw6, 210, 104, 210, 130)
draw_sketch_line(draw6, 210, 130, 300, 130)
draw_sketch_line(draw6, 210, 50, 300, 50)

# Parallel Resistor RN = 5 ohm
draw_sketch_resistor(draw6, 255, 50, 0, 80, orientation="vertical", fill="black")
draw6.text((230, 80), "RN = 5 Ω", fill="black", font=font_medium)

# Terminals A & B
draw_sketch_circle(draw6, 300, 50, 3, fill="black", outline="black")
draw_sketch_circle(draw6, 300, 130, 3, fill="black", outline="black")
draw6.text((305, 42), "A", fill="black", font=font_large)
draw6.text((305, 122), "B", fill="black", font=font_large)

# Load Resistor RL = 1.5 ohm
draw_sketch_resistor(draw6, 300, 50, 0, 80, orientation="vertical", fill="green", width=3)
draw6.text((305, 80), "RL = 1.5 Ω", fill="green", font=font_medium)

# Title Divider
draw_sketch_line(draw6, 185, 20, 185, 180, fill="grey", width=1)
draw6.text((45, 160), "Original Circuit", fill="black", font=font_medium)
draw6.text((205, 160), "Norton Equivalent", fill="black", font=font_medium)

img6.save("images/norton_circuit_solved.png")

print("All 6 solved MST1 diagrams generated successfully!")
