# gym_trading/models.py
import tensorflow as tf
from tensorflow.keras import layers

class DQN(tf.keras.Model):
    def __init__(self, input_dim, output_dim, hidden_dim=128):
        super(DQN, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.hidden_dim = hidden_dim

        self.layer1 = layers.Dense(hidden_dim, activation='relu')
        self.layer2 = layers.Dense(hidden_dim, activation='relu')
        self.output_layer = layers.Dense(output_dim)

    def call(self, inputs):
        x = self.layer1(inputs)
        x = self.layer2(x)
        q_values = self.output_layer(x)
        return q_values
