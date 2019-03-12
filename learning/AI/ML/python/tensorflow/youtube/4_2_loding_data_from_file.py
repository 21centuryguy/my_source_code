"""
https://docs.google.com/presentation/d/1WF5yphSXyzYLG8wmVvOpRmgAlw4vewbK51ZwLAOFZXk/edit#slide=id.g1ecff18dc7_0_323

https://github.com/hunkim/DeepLearningZeroToAll/blob/master/lab-04-3-file_input_linear_regression.py

https://github.com/hunkim/DeepLearningZeroToAll/blob/master/data-01-test-score.csv
"""


def main():

	# Lab 4 Multi-variable linear regression
	import tensorflow as tf
	import numpy as np
	tf.set_random_seed(777)  # for reproducibility

	xy = np.loadtxt('data-01-test-score.csv', delimiter=',', dtype=np.float32)
	x_data = xy[:, 0:-1]
	y_data = xy[:, [-1]]

	# Make sure the shape and data are OK
	print(x_data.shape, x_data, len(x_data))
	print(y_data.shape, y_data)

	# placeholders for a tensor that will be always fed.
	X = tf.placeholder(tf.float32, shape=[None, 3])
	Y = tf.placeholder(tf.float32, shape=[None, 1])

	W = tf.Variable(tf.random_normal([3, 1]), name='weight')
	b = tf.Variable(tf.random_normal([1]), name='bias')

	# Hypothesis
	hypothesis = tf.matmul(X, W) + b

	# Simplified cost/loss function
	cost = tf.reduce_mean(tf.square(hypothesis - Y))

	# Minimize
	optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
	train = optimizer.minimize(cost)

	# Launch the graph in a session.
	sess = tf.Session()
	# Initializes global variables in the graph.
	sess.run(tf.global_variables_initializer())

	# Launch the graph in a session
	sess = tf.Session()
	sess.run(tf.global_variables_initializer()) # Initializes golobal variables in the graph.

	for step in range(2001):
	    cost_val, hy_val, _ = sess.run(
	        [cost, hypothesis, train], feed_dict={X: x_data, Y: y_data})
	    if step % 10 == 0:
	        print(step, "Cost: ", cost_val, "\nPrediction:\n", hy_val)

	# Ask my scort
	print("Your score will be ", sess.run(hypothesis,
		feed_dict={X: [[100, 70, 101]]}))

	print("Other score will be ", sess.run(hypothesis,
		feed_dict={X: [[60, 70, 110], [90, 100, 80]]}))

	##################
	### debugging 

	def debugging():
		print(xy)
		print('\n')

		print(x_data)
		print('\n')

		print(y_data)
		print('\n')

		print("X's type", type(X))
		print('\n')

		print("Y's type", type(Y))
		print('\n')

	# debugging()

main()

