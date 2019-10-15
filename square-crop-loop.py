import os
import cv2

def main():
    outPath = '/home/hduser/Desktop/test2'
    path = '/home/hduser/Desktop/test'

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        '''
        # for loading color image
        img_to_crop = cv2.imread(input_path)
        height, width, channels = img_to_crop.shape
        '''
        # for loading grayscale image
        img_to_crop = cv2.imread(input_path, 0)
        height, width = img_to_crop.shape

        # new position for square image cropping
        upper_left = (int((width - height) / 2), 0)
        bottom_right = (int((width + height) / 2), height)

        # crop the image
        img_crop = img_to_crop[upper_left[1]:bottom_right[1], upper_left[0]:bottom_right[0]]

        # create full output path & save the file to disk
        fullpath = os.path.join(outPath, 'crop_'+image_path)
        cv2.imwrite(fullpath, img_crop)

if __name__ == '__main__':
    main()

'''
# view crop image in window. default WINDOW_AUTOSIZE
cv2.namedWindow('crop', cv2.WINDOW_NORMAL)
cv2.imshow('crop', img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

