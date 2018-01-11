import matplotlib.pyplot as plt

losses =[0.1355, 0.1072, 0.1434, 0.0449, 0.0620, 0.0646, 0.0606, 0.0237, 0.0146, 0.0383, 0.0504, 0.0477, 0.0494, 0.0123, 0.0178]
plt.plot(losses)

plt.title("Training loss for fully convolutional network")
plt.xlabel("Epoches")
plt.xticks([0,3,6,9,15])
plt.ylabel('Training Loss')
plt.show()