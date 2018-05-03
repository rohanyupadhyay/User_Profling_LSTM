import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
import ast

f=open('final/pp_in.txt','r')
inps=ast.literal_eval(f.readline())
#print(inps)



with tf.Session(graph=tf.Graph()) as sess:
    tf.saved_model.loader.load(sess,[tf.saved_model.tag_constants.SERVING],"model/")
    t_X=tf.get_default_graph().get_tensor_by_name('input:0')
    t_prediction=tf.get_default_graph().get_tensor_by_name('prediction:0')
    #print(tf.get_collection(tf.GraphKeys.key))
    #print(sess.graph.get_collection('variables'))
    print(sess.run(t_prediction,feed_dict={t_X:inps}))

    
    






    
    
    #ans=sess.run(output, feed_dict={X: x})
    #print(sess.run(prediction, feed_dict={X: x}))
    