import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasClassifier

feature_names = ['party','handicapped-infants', 'water-project-cost-sharing',
					'adoption-of-the-budget-resolution', 'physician-fee-freeze',
					'el-salvador-aid', 'religious-groups-in-schools',
					'anti-satellite-test-ban', 'aid-to-nicaraguan-contras',
					'mx-missle', 'immigration', 'synfuels-corporation-cutback',
					'education-spending', 'superfund-right-to-sue', 'crime',
					'duty-free-exports', 'export-administration-act-south-africa']

voting_data = pd.read_csv( 'house-votes-84.data.txt', na_values = ['?'], names = feature_names )
# print (voting_data.describe())
voting_data.dropna( inplace = True )
# print (voting_data.describe())
voting_data.replace( ( 'y', 'n' ), ( 1, 0 ), inplace = True )
voting_data.replace( ( 'democrat', 'republican' ), ( 1, 0 ), inplace = True )
# print (voting_data.head(10))

all_features = voting_data[feature_names].drop( 'party', axis = 1 ).values
all_classes = voting_data['party'].values

# print(all_classes)
# print(all_features)

def create_model() :
	model = Sequential()
	# 16 features going in 32-unit layer of neuron(unit)
	model.add( Dense( 32, input_dim = 16, kernel_initializer = 'normal', activation = 'relu' ) )
	# adding hidden layer 16 units
	model.add( Dense( 16, kernel_initializer = 'normal', activation = 'relu' ) )
	# output layer of binary classification( Democrat or Republican Party )
	model.add( Dense( 1, kernel_initializer = 'normal', activation = 'sigmoid' ) )
	# compile model
	model.compile( loss = 'binary_crossentropy',
					optimizer = 'rmsprop',
					metrics = ['accuracy'] )
	# print(model.summary())

	return model

# wrap keras model in an estimator compatible with scikit_learn

estimator = KerasClassifier( build_fn = create_model, nb_epoch = 100, verbose = 0 )

# sci kit learns's cross val score to evaluate model
cv_scores = cross_val_score( estimator, all_features, all_classes, cv = 10 )
print(cv_scores.mean())
