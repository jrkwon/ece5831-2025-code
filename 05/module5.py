from mnist_data import MnistData
import matplotlib.pyplot as plt

mnist_data = MnistData()
(_, _), (test_images, test_labels) = mnist_data.get_dataset()
img = test_images[500]
label = test_labels[500]
plt.imshow(img, cmap='gray')
print(label)
plt.show()
