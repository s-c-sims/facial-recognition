import io
import os
import PySimpleGUI as sg
from PIL import Image
import cv2


fileTypes = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

face_cascade = cv2.CascadeClassifier('face_detector.xml')

layout = [
        [ sg.Image(key="-IMAGE-") ],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=fileTypes),
            sg.Button("Load Image"),
        ],
    ]   

def getFaces(file, name):
    img = cv2.imread(file)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y , w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imwrite(name, img)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def main():
    
    window = sg.Window("Upload Image", layout)
    
    while True:
        
        event, values = window.read()
        
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            
            filename = values["-FILE-"]
            
            getFaces(filename, 'faces_detected.png')
            
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())
         
    window.close()
    
if __name__ == "__main__":
    main()
