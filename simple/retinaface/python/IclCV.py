"""
A IclCV demo using Icleague cv api.
"""

# -*- coding: utf-8 -*

import os
import sys
import cv2
import numpy as np
import sophon.sail as icl

class IclCV(object):
    """
    description: A IclCV class that warps Icleague cv oprations.
    """

    def __init__(self, tpu_id):
        """
        :param tpu_id: tpu id
        """
        # Create a Context on sophon device
        tpu_count = icl.get_available_tpu_num()
        print('{} TPUs Detected, using TPU {} \n'.format(tpu_count, tpu_id))
        self.engine = icl.Engine(tpu_id)
        self.handle = self.engine.get_handle()

        self.input_scale = 1.0
        self.input_w = 640
        self.input_h = 640
        self.img_dtype = icl.ImgDtype.DATA_TYPE_EXT_FLOAT32
        # input = icl.Tensor(self.handle, input_shape, input_dtype, False, False)
        # output = icl.Tensor(self.handle, output_shape, output_dtype, True, True)

        # create bmcv handle
        self.bmcv = icl.Bmcv(self.handle)

        self.ab_bgr = [x * self.input_scale for x in [1, -104, 1, -117, 1, -123]]
        # self.mean_bgr = (104, 117, 123)

    def preprocess_with_bmcv(self, bm_image):
        """
        description: preprocess the input bm_image, resize and pad it to target size,
                     normalize to [0,1],transform to NCHW format.
        param:
            bm_image: BMImage
        return:
            image:  the processed bm_image
            h: original height
            w: original width
        """

        # img_w = bm_image.width()
        # img_h = bm_image.height()

        resized_img = self.bmcv.vpp_resize(bm_image, self.input_w, self.input_h)
        self.bmcv.imwrite("resized_img.bmp", resized_img)

        input_img = icl.BMImage(self.handle, self.input_h, self.input_w,
                                           icl.Format.FORMAT_BGR_PLANAR, self.img_dtype)
        self.bmcv.convert_to(
            resized_img, input_img, \
            ((self.ab_bgr[0], self.ab_bgr[1]), (self.ab_bgr[2], self.ab_bgr[3]), (self.ab_bgr[4], self.ab_bgr[5])))

        return input_img

    def predict_bmimage(self, frame):

        if not isinstance(frame, type(None)):

            # Do image preprocess
            result_image = self.preprocess_with_bmcv(frame)
            
            return result_image


if __name__ == "__main__":
    device_id = 0
    icl_cv = IclCV(tpu_id=device_id)
    input_file = "retinaface/data/images/face1.jpg"
    frame = cv2.imread(input_file, 0)
    print("processing file: {}".format(input_file))
    if frame is not None:  # is picture file
        decoder = icl.Decoder(input_file, False, device_id)

        input_bmimg = icl.BMImage()
        ret = decoder.read(icl_cv.handle, input_bmimg)
        if ret:
            print("decode error\n")
            exit(-1)

        result_image = icl_cv.predict_bmimage(input_bmimg) # opt.use_np_file_as_input
        
        icl_cv.bmcv.imwrite("test_output.jpg", result_image)

    print("===================================================")
    # scp IclCV.py e00130@10.10.20.8:/home/e00130/workspace/project/BitMain/sophonsdk_v3.0_examples/sophon-ai-examples/simple/retinaface/python