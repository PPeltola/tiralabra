from os.path import dirname
import pickle
#from UI import draw_image

CURRENT_DIR = dirname(__file__)
DATA_FOLDER = "/".join(CURRENT_DIR.split("/")[:-1]) + "/data/"
TRAINING_IMAGES = "train-images.idx3-ubyte"
TRAINING_LABELS = "train-labels.idx1-ubyte"
TEST_IMAGES = "t10k-images.idx3-ubyte"
TEST_LABELS = "t10k-labels.idx1-ubyte"

def read_images(which='train'):
    imgfile = TRAINING_IMAGES
    
    if which == 'test':
        imgfile = TEST_IMAGES

    with open(DATA_FOLDER + imgfile, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        amount = int.from_bytes(f.read(4), 'big')
        width = int.from_bytes(f.read(4), 'big')
        height = int.from_bytes(f.read(4), 'big')

        images = []
        for i in range(amount):
            images.append(__read_image(f, width, height))
        return images

def read_labels(which='train'):
    labelfile = TRAINING_LABELS

    if which == 'test':
        labelfile = TEST_LABELS
    
    with open(DATA_FOLDER + labelfile, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        amount = int.from_bytes(f.read(4), 'big')

        labels = []
        for i in range(amount):
            labels.append(int.from_bytes(f.read(1), 'big'))
        return labels

def save_image(i, name):
    import UI
    img = UI.draw_image(i)
    img.save(name + ".png")

def save_layer(layer, name):
    pickle.dump(layer, open(DATA_FOLDER + name + ".p", "wb"))

def load_layer(name):
    layer = pickle.load(open(DATA_FOLDER + name + ".p", "rb"))
    return layer
    
def __read_image(f, w=28, h=28):
    img = []
    for i in range(h):
        row = []
        for j in range(w):
            row.append(int.from_bytes(f.read(1), 'big'))
        img.append(row)
    return img