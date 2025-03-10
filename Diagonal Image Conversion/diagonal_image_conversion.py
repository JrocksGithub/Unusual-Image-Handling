from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

"""
    Rebuild the image based on a pixel list

    @param object image
    @param list pixel_list
    @param string image_destionation

    return void
"""
def create_image_from_rgb_list(image, pixel_list, image_destination):
    image_out = Image.new(image.mode, image.size)

    pixel_list = list(tuple(pixel_list))
    image_out.putdata(pixel_list)

    image_out.save(image_destination)


"""
    Prepare pixel array based on offset for a different starting point to flip and reverse diagonally
    
    @param string image_location
    @param string image_destination
    @param integer split_offset
    @param integer pixel_width
    
    return void
"""
def rebuild_image_offset(image_location, image_destination, split_offset, pixel_width):
    image = Image.open(image_location, 'r')

    pix_val = list(image.getdata())
    composite_list = [pix_val[x:x + 415] for x in range(0, len(pix_val), 415)]

    new_pixels = []
    split = split_offset
    for item in composite_list:
        part_one = item[0:split]
        part_two = item[split:pixel_width]

        for item_two in part_two:
            new_pixels.append(item_two)

        for item_one in part_one:
            new_pixels.append(item_one)

        split += 1

    create_image_from_rgb_list(image, new_pixels, image_destination)


rebuild_image_offset('example_image.png', 'cool_result.png', 116, 415)