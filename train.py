import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
import ast
import os
#tf.reset_default_graph()

f3=open('final/users.txt','r')
#f4=open('final/test/pp_in.txt','r')
#tx=ast.literal_eval(f4.readline())
tx=np.load('final/test/pp_in.npy')
#f5=open('final/test/pp_out.txt','r')
#ty=ast.literal_eval(f5.readline())
ty=np.load('final/test/pp_out.npy')
users=ast.literal_eval(f3.readline())
num_classes = len(users) #output classes
users=tf.identity(users,name="users")

#learning_rate = 0.0001
training_steps = 1000
display_step = 1

num_input = 19 # number of features
timesteps = 250 # timesteps
num_hidden = 75 # cells in hidden layer
hidden_layers=2

X=tf.placeholder("float",[None,timesteps,num_input],name='input')
Y=tf.placeholder("float",[None,num_classes],name='output')

weights = {
    'out': tf.Variable(tf.random_normal([num_hidden, num_classes]))
}
biases = {
    'out': tf.Variable(tf.random_normal([num_classes]))
}

layer = rnn.BasicLSTMCell(num_hidden,forget_bias=1.0)
cell = rnn.MultiRNNCell([rnn.BasicLSTMCell(num_hidden) for _ in range(hidden_layers)])
#x=tf.unstack(X,axis=1)

output,state=tf.nn.dynamic_rnn(cell,X,dtype=tf.float32)

prediction=tf.matmul(output[:,-1],weights['out']) +biases['out']
prediction=tf.identity(prediction,name="prediction")
SM_prediction=tf.nn.softmax(prediction)
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=prediction,labels=Y))
optimizer=tf.train.AdamOptimizer()
train=optimizer.minimize(loss)
accuracy=tf.reduce_mean((Y*SM_prediction) + (1-Y)*(1-SM_prediction))

saver=tf.train.Saver()

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    saver.restore(sess,"checkpoint/here.ckpt")

    print("0",format(sess.run(accuracy, feed_dict={X: tx,Y:ty})))
    for i in range(training_steps):
        epocAcc=[]
        for j in range(len(os.listdir('final/in'))):
            #f1=open('final/in/pp_in_'+str(j+1)+'.txt','r')
            #f2=open('final/out/pp_out_'+str(j+1)+'.txt','r')
            #x=f1.readline()
            #x=ast.literal_eval(x)
            #y=f2.readline()
            #y=ast.literal_eval(y)
            x=np.load('final/in/pp_in_'+str(j+1)+'.npy')
            y=np.load('final/out/pp_out_'+str(j+1)+'.npy')
            for k in range(1):
                sess.run(train, feed_dict={X: x,Y:y})
            iterAcc=sess.run(accuracy, feed_dict={X: x,Y:y})
            print("Iteration:",j+1,format(iterAcc))
            epocAcc.append(iterAcc)
        epocAcc=np.array(epocAcc)
        printpred=sess.run(SM_prediction, feed_dict={X: tx})
        npp=np.array(printpred)
        print('\n')
        print(np.mean(npp[0:251,:],axis=0))
        print(np.mean(npp[251:502,:],axis=0))
        print(np.mean(npp[502:753,:],axis=0))
        print("\nEpoch:",i+1,format(sess.run(accuracy, feed_dict={X: tx,Y:ty})),np.mean(epocAcc),"\n\n\n")
        if i%1==0:
            saver.save(sess,"checkpoint/here.ckpt")
            #tf.saved_model.simple_save(sess,"model/",inputs={"X":X},outputs={"prediction":prediction})
    saver.save(sess,"checkpoint/here.ckpt")
    #tf.saved_model.simple_save(sess,"model/",inputs={"X":X},outputs={"prediction":prediction})
    
    
    #ans=sess.run(output, feed_dict={X: x})
    printpred=sess.run(SM_prediction, feed_dict={X: tx})
    npp=np.array(printpred)
    print(np.mean(npp[0:251,:],axis=0))
    print(np.mean(npp[251:502,:],axis=0))
    print(np.mean(npp[502:753,:],axis=0))
    print(sess.run(accuracy, feed_dict={X: tx,Y:ty}))
