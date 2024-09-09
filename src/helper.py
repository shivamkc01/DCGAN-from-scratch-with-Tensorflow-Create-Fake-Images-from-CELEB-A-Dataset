import os
import config

for path in os.listdir(config.full_image_train_path):
    if '.jpg' in path:
        config.all_image_path.append(os.path.join(config.full_image_train_path, path))


image_path_50k = config.all_image_path[0:500]
len(image_path_50k)
