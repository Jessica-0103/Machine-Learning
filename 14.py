# Jessica Chouhan 0827CI201087  import numpy as np import tensorflow as tf from tensorflow import keras from tensorflow.keras import layers   model = keras.Sequential()  
# Add an Embedding layer expecting input vocab of size 1000, and  # output embedding dimension of size 64.  model.add(layers.Embedding(input_dim=1000, output_dim=64))   # Add a LSTM layer with 128 internal units.  
model.add(layers.LSTM(128))  
  
# Add a Dense layer with 10 units.  
model.add(layers.Dense(10))  
  
model.summary() model = keras.Sequential() model.add(layers.Embedding(input_dim=1000, output_dim=64))   
# The output of GRU will be a 3D tensor of shape (batch_size, timesteps, 256) model.add(layers.GRU(256, return_sequences=True))   
# The output of SimpleRNN will be a 2D tensor of shape (batch_size, 128) model.add(layers.SimpleRNN(128))  
 model.add(layers.Dense(10))  
 
model. Summary()  

encoder_vocab = 1000 decoder_vocab = 2000
encoder_input = layers.Input(shape=(None,)) encoder_embedded = layers.Embedding(input_dim=encoder_vocab, output_dim=64)(     encoder_input  )

# Return states in addition to output output, state_h, state_c =
layers.LSTM(64, return_state=True, name="encoder")(     encoder_embedded
) encoder_state = [state_h, state_c]
decoder_input = layers.Input(shape=(None,)) decoder_embedded = layers.Embedding(input_dim=decoder_vocab, output_dim=64)(     decoder_input  )

# Pass the 2 states to a new LSTM layer, as initial state decoder_output = layers.LSTM(64, name="decoder")(     decoder_embedded, initial_state=encoder_state
) output =
layers.Dense(10)(decoder_output)
model = keras.Model([encoder_input, decoder_input], output) model.summary()
