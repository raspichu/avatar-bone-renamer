import bpy
from . import avatar_data

def get_armature_names(self, context):
    return [(obj.name, obj.name, "") for obj in context.scene.objects if obj.type == 'ARMATURE']

def get_avatar_bases(self, context):
    return [(name, name, "") for name in avatar_data.AVATAR_BONE_HIERARCHY.keys()]

class BoneRenamerProperties(bpy.types.PropertyGroup):
    target_armature: bpy.props.EnumProperty(
        name="Target Armature",
        description="Select the armature to rename bones",
        items=get_armature_names
    )
    from_avatar_base: bpy.props.EnumProperty(
        name="From Base",
        description="Rename from this avatar base",
        items=get_avatar_bases
    )
    to_avatar_base: bpy.props.EnumProperty(
        name="To Base",
        description="Rename to this avatar base",
        items=get_avatar_bases
    )
