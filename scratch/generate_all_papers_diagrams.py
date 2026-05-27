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

# Fonts
try:
    font_large = ImageFont.truetype("arial.ttf", 13)
    font_medium = ImageFont.truetype("arial.ttf", 10)
    font_small = ImageFont.truetype("arial.ttf", 8)
except IOError:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_small = ImageFont.load_default()

# ----------------- 1. Cable Types Cross Sections -----------------
img1 = Image.new("RGB", (320, 150), "white")
draw1 = ImageDraw.Draw(img1)

# Solid Wire
draw_sketch_circle(draw1, 50, 60, 20, fill="grey", outline="black")
draw_sketch_circle(draw1, 50, 60, 8, fill="orange", outline="black")
draw1.text((35, 90), "Solid Wire", fill="black", font=font_medium)

# Stranded Wire
draw_sketch_circle(draw1, 120, 60, 20, fill="grey", outline="black")
for dx, dy in [(0,0), (-5,-5), (5,-5), (-5,5), (5,5), (0,-7), (0,7), (-7,0), (7,0)]:
    draw_sketch_circle(draw1, 120+dx, 60+dy, 2, fill="orange", outline="black", width=1)
draw1.text((100, 90), "Stranded Wire", fill="black", font=font_medium)

# Coaxial Cable
draw_sketch_circle(draw1, 190, 60, 20, fill="black", outline="black")
draw_sketch_circle(draw1, 190, 60, 16, fill="grey", outline="black") # shield
draw_sketch_circle(draw1, 190, 60, 12, fill="white", outline="black") # dielectric
draw_sketch_circle(draw1, 190, 60, 3, fill="orange", outline="black") # inner
draw1.text((175, 90), "Coaxial", fill="black", font=font_medium)

# Twisted Pair
draw_sketch_circle(draw1, 260, 60, 20, fill="grey", outline="black")
draw_sketch_circle(draw1, 255, 60, 8, fill="blue", outline="black")
draw_sketch_circle(draw1, 255, 60, 3, fill="orange", outline="black")
draw_sketch_circle(draw1, 265, 60, 8, fill="green", outline="black")
draw_sketch_circle(draw1, 265, 60, 3, fill="orange", outline="black")
draw1.text((245, 90), "Twisted Pair", fill="black", font=font_medium)

img1.save("images/cable_types.png")

# ----------------- 2. Induction Motor Power Flow -----------------
img2 = Image.new("RGB", (320, 120), "white")
draw2 = ImageDraw.Draw(img2)

def draw_block_box(draw, x, y, w, h, text, title_color="black"):
    draw_sketch_line(draw, x, y, x+w, y)
    draw_sketch_line(draw, x+w, y, x+w, y+h)
    draw_sketch_line(draw, x+w, y+h, x, y+h)
    draw_sketch_line(draw, x, y+h, x, y)
    draw.text((x + 5, y + h/2 - 5), text, fill=title_color, font=font_small)

draw_block_box(draw2, 10, 40, 50, 40, "P_in (Stator)", "blue")
draw_sketch_line(draw2, 60, 60, 90, 60)
draw_block_box(draw2, 90, 40, 50, 40, "Air Gap P_g", "orange")
draw_sketch_line(draw2, 140, 60, 170, 60)
draw_block_box(draw2, 170, 40, 60, 40, "Mech Power", "purple")
draw_sketch_line(draw2, 230, 60, 260, 60)
draw_block_box(draw2, 260, 40, 50, 40, "P_out (Shaft)", "green")

# Losses arrows pointing down
draw_sketch_line(draw2, 75, 60, 75, 90, fill="red")
draw2.text((60, 95), "Stator Cu Loss", fill="red", font=font_small)

draw_sketch_line(draw2, 155, 60, 155, 90, fill="red")
draw2.text((140, 95), "Rotor Cu Loss", fill="red", font=font_small)

draw_sketch_line(draw2, 245, 60, 245, 90, fill="red")
draw2.text((230, 95), "Friction Loss", fill="red", font=font_small)

img2.save("images/im_power_flow.png")

# ----------------- 3. Star Phasor -----------------
img3 = Image.new("RGB", (200, 200), "white")
draw3 = ImageDraw.Draw(img3)
cx, cy = 100, 100

# Draw Vph
for angle, color, label in [(90, "red", "VR"), (330, "blue", "VY"), (210, "green", "VB")]:
    rad = math.radians(angle)
    x = cx + int(40 * math.cos(rad))
    y = cy - int(40 * math.sin(rad))
    draw_sketch_line(draw3, cx, cy, x, y, fill=color, width=2)
    draw3.text((x, y), label, fill=color, font=font_medium)

# Draw VL (VR - VY)
rad1 = math.radians(90)
x1 = cx + int(40 * math.cos(rad1))
y1 = cy - int(40 * math.sin(rad1))

rad2 = math.radians(150) # -VY
x2 = cx + int(40 * math.cos(rad2))
y2 = cy - int(40 * math.sin(rad2))
draw_sketch_line(draw3, cx, cy, x2, y2, fill="grey", width=1) # dotted -VY
draw_sketch_line(draw3, x1, y1, x1+(x2-cx), y1+(y2-cy), fill="grey", width=1) 
draw_sketch_line(draw3, x2, y2, x1+(x2-cx), y1+(y2-cy), fill="grey", width=1) 

vry_x = x1+(x2-cx)
vry_y = y1+(y2-cy)
draw_sketch_line(draw3, cx, cy, vry_x, vry_y, fill="black", width=2)
draw3.text((vry_x, vry_y), "VRY (Line)", fill="black", font=font_medium)

img3.save("images/star_phasor_solved.png")

print("Generated new diagrams!")
