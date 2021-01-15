"""
根据给定的起始坐标点(x,y)左上点和宽高来裁切图像
"""
import os
from glob import glob
from tqdm import tqdm
from skimage import io
import shutil

if __name__ == '__main__':
    start_point = (400, 100)  # x,y top_left
    w, h = 400, 864

    images_dir = "/home/jaychen/Desktop/PycharmProjects/Completed_Project/GetMasks/datasets/Obay/output_image"
    masks_dir = "/home/jaychen/Desktop/PycharmProjects/Completed_Project/GetMasks/datasets/Obay/output_label"

    a = os.listdir(images_dir)
    b = os.listdir(masks_dir)
    assert len(a) == len(b)

    images_saved_dir = os.path.join(images_dir, "output")
    masks_saved_dir = os.path.join(masks_dir, "output")

    for s in [images_saved_dir, masks_saved_dir]:
        if not os.path.exists(s):
            os.makedirs(s)
        else:
            shutil.rmtree(s)
            os.makedirs(s)

    for image in glob(os.path.join(images_dir, "*.png")):
        cur_image_name = image.strip().split("/")[-1]
        cur_image = io.imread(image, as_gray=True)[start_point[1]:start_point[1] + h, start_point[0]:start_point[0] + w]
        cur_mask = io.imread(os.path.join(masks_dir, cur_image_name), as_gray=True)[start_point[1]:start_point[1] + h,
                   start_point[0]:start_point[0] + w]
        io.imsave(os.path.join(images_saved_dir, cur_image_name), cur_image)
        io.imsave(os.path.join(masks_saved_dir, cur_image_name), cur_mask)
