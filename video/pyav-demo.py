import av

# OpenCV 可用于解码视频，并提取帧数据：

input_file = "/Users/zhangqi/Documents/汇合人才/paxos.mp4"

container = av.open(input_file)
for frame in container.decode(video=0):
    frame.to_image().save(f"frame-{frame}.jpg")
