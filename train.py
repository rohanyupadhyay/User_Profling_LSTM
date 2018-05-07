import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
import ast
#tf.reset_default_graph()
f1=open('final/pp_in.txt','r')
f2=open('final/pp_out.txt','r')
f3=open('final/users.txt','r')
x=f1.readline()
x=ast.literal_eval(x)
y=f2.readline()
y=ast.literal_eval(y)
users=ast.literal_eval(f3.readline())
users=tf.identity(users,name="users")



#learning_rate = 0.0001
training_steps = 10
display_step = 1

num_input = 19 # number of features
timesteps = 250 # timesteps
num_hidden = 100 # hidden layer 1
num_classes = len(y[0]) #output classes




X=tf.placeholder("float",[None,timesteps,num_input],name='input')
Y=tf.placeholder("float",[None,num_classes],name='output')


weights = {
    'out': tf.Variable(tf.random_normal([num_hidden, num_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([num_classes]))
}

layer = rnn.BasicLSTMCell(num_hidden,forget_bias=1.0)
cell = rnn.MultiRNNCell([rnn.BasicLSTMCell(num_hidden) for _ in range(3)])
#x=tf.unstack(X,axis=1)

output,state=tf.nn.dynamic_rnn(cell,X,dtype=tf.float32)

prediction=tf.nn.softmax(tf.matmul(output[:,-1],weights['out']) +biases['out'])
prediction=tf.identity(prediction,name="prediction")
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=prediction,labels=Y))
optimizer=tf.train.AdamOptimizer()
train=optimizer.minimize(loss)
accuracy=tf.reduce_mean((Y*prediction) + (1-Y)*(1-prediction))

saver=tf.train.Saver()

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    #saver.restore(sess,"checkpoint/here.ckpt")



    for i in range(training_steps):
        sess.run(train, feed_dict={X: x,Y:y})
        print(i+1,format(sess.run(accuracy, feed_dict={X: x,Y:y})))
        if i%10==0:
            saver.save(sess,"checkpoint/here.ckpt")
            #tf.saved_model.simple_save(sess,"model/",inputs={"X":X},outputs={"prediction":prediction})
    saver.save(sess,"checkpoint/here.ckpt")
    #tf.saved_model.simple_save(sess,"model/",inputs={"X":X},outputs={"prediction":prediction})
    
    
    #ans=sess.run(output, feed_dict={X: x})
    print(sess.run(prediction, feed_dict={X: x}))
    print(sess.run(accuracy, feed_dict={X: x,Y:y}))