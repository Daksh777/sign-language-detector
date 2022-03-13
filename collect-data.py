import cv2
import os
from coordinates import click_event

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    for i in "abcdefghijklmnopqrstuvwxyz":
        os.makedirs(f"data/train/{i}")
        os.makedirs(f"data/test/{i}")
    for i in ["del", "space", "nothing"]:
        os.makedirs(f"data/train/{i}")
        os.makedirs(f"data/test/{i}")
    

# Train or test 
mode = 'train'
directory = 'data/'+mode+'/'

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)

    
    # Getting count of existing images
    count = {"del":len(os.listdir(directory+'/del')), "space":len(os.listdir(directory+'/space')),"nothing":len(os.listdir(directory+'/nothing'))}
    for i in "abcdefghijklmnopqrstuvwxyz":
        count[i] = len(os.listdir(directory+'/'+i))


    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE: "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "A: "+str(count['a']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "B: "+str(count['b']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "C: "+str(count['c']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "D: "+str(count['d']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "E: "+str(count['e']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "F: "+str(count['f']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "G: "+str(count['g']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "H: "+str(count['h']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "I: "+str(count['i']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "J: "+str(count['j']), (10, 320), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "K: "+str(count['k']), (10, 340), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "L: "+str(count['l']), (10, 360), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "M: "+str(count['m']), (10, 380), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "N: "+str(count['n']), (10, 400), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "O: "+str(count['o']), (10, 420), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "P: "+str(count['p']), (10, 440), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Q: "+str(count['q']), (10, 460), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "R: "+str(count['r']), (10, 480), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "S: "+str(count['s']), (10, 500), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "T: "+str(count['t']), (10, 520), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "U: "+str(count['u']), (10, 540), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "V: "+str(count['v']), (10, 560), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "W: "+str(count['w']), (10, 580), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "X: "+str(count['x']), (10, 600), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Y: "+str(count['y']), (10, 620), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "Z: "+str(count['z']), (10, 640), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "DEL: "+str(count['del']), (10, 660), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "SPACE: "+str(count['space']), (10, 680), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)
    cv2.putText(frame, "NOTHING: "+str(count['nothing']), (10, 700), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,255), 1)

    # Region of interest
    cv2.rectangle(frame, (800, 100), (1230, 500), (255, 255, 255), 2)
    roi = frame[100:500, 800:1230]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.GaussianBlur(roi, (5, 5), 0)
    _, roi = cv2.threshold(roi, 150, 255, cv2.THRESH_OTSU)
    roi = cv2.resize(roi, (64, 64)) 
    cv2.imshow("Frame", frame)
    cv2.setMouseCallback("Frame", click_event)
    cv2.imshow("ROI", roi)

    interrupt = cv2.waitKey(1)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'a/'+str(count['a'])+'.jpg', roi)
    if interrupt & 0xFF == ord('b'):
            cv2.imwrite(directory+'b/'+str(count['b'])+'.jpg', roi)
    if interrupt & 0xFF == ord('c'):
            cv2.imwrite(directory+'c/'+str(count['c'])+'.jpg', roi)
    if interrupt & 0xFF == ord('d'):
            cv2.imwrite(directory+'d/'+str(count['d'])+'.jpg', roi)
    if interrupt & 0xFF == ord('e'):
            cv2.imwrite(directory+'e/'+str(count['e'])+'.jpg', roi)
    if interrupt & 0xFF == ord('f'):
            cv2.imwrite(directory+'f/'+str(count['f'])+'.jpg', roi)
    if interrupt & 0xFF == ord('g'):
            cv2.imwrite(directory+'g/'+str(count['g'])+'.jpg', roi)
    if interrupt & 0xFF == ord('h'):
            cv2.imwrite(directory+'h/'+str(count['h'])+'.jpg', roi)
    if interrupt & 0xFF == ord('i'):
            cv2.imwrite(directory+'i/'+str(count['i'])+'.jpg', roi)
    if interrupt & 0xFF == ord('j'):
            cv2.imwrite(directory+'j/'+str(count['j'])+'.jpg', roi)
    if interrupt & 0xFF == ord('k'):
            cv2.imwrite(directory+'k/'+str(count['k'])+'.jpg', roi)
    if interrupt & 0xFF == ord('l'):
            cv2.imwrite(directory+'l/'+str(count['l'])+'.jpg', roi)
    if interrupt & 0xFF == ord('m'):
            cv2.imwrite(directory+'m/'+str(count['m'])+'.jpg', roi)
    if interrupt & 0xFF == ord('n'):
            cv2.imwrite(directory+'n/'+str(count['n'])+'.jpg', roi)
    if interrupt & 0xFF == ord('o'):
            cv2.imwrite(directory+'o/'+str(count['o'])+'.jpg', roi)
    if interrupt & 0xFF == ord('p'):
            cv2.imwrite(directory+'p/'+str(count['p'])+'.jpg', roi)
    if interrupt & 0xFF == ord('q'):
            cv2.imwrite(directory+'q/'+str(count['q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('r'):
            cv2.imwrite(directory+'r/'+str(count['r'])+'.jpg', roi)
    if interrupt & 0xFF == ord('s'):
            cv2.imwrite(directory+'s/'+str(count['s'])+'.jpg', roi)
    if interrupt & 0xFF == ord('t'):
            cv2.imwrite(directory+'t/'+str(count['t'])+'.jpg', roi)
    if interrupt & 0xFF == ord('u'):
            cv2.imwrite(directory+'u/'+str(count['u'])+'.jpg', roi)
    if interrupt & 0xFF == ord('v'):
            cv2.imwrite(directory+'v/'+str(count['v'])+'.jpg', roi)
    if interrupt & 0xFF == ord('w'):
            cv2.imwrite(directory+'w/'+str(count['w'])+'.jpg', roi)
    if interrupt & 0xFF == ord('x'):
            cv2.imwrite(directory+'x/'+str(count['x'])+'.jpg', roi)
    if interrupt & 0xFF == ord('y'):
            cv2.imwrite(directory+'y/'+str(count['y'])+'.jpg', roi)
    if interrupt & 0xFF == ord('z'):
            cv2.imwrite(directory+'z/'+str(count['z'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
            cv2.imwrite(directory+'del/'+str(count['del'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
            cv2.imwrite(directory+'space/'+str(count['space'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
            cv2.imwrite(directory+'nothing/'+str(count['nothing'])+'.jpg', roi)
    
cap.release()
cv2.destroyAllWindows()