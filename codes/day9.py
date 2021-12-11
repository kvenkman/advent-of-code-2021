from collections import defaultdict
test = False

if test:
    input = '../inputs/day9_test'
else:
    input = '../inputs/day9_input'

with open(input, 'r') as f:
    lines = f.readlines()

# Part 1
def parse_map(heatmap):
    low_point = 0
    risk_level = 0
    lp_coordinates = []

    for i, v1 in enumerate(heatmap):
        for j, v2 in enumerate(v1):
            #print(i, j, v2)
            local_low_point = 0
            surrounding_points = []

            # check element above
            if (i-1) >= 0:
                if heatmap[i-1][j] > v2:
                    local_low_point += 1
                    surrounding_points.append(heatmap[i-1][j])
            else:
                local_low_point += 1

            # check element below
            if (i+1) < len(heatmap):
                if heatmap[i+1][j] > v2:
                    local_low_point += 1
                    surrounding_points.append(heatmap[i+1][j])
            else:
                local_low_point += 1

            # check element to the left
            if (j-1) >= 0:
                if heatmap[i][j-1] > v2:
                    local_low_point += 1
                    surrounding_points.append(heatmap[i][j-1])
            else:
                local_low_point += 1

            # check element to the right
            if (j+1) < len(v1):
                if heatmap[i][j+1] > v2:
                    local_low_point += 1
                    surrounding_points.append(heatmap[i][j+1])
            else:
                local_low_point += 1

            if local_low_point == 4:
                # print(i, j, v2, surrounding_points)
                lp_coordinates.append((i, j))
                low_point += 1
                risk_level += (v2+1)

    return lp_coordinates, low_point, risk_level

heatmap = [[int(i) for i in x] for x in [list(l.strip()) for l in lines]]
lp_coordinates, low_point, risk_level = parse_map(heatmap)
print(risk_level)

# Part 2
# Starting from the low point coordinates, we propagate outwards to find the corresponding basin
def return_basin_size(coordinates, heatmap):
    # basin_size = 1
    # prev_size, cur_size = 0, 1
    process_queue, basin = [coordinates], set()
    while process_queue:
    # for _ in range(3):
        # find all the points around the current coordinate that are not of height 9
        coordinate = process_queue[0]
        x, y = coordinate
        
        # top
        if x-1 >= 0:
            height = heatmap[x-1][y]
            if height != 9 and (x-1, y) not in basin:
                process_queue.append((x-1, y))

        # bottom
        if x+1 < len(heatmap):
            height = heatmap[x+1][y]
            if height != 9 and (x+1, y) not in basin:
                process_queue.append((x+1, y))

        # left
        if y-1 >= 0:
            height = heatmap[x][y-1]
            if height != 9 and (x, y-1) not in basin:
                process_queue.append((x, y-1))

        # right
        if y+1 < len(heatmap[0]):
            height = heatmap[x][y+1]
            if height != 9 and (x, y+1) not in basin:
                process_queue.append((x, y+1))

        basin.add(coordinate)
        process_queue.remove(coordinate)

    return len(basin)


basin_sizes = []
for point in lp_coordinates:
    basin_sizes.append(return_basin_size(point, heatmap))

basin_sizes.sort()
print(basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3])