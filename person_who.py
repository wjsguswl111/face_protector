import cv2
import fine_face
import face_recognition

#face_location = 튜플(top, right, bottom, left)
#내가 한거 = 시작점(startX, startY), 종료점(endX, endY)
#top = startY, right = endX, bottom = endY, left = startX

def who_person(self, frame):
    rgb = frame[:, :, ::-1]
    
    boxes = [fine_face.startY, fine_face.endX, fine_face.endY, fine_face.startX]

    encodings = face_recognition.face_encodings(rgb, boxes)

    faces = []
    for i, box in enumerate(boxes):
        face_image