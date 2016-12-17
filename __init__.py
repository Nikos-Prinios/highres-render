bl_info = {
    "name": "Highres-render",
    "author": "Nikos Priniotakis",
    "version": (1, 0),
    "blender": (2, 78, 0),
    "description": "Swap images to high resolution when rendering",
    "warning": "",
    "wiki_url": "",
    "category": "Render",
    }


import bpy
import os.path
from bpy.app.handlers import persistent
global images

images = []

@persistent
def turn_high(context):
    global images
    images = []
    for x in bpy.data.images:
        if 'low_' in x.filepath :
            images.append(x)
            high = x.filepath.replace('low_', '')
            x.filepath = high
            print(images)


@persistent           
def turn_low(context):
    global images
    for x in images:
        path = bpy.path.abspath(x.filepath)
        low = os.path.dirname(path)+ '/' +'low_'+ os.path.basename(path)
        if os.path.exists(low) :
            print('exists')
            x.filepath = low
            
            

def register():
    bpy.app.handlers.render_pre.append(turn_high)
    bpy.app.handlers.render_post.append(turn_low)


def unregister():
    bpy.app.handlers.render_pre.remove(turn_high)
    bpy.app.handlers.render_post.remove(turn_low)


if __name__ == "__main__":
    register()
