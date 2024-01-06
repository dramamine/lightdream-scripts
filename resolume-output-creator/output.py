import xml.etree.ElementTree as ET
import copy
tree = ET.parse('Greenhouse Test 2.xml')
root = tree.getroot()

screens = root.findall('.//screens')[0]
main_screen = root.findall('.//DmxScreen')[0]
print(main_screen)

# bottom_left_x, bottom_left_y, bottom_right_x, bottom_right_y, height
rectangle = [600, 600, 700, 600, 100]

point_0 = {"x": rectangle[0], "y": rectangle[1]}
point_1 = {"x": rectangle[2], "y": rectangle[1]}
point_2 = {"x": rectangle[2], "y": rectangle[1]+4}
point_3 = {"x": rectangle[0], "y": rectangle[1]+4}

for i in range(1):
    screen = copy.deepcopy(main_screen)
    screen.set("name", "Lumiverse 2")
    screen.set("uniqueId", "1671490627555")
    for slice in screen.findall('.//DmxSlice'):
        rect = slice.find(".//InputRect")
        vecs = rect.findall(".//v")
        vecs[0].set("x", str(point_0["x"]))
        vecs[0].set("y", str(point_0["y"]))
        vecs[1].set("x", str(point_1["x"]))
        vecs[1].set("y", str(point_1["y"]))
        vecs[2].set("x", str(point_2["x"]))
        vecs[2].set("y", str(point_2["y"])) 
        vecs[3].set("x", str(point_3["x"]))
        vecs[3].set("y", str(point_3["y"]))       
    screens.append(screen)

# slices have uniqueId, names like "1 - 72 led 24 LR"
# layers = root.findall('.//layers')[0]
# print(layers)


# slices have uniqueId, names like "1 - 72 led 24 LR"
# print(root.findall('.//DmxSlice'))

tree.write('output.xml')
