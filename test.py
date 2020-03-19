from math import floor
from PIL import Image

fps = 32

source_img = Image.open("GG Python.jpg")

og_size = source_img.size

first_frame = [source_img.resize((round(og_size[0]*(1.5**4)), og_size[1])),
               source_img.resize((round(og_size[0]*(1.5**3)), og_size[1])),
               source_img.resize((round(og_size[0]*(1.5**2)), og_size[1])),
               source_img.resize((round(og_size[0]*(1.5**1)), og_size[1])),
               source_img,
               source_img.resize((round(og_size[0]*(0.5**1)), og_size[1])),
               source_img.resize((round(og_size[0]*(0.5**2)), og_size[1])),
               source_img.resize((round(og_size[0]*(0.5**3)), og_size[1])),
               source_img.resize((round(og_size[0]*(0.5**4)), og_size[1]))]

frames = [first_frame]

width_delta_steps = []

for i in range(len(first_frame)):
    width_delta_steps.append(floor((first_frame[i].size[0]-first_frame[-i-1].size[0])/(fps * 2)))

for frame in range(1, fps * 2):
    new_frame = []
    for i in range(9):
        previous_frame_image = frames[frame-1][i]
        previous_frame_image_size = previous_frame_image.size
        new_frame.append(source_img.resize((previous_frame_image_size[0]-width_delta_steps[i], previous_frame_image_size[1])))
    frames.append(new_frame)

frames_bis = [frames[-1]]

width_delta_steps_bis = []

for i in range(len(frames[-1])):
    width_delta_steps_bis.append(floor((first_frame[-i-1].size[0]-first_frame[i].size[0])/(fps * 2.35)))

for frame in range(1, fps * 2):
    new_frame = []
    for i in range(9):
        previous_frame_image = frames_bis[frame-1][i]
        previous_frame_image_size = previous_frame_image.size
        new_frame.append(source_img.resize((previous_frame_image_size[0]-width_delta_steps_bis[i], previous_frame_image_size[1])))
    frames_bis.append(new_frame)

frames += frames_bis

images = []

for frame in range(len(frames)):
    widths, heights = zip(*(i.size for i in frames[frame]))
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in frames[frame]:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save(f'frames_bis/{frame}.jpg')
    images.append(new_im)

images[0].save('ray_bis.gif', save_all=True, append_images=images[1:], optimize=False, duration=floor(1000/fps), loop=0)
