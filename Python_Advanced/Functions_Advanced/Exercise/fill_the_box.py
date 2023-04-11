def fill_the_box(*args):
    height_of_box = args[0]
    length_of_box = args[1]
    width_of_box = args[2]

    total_possible_boxes = height_of_box * length_of_box * width_of_box
    total_occupied_boxes = 0
    cubes_left = 0

    for element in range(3, len(args) + 1):
        current_boxes = args[element]
        if current_boxes == "Finish":
            break
        if total_occupied_boxes < total_possible_boxes and (
                total_occupied_boxes + current_boxes) <= total_possible_boxes:
            total_occupied_boxes += current_boxes
        elif total_occupied_boxes < total_possible_boxes:
            x = total_possible_boxes - total_occupied_boxes
            cubes_left += current_boxes - x
            total_occupied_boxes = total_possible_boxes
        elif total_occupied_boxes == total_possible_boxes:
            cubes_left += current_boxes
    if cubes_left == 0:
        return f"There is free space in the box. You could put {total_possible_boxes - total_occupied_boxes} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."
