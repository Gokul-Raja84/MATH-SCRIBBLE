import tensorflow as tf

def create_dataset(X, y, batch_size=32, shuffle=True):
    dataset = tf.data.Dataset.from_tensor_slices((X, y))
    if shuffle:
        dataset = dataset.shuffle(buffer_size=len(X))
    dataset = dataset.batch(batch_size)
    return dataset

def train_bttr_model(model, train_dataset, val_dataset, epochs=5, learning_rate=1e-3):
    optimizer = tf.keras.optimizers.Adam(learning_rate)
    loss_function = tf.keras.losses.BinaryCrossentropy()

    model.compile(optimizer=optimizer, loss=loss_function, metrics=['accuracy'])
    model.summary()

    history = model.fit(train_dataset, validation_data=val_dataset, epochs=epochs)
    return history

if __name__ == "__main__":
    # Example usage
    vocab_size = 10000
    max_seq_length = 256
    embedding_dim = 128
    num_heads = 4
    ff_dim = 4
    num_transformer_blocks = 3

    model = BTTRModel(vocab_size, max_seq_length, embedding_dim, num_heads, ff_dim, num_transformer_blocks)

    # Replace the following with your actual training data
    X_train = tf.random.uniform((1000, max_seq_length), minval=0, maxval=vocab_size, dtype=tf.int32)
    y_train = tf.random.uniform((1000, 1), minval=0, maxval=2, dtype=tf.int32)
    X_val = tf.random.uniform((200, max_seq_length), minval=0, maxval=vocab_size, dtype=tf.int32)
    y_val = tf.random.uniform((200, 1), minval=0, maxval=2, dtype=tf.int32)

    train_dataset = create_dataset(X_train, y_train)
    val_dataset = create_dataset(X_val, y_val)

    train_bttr_model(model, train_dataset, val_dataset, epochs=5, learning_rate=1e-3)
