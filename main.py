import cv2

# Load the pre-trained face detection cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize speaker detection model (not implemented in this example)
def detect_speakers(audio_data):
    # Placeholder implementation: Count the number of speakers as 2
    num_speakers = 2
    return num_speakers

def main():
    # Load the video
    video_path = r"C:\Users\savan\Desktop\Video_object_Detection\Sample.mp4"
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces using the Haarcascade classifier
        detected_faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Detect speakers using the placeholder implementation
        audio_data = None  # Placeholder for audio data extraction
        num_speakers = detect_speakers(audio_data)

        for (x, y, w, h) in detected_faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(frame, f"Faces: {len(detected_faces)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Speakers: {num_speakers}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
