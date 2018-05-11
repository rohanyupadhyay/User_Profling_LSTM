import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
import ast
import os
#tf.reset_default_graph()

f3=open('final/users.txt','r')
f4=open('final/test/pp_in.txt','r')
tx=ast.literal_eval(f4.readline())
f5=open('final/test/pp_out.txt','r')
ty=ast.literal_eval(f5.readline())
users=ast.literal_eval(f3.readline())
num_classes = len(users) #output classes
users=tf.identity(users,name="users")



#learning_rate = 0.0001
training_steps = 2
display_step = 1

num_input = 19 # number of features
timesteps = 250 # timesteps
num_hidden = 50 # hidden layer 1





X=tf.placeholder("float",[None,timesteps,num_input],name='input')
Y=tf.placeholder("float",[None,num_classes],name='output')


weights = {
    'out': tf.Variable(tf.random_normal([num_hidden, num_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([num_classes]))
}

layer = rnn.BasicLSTMCell(num_hidden,forget_bias=1.0)
cell = rnn.MultiRNNCell([rnn.BasicLSTMCell(num_hidden) for _ in range(1)])
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

    saver.restore(sess,"checkpoint/here.ckpt")

    print("0",format(sess.run(accuracy, feed_dict={X: tx,Y:ty})))
    for i in range(training_steps):
        for j in range(len(os.listdir('final/in'))):
            f1=open('final/in/pp_in_'+str(j+1)+'.txt','r')
            f2=open('final/out/pp_out_'+str(j+1)+'.txt','r')
            x=f1.readline()
            x=ast.literal_eval(x)
            y=f2.readline()
            y=ast.literal_eval(y)
            for k in range(1):
                sess.run(train, feed_dict={X: x,Y:y})
            print("Iteration:",j+1,format(sess.run(accuracy, feed_dict={X: x,Y:y})))
        print("\n\n\nEpoch:",i+1,format(sess.run(accuracy, feed_dict={X: tx,Y:ty})),"\n")
        if i%1==0:
            saver.save(sess,"checkpoint/here.ckpt")
    saver.save(sess,"checkpoint/here.ckpt")
    #tf.saved_model.simple_save(sess,"model/",inputs={"X":X},outputs={"prediction":prediction})
    
    
    #ans=sess.run(output, feed_dict={X: x})
    print(sess.run(prediction, feed_dict={X: tx}))
    print(sess.run(accuracy, feed_dict={X: tx,Y:ty}))