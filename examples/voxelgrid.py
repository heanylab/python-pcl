#port of
#http://pointclouds.org/documentation/tutorials/cylinder_segmentation.php
#you need to download
#http://svn.pointclouds.org/data/tutorials/table_scene_mug_stereo_textured.pcd

import pcl

cloud = pcl.load("table_scene_mug_stereo_textured.pcd")

print(cloud.size)

fil = cloud.make_voxel_grid_filter()
leaf_size = 0.02
fil.set_leaf_size(leaf_size, leaf_size, leaf_size)
cloud_filtered = fil.filter()

print(cloud_filtered.size)

cloud_filtered.to_file("table_scene_mug_stereo_textured_down.pcd")
