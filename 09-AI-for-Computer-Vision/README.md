# 09-AI-for-Computer-Vision

This repository contains a Jupyter Notebooks that demonstrates how to perform computer vision tasks using Keras and TensorFlow.


## Dependencies

- TensorFlow
- Keras
- Matplotlib
- Seaborn
- Scikit-learn
- Hugging Face Transformers
- Pillow (PIL)
- Requests

## Data 

- Fashion MNIST dataset (loaded using Keras)


## Usage

1. **Clone the repository:**
2. **Open the Jupyter Notebook:**
   - Navigate to the cloned repository.
   - Open the notebook `fashion_mnist_classification.ipynb` (please rename the notebook to this name).

2. **Run the notebook cells:**
   - Execute the cells in the notebook sequentially to load the data, train the models, evaluate the performance, and visualize the results.


## Notebook-1 Contents

**1. Convolutional Neural Network (CNN) for Clothes Classification:**
- Explains the concept of CNNs and their application in image classification.
- Provides a breakdown of the different layers used in a CNN (Conv2D, MaxPooling2D, Flatten, Dense, Dropout).

**2. Fashion MNIST Dataset:**
- Loads the Fashion MNIST dataset using Keras.
- Visualizes sample images from the dataset.
- Preprocesses the data by reshaping and normalizing the images and converting labels to categorical format.

**3. CNN Model Training:**
- Builds a CNN model using Keras with multiple convolutional and dense layers.
- Compiles the model with the Adam optimizer and categorical cross-entropy loss function.
- Trains the model using the training data and monitors performance with a validation split.
- Saves the best performing model during training using ModelCheckpoint.

**4. Model Evaluation and Visualization:**
- Evaluates the trained model on the test data and prints the test accuracy.
- Visualizes the training and validation accuracy over epochs using Matplotlib.
- Plots a confusion matrix to analyze the model's predictions.

**5. Model Saving:**
- Saves the final trained model using Keras.

**6. Improved Model with Hugging Face:**
- Introduces a pre-trained model from Hugging Face for better performance.
- Demonstrates how to load and use the model and processor from Hugging Face.
- Includes a function to classify images from URLs using the Hugging Face model.
- Provides example usage with different image URLs.