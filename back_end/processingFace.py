# 处理人脸
import base64
import csv

import cv2
import dlib
import numpy as np

# 加载人脸检测器
detector = dlib.get_frontal_face_detector()
# 关键点检测
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
# 人脸特征编码模型
encoder = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")


# 单张人脸处理
def singlePictureProcessing(mask):  # mask 前端传输的人脸数据
    # 检测人脸
    faces = detector(mask, 1)
    if len(faces) != 0:
        facesKeyPoints = [predictor(mask, face) for face in faces]  # 存储每张人脸的关键点
        return [np.array(encoder.compute_face_descriptor(mask, faces_keypoint, 1)) for faces_keypoint in
                facesKeyPoints][0]  # 取第一张人脸,并进行存储


# 得到的人脸存储进csv文件
def storageCsv(username, mask_csv):  # 注册的用户名以及它的人脸信息
    filename = './face/' + username + '.csv'
    with open(filename, 'a', newline='') as f:
        try:
            data = csv.writer(f, dialect='excel')
            data.writerow(mask_csv)
        except:
            pass


# 判断是否采集人脸数据是否达到标准
def judge(username):
    filename = './face/' + username + '.csv'
    with open(filename, 'r') as f:
        personal_list = []
        rete = csv.reader(f)
        for x in rete:
            x = [eval(k) for k in x]
            personal_list.append(x)
        if len(personal_list) > 25:
            return np.array(personal_list).mean(axis=0)
        else:
            return {'len': len(personal_list)}


# 参数1：从数据库取出存储的特征点
# 参数2：视屏中读取转换的特征点
# 欧式距离
def distance(face_encoding, test_encoding):
    try:
        return list(np.linalg.norm(np.array(face_encoding) - np.array(test_encoding), axis=1))
    except:
        pass


# 获取图片img
def obtainImg(result):
    img_data = base64.b64decode(result)
    img_array = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img


if __name__ == '__main__':
    print(judge('余俊雄'))
