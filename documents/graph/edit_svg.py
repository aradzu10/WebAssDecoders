import re

INCREASE_Y = 10
INPUT = "graph.svg"
OUTPUT = "graphout.svg"


def get_circles(shapes):
    return [shape for shape in shapes if shape["type"] == "circle"]


def get_paths(shapes):
    return [shape for shape in shapes if shape["type"] == "path"]


def get_circle_by_y(circles, pofloat):
    for circle in circles:
        if circle["cy"] == pofloat[1]:
            return circle


def get_start_end_pofloat_path(circles, path):
    cords = re.findall("([0-9,.]+)", path["d"])
    start_circ = get_circle_by_y(circles, cords[0].split(","))
    end_pofloat = cords[1].split(",")
    end_circ = get_circle_by_y(circles, end_pofloat if len(end_pofloat) is 2 else end_pofloat[-2:])
    return start_circ, end_circ


def parse_svg_line(line):
    shape = {}
    line = line.strip().strip("</>\n")
    shape["type"] = line.split()[0]
    line_s = re.findall('([^ ]+=".+?")', line)

    for att in line_s:
        att_s = att.split("=")
        shape[att_s[0]] = att_s[1].strip('"')

    return shape


def write_shape(shape):
    tmp = shape.copy()
    line = "<%s " % shape["type"]
    tmp.pop("type")
    line += " ".join('%s="%s"' % (k, v) for k, v in tmp.items())
    line += "/>"
    return line


def manipulate_circles(circles):
    for i, circle in enumerate(circles):
        circle["cy"] = str(float(circle["cy"]) + INCREASE_Y*i)


def get_circles_sorted_by_rows(shapes):
    circles = get_circles(shapes)
    circles = sorted(circles, key=lambda s: float(s["cy"]))
    return circles


def get_circles_sorted_by_col(shapes):
    circles = get_circles(shapes)
    circles = sorted(circles, key=lambda s: float(s["cx"]))
    return circles


def get_path_with_circle_pofloats(shapes):
    path_to_do = []
    circles = get_circles(shapes)
    paths = get_paths(shapes)
    for path in paths:
        tmp = get_start_end_pofloat_path(circles, path)
        path_to_do.append((path, tmp[0], tmp[1]))
    return path_to_do


def manipulate_paths(paths_with_start_end):
    for path, start_circ, end_circ in paths_with_start_end:
        cords = re.findall("([0-9,.]+)", path["d"])
        start_p = cords[0].split(",")
        end_p = cords[1].split(",")

        dis = float(start_circ["cy"]) - float(start_p[-1])
        start_p[-1] = start_circ["cy"]

        cords = "M" + ",".join(start_p)

        if len(end_p) == 2:
            cords += "L"
            end_p[-1] = end_circ["cy"]
        else:
            cords += "C"
            end_p[1] = str(float(end_p[1]) + dis)
            end_p[3] = str(float(end_p[3]) + dis)
            end_p[5] = str(float(end_p[5]) + dis)

        cords += ",".join(end_p)
        path["d"] = cords


def set_svg_size(svg):
    bar = svg[0]
    circles = get_circles_sorted_by_rows(svg)
    start_circ = float(circles[0]["cy"])
    end_circ = float(circles[-1]["cy"])
    height = end_circ + start_circ
    bar["height"] = str(height)
    circles = get_circles_sorted_by_col(svg)
    start_circ = float(circles[0]["cx"])
    end_circ = float(circles[-1]["cx"])
    width = end_circ + start_circ
    bar["width"] = str(width)


def read_svg():
    with open(INPUT) as f:
        svg = f.readlines()

    svg = [parse_svg_line(l) for l in svg]

    return svg


def write_svg(shapes):

    lines = [write_shape(shapes[0]).replace("/>", ">") + "\n"] + [write_shape(s) + "\n" for s in shapes[1:]]
    with open(OUTPUT, "w") as f:
        f.writelines(lines)


def main():
    svg = read_svg()
    path_start_end = get_path_with_circle_pofloats(svg)
    circles = get_circles_sorted_by_rows(svg)
    manipulate_circles(circles)
    manipulate_paths(path_start_end)
    set_svg_size(svg)
    write_svg(svg)


if __name__ == '__main__':
    main()
