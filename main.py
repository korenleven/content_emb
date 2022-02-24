import os
import openpose.examples.tutorial_api_python.openpose_python as openpose_main
import smplify_x.smplifyx.main as smplx_main
import argparse
from smplify_x.smplifyx.cmd_parser import parse_config
import pickle

def main(smplx_args, openpose_args, op_main_dir):
    smplx_args['interpenetration'] = False
    current_dir = os.getcwd()
    os.chdir(os.path.join(current_dir, op_main_dir))
    openpose_main.main(**openpose_args)
    os.chdir(current_dir)
    smplx_main.main(**smplx_args)
   


if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    args = parser.parse_known_args()
    params = dict()
    smplx_args, openpose_args = parse_config(args[1])

    for i in range(len(openpose_args)):
        curr_item = openpose_args[i]
        if i != len(openpose_args) - 1:
            next_item = openpose_args[i + 1]
        else:
            next_item = "1"
        if "--" in curr_item and "--" in next_item:
            key = curr_item.replace('-', '')
            if key[3:] not in params:  params[key[3:]] = "1"
        elif "--" in curr_item and "--" not in next_item:
            key = curr_item.replace('-', '')
            if key[3:] not in params: params[key[3:]] = next_item

    if not os.path.exists(smplx_args['data_folder']):
         os.makedirs(smplx_args['data_folder'])
    
    op_main_dir = params['main_dir']
    del params['main_dir']
    main(smplx_args, params, op_main_dir)
    
    # data_folder_orig = smplx_args['data_folder']
    # output_folder_orig = smplx_args['output_folder']
    # image_dir_orig = params['image_dir']
    # write_json_orig = params['write_json']
    # for key in list(gender_dict.keys()):
    #     smplx_args['data_folder'] = data_folder_orig + '/' + key
    #     smplx_args['output_folder'] = output_folder_orig + '/' + key
    #     print(smplx_args['output_folder'])      
    #     if os.path.exists(smplx_args['output_folder']): continue
    #     params['image_dir'] = image_dir_orig + '/' + key
    #     params['write_json'] = write_json_orig[:-10] + '/' + key + write_json_orig[-10:]
    #     smplx_args['gender'] = gender_dict[key]
    #     main(smplx_args, params, op_main_dir)