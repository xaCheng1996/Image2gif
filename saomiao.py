import cv2
import os
import numpy as np

path = './fig'
img_1 = 'img_1.png'
img_2 = 'img_2.png'
# fig = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
# print(fig.size)
# fig = cv2.resize(fig, dsize = (494, 370))
# res = fig
for i in range(1, 370, 8):
    fig_1 = cv2.imread(os.path.join(path, img_1), cv2.IMREAD_UNCHANGED)
    fig_2 = cv2.imread(os.path.join(path, img_2), cv2.IMREAD_UNCHANGED)

    fig_1 = cv2.resize(fig_1, dsize=(490, 370))
    fig_2 = cv2.resize(fig_2, dsize=(490, 370))
    # print(fig_1.shape)
    # print(fig_2.shape)

    fig1_crop = fig_1[i:, :, 0:3]
    fig2_crop = fig_2[0:i, :,0:3]

    # print(fig1_crop.shape)
    # print(fig2_crop.shape)

    fig_f = np.concatenate([fig2_crop, fig1_crop ], axis=0)

    img_name = 'test_'+ '%03d'%(i) + ".jpg"
    # cv2.imshow('222',fig_1)
    cv2.line(fig_f, (0, i), (494, i), (0, 0, 255), 3)
    # cv2.imshow('111', fig_1)
    # fig_1 = res
    cv2.imshow('222', fig_f)
    cv2.waitKey(0)
    cv2.imwrite(os.path.join(path, img_name), fig_f)