import tensorflow as tf




def square(lst):
    return list(map(lambda x: x ** 2, lst))









w0=tf.Variable([.1],tf.float32)
w1=tf.Variable([-.1],tf.float32)


x1=tf.placeholder(tf.float32)

linear_model= w1 * x1 + w0

y1=tf.placeholder(tf.float32)

squared_delta = tf.square(linear_model-y1)
loss=tf.reduce_sum(squared_delta)

optimizer = tf.train.GradientDescentOptimizer(0.01)

train=optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init)


newx=list(range(1,5,1))
newy=square(newx)
#newy=newx

for i in range (1000):
    sess.run(train,{x1:newx,y1:newy})

print(sess.run([w0,w1]))