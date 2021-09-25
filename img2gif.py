import imageio
import os
from tqdm import tqdm

def create_gif(image_list, gif_name, duration=0.35):
    frames = []
    for image_name in tqdm(image_list):
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return


def main():
    path = './fig'
    image_list = [os.path.join(path, i) for i in os.listdir(os.path.join(path)) if i.startswith('test') and i.endswith('.jpg')]
    for i in range(20):
        image_list.append(image_list[-1])
    # image_list = image_list[182:282]
    # image_list = ['cat/1.png', 'cat/2.png', 'cat/3.png', 'cat/4.png', 'cat/5.png', 'cat/6.png']
    gif_name = 'fig/feigang1.gif'
    duration = 0.05
    create_gif(image_list, gif_name, duration)


if __name__ == '__main__':
    main()