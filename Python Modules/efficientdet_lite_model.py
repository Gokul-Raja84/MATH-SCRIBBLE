import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.applications import EfficientNetB0

def efficientdet_lite(phi, num_classes=20):
    # EfficientDet Parameters
    compound_coef = phi
    image_size = 512 if phi == 0 else (640, 768, 896, 1024, 1280, 1280, 1536)[phi]
    
    # Backbone: EfficientNetB0
    backbone = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(image_size, image_size, 3))
    backbone.trainable = False
    
    # Feature Pyramid Network
    features = backbone.get_layer('block6a_expand_activation').output
    features = layers.Conv2D(384, (1, 1), activation='relu')(features)
    features = layers.GlobalAveragePooling2D()(features)

    # Classification and Regression Heads
    classification_head = layers.Dense(num_classes, activation='softmax', name='classification_head')(features)
    regression_head = layers.Dense(4, activation='linear', name='regression_head')(features)

    # Model
    model = tf.keras.Model(inputs=backbone.input, outputs=[classification_head, regression_head], name='efficientdet_lite')

    return model

def efficientdet_lite_model(input_size=(512, 512, 3), num_classes=20):
    phi = 0  # Choose the EfficientDet-Lite model variant (0 to 6)
    efficientdet_model = efficientdet_lite(phi, num_classes)
    
    # Compile the model (customize as needed)
    efficientdet_model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss={
            'classification_head': 'categorical_crossentropy',
            'regression_head': 'mse'
        },
        metrics={
            'classification_head': 'accuracy',
            'regression_head': 'mae'
        }
    )
    
    return efficientdet_model

if __name__ == "__main__":
    # Example usage
    model = efficientdet_lite_model()
    model.summary()
