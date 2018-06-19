import glob
import numpy as np
import os
import shutil
def analysis_dr(arr_path):
    target_arr = np.load(name).reshape(-1)
    arr_max = max(abs(target_arr))
    arr_min = min(abs(target_arr[target_arr != 0]))
    return arr_min, arr_max, np.log2(arr_max/arr_min)



if __name__ == '__main__':
    target_dir_path = 'graph/'
    result_path = 'analysis_result/'
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
            arr_min, arr_max, arr_dr = analysis_dr(name)
            print (iter_num)
            with open(result_path + fp_name + '.txt', 'a') as f:
                f.write(iter_num + ',' + str(arr_min) + ',' + str(arr_max) + ',' + str(arr_dr) + '\n')

        print ('bp')
        for name in sorted(glob.iglob(target_dir_path + bp_name + '_*')):
            iter_num = name.replace(target_dir_path + bp_name + '_', '').replace('.npy', '')
            arr_min, arr_max, arr_dr = analysis_dr(name)
            print (iter_num)
            with open(result_path + bp_name + '.txt', 'a') as f:
                f.write(iter_num + ',' + str(arr_min) + ',' + str(arr_max) + ',' + str(arr_dr) + '\n')
    print ('analysis D... done!')

    print ('analysis G...')
    for g_name in g_name_list:
        fp_name = 'generator_g_' + g_name
        bp_name = 'grads_generator_g_' + g_name
        
        print ('fp')
        for name in sorted(glob.iglob(target_dir_path + fp_name + '_*')):
            iter_num = name.replace(target_dir_path + fp_name + '_', '').replace('.npy', '')
            arr_min, arr_max, arr_dr = analysis_dr(name)
            print (iter_num)
            with open(result_path + fp_name + '.txt', 'a') as f:
                f.write(iter_num + ',' + str(arr_min) + ',' + str(arr_max) + ',' + str(arr_dr) + '\n')

        print ('bp')
        for name in sorted(glob.iglob(target_dir_path + bp_name + '_*')):
            iter_num = name.replace(target_dir_path + bp_name + '_', '').replace('.npy', '')
            arr_min, arr_max, arr_dr = analysis_dr(name)
            print (iter_num)
            with open(result_path + bp_name + '.txt', 'a') as f:
                f.write(iter_num + ',' + str(arr_min) + ',' + str(arr_max) + ',' + str(arr_dr) + '\n')
    print ('analysis D... done!')

    #analysis_dr(target_dir_path, result_path)
