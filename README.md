# 🦴 Avatar Bone Renamer

A Blender add-on for easily transferring bone names between two avatar armatures based on predefined avatar base mappings. Ideal for working with VRChat avatars or other avatar rigs that share similar bone hierarchies but use different naming conventions.

---

## ✨ Features

- Rename bones inside a single armature using mappings from one avatar base to another.
- Automatically apply hierarchical replacements using JSON templates.
- Convenient UI in the **3D Viewport Sidebar**.

---

## 📂 Installation

1. Download or clone this repository.
2. Open Blender.
3. Go to **Edit > Preferences > Add-ons**.
4. Click **Install...**, then select the `.zip` file or folder.
5. Enable **Avatar Bone Renamer** from the list.

---

## 🛠️ Usage

1. Open the **Sidebar (N)** in the **3D Viewport**.
2. Go to the **Bone Renamer** tab.
3. Choose an armature in your scene.
4. Select the **source avatar base** (current bone naming) and the **target avatar base** (desired naming).
5. Click **Transfer Bone Names**.

---

## ✅ Currently Supported Avatars

The following avatars have pre-defined JSON mapping files:

- **Manuka**
- **Airi**

These files live inside the `avatar_bones/` folder and define the bone hierarchies and naming conventions used for renaming.

---

## 🧪 Planned/Future Support

 - **Add more avatars**
 - **Add a way to be able to drag your own JSON**

## 🧠 Avatar Base Mappings

Mappings are stored as JSON files in the `avatar_bones/` folder.

Each file represents a base (e.g., `Manuka.json`, `Airi.json`) with a tree-like structure of bones.

### Example:
```json
"Hips": {
    "name": "Hips",
    "children": {
        "UpperLeg_L": {
            "name": "UpperLeg_L",
            "children": {
                "LowerLeg_L": {
                    "name": "LowerLeg_L",
                    "children": {
                        "Foot_L": {
                            "name": "Foot_L",
                            "children": {
                                // If there's no children you can just use a string directly instead of a dictionary
                                "Toe_L": "Toe_L" 
                            }
                        }
                    }
                }
            }
        },
        "UpperLeg_R": {
            "name": "UpperLeg_R",
            "children": {
                "LowerLeg_R": {
                    "name": "LowerLeg_R",
                    "children": {
                        "Foot_R": {
                            "name": "Foot_R",
                            "children": {
                                "Toe_R": "Toe_R"
                            }
                        }
                    }
                }
            }
        },
        "Spine": {
            "name": "Spine",
            "children": {
                "Chest": {
                    "name": "Chest",
                    "children": {
                        "Neck": {
                            "name": "Neck",
                            "children": {
                                "Head": "Head"
                            }
                        }
                    }
                }
            }
        }
    }
}
```

## Repository tree
```
./
├── 📁 avatar_bones
│   ├── 📄 {AVATAR}.json
│   └── 📄 example.json
├── 📄 __init__.py
├── 📄 avatars_data.py
├── 📄 operators.py
├── 📄 properties.py
├── 📄 ui.py
├── ℹ️ README.md
```
