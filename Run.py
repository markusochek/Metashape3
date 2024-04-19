import Metashape
import os

print(Metashape.app.activated)
print()

doc = Metashape.Document()
doc.open("project.psz")
chunk = doc.chunk
directory = 'images'
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    chunk.addPhotos(file)

chunk.matchPhotos(downscale=1, generic_preselection=True, reference_preselection=False)
chunk.alignCameras()
chunk.buildDepthMaps(downscale=4, filter_mode=Metashape.AggressiveFiltering)
chunk.buildPointCloud()
chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation)
chunk.buildUV(mapping_mode=Metashape.GenericMapping)
chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=4096)
doc.save()
