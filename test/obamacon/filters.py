from PIL import Image

file_name = 'doge.jpg'
def load_img(file_name):
    img = Image.open(file_name)
    return img

def show_img(img_object):
    img_object = load_img(img_object)
    img_object.show()

def save_img(img_object, save_name):
    img_object.save(save_name)

load_img(file_name)
show_img(img_object)
save_img(img_object, save_name)
#return image object w filter
#def obamicon(img_object):
#   og_pix = img_obj.getdata()
 #   for i in og_pixels:
        