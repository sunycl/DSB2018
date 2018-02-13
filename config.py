# configure hyperparameters
n_epoch = 300
n_ckpt_epoch = 10
n_batch = 10
n_worker = 4
print_freq = 60
learn_rate = 0.0001
cv_ratio = 0.1
cv_seed = 666 # change it if different shuffle cv required 
width = 256 # model input size
cuda = True
threshold = 0.5 # possibility gating threshold
model_name = 'unet_iou_loss' # a name for log description
# data augmentation config
mean = [0.5, 0.5, 0.5] # per RGB channels
std  = [0.5, 0.5, 0.5]
label_to_binary = True
color_invert = False
color_jitter = True
elastic_distortion = True
color_equalize = False
# data cleanup
fill_holes = True
# dcan multitask threshold
threshold_sgmt = 0.5
threshold_edge = 0.7
# post-process config
post_segmentation = True
seg_ratio = 0.5
seg_scale = 0.55
post_remove_objects = True
min_object_size = 5