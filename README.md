# pycococreator
生成实例分割的coco的json标注文件  
  
文件应具有以下格式  
  
  图片的命名：<image_id>.jpg(jpeg, ...)  
  标注掩模的命名：<image_id>\_\<ann_id>\_\<supercategory>\_\<category>\_\<iscrowd>.png(...)  
    
使用  
    
  imgs_info(imgs_path, [date_captured, license_id, coco_url, flickr_url])  
  anns_info(anns_path, [cate_dict, img_size, tolerance, bbox])                 (tolerance为掩模多边形化时的容忍度）  
  tococo(imgs_path, anns_path, [date_captured, license_id, coco_url, flickr_url, img_size, tolerance, bbox, info, licenses, categories])  
  tococofile(imgs_path, anns_path, json_path, [date_captured, license_id, coco_url, flickr_url, img_size, tolerance, bbox, info, licenses, categories, rm])  
  cut2trte(imgs_path, anns_path, cut_path, [cut_rate, rm])  
  以上,rm为真将删除已存在的文件并重新创建
 如果需要个性化的定制可以在_pycococreatortools.py的更基本函数上进行  
   
安装
  
  pip install git+git://github.com/Faresx/pycococreator.git
