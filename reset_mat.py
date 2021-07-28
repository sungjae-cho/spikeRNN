import pickle
import scipy.io

pkl_path = 'rate/outdir/models/go-nogo/P_rec_0.2_Taus_4.0_20.0/spikeRNN_Fig-S3-SST-run-01_Task_go-nogo_N_200_Taus_4.0_20.0_Act_sigmoid_2021_07_09_173315.pkl'
mat_path = pkl_path.replace('.pkl', '.mat')
with open(pkl_path, 'rb') as f:
    var = pickle.load(f)
scipy.io.savemat(mat_path, var)
