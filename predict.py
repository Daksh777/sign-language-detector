from keras.models import load_model
import operator
import cv2
from coordinates import click_event

loaded_model = load_model("model.h5")
print("Model loaded")

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

msg = ""
while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Region of interest
    cv2.rectangle(frame, (800, 100), (1230, 500), (255, 255, 255), 2)
    roi = frame[100:500, 800:1230]
    
    # Resizing the ROI so it can be fed to the model for prediction
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi = cv2.GaussianBlur(roi, (5, 5), 0)
    _, roi = cv2.threshold(roi, 125, 255, cv2.THRESH_OTSU)
    test_image = cv2.resize(roi, (64, 64)) 
    cv2.imshow("test", test_image)

    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
    prediction = {  
                    'A': result[0][0],
                    'B': result[0][1], 
                    'C': result[0][2], 
                    'D': result[0][3], 
                    'DEL': result[0][4],
                    'E': result[0][5], 
                    'F': result[0][6], 
                    'G': result[0][7], 
                    'H': result[0][8], 
                    'I': result[0][9], 
                    'J': result[0][10], 
                    'K': result[0][11], 
                    'L': result[0][12], 
                    'M': result[0][13], 
                    'N': result[0][14], 
                    'NOTHING': result[0][15],
                    'O': result[0][16], 
                    'P': result[0][17], 
                    'Q': result[0][18], 
                    'R': result[0][19], 
                    'S': result[0][20], 
                    'SPACE': result[0][21],
                    'T': result[0][22], 
                    'U': result[0][23], 
                    'V': result[0][24], 
                    'W': result[0][25], 
                    'X': result[0][26], 
                    'Y': result[0][27], 
                    'Z': result[0][28],
                    }
    # Sorting based on top prediction
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)

    cv2.putText(frame, "Predicted: "+prediction[0][0], (912, 532), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 2)

    interrupt = cv2.waitKey(1)

    if prediction[0][0] != "NOTHING":
        if prediction[0][0] == "SPACE":
            if interrupt & 0xFF == 122:
                msg += " "
        if prediction[0][0] == "DEL":
            if interrupt & 0xFF == 122:
                msg = msg[:-1]
        elif prediction[0][0] != "DEL" and prediction[0][0] != "SPACE":
            if interrupt & 0xFF == 122:
                msg += prediction[0][0]
    # Displaying the predictions
    cv2.putText(frame, "Sentence: "+msg, (50, 700), cv2.FONT_HERSHEY_PLAIN, 4, (0, 0, 0), 2) 
    cv2.imshow("Frame", frame)
    cv2.setMouseCallback("Frame", click_event)
   
    
    if interrupt & 0xFF == 27: # esc key
        break
        
 
cap.release()
cv2.destroyAllWindows()
