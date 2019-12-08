def pixel_value_from_layers(layer_vals):
    for val in layer_vals:
        if val == 1:
            return 1
        if val == 0:
            return 0


IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6

IMAGE_LAYER_NUMBER_OF_PIXELS = IMAGE_WIDTH * IMAGE_HEIGHT

image_input = [int(s) for s in (open("input.txt", "r").readline().strip())]

number_of_layers = len(image_input) / IMAGE_LAYER_NUMBER_OF_PIXELS

image_layers = [image_input[(n - 1) * IMAGE_LAYER_NUMBER_OF_PIXELS:n * IMAGE_LAYER_NUMBER_OF_PIXELS] for n in
                range(1, number_of_layers+1)]

pixel_layers = [[] for n in range(IMAGE_LAYER_NUMBER_OF_PIXELS)]


decoded_image = map(lambda x: pixel_value_from_layers(x), zip(*image_layers))


pixel_rows = [decoded_image[(n-1) * IMAGE_WIDTH:n * IMAGE_WIDTH] for n in range(1, IMAGE_HEIGHT + 1)]
for row in pixel_rows:
    for num in row:
        if num == 1:
            print "@",
        else:
            print " ",
    print ""
