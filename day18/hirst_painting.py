import colorgram 
colors = colorgram.extract('C:\Learn IT\python_bootcamp\day18\image.jpg', 30)
colors_n = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    colors_n.append(new_color)

print(colors_n)