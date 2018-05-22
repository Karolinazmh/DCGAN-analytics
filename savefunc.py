import matplotlib.pyplot as plt
import numpy as np
import pickle

def save_graph_params(params, epoch):
    fig = plt.figure(figsize=(20,10))
    i = 1
    w_maxes = [max(params['h0_w'].reshape(-1)), max(params['h1_w'].reshape(-1)), max(params['h2_w'].reshape(-1)), \
               max(params['h3_w'].reshape(-1)), max(params['h4_w'].reshape(-1))]
    w_width = max(w_maxes)
    w_range = [-w_width, w_width]
    b_maxes = [max(params['h0_b'].reshape(-1)), max(params['h1_b'].reshape(-1)), max(params['h2_b'].reshape(-1)), \
               max(params['h3_b'].reshape(-1)), max(params['h4_b'].reshape(-1))]
    b_width = max(b_maxes)
    b_range = [-b_width, b_width]
    plt.title("Weights and Biases Histgram : epoch "+str(epoch))
    with open('graph/params_data.txt', 'a') as f:
        f.write("epoch,abs_max,abs_min,abs_smin")
    for target in params:
        ax = plt.subplot(5,2,i)
        if i % 2 == 0:
            color = 'red'
            plt_range = b_range
        else:
            color = 'blue'
        plt_range = w_range
        data = params[target].reshape(-1)
        min_data = min(data)
        max_data = max(data)
        med_data = np.median(data)
        ave_data = np.average(data)
        var_data = np.var(data)
        tmp_data = data.copy()
        tmp_data[tmp_data == 0] = 1.0
        abs_min_data = min(abs(tmp_data))
        abs_max_data = max(abs(data))
        tmp2_data = tmp_data.copy()
        tmp2_data[tmp2_data == abs_min_data] = 1.0
        tmp2_data[tmp2_data == -abs_min_data] = 1.0
        abs_smin_data = min(abs(tmp2_data))
        with open('graph/params_data.txt', 'a') as f:
            f.write('\n' + str(epoch) + "," + str(abs_max_data) + ',' + str(abs_min_data) + ',' + str(abs_smin_data))
        bit_range = np.log2(abs_max_data/abs_min_data)
        binnum = 500
        data_info = 'num : ' + str(len(data)) + '\nmin : ' + str("%9.3e" % min_data) + '\nmax : ' + str("%9.3e" % max_data)\
                        + '\namin : ' + str("%9.3e" % abs_min_data) + '\namax : ' + str("%9.3e" % abs_max_data) + '\nrange : ' + str("%.2f" % bit_range) + '\nsmin : ' + str("%9.3e" % abs_smin_data)
        ax.hist(data,bins=binnum,range=plt_range, normed=1, alpha=1, color=color, label=str(target))
        # ax_yticklocs = ax.yaxis.get_ticklocs()
        # ax_yticklocs = list(map(lambda x: x * len(range(plt_range[0], plt_range[1]))*1.0/binnum, ax_yticklocs))
        # ax.yaxis.set_ticklabels(list(map(lambda x: "%0.2f" % x, ax_yticklocs)))
        # ax_pos = ax.get_position()
        ax.text(0.8 , 0.1, data_info, transform=ax.transAxes)
        ax.legend()
        i += 1
    plt.suptitle("Weights and Biases Histgram : epoch "+str(epoch))
    plt.savefig("graph/params" + str(epoch) + ".png")
    with open('graph/params_data.txt', 'a') as f:
        f.write('\n')
    #print ('saved'+str(epoch))
    #plt.show()]

def save_data_params(type, params, epoch):
    w_maxes = [max(params['h0_w'].reshape(-1)), max(params['h1_w'].reshape(-1)), max(params['h2_w'].reshape(-1)), \
               max(params['h3_w'].reshape(-1)), max(params['h4_w'].reshape(-1))]
    w_width = max(w_maxes)
    w_range = [-w_width, w_width]
    b_maxes = [max(params['h0_b'].reshape(-1)), max(params['h1_b'].reshape(-1)), max(params['h2_b'].reshape(-1)), \
               max(params['h3_b'].reshape(-1)), max(params['h4_b'].reshape(-1))]
    b_width = max(b_maxes)
    b_range = [-b_width, b_width]
    for target in params:
        plt_range = w_range
        data = params[target].reshape(-1)
        min_data = min(data)
        max_data = max(data)
        med_data = np.median(data)
        ave_data = np.average(data)
        var_data = np.var(data)
        tmp_data = data.copy()
        tmp_data[tmp_data == 0] = 1.0
        abs_min_data = min(abs(tmp_data))
        abs_max_data = max(abs(data))
        tmp2_data = tmp_data.copy()
        tmp2_data[tmp2_data == abs_min_data] = 1.0
        tmp2_data[tmp2_data == -abs_min_data] = 1.0
        abs_smin_data = min(abs(tmp2_data))
        with open('graph/' + type + '_params_abst_' + str(target) + '_' + str(epoch) +'.txt', 'a') as f:
            f.write(str(epoch) + "," + str(abs_max_data) + ',' + str(abs_min_data) + ',' + str(abs_smin_data) + '\n')
        np.save('graph/' + type + '_params_data_' + str(target) + '_' + str(epoch) +'.npy', params[target])
