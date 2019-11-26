import tensorflow as tf
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
tf.test.is_gpu_available(
    cuda_only=False,
    min_cuda_compute_capability=None
)