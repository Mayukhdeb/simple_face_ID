import tensorflow as tf

import numpy as np

#learning from handwritten digits

# feed forward + back propagation = epoch



mnist = np.array(np.load("training_data_shuffled.npy"))

#10 classes 0 to 9
'''
under a one_hot situation one of the output nodes is "hot"-- 1

and the others are zero


for example

0 = [ 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


## now what are biases ??

 Y = mX + C

 m = weight

 C = bias


'''


n_nodes_hl1 = 500

n_nodes_hl2 = 500

n_nodes_hl3 = 500

n_classes = 10

batch_size = 100  # go through 100 features(pictures) and feed them at a time and manipulate the weights

x = tf.placeholder('float',[None, 784] )  #input data with [height, width]
y = tf.placeholder ('float')


def neural_network_model(data):
    hidden_1_layer = {'weights':tf.Variable(tf.random_normal([784, n_nodes_hl1])), 'biases':tf.Variable(tf.random_normal([n_nodes_hl1]))} #making hidden layer with random weights first

    hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])), 'biases':tf.Variable(tf.random_normal([n_nodes_hl2]))} #

    hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])), 'biases':tf.Variable(tf.random_normal([n_nodes_hl3]))} #

    output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])), 'biases':tf.Variable(tf.random_normal([n_classes]))} #


    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']) , hidden_1_layer['biases'])  ## defining y = mx + c thing in a layer

    l1 = tf.nn.relu(l1) #activation function

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']) , hidden_2_layer['biases'])  ## defining y = mx + c thing in a layer

    l2 = tf.nn.relu(l2) #activation function

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']) , hidden_3_layer['biases'])  ## defining y = mx + c thing in a layer

    l3 = tf.nn.relu(l3) #activation function

    output =  tf.matmul(l3, output_layer['weights']) + output_layer['biases']  ## defining y = mx + c thing in a layer


    return output



def train_neural_network(x):
    prediction = neural_network_model(x)  ## returns a one hot array

    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits = prediction, labels=y)) ## cost function

    optimizer = tf.train.AdamOptimizer().minimize(cost)

    hm_epochs = 10

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())   #the session has started running

        for epoch in range(hm_epochs): ##training starts 
            epoch_loss = 0

            for _ in range(int(mnist.train.num_examples/batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)

                _, c = sess.run([optimizer, cost], feed_dict = {x: epoch_x, y: epoch_y})

                epoch_loss += c
            print ("Epoch --", epoch, "completed out of-- ", hm_epochs, "  loss -- ", epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y,1)) ## comparing prediction to actual label

        accuracy = tf.reduce_mean(tf.cast(correct,'float'))

        print ("   ACCURACY -- ", accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))




train_neural_network(x)
    


















