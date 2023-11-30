import tensorflow as tf
from tensorflow.keras import layers

class BTTRModel(tf.keras.Model):
    def __init__(self, vocab_size, max_seq_length, embedding_dim=128, num_heads=4, ff_dim=4, num_transformer_blocks=3):
        super(BTTRModel, self).__init__()

        self.embedding = layers.Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_seq_length)
        self.transformer_blocks = [TransformerBlock(embedding_dim, num_heads, ff_dim) for _ in range(num_transformer_blocks)]
        self.pooling = layers.GlobalAveragePooling1D()
        self.output_layer = layers.Dense(1, activation='sigmoid')

    def call(self, inputs):
        x = self.embedding(inputs)
        for transformer_block in self.transformer_blocks:
            x = transformer_block(x)
        x = self.pooling(x)
        return self.output_layer(x)

class TransformerBlock(layers.Layer):
    def __init__(self, embedding_dim, num_heads, ff_dim, rate=0.1):
        super(TransformerBlock, self).__init__()
        self.att = layers.MultiHeadAttention(num_heads=num_heads, key_dim=embedding_dim)
        self.ffn = tf.keras.Sequential([layers.Dense(ff_dim, activation='relu'), layers.Dense(embedding_dim)])
        self.layernorm1 = layers.LayerNormalization(epsilon=1e-6)
        self.layernorm2 = layers.LayerNormalization(epsilon=1e-6)
        self.dropout1 = layers.Dropout(rate)
        self.dropout2 = layers.Dropout(rate)

    def call(self, inputs):
        attn_output = self.att(inputs, inputs)
        attn_output = self.dropout1(attn_output)
        out1 = self.layernorm1(inputs + attn_output)
        ffn_output = self.ffn(out1)
        ffn_output = self.dropout2(ffn_output)
        return self.layernorm2(out1 + ffn_output)
