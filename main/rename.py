# Purpose:
# This file goes through all batches, renames, and sorts all nft files to a Complete_Collection folder in Blend_My_NFTs

import os
import bpy
import json
import shutil
import logging

from .helpers import remove_file_by_extension

log = logging.getLogger(__name__)


def rename_bones():
    for b in bpy.context.object.data.bones:
        b.name = b.name.replace("mixamorig", "DDanceRig")

def getChildren(myObject):
    children = []
    for ob in bpy.data.objects:
        if ob.parent == myObject:
            children.append(ob)
    return children

def rename_nft_collection(refactor_panel_input):

    rename_bones()

