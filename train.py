import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np

learning_rate = 0.001
training_steps = 1000
batch_size = 20
display_step = 1

num_input = 1 # MNIST data input (img shape: 28*28)
timesteps = 10 # timesteps
num_hidden = 10 # hidden layer num of features
num_classes = 2 # MNIST total classes (0-9 digits)

X = tf.placeholder("float", [None, timesteps, num_input])
Y = tf.placeholder("float", [None, num_classes])

weights = {
    'out': tf.Variable(tf.random_normal([num_hidden, num_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([num_classes]))
}

def RNN(x, weights, biases):

    lstm_cell = rnn.BasicLSTMCell(num_hidden, forget_bias=1.0)
    x = tf.unstack(x, timesteps, 1)
    outputs, states = rnn.static_rnn(lstm_cell, x, dtype=tf.float32)
    return tf.matmul(outputs[-1], weights['out']) + biases['out']


logits = RNN(X, weights, biases)
prediction=logits

loss_op=tf.reduce_mean(tf.squared_difference(logits,Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
train_op = optimizer.minimize(loss_op)


correct_pred = tf.equal(tf.argmax(prediction, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    batch_x1=list(range(1,101))#.append(range(101,301,2))
    batch_x2=list(range(1,201,2))
    batch_x=batch_x1+batch_x2
    print(batch_x)
    batch_y=[]
    for i in range (10):
        batch_y.append([1,0])
    for i in range (10):
        batch_y.append([0,1])
    print(batch_y)

    #print(batch_y)
    batch_x=np.reshape(batch_x,(batch_size,timesteps,num_input))
    batch_y=np.reshape(batch_y,(20,num_classes))
    #print(batch_y)
    for step in range(1, training_steps+1):
        sess.run(train_op, feed_dict={X: batch_x, Y: batch_y})


        if step % display_step == 0 or step == 1:
            # Calculate batch loss and accuracy
            loss, acc = sess.run([loss_op, accuracy], feed_dict={X: batch_x,
                                                                 Y: batch_y})
            print("Step " + str(step) + ", Minibatch Loss= " + \
                  "{:.4f}".format(loss) + ", Training Accuracy= " + \
                  "{:.3f}".format(acc))

    print("Optimization Finished!")
    test_len=10
    test_data=list(range(51,61,1))
    test_data=np.reshape(test_data,(1,timesteps,num_input))
    print(sess.run(logits, feed_dict={X: test_data}))
    
