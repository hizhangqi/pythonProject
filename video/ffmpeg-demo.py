import ffmpeg
import os

# ffmpeg-python：封装 FFmpeg 命令行工具，适用于音视频解码、编码、剪辑等操作。

input_file = "/Users/zhangqi/Documents/汇合人才/paxos.mp4"
output_file = "/Users/zhangqi/Documents/汇合人才/audio.wav"

try:
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"输入文件不存在: {input_file}")

    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        raise FileNotFoundError(f"输出目录不存在: {output_dir}")

    ffmpeg.input(input_file).output(output_file, format='wav').run()
    print("转换成功！")
except Exception as e:
    print(f"发生错误: {e}")
