# %% [markdown]
# # Let's do Teachable

# %% [markdown]
# Note: Teachable model file is only compatiable with Tensorflow 2.12. So use `==2.12` when you install tensorflow. 
# 
# ```
# # For GPU users
# pip install tensorflow[and-cuda]==2.12
# # For CPU users
# pip install tensorflow==2.12
# ```

# %% [markdown]
# ## Rock, Paper, Scissors

# %% [markdown]
# Let's try the sample code.

# %%
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

# %%
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# %%
# Load the model
model = load_model("model/keras_model.h5", compile=False)


# %%
# Load the labels
class_names = open("model/labels.txt", "r").readlines()


# %%
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# %%
# Replace this with the path to your image
# image = Image.open("test_images/scissors4-black-bg.png").convert("RGB")

# %%
# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)


# %%
import cv2
import time

# Open webcam
## To address the waring: 
## isPipelinePlaying OpenCV | GStreamer warning: GStreamer: pipeline have not been created
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Show the live camera image
        cv2.imshow('Live Camera', frame)

        # Convert frame to PIL Image
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized_image_array

        # Predict
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        print(f"Class: {class_name[2:].strip()} | Confidence: {confidence_score:.4f}")

        time.sleep(0.5)  # Adjust delay as needed

except KeyboardInterrupt:
    print("Stopped by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()


