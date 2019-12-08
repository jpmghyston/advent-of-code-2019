import functools


def numbers_of_digits(layer):
    return functools.reduce(
        lambda y, x: (y[0] + 1 if x == 0 else y[0], y[1] + 1 if x == 1 else y[1], y[2] + 1 if x == 2 else y[2]),
        layer,
        (0, 0, 0))


IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6

IMAGE_LAYER_NUMBER_OF_PIXELS = IMAGE_WIDTH * IMAGE_HEIGHT

image_input = [int(s) for s in (open("input.txt", "r").readline().strip())]

number_of_layers = len(image_input) / IMAGE_LAYER_NUMBER_OF_PIXELS

image_layers = [image_input[(n - 1) * IMAGE_LAYER_NUMBER_OF_PIXELS:n * IMAGE_LAYER_NUMBER_OF_PIXELS] for n in
                range(1, number_of_layers+1)]

digit_numbers = map(numbers_of_digits, image_layers)

sorted_numbers = sorted(digit_numbers, key=lambda x: x[0])

print sorted_numbers[0][1] * sorted_numbers[0][2]
