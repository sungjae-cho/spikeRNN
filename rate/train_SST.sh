python main.py \
--project spikeRNN --run Fig-S3-SST-run-01 \
--gpu 2 --gpu_frac 1.0 \
--n_trials 6000 --mode train \
--N 200 --P_inh 0.33 --som_N 20 --apply_dale True \
--gain 1.5 --task go-nogo --act sigmoid --loss_fn l2 \
--decay_taus 4 20 --output_dir outdir
