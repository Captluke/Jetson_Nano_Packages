from jetcam.usb_camera import USBCamera
import ipywidgets
from IPython.display import display
from jetcam.utils import bgr8_to_jpeg
import traitlets


camera = USBCamera(capture_device=0)
image = camera.read()
print(image.shape)
print(camera.value.shape)

image_widget = ipywidgets.Image(format='jpeg')

image_widget.value = bgr8_to_jpeg(image)

display(image_widget)
camera.running = True

def update_image(change):
    image = change['new']
    image_widget.value = bgr8_to_jpeg(image)
    
camera.observe(update_image, names='value')
camera.unobserve(update_image, names='value')


camera_link = traitlets.dlink((camera, 'value'), (image_widget, 'value'), transform=bgr8_to_jpeg)
camera_link.unlink()
