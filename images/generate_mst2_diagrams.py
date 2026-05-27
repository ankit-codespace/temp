import os
import math
import random
from PIL import Image, ImageDraw, ImageFont

# Ensure output directory exists
os.makedirs("images", exist_ok=True)

# Helper function to add a hand-drawn sketch effect by adding multiple slightly jittered lines
def draw_sketch_line(draw, x1, y1, x2, y2, fill="black", width=2):
    strokes = 2
    for _ in range(strokes):
        j_x1 = x1 + random.uniform(-0.8, 0.8)
        j_y1 = y1 + random.uniform(-0.8, 0.8)
        j_x2 = x2 + random.uniform(-0.8, 0.8)
        j_y2 = y2 + random.uniform(-0.8, 0.8)
        draw.line([j_x1, j_y1, j_x2, j_y2], fill=fill, width=int(width))

# Helper to draw a sketchy circle
def draw_sketch_circle(draw, cx, cy, r, fill=None, outline="black", width=2):
    strokes = 2
    for _ in range(strokes):
        j_cx = cx + random.uniform(-0.8, 0.8)
        j_cy = cy + random.uniform(-0.8, 0.8)
        j_r = r + random.uniform(-0.4, 0.4)
        bbox = [j_cx - j_r, j_cy - j_r, j_cx + j_r, j_cy + j_r]
        draw.ellipse(bbox, fill=fill, outline=outline, width=int(width))

# Draw a sketchy zig-zag resistor
def draw_sketch_resistor(draw, x, y, dx, dy, orientation="horizontal", fill="black", width=2):
    if orientation == "horizontal":
        segments = [
            (x, y),
            (x + dx*0.2, y),
            (x + dx*0.25, y - 6),
            (x + dx*0.35, y + 6),
            (x + dx*0.45, y - 6),
            (x + dx*0.55, y + 6),
            (x + dx*0.65, y - 6),
            (x + dx*0.75, y + 6),
            (x + dx*0.8, y),
            (x + dx, y)
        ]
    else: # vertical
        segments = [
            (x, y),
            (x, y + dy*0.2),
            (x - 6, y + dy*0.25),
            (x + 6, y + dy*0.35),
            (x - 6, y + dy*0.45),
            (x + 6, y + dy*0.55),
            (x - 6, y + dy*0.65),
            (x + 6, y + dy*0.75),
            (x, y + dy*0.8),
            (x, y + dy)
        ]
    for i in range(len(segments) - 1):
        draw_sketch_line(draw, segments[i][0], segments[i][1], segments[i+1][0], segments[i+1][1], fill=fill, width=width)

# Draw a sketchy AC source symbol
def draw_sketch_ac_source(draw, cx, cy, r, fill="black", width=2):
    draw_sketch_circle(draw, cx, cy, r, fill=None, outline=fill, width=width)
    points = []
    for x in range(cx - r + 3, cx + r - 3):
        t = (x - (cx - r + 3)) / (2 * r - 6)
        y = cy - int(5 * math.sin(2 * math.pi * t))
        points.append((x, y))
    for i in range(len(points) - 1):
        draw_sketch_line(draw, points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill=fill, width=width)

# Fonts
try:
    font_large = ImageFont.truetype("arial.ttf", 13)
    font_medium = ImageFont.truetype("arial.ttf", 10)
    font_small = ImageFont.truetype("arial.ttf", 8)
except IOError:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_small = ImageFont.load_default()

# ----------------- 1. LVDT Characteristic Graph -----------------
# size: 320 x 200
img1 = Image.new("RGB", (320, 200), "white")
draw1 = ImageDraw.Draw(img1)
cx, cy = 160, 100
# Axes
draw_sketch_line(draw1, 30, cy, 290, cy, fill="black", width=2) # X-axis
draw_sketch_line(draw1, cx, 20, cx, 180, fill="black", width=2) # Y-axis
# Arrows
draw_sketch_line(draw1, 290, cy, 284, cy - 4)
draw_sketch_line(draw1, 290, cy, 284, cy + 4)
draw_sketch_line(draw1, cx, 20, cx - 4, 26)
draw_sketch_line(draw1, cx, 20, cx + 4, 26)

# Labels
draw1.text((cx + 8, 12), "Output Voltage (V_out)", fill="blue", font=font_medium)
draw1.text((230, cy + 8), "Displacement (x)", fill="black", font=font_medium)
draw1.text((cx - 22, cy + 4), "Null Point", fill="red", font=font_medium)

# Curve (Diagonal passing through origin with non-linear bends at extremes)
# Left non-linear region
draw_sketch_line(draw1, 50, 150, 70, 145, fill="red", width=2)
# Linear left to right
draw_sketch_line(draw1, 70, 145, cx, cy, fill="red", width=2.5)
draw_sketch_line(draw1, cx, cy, 250, 55, fill="red", width=2.5)
# Right non-linear region
draw_sketch_line(draw1, 250, 55, 270, 50, fill="red", width=2)

# Auxiliary labels
draw1.text((50, 155), "-x (Left Shift)", fill="black", font=font_medium)
draw1.text((215, 110), "+x (Right Shift)", fill="black", font=font_medium)
draw1.text((220, 42), "In-Phase (0°)", fill="green", font=font_medium)
draw1.text((45, 125), "180° Out-of-Phase", fill="orange", font=font_medium)
draw1.text((120, 72), "Linear Region", fill="black", font=font_small)

img1.save("images/lvdt_characteristic_solved.png")

# ----------------- 2. MCB Construction Schematic -----------------
# size: 320 x 200
img2 = Image.new("RGB", (320, 200), "white")
draw2 = ImageDraw.Draw(img2)

# Outline housing box
draw_sketch_line(draw2, 15, 15, 305, 15)
draw_sketch_line(draw2, 305, 15, 305, 185)
draw_sketch_line(draw2, 305, 185, 15, 185)
draw_sketch_line(draw2, 15, 185, 15, 15)
draw2.text((20, 20), "MCB Housing", fill="grey", font=font_medium)

# Wiring path: Input -> Bimetallic -> Solenoid -> Contacts -> Output
# Input Terminal
draw_sketch_circle(draw2, 40, 50, 6, fill="grey", outline="black")
draw2.text((32, 30), "IN", fill="blue", font=font_large)
draw_sketch_line(draw2, 40, 56, 40, 80)

# Bimetallic Strip (Thermal overload)
# Draw as two parallel rectangular strips
draw_sketch_line(draw2, 36, 80, 36, 120, fill="orange", width=3)
draw_sketch_line(draw2, 44, 80, 44, 120, fill="red", width=2)
draw2.text((50, 95), "Bimetallic Strip\n(Overload)", fill="orange", font=font_medium)
draw_sketch_line(draw2, 40, 120, 40, 140)

# Solenoid (Short-circuit electromagnet)
# Draw circular windings around central plunger
draw_sketch_line(draw2, 40, 140, 100, 140)
draw_sketch_circle(draw2, 120, 140, 10, fill=None, outline="green", width=2)
draw_sketch_line(draw2, 120, 130, 120, 150, fill="green", width=2) # plunger
draw_sketch_line(draw2, 130, 140, 170, 140)
draw2.text((105, 155), "Solenoid Coil\n(Short Circuit)", fill="green", font=font_medium)

# Manual Toggle and latch
draw_sketch_circle(draw2, 120, 50, 8, fill="grey", outline="black")
draw_sketch_line(draw2, 120, 42, 110, 25, width=4, fill="black") # switch handle
draw2.text((132, 45), "Toggle Switch", fill="black", font=font_medium)
draw_sketch_line(draw2, 120, 58, 120, 100, fill="black", width=1) # trip latch rod
draw_sketch_circle(draw2, 120, 100, 3, fill="black")
draw2.text((125, 95), "Trip Latch", fill="black", font=font_small)

# Contacts (Tripping boundary)
# Stationary contact at (190, 140), moving contact pivot
draw_sketch_circle(draw2, 190, 140, 3, fill="black")
draw_sketch_line(draw2, 170, 140, 187, 140) # fixed line
# Moving contact arm slightly tilted UP showing TRIPPED or CLOSED
draw_sketch_line(draw2, 190, 140, 215, 120, fill="red", width=2) # open contact arm
draw_sketch_circle(draw2, 215, 120, 3, fill="red")
draw2.text((170, 110), "Contacts (OPEN)", fill="red", font=font_medium)

# Arc Chute next to contacts
# Draw parallel lines
for i in range(4):
    y_pos = 100 + i * 8
    draw_sketch_line(draw2, 225, y_pos, 250, y_pos, fill="blue", width=1.5)
draw2.text((225, 135), "Arc Chute\n(Splitters)", fill="blue", font=font_small)

# Output Terminal
draw_sketch_line(draw2, 215, 140, 270, 140)
draw_sketch_circle(draw2, 270, 140, 6, fill="grey", outline="black")
draw2.text((260, 150), "OUT", fill="blue", font=font_large)

img2.save("images/mcb_construction_solved.png")

# ----------------- 3. LVDT Coils / Schematic -----------------
# size: 320 x 200
img3 = Image.new("RGB", (320, 200), "white")
draw3 = ImageDraw.Draw(img3)

# Former tube outline
draw_sketch_line(draw3, 40, 60, 280, 60, fill="grey")
draw_sketch_line(draw3, 40, 110, 280, 110, fill="grey")

# Central Primary coil Symmetrical coils on sides
# S1 (left), P (middle), S2 (right)
draw_sketch_resistor(draw3, 60, 60, 40, 0, orientation="horizontal", fill="blue")
draw2.text((70, 42), "S1 (Coil 1)", fill="blue", font=font_medium)
draw_sketch_resistor(draw3, 140, 60, 40, 0, orientation="horizontal", fill="red")
draw2.text((150, 42), "P (Primary)", fill="red", font=font_medium)
draw_sketch_resistor(draw3, 220, 60, 40, 0, orientation="horizontal", fill="blue")
draw2.text((230, 42), "S2 (Coil 2)", fill="blue", font=font_medium)

# Ferromagnetic core inside hollow former
# Represented as a solid grey rounded bar with displacement arrow
draw_sketch_circle(draw3, 110, 85, 12, fill="grey", outline="black")
draw_sketch_line(draw3, 110, 85, 210, 85, fill="black", width=14)
draw2.text((120, 80), "Soft Iron Core", fill="white", font=font_medium)

# Core displacement rod & arrow
draw_sketch_line(draw3, 210, 85, 290, 85, fill="black", width=2)
# Displacement arrow
draw_sketch_line(draw3, 260, 98, 290, 98, fill="red", width=2)
draw_sketch_line(draw3, 290, 98, 284, 94, fill="red")
draw_sketch_line(draw3, 290, 98, 284, 102, fill="red")
draw3.text((245, 102), "Displacement (x)", fill="red", font=font_small)

# Connections for AC Input to primary P
draw_sketch_line(draw3, 140, 60, 140, 150)
draw_sketch_line(draw3, 180, 60, 180, 150)
draw_sketch_ac_source(draw3, 160, 150, 12, fill="red")
draw2.text((180, 150), "AC Supply\n(Excitation)", fill="red", font=font_medium)

# Series opposition connection for S1 and S2
# Vout = V_S1 - V_S2
draw_sketch_line(draw3, 60, 60, 50, 60)
draw_sketch_line(draw3, 50, 60, 50, 160)
draw_sketch_line(draw3, 50, 160, 90, 160) # Vout + terminal

draw_sketch_line(draw3, 100, 60, 110, 60)
draw_sketch_line(draw3, 110, 60, 110, 130) # middle bridge to S2
draw_sketch_line(draw3, 110, 130, 220, 130)
draw_sketch_line(draw3, 220, 130, 220, 60) # series connect opposingly

draw_sketch_line(draw3, 260, 60, 270, 60)
draw_sketch_line(draw3, 270, 60, 270, 160)
draw_sketch_line(draw3, 270, 160, 230, 160) # Vout - terminal

# Output Meter
draw_sketch_circle(draw3, 160, 175, 12, fill="white", outline="black")
draw3.text((150, 170), "Vout", fill="blue", font=font_medium)
draw_sketch_line(draw3, 90, 160, 148, 175)
draw_sketch_line(draw3, 230, 160, 172, 175)

img3.save("images/lvdt_coils_solved.png")

# ----------------- 4. Torque-Slip Characteristic Curve -----------------
# size: 320 x 200
img4 = Image.new("RGB", (320, 200), "white")
draw4 = ImageDraw.Draw(img4)

# Axes
draw_sketch_line(draw4, 40, 150, 290, 150, fill="black", width=2) # X-axis (Slip)
draw_sketch_line(draw4, 40, 20, 40, 150, fill="black", width=2)   # Y-axis (Torque)
# Arrows
draw_sketch_line(draw4, 290, 150, 284, 146)
draw_sketch_line(draw4, 290, 150, 284, 154)
draw_sketch_line(draw4, 40, 20, 36, 26)
draw_sketch_line(draw4, 40, 20, 44, 26)

# Labels
draw4.text((15, 10), "Torque (T)", fill="black", font=font_medium)
draw4.text((250, 158), "Slip (s)", fill="black", font=font_medium)

# Slip values on X-axis (Right to left standard: 0 on right, 1 on left/standstill)
# Let's map s=1 at x=60 (Standstill), s=0 at x=260 (Synchronous speed)
# Starting Torque (T_st) at s=1: x=60, y=110 (moderate torque)
# Breakdown Torque (T_max) at s=0.2: x=220, y=40 (very high torque)
# Torque drops to 0 at s=0: x=260, y=150

# Draw stable/unstable dividing line
draw_sketch_line(draw4, 220, 40, 220, 150, fill="grey", width=1) # line at breakdown slip
draw4.text((205, 155), "s_mt", fill="red", font=font_medium)

# Draw Torque-Slip curve (Smooth curves between points)
# From standstill s=1 to breakdown slip s=0.2
curve_points = []
for i in range(60, 261):
    # Calculate representative slip
    s_val = 1.0 - (i - 60) / 200.0 # 1.0 to 0.0
    # Custom induction motor torque shape
    # T = k * s * R2 / (R2^2 + (s * X2)^2)
    # peak around s = 0.2 (x=220)
    denom = (0.2)**2 + (s_val * 0.8)**2
    num = 0.05 * s_val * 0.2
    y_val = 150 - int(250 * (num / denom))
    # Cap y to look nice
    if y_val < 40: y_val = 40
    curve_points.append((i, y_val))

for i in range(len(curve_points) - 1):
    draw_sketch_line(draw4, curve_points[i][0], curve_points[i][1], curve_points[i+1][0], curve_points[i+1][1], fill="blue", width=3)

# Key markings
draw_sketch_circle(draw4, 60, 110, 3, fill="red") # Starting torque
draw4.text((65, 102), "T_st\n(s=1)", fill="red", font=font_medium)

draw_sketch_circle(draw4, 220, 40, 3, fill="red") # Breakdown torque
draw4.text((178, 25), "T_max (Breakdown)", fill="red", font=font_medium)

draw_sketch_circle(draw4, 260, 150, 3, fill="black") # Null speed
draw4.text((250, 134), "s=0\n(Ns)", fill="black", font=font_small)

# Region shadings/labels
# Unstable region: s = s_mt to 1 (left side)
draw4.text((90, 75), "UNSTABLE\nREGION", fill="orange", font=font_medium)
# Stable region: s = 0 to s_mt (right side)
draw4.text((225, 75), "STABLE\nREGION", fill="green", font=font_medium)

img4.save("images/induction_motor_torque_solved.png")

# ----------------- 5. DC Motor Construction -----------------
# size: 320 x 200
img5 = Image.new("RGB", (320, 200), "white")
draw5 = ImageDraw.Draw(img5)
cx, cy = 160, 100

# Yoke (Outer casing)
draw_sketch_circle(draw5, cx, cy, 75, fill=None, outline="black", width=3)
draw5.text((205, 40), "Yoke (Frame)", fill="black", font=font_medium)

# Main Pole structures (North Pole left, South Pole right)
# North Pole (Left)
draw_sketch_line(draw5, cx - 74, cy - 25, cx - 50, cy - 20)
draw_sketch_line(draw5, cx - 50, cy - 20, cx - 50, cy + 20)
draw_sketch_line(draw5, cx - 50, cy + 20, cx - 74, cy + 25)
draw_sketch_circle(draw5, cx - 62, cy, 4, fill="orange") # field winding representation
draw5.text((cx - 68, cy - 10), "N", fill="black", font=font_large)

# South Pole (Right)
draw_sketch_line(draw5, cx + 74, cy - 25, cx + 50, cy - 20)
draw_sketch_line(draw5, cx + 50, cy - 20, cx + 50, cy + 20)
draw_sketch_line(draw5, cx + 50, cy + 20, cx + 74, cy + 25)
draw_sketch_circle(draw5, cx + 62, cy, 4, fill="orange") # field winding representation
draw5.text((cx + 58, cy - 10), "S", fill="black", font=font_large)

draw5.text((cx - 130, cy + 30), "Field Winding\n& Pole", fill="orange", font=font_medium)

# Armature Rotor (Center circle)
draw_sketch_circle(draw5, cx, cy, 40, fill="grey", outline="black", width=2)
draw5.text((cx - 30, cy - 35), "Armature Core", fill="white", font=font_small)

# Armature Slots / Conductors (Small circles inside armature boundary)
for angle in range(0, 360, 45):
    rad = math.radians(angle)
    sx = cx + int(30 * math.cos(rad))
    sy = cy + int(30 * math.sin(rad))
    draw_sketch_circle(draw5, sx, sy, 3, fill="red", outline="black")
draw5.text((cx - 75, cy - 65), "Armature Winding", fill="red", font=font_medium)

# Commutator & Brushes in center
# Commutator (very small segmented ring)
draw_sketch_circle(draw5, cx, cy, 14, fill="white", outline="black")
draw_sketch_line(draw5, cx - 14, cy, cx + 14, cy, fill="grey")
# Carbon Brushes (black rectangular blocks pressing on commutator)
draw_sketch_line(draw5, cx - 20, cy - 4, cx - 14, cy - 4)
draw_sketch_line(draw5, cx - 20, cy + 4, cx - 14, cy + 4)
draw_sketch_line(draw5, cx - 20, cy - 4, cx - 20, cy + 4)
draw_sketch_line(draw5, cx - 14, cy - 4, cx - 14, cy + 4)

draw_sketch_line(draw5, cx + 20, cy - 4, cx + 14, cy - 4)
draw_sketch_line(draw5, cx + 20, cy + 4, cx + 14, cy + 4)
draw_sketch_line(draw5, cx + 20, cy - 4, cx + 20, cy + 4)
draw_sketch_line(draw5, cx + 14, cy - 4, cx + 14, cy + 4)

draw5.text((cx - 35, cy + 18), "Commutator", fill="black", font=font_small)
draw5.text((cx + 25, cy + 18), "Carbon Brush", fill="black", font=font_small)

img5.save("images/dc_motor_construction_solved.png")

# ----------------- 6. Pipe Earthing Pit Installation -----------------
# size: 320 x 220
img6 = Image.new("RGB", (320, 220), "white")
draw6 = ImageDraw.Draw(img6)

# Ground Level (Horizontal line)
draw_sketch_line(draw6, 20, 40, 300, 40, fill="black", width=2)
draw6.text((25, 25), "Ground Level", fill="black", font=font_medium)

# Concrete Chamber at the top (Masonry enclosure)
draw_sketch_line(draw6, 120, 20, 200, 20, fill="grey", width=3) # CI cover
draw6.text((125, 8), "CI Cover", fill="grey", font=font_small)
draw_sketch_line(draw6, 120, 20, 120, 60, fill="grey")
draw_sketch_line(draw6, 200, 20, 200, 60, fill="grey")

# Watering Funnel inside Concrete enclosure
draw_sketch_line(draw6, 150, 35, 170, 35) # funnel top
draw_sketch_line(draw6, 150, 35, 158, 55)
draw_sketch_line(draw6, 170, 35, 162, 55)
draw_sketch_line(draw6, 158, 55, 158, 70) # funnel tube into pipe
draw_sketch_line(draw6, 162, 55, 162, 70)
draw6.text((172, 38), "Funnel + Mesh", fill="blue", font=font_small)

# GI Pipe (Vertical buried electrode)
# Buried from y=60 to y=190
px1, px2 = 152, 168
draw_sketch_line(draw6, px1, 60, px1, 190, fill="grey", width=2)
draw_sketch_line(draw6, px2, 60, px2, 190, fill="grey", width=2)
# Rounded bottom of pipe
draw_sketch_line(draw6, px1, 190, px2, 190, fill="grey", width=2)

# Perforations (small holes along pipe)
for py in range(90, 180, 20):
    draw_sketch_circle(draw6, px1 + 4, py, 2, fill="black")
    draw_sketch_circle(draw6, px2 - 4, py, 2, fill="black")
draw6.text((172, 100), "GI Pipe\n(38mm Dia\n2.5m Deep)", fill="grey", font=font_medium)

# Earth Wire clamp
draw_sketch_circle(draw6, px1 - 3, 50, 3, fill="black")
draw_sketch_line(draw6, px1 - 3, 50, 80, 50, fill="green", width=2) # Earth wire going to equipment
draw6.text((40, 55), "GI Earth Wire", fill="green", font=font_medium)

# Alternate layers of charcoal and salt (from y=70 to y=195)
# Draw bounding box for backfill
draw_sketch_line(draw6, 110, 70, 110, 195, fill="orange")
draw_sketch_line(draw6, 210, 70, 210, 195, fill="orange")
draw_sketch_line(draw6, 110, 195, 210, 195, fill="orange")

# Alternate layers (Charcoal = dark block, Salt = dotted white block)
# Layer 1: Salt (y=70 to y=100)
draw6.text((68, 80), "Salt Layer", fill="orange", font=font_small)
# Layer 2: Charcoal (y=100 to y=130) - represent with charcoal hashing
draw_sketch_line(draw6, 112, 110, 148, 120, fill="grey")
draw_sketch_line(draw6, 172, 115, 208, 125, fill="grey")
draw6.text((58, 110), "Charcoal Layer\n(15cm)", fill="black", font=font_small)
# Layer 3: Salt (y=130 to y=160)
draw6.text((68, 140), "Salt Layer", fill="orange", font=font_small)
# Layer 4: Charcoal (y=160 to y=190)
draw_sketch_line(draw6, 112, 170, 148, 180, fill="grey")
draw_sketch_line(draw6, 172, 175, 208, 185, fill="grey")

img6.save("images/pipe_earthing_construction_solved.png")

# ----------------- 7. Transducer System Block Diagram -----------------
# size: 320 x 140
img7 = Image.new("RGB", (320, 140), "white")
draw7 = ImageDraw.Draw(img7)

# Helper to draw a text box
def draw_block_box(draw, x, y, w, h, text, title_color="black"):
    draw_sketch_line(draw, x, y, x+w, y)
    draw_sketch_line(draw, x+w, y, x+w, y+h)
    draw_sketch_line(draw, x+w, y+h, x, y+h)
    draw_sketch_line(draw, x, y+h, x, y)
    draw.text((x + 8, y + h/2 - 6), text, fill=title_color, font=font_medium)

# Blocks
# 1. Physical Input (30, 45)
draw_block_box(draw7, 15, 45, 65, 40, "Measurand\n(Input)", "blue")
# Arrow 1
draw_sketch_line(draw7, 80, 65, 100, 65)
draw_sketch_line(draw7, 100, 65, 96, 61)
draw_sketch_line(draw7, 100, 65, 96, 69)

# 2. Sensing Element (100, 45)
draw_block_box(draw7, 100, 45, 75, 40, "Sensing\nElement", "purple")
# Arrow 2
draw_sketch_line(draw7, 175, 65, 195, 65)
draw_sketch_line(draw7, 195, 65, 191, 61)
draw_sketch_line(draw7, 195, 65, 191, 69)
draw7.text((172, 50), "Inter.", fill="grey", font=font_small)

# 3. Signal Conditioning (195, 45)
draw_block_box(draw7, 195, 45, 80, 40, "Conditioning\n(Secondary)", "orange")
# Arrow 3
draw_sketch_line(draw7, 275, 65, 295, 65)
draw_sketch_line(draw7, 295, 65, 291, 61)
draw_sketch_line(draw7, 295, 65, 291, 69)

# 4. Output (295, 45) -> arrow goes to text
draw7.text((298, 55), "Output\n(V / I)", fill="green", font=font_large)

# Block Diagram Title
draw7.text((15, 10), "Functional Block Diagram of a Transducer System", fill="black", font=font_large)
draw7.text((15, 100), "Sensing (Primary Transducer) -> Conditioning (Secondary Transducer)", fill="grey", font=font_small)

img7.save("images/transducer_block_solved.png")

# ----------------- 8. ELCB Working Schematic -----------------
# size: 320 x 200
img8 = Image.new("RGB", (320, 200), "white")
draw8 = ImageDraw.Draw(img8)

# Toroidal core in center
tcx, tcy = 130, 100
draw_sketch_circle(draw8, tcx, tcy, 24, fill="grey", outline="black", width=4)
draw_sketch_circle(draw8, tcx, tcy, 14, fill="white", outline="black", width=2)
draw8.text((tcx - 20, tcy - 8), "CBCT", fill="white", font=font_medium)

# Live Line (top) passing through toroid
draw_sketch_line(draw8, 20, 60, tcx - 16, 60)
draw_sketch_line(draw8, tcx - 16, 60, tcx - 10, 86) # winding loop
draw_sketch_line(draw8, tcx - 10, 86, tcx - 4, 60)
draw_sketch_line(draw8, tcx - 4, 60, 240, 60)
draw8.text((30, 45), "Live (IL)", fill="red", font=font_medium)

# ELCB Trip contacts on Live wire (left side)
draw_sketch_circle(draw8, 50, 60, 3, fill="black")
draw_sketch_line(draw8, 50, 60, 70, 45, fill="red", width=2) # contacts open
draw_sketch_circle(draw8, 70, 60, 3, fill="black")
draw8.text((45, 30), "Trip Contacts", fill="red", font=font_small)

# Neutral Line (bottom) passing through toroid
draw_sketch_line(draw8, 20, 140, tcx - 16, 140)
draw_sketch_line(draw8, tcx - 16, 140, tcx - 10, 114) # winding loop (opposing direction)
draw_sketch_line(draw8, tcx - 10, 114, tcx - 4, 140)
draw_sketch_line(draw8, tcx - 4, 140, 240, 140)
draw8.text((30, 145), "Neutral (IN)", fill="blue", font=font_medium)

# Load on right side
draw_sketch_resistor(draw8, 240, 60, 0, 80, orientation="vertical", fill="black")
draw8.text((250, 95), "Load", fill="black", font=font_large)

# Sensing coil on toroid feeding trip relay
draw_sketch_circle(draw8, tcx, tcy + 18, 3, fill="orange") # winding connection
draw_sketch_line(draw8, tcx, tcy + 18, tcx, 160)
draw_sketch_line(draw8, tcx + 5, tcy + 18, tcx + 5, 160)
draw_sketch_resistor(draw8, tcx - 10, 160, 25, 0, orientation="horizontal", fill="orange")
draw8.text((tcx + 20, 160), "Trip Relay\n& Solenoid", fill="orange", font=font_small)

# Dotted mechanical link from relay to trip contacts
for y in range(65, 160, 10):
    draw_sketch_line(draw8, 60, y, 60, y + 5, fill="grey", width=1)
draw_sketch_line(draw8, 60, 160, tcx - 10, 160, fill="grey", width=1)

# Earth Leakage Fault representer
# Fault wire from load live back to ground via human shock path
draw_sketch_line(draw8, 240, 80, 280, 80)
# Shock path
draw_sketch_circle(draw8, 280, 100, 8, fill=None, outline="red") # human head
draw_sketch_line(draw8, 280, 108, 280, 140, fill="red") # body
draw_sketch_line(draw8, 270, 120, 290, 120, fill="red") # arms
draw_sketch_line(draw8, 280, 140, 275, 165, fill="red") # legs
draw_sketch_line(draw8, 280, 140, 285, 165, fill="red")
draw8.text((290, 110), "IFault\n(Leakage)", fill="red", font=font_small)

# Ground path
draw_sketch_line(draw8, 270, 165, 290, 165)
draw_sketch_line(draw8, 273, 169, 287, 169)
draw_sketch_line(draw8, 277, 173, 283, 173)

img8.save("images/elcb_construction_solved.png")

# ----------------- 9. LVDT Waveforms / Phase Relationship -----------------
# size: 320 x 200
img9 = Image.new("RGB", (320, 200), "white")
draw9 = ImageDraw.Draw(img9)

# We will draw three horizontal slots: Null, Left (+x), Right (-x)
# Horizontal slot 1: Null Position
draw_sketch_line(draw9, 10, 45, 310, 45, fill="grey", width=1)
draw9.text((15, 12), "1. Core at Null Position (Center)", fill="black", font=font_medium)
draw_sketch_line(draw9, 100, 32, 280, 32, fill="red", width=2) # straight 0V line
draw9.text((210, 18), "Output V_out = 0V", fill="red", font=font_small)

# Horizontal slot 2: Core Left (+x) S1 side
draw_sketch_line(draw9, 10, 115, 310, 115, fill="grey", width=1)
draw9.text((15, 52), "2. Core Left (+x): VS1 > VS2", fill="blue", font=font_medium)
# Sine wave in phase with primary (0 deg shift)
w2_points = []
for x in range(100, 280):
    t = (x - 100) / 180.0
    y = 80 - int(15 * math.sin(4 * math.pi * t))
    w2_points.append((x, y))
for i in range(len(w2_points) - 1):
    draw_sketch_line(draw9, w2_points[i][0], w2_points[i][1], w2_points[i+1][0], w2_points[i+1][1], fill="blue", width=2)
draw9.text((200, 95), "In-Phase with Primary (0°)", fill="blue", font=font_small)

# Horizontal slot 3: Core Right (-x) S2 side
draw9.text((15, 122), "3. Core Right (-x): VS2 > VS1", fill="orange", font=font_medium)
# Sine wave 180 deg out of phase (inverted sine)
w3_points = []
for x in range(100, 280):
    t = (x - 100) / 180.0
    y = 155 + int(15 * math.sin(4 * math.pi * t)) # inverted
    w3_points.append((x, y))
for i in range(len(w3_points) - 1):
    draw_sketch_line(draw9, w3_points[i][0], w3_points[i][1], w3_points[i+1][0], w3_points[i+1][1], fill="orange", width=2)
draw9.text((200, 172), "180° Out-of-Phase (Inverted)", fill="orange", font=font_small)

img9.save("images/lvdt_waveforms_solved.png")

print("All 9 solved MST2 diagrams generated successfully!")
