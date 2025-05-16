import bpy

from mathutils import Euler, Matrix, Vector, Quaternion

rig_id = "P2D-TRIDENT-RIG-ALIVE"


class TRIDENT_PT_rigui(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'
    bl_label = "Rig UI"
    bl_idname = "TRIDENT_PT_rigui"

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        
        # pull in the properties from 'TRIDENT_properties' stored in the scene
        scn = context.scene
        trident_props = scn.trident_props
        # this is the property we are storing the on off state in
        tweak_mode = trident_props.show_tweaks
        tweak_icon = 'HIDE_ON' if not tweak_mode else 'HIDE_OFF'
        collection = context.active_object.data.collections_all


        row = col.row(align=True)
        row.prop(collection["Layer 9 - ROOT"],'is_visible',toggle=True, text='ROOT')
        row.operator("trident.tweaktoggle", emboss=True, text="", icon=tweak_icon)

        row = col.row(align=True)
        row.prop(collection["Layer 11 - TORSO"],'is_visible', toggle=True, text='TORSO')
        row.prop(collection["Layer 11 - TORSO"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)        
        if tweak_mode:
            row = col.row(align=True)
            row.prop(collection["Layer 12 - TORSO-TWEAK"],'is_visible', toggle=True, text='TORSO-TWEAK')
            row.prop(collection["Layer 12 - TORSO-TWEAK"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True) 

        row = col.row(align=True)
        row.prop(collection["Layer 7 - FACE"],'is_visible', toggle=True, text='FACE')
        row.prop(collection["Layer 7 - FACE"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
                
        if tweak_mode:
            row.prop(collection["Layer 8 - FACE-SECONDARY"],'is_visible', toggle=True, text='FACE-SECONDARY')
            row.prop(collection["Layer 8 - FACE-SECONDARY"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        
        row = col.row(align=True)
        row = col.row(align=True)
        row = col.row(align=True)
        row = col.row(align=True)
        row.prop(collection["Layer 17 - LEG-FK.L"],'is_visible', toggle=True, text='LEG-FK.L')
        row.prop(collection["Layer 17 - LEG-FK.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        row.prop(collection["Layer 20 - LEG-FK.R"],'is_visible', toggle=True, text='LEG-FK.R')
        row.prop(collection["Layer 20 - LEG-FK.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)


        row = col.row(align=True)
        row.prop(collection["Layer 18 - LEG-IK.L"],'is_visible', toggle=True, text='LEG-IK.L')
        row.prop(collection["Layer 18 - LEG-IK.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        row.prop(collection["Layer 21 - LEG-IK.R"],'is_visible', toggle=True, text='LEG-IK.R')
        row.prop(collection["Layer 21 - LEG-IK.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        
        
        if tweak_mode:
            row = col.row(align=True)
            row.prop(collection["Layer 19 - LEG-TWEAK.L"],'is_visible', toggle=True, text='LEG-TWEAK.L')
            row.prop(collection["Layer 19 - LEG-TWEAK.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
            row.prop(collection["Layer 22 - LEG-TWEAK.R"],'is_visible', toggle=True, text='LEG-TWEAK.R')
            row.prop(collection["Layer 22 - LEG-TWEAK.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)


        row = col.row(align=True)
        row.prop(collection["Layer 23 - ARM-FK.L"],'is_visible', toggle=True, text='ARM-FK.L')
        row.prop(collection["Layer 23 - ARM-FK.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        row.prop(collection["Layer 26 - ARM-FK.R"],'is_visible', toggle=True, text='ARM-FK.R')
        row.prop(collection["Layer 26 - ARM-FK.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        
        row = col.row(align=True)

        row.prop(collection["Layer 24 - ARM-IK.L"],'is_visible', toggle=True, text='ARM-IK.L')
        row.prop(collection["Layer 24 - ARM-IK.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        row.prop(collection["Layer 27 - ARM-IK.R"],'is_visible', toggle=True, text='ARM-IK.R')
        row.prop(collection["Layer 27 - ARM-IK.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        
        if tweak_mode:
            row = col.row(align=True)
            row.prop(collection["Layer 25 - ARM-TWEAK.L"],'is_visible', toggle=True, text='ARM-TWEAK.L')
            row.prop(collection["Layer 25 - ARM-TWEAK.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
            row.prop(collection["Layer 28 - ARM-TWEAK.R"],'is_visible', toggle=True, text='ARM-TWEAK.R')
            row.prop(collection["Layer 28 - ARM-TWEAK.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)

        row = col.row(align=True)
        row = col.row(align=True)
        row = col.row(align=True)
        row.prop(collection["Layer 29 - HAND.L"],'is_visible', toggle=True, text='HAND.L')
        row.prop(collection["Layer 29 - HAND.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        row.prop(collection["Layer 30 - HAND.R"],'is_visible', toggle=True, text='HAND.R')
        row.prop(collection["Layer 30 - HAND.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        
        if tweak_mode:
            row = col.row(align=True)
            row.prop(collection["Layer 31 - HAND-TWEAK.L"],'is_visible', toggle=True, text='HAND-TWEAK.L')
            row.prop(collection["Layer 31 - HAND-TWEAK.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
            row.prop(collection["Layer 32 - HAND-TWEAK.R"],'is_visible', toggle=True, text='HAND-TWEAK.R')
            row.prop(collection["Layer 32 - HAND-TWEAK.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)

        
        row = col.row(align=True)
        row = col.row(align=True)
        row = col.row(align=True)
        row = col.row(align=True)
        row.prop(collection["Layer 13 - LONG SWORD"],'is_visible', toggle=True, text='LONG SWORD')
        row.prop(collection["Layer 13 - LONG SWORD"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        row.prop(collection["Layer 14 - SPEAR"],'is_visible', toggle=True, text='SPEAR')
        row.prop(collection["Layer 14 - SPEAR"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        
        row = col.row(align=True)
        row.prop(collection["Layer 15 - SWORD.L"],'is_visible', toggle=True, text='SWORD.L')
        row.prop(collection["Layer 15 - SWORD.L"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)
        row.prop(collection["Layer 16 - SWORD.R"],'is_visible', toggle=True, text='SWORD.R')
        row.prop(collection["Layer 16 - SWORD.R"],'is_solo', text="", toggle=True, icon='SOLO_OFF', invert_checkbox=False, emboss=True)


# THIS IS ONLY THE PARENT PANEL FOR ALL THE SUB PANELS
class TRIDENT_PT_customprops(bpy.types.Panel):
    bl_category = 'Item'
    bl_label = "Rig Properties"
    bl_idname = "TRIDENT_PT_customprops"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw(self, context):
        layout = self.layout

# EACH SUB PANEL IS A CLASS
class TRIDENT_PT_arm_props(bpy.types.Panel):
    bl_label = "Arm Properties" 
    bl_idname = "TRIDENT_PT_arm_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "TRIDENT_PT_customprops" # this is the same for all it points to the main panel name
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'} # you may not want this? delete if not
    
    def draw(self, context):
        
        # get armature and "PROPERTIES" bone 
        arm = context.active_object
        bone = arm.pose.bones["PROPERTIES"]
        
        # basic layout setup
        layout = self.layout
        # just in we case want to change the split makes make a variable
        split_size = 0.7
        
        # then we start making rows        
        box = layout.box()
        col = box.column(align=True)
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        # this is just the label you could call it anything
        row.label(text='ARM FK-IK.L', translate=False)
        row = split.row(align=True)
        # this is the property > format is important
        row.prop(bone, '["ARM FK-IK.L"]', text = "", slider=True)
        
        # copy paste repeat... test as you go
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='ARM-IK-PARENT.L', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM-IK-PARENT.L"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='ARM-ROT-FOLLOW.L', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM-ROT-FOLLOW.L"]', text = "", slider=True)
        
        box = layout.box()
        col = box.column(align=True)
        row = col.row()     
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='ARM FK-IK.R', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM FK-IK.R"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='ARM-IK-PARENT.R', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM-IK-PARENT.R"]', text = "", slider=True)
        
        row = col.row() 
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)
        row.label(text='ARM-ROT-FOLLOW.R', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["ARM-ROT-FOLLOW.R"]', text = "", slider=True)     
        
class TRIDENT_PT_head_props(bpy.types.Panel):
    bl_label = "Head/Neck Properties" 
    bl_idname = "TRIDENT_PT_head_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "TRIDENT_PT_customprops"
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'} 
    
    def draw(self, context):
        arm = context.active_object
        bone = arm.pose.bones["PROPERTIES"]
        
        layout = self.layout
        split_size = 0.7
        
        box = layout.box()
        col = box.column(align=True)
        row = col.row()                
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='HEAD-FOLLOW', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["HEAD-FOLLOW"]', text = "", slider=True)  
        
        row = col.row()                
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='NECK-FOLLOW', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["NECK-FOLLOW"]', text = "", slider=True)  

class TRIDENT_PT_leg_props(bpy.types.Panel):
    bl_label = "Leg Properties" 
    bl_idname = "TRIDENT_PT_leg_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "TRIDENT_PT_customprops"
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'} 
    
    def draw(self, context):
        arm = context.active_object
        bone = arm.pose.bones["PROPERTIES"]
        
        layout = self.layout
        split_size = 0.7
        
        box = layout.box()
        col = box.column(align=True)
        row = col.row()             
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='LEG-FK-IK.L', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG-FK-IK.L"]', text = "", slider=True)  
        
        row = col.row()                    
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='LEG-PARENT.L', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG-PARENT.L"]', text = "", slider=True)  
        
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='LEG-ROT-FOLLOW.L', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG-ROT-FOLLOW.L"]', text = "", slider=True)  
              
        box = layout.box()
        col = box.column(align=True)
        row = col.row()           
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='LEG-FK-IK.R', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG-FK-IK.R"]', text = "", slider=True)   
        
        row = col.row()               
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='LEG-PARENT.R', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG-PARENT.R"]', text = "", slider=True)
                
        row = col.row()               
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='LEG-ROT-FOLLOW.R', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["LEG-ROT-FOLLOW.R"]', text = "", slider=True)
        
class TRIDENT_PT_weapon_props(bpy.types.Panel):
    bl_label = "Weapon Properties" 
    bl_idname = "TRIDENT_PT_weapon_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "TRIDENT_PT_customprops"
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'} 
    
    def draw(self, context):
        arm = context.active_object
        bone = arm.pose.bones["PROPERTIES"]
        
        layout = self.layout
        split_size = 0.7
        
        box = layout.box()
        col = box.column(align=True)
        row = col.row()         
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='SPEAR-PARENT', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["SPEAR-PARENT"]', text = "", slider=True)  
        
        row = col.row()               
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='SWORD-LONG-PARENT', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["SWORD-LONG-PARENT"]', text = "", slider=True)
        
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='SWORD.L-PARENT', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["SWORD.L-PARENT"]', text = "", slider=True)  
        
        row = col.row()           
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='SWORD.R-PARENT', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["SWORD.R-PARENT"]', text = "", slider=True)
        
        box = layout.box()
        col = box.column(align=True)
        row = col.row()              
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='WEAPON-EMIT', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["WEAPON-EMIT"]', text = "", slider=True)
        
        row = col.row()            
        split = row.split(align=True, factor=split_size)
        row = split.row(align=True)        
        row.label(text='WEAPON-SPAWN', translate=False)
        row = split.row(align=True)
        row.prop(bone, '["WEAPON-SPAWN"]', text = "", slider=True)


# ONLY USING THIS FOR THE TWEAK VISABLITY OPERATER NOW    
class TRIDENT_properties(bpy.types.PropertyGroup):      
    show_tweaks: bpy.props.BoolProperty(
    name="Tweak Mode", 
    description="Show/Hide Tweak controls/buttons", 
    default=False)

    
class TRIDENT_PT_vis_props(bpy.types.Panel):
    bl_label = "Visibility Properties" 
    bl_idname = "TRIDENT_PT_vis_props"
    bl_space_type = 'VIEW_3D'
    bl_parent_id = "TRIDENT_PT_customprops"
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        # object list (if you change object names it you will have to change these too)
        trident =  bpy.data.objects['Trident']
        spear =  bpy.data.objects['trident spear']
        sword_L =  bpy.data.objects['trident-sword.L']
        sword_R =  bpy.data.objects['trident-sword.R']
        sword_2_hand =  bpy.data.objects['trident-sword-2handed']
        
        # character modifiers use modifier names (if you change modifier names it you will have to change these too)
        mask_arms = trident.modifiers["MASK-ARMS"]
        mask_torso = trident.modifiers["MASK-TORSO"]
        mask_legs = trident.modifiers["MASK-LEGS"]
        
        # weapon modifiers use modifier names
        mask_spear = spear.modifiers["MASK"]
        mask_sword_L = sword_L.modifiers["MASK"]
        mask_sword_R = sword_R.modifiers["MASK"]
        mask_sword_2_hand = sword_2_hand.modifiers["MASK"]
        
        # start panel layout
        layout = self.layout
        layout.use_property_split = False
        layout.use_property_decorate = False 
        
        # character modifiers
        # if I didn't break it down above the code would be: (kinda messy)
        # row.prop(bpy.data.objects['Trident'].modifiers["MASK-TORSO"], 'show_viewport', text="", toggle = True, icon='HIDE_ON', emboss=False)             
        box = layout.box()
        col = box.column(align=True)
        row = col.row() 
        row.label(text='TORSO', translate=False)   
        row.prop(mask_torso, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
        
        row = col.row(align = True)  
        row.label(text='ARMS', translate=False)             
        row.prop(mask_arms, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
        
        row = col.row(align = True)     
        row.label(text='LEGS', translate=False)             
        row.prop(mask_legs, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
                
        # weapon modifiers   
        row = col.row()  
        row.label(text='SPEAR', translate=False)             
        row.prop(mask_spear, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
        
        row = col.row()    
        row.label(text='SWORD-L', translate=False)             
        row.prop(mask_sword_L, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
        
        row = col.row()    
        row.label(text='SWORD-R', translate=False)             
        row.prop(mask_sword_R, 'show_viewport', text="", icon='HIDE_ON', invert_checkbox=True, emboss=False)
        
        row = col.row()     
        row.label(text='SWORD-2-HANDED', translate=False)             
        row.prop(mask_sword_2_hand, 'show_viewport', icon='HIDE_ON', icon_only=True, invert_checkbox=True, emboss=False)
        

class TRIDENT_OT_tweak_mode(bpy.types.Operator):
    # Toggle All Selected Bones Deform Property
    bl_idname = "trident.tweaktoggle"
    bl_label = "Tweak Mode"
    bl_description = "Toggle tweak bones/buttons visibility"

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        # pull in the properties from 'TRIDENT_properties' stored in the scene
        scn = context.scene
        trident_props = scn.trident_props
        # this is the property we are storing the on off state in
        tweak_mode = trident_props.show_tweaks
        
        arm = context.active_object
        tweak_groups = ['09 - Theme Color Set']
                    
        for pbone in arm.pose.bones:
            #if it has a bone group 'name' and the name is in the list
            if hasattr( pbone.color.palette, "name") and pbone.color.palette.name in tweak_groups:
                if tweak_mode == True:
                    pbone.bone.hide = True        
                else:
                    pbone.bone.hide = False
                    trident_props.show_tweaks = True          
        
        # toggle the stored state            
        if tweak_mode:
            trident_props.show_tweaks = False
        
        else:
            trident_props.show_tweaks = True
        
        return {'FINISHED'}        
        

######################### Snap functions ############################

# returns final world matrix accounting for offset in rest pose
def get_matrix(armature, source_bone, target_bone):
    # rest post matrices
    source_bone_rest_matrix = source_bone.bone.matrix_local
    target_bone_rest_matrix = target_bone.bone.matrix_local

    # rest pose offset matrix
    offset_matrix = source_bone_rest_matrix.inverted() @ target_bone_rest_matrix

    # world_space_matrices
    source_world_matrix = source_bone.matrix

    #world space matrix
    matrix_final =  source_world_matrix @ offset_matrix
    
    return matrix_final

# returns pole location as matrix
def get_pole_matrix(chain_base, chain_mid, chain_end, widget):
    chain_base_head_v = chain_base.head
    chain_base_tail_v = chain_base.tail
    chain_mid_head_v = chain_mid.head
    chain_mid_tail_v = chain_mid.tail
    chain_end_head_v = chain_end.head
    chain_end_tail_v = chain_end.tail

    #midpoint
    midpoint = (chain_base_head_v + chain_end_head_v)/2

    #pole vector at origin
    pole_vector =  (chain_mid_head_v - midpoint).normalized()

    #extend distance by ik_widget rest length
    pole_vector_at_length = pole_vector*widget.bone.length

    #add vector to midpoint
    pole_vector_final = (pole_vector_at_length + midpoint)
    
    matrix_final = Matrix.Translation(pole_vector_final)
    
    return matrix_final

######################### Snap operators ############################        

class TRIDENT_OT_ik_fk_arm(bpy.types.Operator):
    bl_idname = "trident.ik_fk_arm"
    bl_label = ""
    bl_description = "Snap IK > FK"
    bl_options = {'UNDO', 'INTERNAL'}
    
    side: bpy.props.StringProperty(name="'L' or 'R'")

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        side = self.side
        armature = bpy.context.active_object
        pose_bones = armature.pose.bones
        properties = pose_bones['PROPERTIES']
        
        arm_ik_parent = properties[f'ARM-IK-PARENT.{side}'] == 1
        
        # IK BONES
        ik_hand = pose_bones[f'HAND-IK.{side}']
        ik_pole = pose_bones[f'ARM-POLE-IK.{side}']
        ik_widget = pose_bones[f'WGT-ARM-IK.{side}']

        # FK BONES
        fk_hand = pose_bones[f'HAND-FK.{side}']
        fk_forearm = pose_bones[f'FOREARM-FK.{side}']
        fk_arm = pose_bones[f'ARM-FK.{side}']
        
        select_set = (ik_hand, ik_pole, properties)    
            
        hand_matrix = get_matrix(armature, fk_hand, ik_hand)
        pole_matrix = get_pole_matrix(fk_arm, fk_forearm, fk_hand, ik_widget)

        ik_hand.matrix = hand_matrix
        ik_pole.matrix = pole_matrix
    
        # switch_mode   
        properties[f'ARM FK-IK.{side}'] = 1
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        # select bones and key if 'auto keyframe' enabled
        for pbone in select_set:
            armature.data.bones.active = pbone.bone

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                try:
                    bpy.ops.anim.keyframe_insert_menu(type='Available')
                except RuntimeError:
                    self.report({'WARNING'}, f'{pbone.name} has no active keyframes')
                    pass        
        
        return {'FINISHED'}
    

class TRIDENT_OT_fk_ik_arm(bpy.types.Operator):
    bl_idname = "trident.fk_ik_arm"
    bl_label = ""
    bl_description = "Snap FK > IK"
    bl_options = {'UNDO', 'INTERNAL'}
    
    side: bpy.props.StringProperty(name="'L' or 'R'")

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        side = self.side
        armature = bpy.context.active_object
        pose_bones = armature.pose.bones
        properties = pose_bones['PROPERTIES']
        
        # FK BONES
        fk_hand = pose_bones[f'HAND-FK.{side}']
        fk_forearm = pose_bones[f'FOREARM-FK.{side}']
        fk_arm = pose_bones[f'ARM-FK.{side}']
        
        # IK BONES
        ik_hand = pose_bones[f'HAND-IK.{side}']
        ik_forearm = pose_bones[f'MCH-IK-FOREARM.{side}']
        ik_arm = pose_bones[f'MCH-IK-ARM.{side}']
        
        select_set = (fk_hand, fk_forearm, fk_arm, properties) 
        
        hand_matrix = get_matrix(armature, ik_hand, fk_hand)
        forearm_matrix = get_matrix(armature, ik_forearm, fk_forearm)
        arm_matrix = get_matrix(armature, ik_arm, fk_arm)
        
        fk_arm.matrix = arm_matrix
        bpy.context.view_layer.update()        
        fk_forearm.matrix = forearm_matrix
        bpy.context.view_layer.update()
        fk_hand.matrix = hand_matrix
        bpy.context.view_layer.update()
        
        # switch_mode   
        properties[f'ARM FK-IK.{side}'] = 0        
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        for pbone in select_set:
            armature.data.bones.active = pbone.bone

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                try:
                    bpy.ops.anim.keyframe_insert_menu(type='Available')
                except RuntimeError:
                    self.report({'WARNING'}, f'{pbone.name} has no active keyframes')
                    pass        
        
        return {'FINISHED'}


class TRIDENT_OT_ik_fk_leg(bpy.types.Operator):
    bl_idname = "trident.ik_fk_leg"
    bl_label = ""
    bl_description = "Snap IK > FK"
    bl_options = {'UNDO', 'INTERNAL'}
    
    side: bpy.props.StringProperty(name="'L' or 'R'")

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        side = self.side
        armature = bpy.context.active_object
        pose_bones = armature.pose.bones
        properties = pose_bones['PROPERTIES']
        
        leg_ik_parent_state = properties[f'LEG-PARENT.{side}']
        
        # IK BONES
        ik_foot = pose_bones[f'FOOT-IK-MASTER.{side}']  
        
        ik_pole = pose_bones[f'LEG-POLE-IK.{side}']
        ik_widget = pose_bones[f'WGT-IK-POLE-LEG.{side}']

        # FK BONES
        fk_foot = pose_bones[f'FOOT-FK.{side}']
        fk_shin = pose_bones[f'SHIN-FK.{side}']
        fk_leg = pose_bones[f'LEG-FK.{side}']
        
        select_set = (ik_foot, ik_pole, properties)    
        
        foot_matrix = get_matrix(armature, fk_foot, ik_foot)
        pole_matrix = get_pole_matrix(fk_leg, fk_shin, fk_foot, ik_widget)
                   
        ik_foot.matrix = foot_matrix
        ik_pole.matrix = pole_matrix
        
        # switch_mode   
        properties[f'LEG-FK-IK.{side}'] = 1
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        # select bones and key if 'auto keyframe' enabled
        for pbone in select_set:
            armature.data.bones.active = pbone.bone

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                try:
                    bpy.ops.anim.keyframe_insert_menu(type='Available')
                except RuntimeError:
                    self.report({'WARNING'}, f'{pbone.name} has no active keyframes')
                    pass        
        
        return {'FINISHED'}    
    

class TRIDENT_OT_fk_ik_leg(bpy.types.Operator):
    bl_idname = "trident.fk_ik_leg"
    bl_label = ""
    bl_description = "Snap FK > IK"
    bl_options = {'UNDO', 'INTERNAL'}
    
    side: bpy.props.StringProperty(name="'L' or 'R'")

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
    
    def execute(self, context):
        side = self.side
        armature = bpy.context.active_object
        pose_bones = armature.pose.bones
        properties = pose_bones['PROPERTIES']
        
        # FK BONES
        fk_foot = pose_bones[f'FOOT-FK.{side}']
        fk_shin = pose_bones[f'SHIN-FK.{side}']
        fk_leg = pose_bones[f'LEG-FK.{side}']
        
        # IK BONES
        ik_foot = pose_bones[f'FOOT-IK-MASTER.{side}']
        ik_shin = pose_bones[f'MCH-IK-SHIN-FK.{side}']
        ik_leg = pose_bones[f'MCH-IK-LEG.{side}']
        
        select_set = (fk_foot, fk_shin, fk_leg, properties) 
        
        foot_matrix = get_matrix(armature, ik_foot, fk_foot)
        shin_matrix = get_matrix(armature, ik_shin, fk_shin)
        leg_matrix = get_matrix(armature, ik_leg, fk_leg)
        
        fk_leg.matrix = leg_matrix
        bpy.context.view_layer.update()        
        fk_shin.matrix = shin_matrix
        bpy.context.view_layer.update()
        fk_foot.matrix = foot_matrix
        bpy.context.view_layer.update()
        
        # switch_mode   
        properties[f'LEG-FK-IK.{side}'] = 0        
        
        bpy.ops.pose.select_all(action='DESELECT')
        
        for pbone in select_set:
            armature.data.bones.active = pbone.bone

            if bpy.context.scene.tool_settings.use_keyframe_insert_auto:
                try:
                    bpy.ops.anim.keyframe_insert_menu(type='Available')
                except RuntimeError:
                    self.report({'WARNING'}, f'{pbone.name} has no active keyframes')
                    pass        
        
        return {'FINISHED'}      
        
        
    
#################################################################################

class TRIDENT_PT_snap_panel(bpy.types.Panel):
    bl_category = 'Item'
    bl_label = "Snap Utilities"
    bl_idname = "TRIDENT_PT_snap_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        try:
            return (context.active_object.data.get("rig_id") == rig_id)
        except (AttributeError, KeyError, TypeError):
            return False
        
    def draw(self, context):
        layout = self.layout
        #box = layout.box()
        col = layout.column(align=True)
        row = col.row()
        row.operator("trident.ik_fk_arm", emboss=True, text="Arm L IK > FK", icon='SNAP_ON').side = 'L'
        row.operator("trident.ik_fk_arm", emboss=True, text="Arm R IK > FK", icon='SNAP_ON').side = 'R'
        
        row = col.row()
        row.operator("trident.fk_ik_arm", emboss=True, text="Arm L FK > IK", icon='SNAP_ON').side = 'L'
        row.operator("trident.fk_ik_arm", emboss=True, text="Arm R FK > IK", icon='SNAP_ON').side = 'R'
        
        col = layout.column(align=True)
        row = col.row()
        row.operator("trident.ik_fk_leg", emboss=True, text="Leg L IK > FK", icon='SNAP_ON').side = 'L'
        row.operator("trident.ik_fk_leg", emboss=True, text="Leg R IK > FK", icon='SNAP_ON').side = 'R'
        
        row = col.row()
        row.operator("trident.fk_ik_leg", emboss=True, text="Leg L FK > IK", icon='SNAP_ON').side = 'L'
        row.operator("trident.fk_ik_leg", emboss=True, text="Leg R FK > IK", icon='SNAP_ON').side = 'R'
                                            
#THE ORDER HERE DEFINES THE ORDER IN THE PANEL
classes = (TRIDENT_PT_rigui,
           TRIDENT_PT_snap_panel, 
           TRIDENT_PT_customprops,
           TRIDENT_PT_head_props,
           TRIDENT_PT_arm_props,
           TRIDENT_PT_leg_props,
           TRIDENT_PT_weapon_props,
           TRIDENT_PT_vis_props,
           TRIDENT_properties,
           TRIDENT_OT_tweak_mode,
           TRIDENT_OT_ik_fk_arm,
           TRIDENT_OT_fk_ik_arm,
           TRIDENT_OT_ik_fk_leg,
           TRIDENT_OT_fk_ik_leg,
           )

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.Scene.trident_props = bpy.props.PointerProperty(type=TRIDENT_properties)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
    
    del bpy.types.Scene.trident_props

if __name__ == "__main__":
    register()