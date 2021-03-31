import cv2 as cv

net = cv.dnn.readNetFromTensorflow('apps/session/utils/graph_opt.pb')

BODY_PARTS = {"Nose": 0, "Neck": 1}


inWidth = 368  # Redimensionne l'image à la largeur souhaité
inHeight = 368  # Redimensionne l'image à la hauteur souhaité
thr = 0.2  # l'échelle pour le blob


def pose_estimation(frame):

    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]

    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                                      (127.5, 127.5, 127.5), swapRB=True, crop=False))

    out = net.forward()
    out = out[:, :2, :, :]

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        # Slice heatmap of corresponding body's part.
        heatMap = out[0, i, :, :]

        # Originally, we try to find all the local maximums. To simplify a sample
        # we just find a global one. However only a single pose at the same time
        # could be detected this way.
        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]

        # Add a point if it's confidence is higher than threshold.
        points.append((int(x), int(y)) if conf > thr else None)

    try:
        return points[1][1]
    except:
        return 0
