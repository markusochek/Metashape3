import Metashape
import os
import cv2

# cam = cv2.VideoCapture("video_2024-04-23_16-05-47.mp4")
# try:
#     if not os.path.exists('images/mouse'):
#         os.makedirs('images/mouse')
# except OSError:
#     print('Error: Creating directory of images/mouse')
#
# currentframe = 0
# while True:
#     ret, frame = cam.read()
#     if ret:
#         if currentframe % 40 == 0:
#             name = './images/mouse/frame' + str(currentframe) + '.jpg'
#             print('Creating...' + name)
#             cv2.imwrite(name, frame)
#         currentframe += 1
#     else:
#         break
# cam.release()
# cv2.destroyAllWindows()

print(Metashape.app.activated)
print()

# doc = Metashape.Document()
# chunk = doc.addChunk()
doc = Metashape.Document()
doc.open("project.psz")
chunk = doc.chunk

# directory = 'images/cup'
# i = 0
# for filename in os.listdir(directory):
#     if i % 3 == 0:
#         file = os.path.join(directory, filename)
#         chunk.addPhotos(file)
#     i = i + 1

chunk.matchPhotos(downscale=1, generic_preselection=True, reference_preselection=False)
# chunk.alignCameras()
# chunk.buildDepthMaps(downscale=4, filter_mode=Metashape.AggressiveFiltering)
# chunk.buildPointCloud()
# chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation)
# chunk.buildUV(mapping_mode=Metashape.GenericMapping)
# chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=4096)
doc.save("project.psz")
# doc.save()
