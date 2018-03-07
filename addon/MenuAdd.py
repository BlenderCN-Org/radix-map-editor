from bpy.types import Menu
from bpy.utils import register_class, unregister_class


menuStructure = [
  {
    "label": "Walls",
    "id": "menu_add_walls",
    "icon": 'MOD_BUILD',
    "action": [
      {
        "label": "Portalable",
        "icon": 'MESH_PLANE',
        "action": "radix.wall_add_portalable"
      },
      {
        "label": "Metal",
        "icon": 'META_PLANE',
        "action": "radix.wall_add_metal"
      }
    ]
  },
  {
    "label": "Volumes",
    "id": "menu_add_volumes",
    "icon": 'MOD_FLUIDSIM',
    "action": [
      {
        "label": "Acid",
        "icon": 'MESH_CUBE',
        "action": "radix.volume_add_acid"
      }
    ]
  },
  {
    "label": "Triggers",
    "id": "menu_add_triggers",
    "icon": 'MOD_SCREW',
    "action": [
      {
        "label": "Audio",
        "icon": 'MESH_CUBE',
        "action": "radix.trigger_add_audio"
      },
      {
        "label": "Map",
        "icon": 'MESH_CUBE',
        "action": "radix.trigger_add_map"
      },
      {
        "label": "Teleport",
        "icon": 'MESH_CUBE',
        "action": "radix.trigger_add_teleport"
      },
      {
        "label": "Checkpoint",
        "icon": 'MESH_CUBE',
        "action": "radix.trigger_add_checkpoint"
      },
      {
        "label": "Screen",
        "icon": 'MESH_CUBE',
        "action": "radix.trigger_add_screen"
      },
      {
        "label": "Remove",
        "icon": 'MESH_CUBE',
        "action": "radix.trigger_add_remove"
      },
      {
        "label": "Win",
        "icon": 'MESH_CUBE',
        "action": "radix.trigger_add_win"
      },
      {
        "label": "Death",
        "icon": 'MESH_CUBE',
        "action": "radix.trigger_add_death"
      },
      {
        "label": "Radiation",
        "icon": 'RADIO',
        "action": "radix.trigger_add_radiation"
      },
    ]
  },
  {
    "label": "Lights",
    "id": "menu_add_lights",
    "icon": 'LAMP_POINT',
    "action": [
      {
        "label": "Common light",
        "icon": 'LAMP_POINT',
        "action": "radix.add_light_common"
      },
      {
        "label": "End light",
        "icon": 'LAMP_POINT',
        "action": "radix.add_light_end"
      }
    ]
  },
  {
    "label": "Spawn points",
    "id": "menu_add_spawn_points",
    "icon": 'OUTLINER_OB_CAMERA',
    "action": [
      {
        "label": "Spawn",
        "icon": 'OUTLINER_OB_CAMERA',
        "action": "radix.camera_add_spawn"
      },
      {
        "label": "Destination",
        "icon": 'OUTLINER_OB_CAMERA',
        "action": "radix.camera_add_destination"
      }
    ]
  },
  {
    "label": "Radix",
    "id": "menu_add_pripary",
    "icon": 'WORLD',
    "action": [
      {
        "label": "Walls",
        "icon": 'MOD_BUILD',
        "action": "radix.menu_add_walls",
        "menu": True
      },
      {
        "label": "Volumes",
        "icon": 'MOD_FLUIDSIM',
        "action": "radix.menu_add_volumes",
        "menu": True
      },
      {
        "label": "Triggers",
        "icon": 'MOD_SCREW',
        "action": "radix.menu_add_triggers",
        "menu": True
      },
      {
        "label": "Lights",
        "icon": 'LAMP_POINT',
        "action": "radix.menu_add_lights",
        "menu": True
      },
      {
        "label": "Spawn points",
        "icon": 'OUTLINER_OB_CAMERA',
        "action": "radix.menu_add_spawn_points",
        "menu": True
      }
    ]
  }
]

dynamicMenus = []


class MenuBase(Menu):
  bl_idname = "radixMenu.base"
  bl_label = "Radix Base"

  actions = None

  def draw(self, context):
    if self.actions:
      layout = self.layout

      for item in self.actions:
        if "menu" in item:
          if item["menu"]:
            layout.menu(item["action"], text=item["label"], icon=item["icon"])
            continue

        layout.operator(item["action"], text=item["label"], icon=item["icon"])


def addDynamicMenu():
  for item in menuStructure:
    if isinstance(item["action"], list):
      operatorClass = type(
        'MenuDyn_' + item["id"],
        (MenuBase, ),
        {
          'bl_idname': "radix." + item["id"],
          'bl_label': item["label"],
          "actions": item["action"]
        }
      )
      dynamicMenus.append(operatorClass)
      register_class(operatorClass)


def clearDynamicMenu():
  for dynamicClass in dynamicMenus:
    unregister_class(dynamicClass)


def radix_add_menu(self, context):
  layout = self.layout

  layout.menu("radix.menu_add_pripary", icon='WORLD')
  layout.separator()
