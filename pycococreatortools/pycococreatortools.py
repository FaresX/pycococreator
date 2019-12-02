#!/usr/bin/env python3
# encoding=utf-8

from . import _pycococreatortools as _pct
from PIL import Image
import numpy as np
import json
import os
import datetime
import shutil
import random

def search_cates(anns_path):
    id = 0
    cate = []
    cates = []
    for i in os.listdir(anns_path):
        s = i.split("_")
        if s[3] not in cate:
            cate.append(s[3])
            cates.append(
                {
                    "id" : id,
                    "name" : s[3],
                    "supercategory" : s[2]
                }
            )
            id += 1
    return cates

def img_info(img_path, date_captured=datetime.datetime.utcnow().isoformat(' '),
                      license_id=1, coco_url="", flickr_url=""):
    s = os.path.basename(img_path)
    img_id = int(s.split(".")[0])
    width, height = Image.open(img_path).size
    img_info = _pct.create_img_info(img_id, os.path.basename(img_path), 
        width, height, date_captured=date_captured,
        license_id=license_id, coco_url=coco_url, flickr_url=flickr_url)

    return img_info
    
def imgs_info(imgs_path, date_captured=datetime.datetime.utcnow().isoformat(' '),
        license_id=1, coco_url="", flickr_url=""):

    imgs_info = []
    for i in os.listdir(imgs_path):
        try:
            imgs_info.append(img_info(imgs_path+"/"+i, date_captured=date_captured,
                license_id=license_id, coco_url=coco_url, flickr_url=flickr_url))
        except:
            print("路径中可能存在未按规定格式命名的文件")

    return imgs_info

def ann_info(ann_path, cate_dict, img_size=None, tolerance=2, bbox=None):
    s = os.path.basename(ann_path).split("_")
    img_id = int(s[0])
    ann_id = int(s[1])
    cate_id = [i["id"] for i in cate_dict if i["name"] == s[3]][0]
    iscrowd = int(s[4].split(".")[0])
    binary_mask = np.asarray(Image.open(ann_path).convert('1')).astype(np.uint8)
    ann_info = _pct.create_ann_info(ann_id, img_id, cate_id, iscrowd, binary_mask, 
        img_size=img_size, tolerance=tolerance, bbox=bbox)
    
    return ann_info

def anns_info(anns_path, cate_dict=None, img_size=None, tolerance=2, bbox=None):
    if not cate_dict:
        cate_dict = search_cates(anns_path)
    
    anns_info = []
    for i in os.listdir(anns_path):
        try:
            anns_info.append(ann_info(anns_path+"/"+i, cate_dict,
                img_size=img_size, tolerance=tolerance, bbox=bbox))
        except:
            print("路径中可能存在未按规定格式命名的文件")

    return anns_info

def tococo(imgs_path, anns_path, 
        info={"info":"info"}, licenses={"licenses":"licenses"}, categories=None):
    coco = {
        "info" : info,
        "licenses" : licenses,
        "categories" : categories,
        "images" : imgs_info(imgs_path),
        "annotations" : anns_info(anns_path)
    }

    return coco

def tococofile(imgs_path, anns_path, json_path,
        info={"info":"info"}, licenses={"licenses":"licenses"}, categories=None):
    coco = tococo(imgs_path, anns_path, 
        info=info, licenses=licenses, categories=categories)
    with open(json_path, "w") as output:
        json.dump(coco, output)

def cut2trte(imgs_path, anns_path, cut_path, cut_rate=0.7, rm=False):
    if os.path.isdir(cut_path):
        if rm:
            shutil.rmtree(cut_path)
        else:
            print(" 文件夹已存在，若需重新生成，请设置 rm=true")
            return
    os.makedirs(cut_path+"/train/images")
    os.makedirs(cut_path+"/train/annotations")
    os.makedirs(cut_path+"/test/images")
    os.makedirs(cut_path+"/test/annotations")
    imgs_path_list = os.listdir(imgs_path)
    anns_path_list = os.listdir(anns_path)
    n = len(imgs_path_list)
    ind = list(range(0, n))
    random.shuffle(ind)
    trn = int(round(cut_rate*n))
    for i in range(0, trn):
        imgi = imgs_path_list[ind[i]]
        img_id = imgi.split(".")[0]
        shutil.copyfile(anns_path+"/"+imgi, cut_path+"/train/images/"+imgi)
        for j in anns_path_list:
            if img_id == j.split("_")[0]:
                try:
                    shutil.copyfile(anns_path+"/"+j, cut_path+"/train/annotations"+j)
                except:
                    print("路径中可能存在未按规定格式命名的文件")
        
    for i in range(trn, n):
        imgi = imgs_path_list[ind[i]]
        img_id = imgi.split(".")[0]
        shutil.copyfile(imgs_path+"/"+imgi, cut_path+"/test/images/"+imgi)
        for j in anns_path_list:
            if img_id == j.split("_")[0]:
                try:
                    shutil.copyfile(anns_path_list+"/"+j, cut_path+"/test/annotations/"+j)
                except:
                    print("路径中可能存在未按规定格式命名的文件")