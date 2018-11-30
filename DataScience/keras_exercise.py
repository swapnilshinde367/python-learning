import keras
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.layers import Dense, Dropout

(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = mnist.load_data()

train_images	= mnist_train_images.reshape( 60000, 784 )
test_images		= mnist_test_images.reshape( 10000, 784 )
train_images	= train_images.astype( 'float32' )
test_images		= test_images.astype( 'float32' )
train_images = train_images / 255
test_images = test_images / 255

# convert labels from 0-9 laels to on_hot format
train_labels = keras.utils.to_categorical( mnist_train_labels, 10 )
test_labels = keras.utils.to_categorical( mnist_test_labels, 10 )

def display_sample_number( intNumber ) :
	# one_hot array
	print( test_labels[intNumber] )
	# label
	label = train_labels[intNumber].argmax( axis = 0 )
	# image
	image = train_images[intNumber].reshape( [28,28] )
	plt.title('Sample: %d  Label: %d' % ( intNumber, label ) )
	plt.imshow( image, cmap = plt.get_cmap( 'gray_r' ) )
	plt.show()

# display_sample_number(100)

# Let's setup our model / NN
# Feeding 784 features into ReLu layer of 512 nodes which then goes into 10 node with softmax

model = Sequential()
model.add( Dense( 512, activation = 'relu', input_shape = ( 784, ) ) )
model.add( Dense( 10, activation = 'softmax' ) )

# Using Keras' given standard example

# model = Sequential()
# model.add(Dense(512, activation='relu', input_shape=(784,)))
# model.add(Dropout(0.2))
# model.add(Dense(512, activation='relu'))
# model.add(Dropout(0.2))
# model.add(Dense(10, activation='softmax'))

model.summary()

# Wl set up optimizer and loss function
model.compile( loss = 'categorical_crossentropy',
				optimizer = RMSprop(),
				metrics = ['accuracy'] )

# Let's train model with 10 epochs and 100 as batch size
history = model.fit( train_images, train_labels,
					batch_size = 100,
					epochs = 10,
					verbose = 2,
					validation_data = ( test_images, test_labels ) )

score = model.evaluate( test_images, test_labels, verbose = 0 )
print( 'Test Loss : ', score[0] )
print( 'Test Accuracy : ', score[1] )

# Let's test few samples
for x in range( 100 ) :
	test_image = test_images[x,:].reshape( 1, 784 )
	predicted_cat = model.predict( test_image ).argmax()
	label = test_labels[x].argmax()
	if( predicted_cat != label ) :
		plt.title( 'Prediction: %d, Label: %d' % ( predicted_cat, label ) )
		plt.imshow( test_image.reshape( [28,28] ), cmap = plt.get_cmap( 'gray_r' ) )
		plt.show()