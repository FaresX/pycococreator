# pycococreator
生成实例分割的coco的json标注文件  
文件应具有以下格式  
  图片的命名：<image_id>.jpg(jpeg, ...)  
  标注掩模的命名：<image_id>_<ann_id>_<supercategory>_<category>_<iscrowd>.png(...)  
使用  
  imgs_info(imgs_path, [date_captured, license_id, coco_url, flickr_url])  
  anns_info(anns_path, [cate_dict, img_size, tolerance, bbox])                 (tolerance为掩模多边形化时的容忍度）  
  tococo(imgs_path, anns_path, [info, licenses, categories])  
  tococofile(imgs_path, anns_path, json_path, [info, licenses, categories])  
 如果需要个性化的定制可以在_pycococreatortools.py的更基本函数上进行  
  
