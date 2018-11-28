import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

# a = tf.Variable( 1, name = "a" )
# b = tf.Variable( 2, name = "b" )
# f = a + b
# init = tf.global_variables_initializer()

# with tf.Session() as s :
# 	init.run()
# 	print( f.eval() )


session = tf.InteractiveSession()
mnist = input_data.read_data_sets( 'MNIST_data/', one_hot = True )

# Show image from training data.
def display_sample_image( intNumber ) :
	# Print one_hot array of this sample's label
	# print( mnist.train.labels[intNumber] )
	# Print its label by converting it to number
	# print( mnist.train.labels[intNumber].argmax( axis = 0 ) )
	numberLabel = mnist.train.labels[intNumber].argmax( axis = 0 )
	# Reshape 784 values to a 28*28 image
	numberImage = mnist.train.images[intNumber].reshape([28,28])
	plt.title( 'Sample : %d Label : %d' % ( intNumber, numberLabel ) )
	plt.imshow( numberImage, cmap = plt.get_cmap( 'gray_r' ) )
	plt.show()

# display_sample_image(100)

# Showing first 500 images from training data
# numberImages = mnist.train.images[0].reshape( [1,784] )

# for i in range( 1, 500 ) :
# numberImages = np.concatenate( ( numberImages, mnist.train.images[i].reshape( [1,784] ) ) )
# plt.imshow( numberImages, cmap = plt.get_cmap( 'gray_r' ) )
# plt.show()

# these input images and labels we will be assigning to trainign images and target labels
# while testing wl use test images and test labels instead.

input_images = tf.placeholder( tf.float32, shape = [None, 784] )
target_labels = tf.placeholder( tf.float32, shape = [None, 10] )

# Let's setup deep neural network
hidden_nodes = 512
input_weights = tf.Variable( tf.truncated_normal( [784, hidden_nodes] ) )
input_biases = tf.Variable( tf.zeros( [hidden_nodes] ) )

hidden_weights = tf.Variable( tf.truncated_normal( [hidden_nodes, 10] ) )
hidden_biases = tf.Variable( tf.zeros( [10] ) )

# Let's actual setup Neural Network
input_layer = tf.matmul( input_images, input_weights )
hidden_layer = tf.nn.relu( input_layer + input_biases )
digit_weights = tf.matmul( hidden_layer, hidden_weights ) + hidden_biases

# Let's compute loss function by comparing it with output of loss funtion i.e. digit weights with target labels
loss_function = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits_v2( logits = digit_weights, labels = target_labels ) )

# We'll now setup the gradient descent optimizer with learning rate of 0.5 and our loss function
optimizer = tf.train.GradientDescentOptimizer( 0.5 ).minimize( loss_function )

# Let's train our NN, before that let's methods to measure the accuracy
# Correct Prediction will look at the O/P of NN i.e. digit weights and label with highest value
# Accuracy is nothing but average of all correct predictions

correct_prediction = tf.equal( tf.argmax( digit_weights, 1 ), tf.argmax( target_labels, 1 ) )
accuracy = tf.reduce_mean( tf.cast( correct_prediction, tf.float32 ) )

# We'll start the session and initialize variables wl train NN with 2000 steps(or epochs) with batches of 100 samples from
# our training data, at each step wl assign the input images and target label place holders to training images and
# training labels.

# Once training is completed wl measure the accuracy of our model using the accuracy graph we defined above.
# While measuring accuracy wl assign input images and targt label place holders to test images and test labels.

tf.global_variables_initializer().run()

for x in range( 2000 ) :
	batch = mnist.train.next_batch( 100 )
	optimizer.run( feed_dict = {input_images : batch[0], target_labels : batch[1]} )
	if( 0 == ( x + 1 ) % 100 ) :
		print( "Training epoch " + str( x + 1) )
		print( "Accuracy: " + str( accuracy.eval( feed_dict = {input_images : mnist.test.images, target_labels : mnist.test.labels} ) ) )

# Let's test our model

for x in range( 100 ) :

	# Load single test image and its label
	x_test = mnist.test.images[x,:].reshape( 1, 784 )
	y_test = mnist.test.labels[x,:]
	# Convert one-hot label to integer
	label = y_test.argmax()
	# Get final layer's O/P digit weights and convert it to integer
	prediction = session.run( digit_weights, feed_dict = {input_images : x_test} ).argmax()
	# if prediction doesn't match label then display it
	if( prediction != label ) :
		plt.title( 'Prediction: %d Label : %d' % ( prediction, label ) )
		plt.imshow( x_test.reshape( [28,28] ), cmap = plt.get_cmap( 'gray_r' ) )
		plt.show()
