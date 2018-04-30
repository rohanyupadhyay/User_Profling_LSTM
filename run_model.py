import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np

learning_rate = 0.0001
training_steps = 1000
batch_size = 10
display_step = 1

num_input = 1 # number of features
timesteps = 2 # timesteps
num_hidden = 1 # hidden layer 1
num_classes = 1 #output classes (0-9 digits)



X=tf.placeholder("float",[None,timesteps,num_input])
Y=tf.placeholder("float",[None,num_classes])


weights = {
    'out': tf.Variable(tf.random_normal([num_hidden, num_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([num_classes]))
}

layer = rnn.BasicLSTMCell(num_hidden,forget_bias=1.0)
cell = rnn.MultiRNNCell([rnn.BasicLSTMCell(num_hidden) for _ in range(2)])
x=tf.unstack(X,axis=1)

output,state=tf.nn.dynamic_rnn(cell,X,dtype=tf.float32)

prediction=tf.matmul(output[:,-1],weights['out']) +biases['out']

cost=tf.reduce_mean(tf.squared_difference(prediction,Y))
optimizer=tf.train.AdamOptimizer(learning_rate=learning_rate)
train=optimizer.minimize(cost)

saver=tf.train.Saver()

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    saver.restore(sess,"D:/Rohan/here.ckpt")

  
    tempx1=list(range(1,1002))
    x=[]
    for i in range(1000):
        x.extend(tempx1[i:i+2])
    tempx2=list(range(1,2003))
    for i in range(1000):
        x.extend(tempx2[i:i+3:2])
    print(x)
    x=np.reshape(x,(2000,timesteps,num_input))
    ans=sess.run(prediction, feed_dict={X: x})
    for i in ans:
        print(i)