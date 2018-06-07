import glob
import numpy as np
import os
import shutil

def analysis_med(arr_path):
    target_arr = np.load(name).reshape(-1)
    zero_mount = target_arr[target_arr == 0].shape[0]
    nonzero_target_arr = np.delete(target_arr, np.where(target_arr == 0), axis=0)
    log_arr = np.log2(abs(nonzero_target_arr))
    matome = str(min(log_arr)) + ',' + str(max(log_arr)) + ',' + \
             str(np.median(log_arr)) + ',' + str(max(log_arr) - min(log_arr))
    return matome

if __name__ == '__main__':
    target_dir_path = 'graph/'
    result_path = 'analysis_med_result/'
    d_name_list = ['h0_conv_biases', 'h0_conv_w', 'h1_conv_biases', 'h1_conv_w', \
                   'h2_conv_biases', 'h2_conv_w', 'h3_conv_biases', 'h3_conv_w', 'h4_lin_bias_', 'h4_lin_Matrix']
    g_name_list = ['h0_lin_bias', 'h0_lin_Matrix', 'h1_biases', 'h1_w', \
                   'h2_biases', 'h2_w', 'h3_biases', 'h3_w', 'h4_biases', 'h4_w']

    print ('making directory...')
    if os.path.exists(result_path):
        if os.path.exists('bu_' + result_path):
            shutil.rmtree('bu_' + result_path)
            shutil.copytree(result_path, 'bu_' + result_path)
        else:
            shutil.copytree(result_path, 'bu_' + result_path)
        shutil.rmtree(result_path)
        os.mkdir(result_path)
        print ('remove past, made bu')
    else:
        os.mkdir(result_path)
        print ('made')

    print ('analysis D...')
    for d_name in d_name_list:
        fp_name = 'discriminator_d_' + d_name
        bp_name = 'grads_discriminator_d_' + d_name

        print ('fp')
        for name in sorted(glob.iglob(target_dir_path + fp_name + '_*')):
            iter_num = name.replace(target_dir_path + fp_name + '_', '').replace('.npy', '')
            txt_data = analysis_med(name)
            print (iter_num)
            with open(result_path + fp_name + '.txt', 'a') as f:
                f.write(iter_num + ',' + txt_data + '\n')

        print ('bp')
        for name in sorted(glob.iglob(target_dir_path + bp_name + '_*')):
            iter_num = name.replace(target_dir_path + bp_name + '_', '').replace('.npy', '')
            txt_data = analysis_med(name)
            print (iter_num)
            with open(result_path + bp_name + '.txt', 'a') as f:
                f.write(iter_num + ',' + txt_data + '\n')
    print ('analysis D... done!')

    print ('analysis G...')
    for g_name in g_name_list:
        fp_name = 'generator_g_' + g_name
        bp_name = 'grads_generator_g_' + g_name

        print ('fp')
        for name in sorted(glob.iglob(target_dir_path + fp_name + '_*')):
            iter_num = name.replace(target_dir_path + fp_name + '_', '').replace('.npy', '')
            txt_data = analysis_med(name)
            print (iter_num)
            with open(result_path + fp_name + '.txt', 'a') as f:
                f.write(iter_num + ',' + txt_data + '\n')

        print ('bp')
        for name in sorted(glob.iglob(target_dir_path + bp_name + '_*')):
            iter_num = name.replace(target_dir_path + bp_name + '_', '').replace('.npy', '')
            txt_data = analysis_med(name)
            print (iter_num)
            with open(result_path + bp_name + '.txt', 'a') as f:
                f.write(iter_num + ',' + txt_data + '\n')
    print ('analysis D... done!')

    #analysis_med(target_dir_path, result_path)
