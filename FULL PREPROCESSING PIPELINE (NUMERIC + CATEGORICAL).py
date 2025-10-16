import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

# -----------------------------------
# 1️⃣ Identify Numeric Inputs
# -----------------------------------
numerical_inputs = {
    name: input_tensor for name, input_tensor in inputs.items()
    if input_tensor.dtype == tf.float32
}

# Concatenate numeric tensors
numeric_concat = layers.Concatenate()(list(numerical_inputs.values()))

# Normalize numeric features
norm_layer = layers.Normalization()
norm_layer.adapt(np.array(titanic[list(numerical_inputs.keys())]))
all_numeric_inputs = norm_layer(numeric_concat)

# -----------------------------------
# 2️⃣ Handle Categorical Inputs
# -----------------------------------
preprocessed_inputs = [all_numeric_inputs]  # start with numeric part

for name, input_tensor in inputs.items():
    # Skip already processed numeric features
    if input_tensor.dtype == tf.float32:
        continue

    # Build vocabulary from dataset for this feature
    vocab = np.unique(titanic_features[name])
    lookup = layers.StringLookup(vocabulary=vocab)

    # One-hot encoding layer
    one_hot = layers.CategoryEncoding(num_tokens=lookup.vocabulary_size())

    # Convert raw string input -> int tokens
    x = lookup(input_tensor)

    # Convert int tokens -> one-hot vectors
    x = one_hot(x)

    # Add to final preprocessed list
    preprocessed_inputs.append(x)

# -----------------------------------
# 3️⃣ Concatenate All Processed Inputs
# -----------------------------------
final_preprocessed_input = layers.Concatenate()(preprocessed_inputs)

# This final_preprocessed_input is what you pass into your model
# Example:
# model_input = final_preprocessed_input

