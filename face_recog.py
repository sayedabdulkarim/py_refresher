import face_recognition
import cv2

# known image
# known_image = face_recognition.load_image_file("PAN.jpeg")
known_image = face_recognition.load_image_file("Abdul.jpeg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# variables
face_locations = []
face_encodings = []
face_names = []

# Load an unknown image to recognize know faces as per above
# unknown_image = face_recognition.load_image_file("Abdul.jpeg")
unknown_image = face_recognition.load_image_file("me.jpg")
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

for face_encoding in face_encodings:
    matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
    name = "Unknown"

    if True in matches:
        name = "Known Person Name"

    face_names.append(name)

################# result
for (top, right, bottom, left), name in zip(face_locations, face_names):
    # Draw a rectangle around the face
    cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 0, 255), 2)

    # Draw a label with a name below the face
    cv2.rectangle(unknown_image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(unknown_image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

# display the image
cv2.imshow('Image', unknown_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
