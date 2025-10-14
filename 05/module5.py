from mnist_data import MnistData
import matplotlib.pyplot as plt

mnist_data = MnistData()
(_, _), (test_images, test_labels) = mnist_data.get_dataset()
# get two test images and labels
test1 = test_images[3]
test2 = test_images[8]
label1 = test_labels[3]
label2 = test_labels[8]

# Let's plot the test images
plt.subplot(1, 2, 1)
plt.imshow(test1, cmap='gray')
plt.title(f"Label: {label1}")
plt.subplot(1, 2, 2)
plt.imshow(test2, cmap='gray')
plt.title(f"Label: {label2}")
plt.show()
