import zmq
import numpy as np
import pyzed.sl as sl

def main():
    # 初始化 ZED
    zed = sl.Camera()
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.coordinate_units = sl.UNIT.MILLIMETER
    if zed.open(init_params) != sl.ERROR_CODE.SUCCESS:
        print("无法打开ZED摄像头")
        return

    runtime_params = sl.RuntimeParameters()
    image = sl.Mat()

    # 初始化 ZeroMQ
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5555")  # 向本地发送图像数据

    print("ZED 发布中...")
    while True:
        if zed.grab(runtime_params) == sl.ERROR_CODE.SUCCESS:
            zed.retrieve_image(image, sl.VIEW.LEFT)
            frame = image.get_data()
            socket.send(frame.tobytes())  # 原始数据发送

if __name__ == "__main__":
    main()
