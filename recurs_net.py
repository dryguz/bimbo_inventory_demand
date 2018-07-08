import tensorflow as tf


class MyRecNet:

    def __init__(self):
        self.data = None
        self.number_of_layers = 1
        self.stacked_lstm = None
        self.initial_state = None

    def load_data(self, data):
        self.data = data

    def set_layers(self, number_of_layers):
        self.number_of_layers = number_of_layers

        def lstm_cell(self):
            return tf.contrib.rnn.BasicLSTMCell(lstmsize)

        self.stacked_lstm = tf.contrib.rnn.MultiRNNCell(
            [lstm_cell() for _ in range(number_of_layers)]
        )
        return self.stacked_lstm

    def initialize(self, stacked_lstm):
        self.initial_state = state = stacked_lstm.zero_state(batch_size, tf.float32)



sess = tf.Session()

