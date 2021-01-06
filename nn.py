import numpy as np

class NeuralNet:
	def __init__(self, inodes, hnodes, onodes, lr):
		self.inodes = inodes
		self.hnodes = hnodes
		self.onodes = onodes
		self.lr = lr

		self.wih = np.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
		self.who = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

	def sigmoid(self, x):
		return 1 / (1 + np.exp(x))

	def query(self, inputs):
		inputs = np.array(inputs, ndmin=2).T

		hidden_outputs = self.sigmoid(np.dot(self.wih, inputs))
		final_outputs = self.sigmoid(np.dot(self.who, hidden_outputs))

		return final_outputs

	def train(self, inputs, outputs):
		inputs = np.array(inputs, ndmin=2).T
		outputs = np.array(outputs, ndmin=2).T

		hidden_outputs = self.sigmoid(np.dot(self.wih, inputs))
		final_outputs = self.sigmoid(np.dot(self.who, hidden_outputs))

		output_errors = outputs - final_outputs
		hidden_errors = np.dot(self.who.T, output_errors)

		self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), hidden_outputs.T)
		self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), inputs.T)

		pass

# nn = NeuralNet(3, 5, 1, 0.3)

# inputs = np.array([
# 	[1, 0, 0],
# 	[0, 1, 0],
# 	[0, 0, 1],
# 	[0, 1, 1],
# 	[1, 1, 0]
# ])

# outputs = np.array([1, 0, 0, 0, 1], ndmin=2).T

# for i in range(10000):
# 	nn.train(inputs, outputs)

# print(nn.query(np.array([1, 0, 1])).T[0])