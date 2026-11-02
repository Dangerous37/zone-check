def point(value):
    if not isinstance(value, list) or len(value) != 2 or any(type(v) is not int for v in value):
        raise ValueError("expected a pair of integer coordinates")
    return tuple(value)


def in_ring(p, ring):
    x, y = p
    inside = False
    for first, second in zip(ring, ring[1:] + ring[:1]):
        ax, ay = first
        bx, by = second
        cross = (bx - ax) * (y - ay) - (by - ay) * (x - ax)
        if cross == 0 and min(ax, bx) <= x <= max(ax, bx) and min(ay, by) <= y <= max(ay, by):
            return "boundary"
        if (ay > y) != (by > y) and (cross > 0) == (by > ay):
            inside = not inside
    return "inside" if inside else "outside"


def evaluate(data):
    rings = [[point(vertex) for vertex in ring] for ring in data["rings"]]
    if not rings or any(len(set(ring)) < 3 for ring in rings):
        raise ValueError("each ring needs three distinct vertices")
    result = []
    for coords in data["points"]:
        positions = [in_ring(point(coords), ring) for ring in rings]
        status = positions[0]
        if "boundary" in positions:
            status = "boundary"
        elif "inside" in positions[1:]:
            status = "outside"
        result.append({"point": coords, "status": status})
    return result
