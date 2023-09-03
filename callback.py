#creating a tensorboard callback
import datetime

def create_tensorboard_callback(dirname,experiment_name):
    log_dir=dirname+'/'+experiment_name+'/'+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback=tf.keras.callbacks.TensorBoard(log_dir=log_dir)
    return tensorboard_callback