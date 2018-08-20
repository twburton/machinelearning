import pickle
from os import listdir
from PIL import Image as PImage

def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = PImage.open(path + image)
        loadedImages.append(img)

    return loadedImages

path = "C:/Users/twburton/Desktop/Machinelearning/trainingpics/"

# your images in an array
imgs = loadImages(path)

#for img in imgs:
    # you can show every image
    #img.show()

with open('C:/Users/twburton/Desktop/Machinelearning/trainingpics/data.pkl', 'wb') as f:
    pickle.dump(imgs, f)

    '''
# Write to file.
file = open("C:/Users/twburton/Desktop/Machinelearning/trainingpics/data.pkl", "wb")
for i in range(0, 58):
    pickle.dump("C:/Users/twburton/Desktop/Machinelearning/trainingpics/"+str(i)+".png", file)

file.close()

#with open('data.pkl', 'wb') as f:
    #pickle.dump(images, f)
   image = {
    'pixels': im.tostring(),
    'size': im.size,
    'mode': im.mode,
}'''
