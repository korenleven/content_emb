#!/bin/sh
LANG=en_US
export CUDA_VISIBLE_DEVICES=1
cp -r /mnt/smplify_x /bodyshop/smplify_x
cp /mnt/openpose_python.py /bodyshop/openpose_python.py
cp /mnt/conversions.py /usr/local/lib/python3.8/dist-packages/torchgeometry/core/
cd /bodyshop/openpose/build/examples/tutorial_api_python
rm openpose_python.py
cp /bodyshop/openpose_python.py .
cd /bodyshop

#Run the code with the relevant params
xvfb-run -a -s "-screen 0 1024x768x24 -ac +extension GLX +render -noreset" python main.py --config smplify_x/cfg_files/fit_smplx.yaml \
--data_folder /mnt/data/source_images --output_folder /mnt/data/source_smpl --visualize False --model_folder smplify_x/models \
--vposer_ckpt smplify_x/models/vposer_v1_0 --part_segm_fn smplify_x/models/smplx_parts_segm.pkl \
--op_image_dir /mnt/data/source_images/images --op_write_json /mnt/data/source_images/keypoints \
--op_main_dir openpose/build/examples/tutorial_api_python --op_hand True --op_face True --op_display 0 \
--op_render_pose 0 --gender male --single demo1.jpg
$SHELL

#--op_net_resolution 1024x736
