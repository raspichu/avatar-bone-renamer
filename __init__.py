bl_info = {
    "name": "Avatar bone renamer",
    "author": "Pichu",
    "version": (0, 4),
    "blender": (4, 4, 0),
    "location": "View3D > Sidebar > Bone Renamer",
    "description": "Copy avatar's humanoid bone names between two armatures based on avatar base mappings",
    "category": "Rigging",
}

import bpy

# Import individual classes or specifically from sub-modules
from .properties import BoneRenamerProperties
from .operators import BONE_OT_TransferNames
from .ui import BONE_PT_BoneRenamerPanel
from .avatar_data import load_avatar_hierarchies


classes = (
    BoneRenamerProperties,
    BONE_OT_TransferNames,
    BONE_PT_BoneRenamerPanel,
)


def register():
    load_avatar_hierarchies()
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.bone_renamer_props = bpy.props.PointerProperty(type=BoneRenamerProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.bone_renamer_props


if __name__ == "__main__":
    register()