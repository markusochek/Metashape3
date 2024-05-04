import os

import Metashape
import cv2


def create_3d_modal(filename):
    doc = Metashape.Document()
    doc.save("project.psz")
    chunk = doc.addChunk()
    chunk.importVideo('videos/' + filename, 'images', custom_frame_step=5)
    # add_photos_in_chunk(chunk, 'images/' + filename)
    # chunk.matchPhotos(downscale=1, generic_preselection=True, reference_preselection=False)
    # chunk.alignCameras()
    # chunk.buildDepthMaps(downscale=4, filter_mode=Metashape.AggressiveFiltering)
    # chunk.buildPointCloud()
    # chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation)
    # chunk.buildUV(mapping_mode=Metashape.GenericMapping)
    # chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=4096)
    doc.save("project.psz")
    # chunk.exportModel(path='models/', ModelFormat=ModelFormatGLTF)
    # return  open('models/', 'r')


def add_photos_in_chunk(chunk, directory):
    for filename in os.listdir(directory):
        chunk.addPhotos(os.path.join(directory, filename))


def import_video(filename):
    cam = cv2.VideoCapture(filename)
    try:
        if not os.path.exists('images/mouse'):
            os.makedirs('images/mouse')
    except OSError:
        print('Error: Creating directory of images/mouse')

    currentframe = 0
    while True:
        ret, frame = cam.read()
        if ret:
            if currentframe % 40 == 0:
                name = './images/mouse/frame' + str(currentframe) + '.jpg'
                print('Creating...' + name)
                cv2.imwrite(name, frame)
            currentframe += 1
        else:
            break
    cam.release()
    cv2.destroyAllWindows()
