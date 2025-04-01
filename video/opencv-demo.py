import cv2

# PyAV：基于 FFmpeg 的 Python 库，提供更高效的音视频处理能力。

input_file = "/Users/zhangqi/Documents/汇合人才/paxos.mp4"

cap = cv2.VideoCapture(input_file)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Frame", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

