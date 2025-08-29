import bpy
from . import avatar_data

class BONE_OT_TransferNames(bpy.types.Operator):
    bl_idname = "bone.transfer_names"
    bl_label = "Transfer Bone Names"
    bl_description = "Rename bones of the selected armature from one avatar base naming to another"

    def execute(self, context):
        props = context.scene.bone_renamer_props
        armature_name = props.target_armature
        from_base = props.from_avatar_base
        to_base = props.to_avatar_base

        if not armature_name or not from_base or not to_base:
            self.report({'ERROR'}, "Please select an armature and both bases")
            return {'CANCELLED'}

        arm_obj = bpy.data.objects.get(armature_name)
        if not arm_obj:
            self.report({'ERROR'}, "Armature not found")
            return {'CANCELLED'}

        from_hierarchy = avatar_data.AVATAR_BONE_HIERARCHY.get(from_base)
        to_hierarchy = avatar_data.AVATAR_BONE_HIERARCHY.get(to_base)

        if not from_hierarchy or not to_hierarchy:
            self.report({'ERROR'}, "Avatar base hierarchy missing")
            return {'CANCELLED'}

        from_root_key = next(iter(from_hierarchy))
        to_root_key = next(iter(to_hierarchy))

        def rename_bones_recursive(from_node, to_node):
            
            from_name = from_node if isinstance(from_node, str) else from_node.get("name")
            to_name = to_node if isinstance(to_node, str) else to_node.get("name")
            
            self.report({'INFO'}, f"Renaming bone '{from_name}' to '{to_name}'")
            
            bone = arm_obj.data.bones.get(from_name)
            if bone:
                bpy.context.view_layer.objects.active = arm_obj
                arm_obj.select_set(True)

                if bpy.context.object.mode != 'OBJECT':
                    bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.mode_set(mode='EDIT')

                edit_bone = arm_obj.data.edit_bones.get(from_name)
                if edit_bone:
                    edit_bone.name = to_name

                bpy.ops.object.mode_set(mode='OBJECT')

            from_children = from_node.get("children", {}) if isinstance(from_node, dict) else {}
            to_children = to_node.get("children", {}) if isinstance(to_node, dict) else {}
            
            # If children is a empty dict, we assume no children
            if not from_children and not to_children:
                self.report({'INFO'}, f"No children for '{from_name}' and '{to_name}' to process")
                return

            for key in from_children:
                if key in to_children:
                    rename_bones_recursive(from_children[key], to_children[key])
                else:
                    self.report({'WARNING'}, f"Child '{key}' from '{from_name}' not found in '{to_name}' hierarchy")

        rename_bones_recursive(from_hierarchy[from_root_key], to_hierarchy[to_root_key])

        self.report({'INFO'}, "Bone names transferred inside the armature")
        return {'FINISHED'}


