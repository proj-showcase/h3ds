import os 
import cv2 
from PIL import Image, ImageSequence
import imageio
from pygifsicle import optimize
import numpy 

def extract():
    im = Image.open('./org_human_pose.mp4')
    out = './temp_sample/'
    cap = "human_pose"
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
    
def merg_seq_im():
    out = './temp_sample/'
    cap = "human_pose"
    _frame_files = sorted(
        [os.path.join(out, f) for f in os.listdir(out) if f.endswith('.png')]
    )

    frame_files = []
    for idx, ifiles in enumerate(_frame_files):
        frame_files.append(ifiles)
        if idx > 327: ## FRAME NEED APPEND
            for _idx in range(5):
                frame_files.append(ifiles)

    # Load first frame to get size
    frame = cv2.imread(frame_files[0])
    h, w, _ = frame.shape
    video = cv2.VideoWriter(f"{out}{cap}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 30, (w, h))

    for f in frame_files:
        frame = cv2.imread(f)
        video.write(frame)

    video.release()

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

def load():
    out = './temp_sample/'
    cap = cv2.VideoCapture("./org_bread_human_pose.mp4")
    frames = []

    index = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imwrite(f"{out}/frame_%d.png" % index, frame)
        frames.append(frame)
        index+=1
    cap.release()

    print(f"Loaded {len(frames)} frames.")


#load()
#extract()
merg_seq_im()
#test()





