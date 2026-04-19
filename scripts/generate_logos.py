from PIL import Image, ImageDraw, ImageFilter

def generate_pixel_favicon():
    print("Generating pixel art favicon.ico...")
    # T = Transparent, O = Slate Border, S = Bright Silver, D = Dark Silver
    # B = Black Hash, C = Cyan node
    T = (0, 0, 0, 0)
    O = (71, 85, 105, 255)   
    S = (241, 245, 249, 255) 
    D = (148, 163, 184, 255) 
    B = (15, 23, 42, 255)    
    C = (0, 212, 255, 255)   

    # Hand-mapped 16x16 pixel-art matrix
    pixels = [
        [T,T,T,T,T,T,T,T,T,T,T,T,T,T,T,T],
        [T,T,T,O,O,O,O,O,O,O,O,O,O,T,T,T],
        [T,T,O,S,S,S,S,S,D,D,D,D,D,O,T,T],
        [T,T,O,S,S,B,S,S,D,B,D,D,D,O,T,T],
        [T,T,O,S,S,B,S,S,D,B,D,D,D,O,T,T],
        [T,T,O,B,B,B,B,B,B,B,B,B,D,O,T,T],
        [T,T,O,S,S,B,S,S,D,B,C,D,D,O,T,T],
        [T,T,O,S,S,B,S,S,D,B,D,D,D,O,T,T],
        [T,T,O,B,B,B,B,B,B,B,B,B,D,O,T,T],
        [T,T,O,S,S,B,S,S,D,B,D,D,D,O,T,T],
        [T,T,T,O,S,B,S,S,D,B,D,D,O,T,T,T],
        [T,T,T,O,S,S,S,S,D,D,D,D,O,T,T,T],
        [T,T,T,T,O,S,S,S,D,D,D,O,T,T,T,T],
        [T,T,T,T,T,O,S,S,D,D,O,T,T,T,T,T],
        [T,T,T,T,T,T,O,S,D,O,T,T,T,T,T,T],
        [T,T,T,T,T,T,T,O,O,T,T,T,T,T,T,T],
    ]

    img = Image.new("RGBA", (16, 16))
    for y in range(16):
        for x in range(16):
            img.putpixel((x, y), pixels[y][x])

    # Scale to 32x32 via Nearest Neighbor to keep edges sharp
    favicon = img.resize((32, 32), Image.Resampling.NEAREST)
    favicon.save("favicon.ico", format="ICO")
    print("-> favicon.ico saved.")

def generate_high_res_logo():
    print("Generating High-Res logo.png...")
    size = 1024
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Background Drop Shadow
    shadow = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    shield_poly = [(256, 128), (512, 192), (768, 128), (768, 640), (512, 920), (256, 640)]
    shadow_poly = [(x+20, y+30) for x,y in shield_poly]
    s_draw.polygon(shadow_poly, fill=(0, 0, 0, 80))
    shadow = shadow.filter(ImageFilter.GaussianBlur(30))
    img.alpha_composite(shadow)

    # 2. Dual-Tone 3D Shield
    left_half = [(256, 128), (512, 192), (512, 920), (256, 640)]
    right_half = [(512, 192), (768, 128), (768, 640), (512, 920)]
    draw.polygon(left_half, fill="#f8fafc")
    draw.polygon(right_half, fill="#cbd5e1")
    draw.line(shield_poly + [shield_poly[0]], fill="#475569", width=24, joint="curve")

    # 3. Hash Grid
    hash_color = "#0f172a"
    w = 54
    # Verticals
    draw.rounded_rectangle([380, 280, 380+w, 740], radius=16, fill=hash_color)
    draw.rounded_rectangle([580, 280, 580+w, 740], radius=16, fill=hash_color)
    # Horizontals
    draw.rounded_rectangle([250, 400, 770, 400+w], radius=16, fill=hash_color)
    draw.rounded_rectangle([250, 600, 770, 600+w], radius=16, fill=hash_color)

    # 4. Cyan Mesh Nodes at Intersections
    node_r = 30
    intersections = [(380+w//2, 400+w//2), (580+w//2, 400+w//2), (380+w//2, 600+w//2), (580+w//2, 600+w//2)]
    
    for i, (cx, cy) in enumerate(intersections):
        if i == 1: # Highlight top-right node with a glowing rim
            draw.ellipse([cx-node_r-10, cy-node_r-10, cx+node_r+10, cy+node_r+10], fill="#ffffff")
            draw.ellipse([cx-node_r, cy-node_r, cx+node_r, cy+node_r], fill="#00d4ff")

    # Anti-Alias and Save
    final_img = img.resize((1024, 1024), Image.Resampling.LANCZOS)
    final_img.save("omnimesh-logo.png")
    print("-> omnimesh-logo.png saved.")

if __name__ == "__main__":
    generate_pixel_favicon()
    generate_high_res_logo()
