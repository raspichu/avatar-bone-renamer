import bpy

class BONE_PT_BoneRenamerPanel(bpy.types.Panel):
    bl_label = "Avatar bone renamer"
    bl_idname = "BONE_PT_bonerenamer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Bone Renamer'

    def draw(self, context):
        layout = self.layout
        props = context.scene.bone_renamer_props

        layout.prop(props, "target_armature", text="Armature")
        layout.prop(props, "from_avatar_base", text="From Base")
        layout.prop(props, "to_avatar_base", text="To Base")
        
        layout.separator()
        layout.label(text="Transfer Bone Names:")
        layout.operator("bone.transfer_names", icon='FILE_TICK', text="Transfer Names")
