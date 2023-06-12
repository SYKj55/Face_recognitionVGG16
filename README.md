# Face_recognitionVGG16
Face recognition system using VGG-16 and transfer learning
This is my very first deep learning project as a self taught ML enthusiast.
I downloaded the extracted model weights from kaggle along with the vggface2 dataset to train the network as the original vggface dataset is extremely large and would require additional processing units.
Now for training this network, I use a Triplet Loss function. The triplet loss function takes three, 128-D features generated from the above network. Let these three be known as an anchor, a positive, and a negative where

Anchor: An image of a person that will be used for comparison.
Positive: An image of the same person as that of the anchor.
Negative: An image of a different person than the anchor. 
The VGG-16 Network gave me 128D features for anchor, positive, and negative images, which were then fed to the Loss function. Based on a hands on tutorial on medium, I built the model and hosted it on flask. several blogs and youtube videos also aided in this process. 
