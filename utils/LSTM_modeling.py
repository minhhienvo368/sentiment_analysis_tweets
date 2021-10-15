#Twitter Sentiment Analysis using Neural Networks

import os
import tensorflow
os.environ['KERAS_BACKEND'] = 'tensorflow'

import tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import LayerNormalization


import pandas as pd

# Load data
train_data = pd.read_csv('data/clean_train.csv')
test_data = pd.read_csv('data/clean_test.csv')

# Tokenization
tokenizer = Tokenizer(num_words = 2000, split = ' ')
tokenizer.fit_on_texts(train_data['Clean_tweet'].astype(str).values)
train_tweets = tokenizer.texts_to_sequences(train_data['Clean_tweet'].astype(str).values)
max_len = max([len(i) for i in train_tweets])
train_tweets = pad_sequences(train_tweets, maxlen = max_len)
test_tweets = tokenizer.texts_to_sequences(test_data['Clean_tweet'].astype(str).values)
test_tweets = pad_sequences(test_tweets, maxlen = max_len)

# Building the model
model = Sequential()
model.add(Embedding(2000, 128, input_length = train_tweets.shape[1]))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(256, dropout = 0.2))
model.add(Dense(2, activation = 'softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])
model.summary()

# Training the model
history = model.fit(train_tweets, pd.get_dummies(train_data['sentiment2']).values, epochs = 15, batch_size = 128, validation_split = 0.2)

# Testing the model
score, accuracy = model.evaluate(test_tweets, pd.get_dummies(test_data['sentiment2']).values, batch_size = 128)
print("Test accuracy: {}".format(accuracy))
