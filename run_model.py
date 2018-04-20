import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np

learning_rate = 0.001
training_steps = 500
batch_size = 150
display_step = 1

num_input = 1 # number of features
timesteps = 3 # timesteps
num_hidden1 = 50 # hidden layer 1
num_hidden2= 10 # hidden layer 2
num_classes = 1 #output classes (0-9 digits)



trainX=tf.placeholder("float",[None,timesteps,num_input])
trainY=tf.placeholder("float",[None,num_classes])


weights = {
    'out': tf.Variable(tf.random_normal([num_hidden1, num_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([num_classes]))
}


X=tf.placeholder("float",[None,num_input])
Y=tf.placeholder("float",[None,num_classes])
lstm_cell = rnn.BasicLSTMCell(num_hidden1,forget_bias=1.0)
#state=hidden_state,current_state
state=lstm_cell.zero_state(batch_size,dtype=tf.float32)
#X=tf.unstack(X, timesteps, 1)


#logits=tf.matmul(output,weights)+biases
trainState=lstm_cell.zero_state(batch_size,dtype=tf.float32)



tmp=[]
for i in range(timesteps):
    trainOutput,trainState=lstm_cell(trainX[:,i,:],trainState)
finalOutput=trainOutput

logits=tf.matmul(finalOutput,weights['out'])+biases['out']

loss=tf.reduce_mean(tf.squared_difference(logits,trainY))

optimizer=tf.train.AdamOptimizer(learning_rate=learning_rate)

train_op=optimizer.minimize(loss)

saver =tf.train.Saver()

init=tf.global_variables_initializer()


with tf.Session() as sess:
    sess.run(init)
    
    saver.restore(sess,"D:/Rohan/here")


    
    tempx=list(range(1,153))
    x=[]
    for i in range(150):
        x.extend(tempx[i:i+3])
    x=np.reshape(x,(150,timesteps,num_input))

    ans=sess.run(logits, feed_dict={trainX:x})
    print(ans)
   