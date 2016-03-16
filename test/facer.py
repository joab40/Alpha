import keylemon
from cv2 import *
api = keylemon.ApiClient(host="https://klws.keylemon.com",
                         user="joab40",
                         apikey="1tBdvyJOPy5gl9ivADIzITfdKGrptpv395GVU1hDb0Nff2Ntvxrydm")

# First, let's train a model
# See the Model creation section for more details
penelope_urls = (
    "http://81.236.28.170:8000/j5.jpg",
    "http://81.236.28.170:8000/j6.jpg",
    )

#penelope_urls = (
#    "http://www.keylemon.com/images/saas/penelope/Penelope_Cruz_1.jpg",
#    "http://www.keylemon.com/images/saas/penelope/Penelope_Cruz_2.jpg",
#    )

err, res = api.create_model(urls=','.join(penelope_urls))
print err
print res

if not err:
    model_id = res["model_id"]
    print "model works"

# Then to do a recognition test against this model:
# here, we're doing 1 image against 1 model but it's
# possible to do n images against n models.

my_image_to_test = "http://www.keylemon.com/images/saas/penelope/Penelope_Cruz_2.jpg"
my_image_to_test = "http://81.236.28.170:8000/j7.jpg"

# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    #waitKey(0)
    destroyWindow("cam-test")
    imwrite("../share/images/temp_detect/detect.jpg",img) #save image

with open("../share/images/temp_detect/detect.jpg", "r") as img_file:
    image_data = img_file.read()

#err, res = api.recognize_face(model_id, urls=my_image_to_test)
err, res = api.recognize_face(model_id, image_data=image_data)
if not err:
    result_for_face_1 = res["faces"][0]["results"][0]
    print "Test of face {} against model {} has a score of {}".format(
        res["faces"][0]["face_id"],
        result_for_face_1["model_id"],
        result_for_face_1["score"])