import cv2
import numpy as np
def make_neon_image(input_image_path, output_image_path):
    img = cv2.imread("c:\Users\om441\Downloads\depositphotos_346019040-stock-illustration-hand-drawn-illustration-lord-shiva.jpg",cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("error")
        return
    _, thresh=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    height, width=thresh.shape
    neon_lines=np.zeros((height,width,3),dtype=np.uint8)
    neon_lines[thresh==255]=[255, 180, 0]

    blur_light = cv2.GaussianBlur(neon_lines,(5,5),0)
    blur_medium = cv2.GaussianBlur(neon_lines,(21,21),0)
    blur_strong = cv2.GaussianBlur(neon_lines,(41,41),0)

    glow_effect = cv2.addWeighted(neon_lines, 1.0, blur_light, 1.0, 0)
    glow_effect = cv2.addWeighted(glow_effect,1.0,blur_medium,0.8,0)
    glow_effect = cv2.addWeighted(glow_effect,1.0,blur_strong,0.4,0)

    cv2.imwrite(output_image_path, glow_effect)
    print("image save successfully",output_image_path)

input_file="c:\Users\om441\Downloads\depositphotos_346019040-stock-illustration-hand-drawn-illustration-lord-shiva.jpg"
output_file= "mahakal_neon_output.jpg"

make_neon_image(input_file,output_file)