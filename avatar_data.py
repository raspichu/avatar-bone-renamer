import os
import json
import bpy

AVATAR_BONE_HIERARCHY = {}

def load_avatar_hierarchies():
    global AVATAR_BONE_HIERARCHY
    
    print("Loading avatar bone hierarchies...")

    addon_dir = os.path.dirname(os.path.abspath(__file__))
    avatar_folder = os.path.join(addon_dir, "avatar_bones")
    
    AVATAR_BONE_HIERARCHY.clear()
    
    if not os.path.exists(avatar_folder):
        print(f"Avatar bones folder not found: {avatar_folder}")
        return
    
    for filename in os.listdir(avatar_folder):
        if filename.endswith(".json") and filename != 'sample.json':
            path = os.path.join(avatar_folder, filename)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    
                    name = os.path.splitext(filename)[0]
                    AVATAR_BONE_HIERARCHY[name] = data
                except Exception as e:
                    print(f"Failed to load {filename}: {e}")
