import os 
import cv2 
from PIL import Image, ImageSequence
import imageio
from pygifsicle import optimize
import numpy 

def extract():
    im = Image.open('./tfed_sample3/Modify_this_face,_changing_it_from_happiness_to_surprise.gif')
    out = './MODIFY/tfed_sample3/'
    cap = "Modify_this_face,_changing_it_from_happiness_to_surprise"
    index = 1
    vframes = []

    for frame in ImageSequence.Iterator(im):
        #frame.save(f"{out}/frame%d.png" % index)
        frame = Image.fromarray(numpy.uint8(frame.convert("RGB")))
        vframes.append(frame)
        index += 1

    print(index)
    for idx in range(5):
        #frame.save(f"{out}/frame%d.png" % (index + idx))
        frame = Image.fromarray(numpy.uint8(frame))
        vframes.append(frame)
        
    frame_one = vframes[0]
    out_name = os.path.join(out, f"{cap}.gif")
    frame_one.save(out_name, format="GIF", append_images=vframes, save_all=True, duration=100, loop=0) 
    

def reduce():
    im = Image.open('./TEST/page/Modify_this_face,_changing_it_this_face_from_fear_to_disgust.gif')
    out = './Change_this_face_from_disgust_to_happiness/frames/'
    index = 1
    frames = []
    for frame in ImageSequence.Iterator(im):
        frames.append(frame)
        index += 1

    out_name = "./TEST/page/s.gif"    
    frame_one = frames[0]
    print(len(frames))
    frame_one.save(out_name, format="GIF", append_images=frames, save_all=True, duration=100, loop=0) 
    

def test():
    im = imageio.mimread('./our_sample1/rome_rgb_Turn this face from fear to surprise.gif')
    
    frame = im[len(im)-1]
    print(len(im))
    for idx in range(10):
        im.append(frame)
    
    imageio.mimsave('./MODIFY/our_sample1/rome_rgb_Turn this face from fear to surprise/frames/output.gif', im)


extract()
#test()





