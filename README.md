# User Profiling with LSTM using Tensorflow
Title: Profiling the behaviour of a user on a computer system.

This program will moniter the user on a windows system and try to identify and verify the identity of the user.


Steps:

1. Collect computer usage data of different users by running the 'data_collect.py' file. The user data wil be saved in the 'data' folder. Pressing escape key stops data collection.
2. Collect the users data from different users and copy and paste all the data into the 'data' folder. (Leave some data out for testing set.)
3. After putting all the users' (training) data into the data folder, run the preprocess.py to preprocess the data. Multiple input and output files will be created in 'final/in' and 'final/out' folders.
4. Now preprocess thes testing data by just keeping the testing data in the 'data' folder and run 'preprocess.py'. Make sure that the 'final/in' and 'final/out' folders are empty before running preprocess.py otherwise all the data will be appended to the previous training data (Just temporarily copy your previous folder to some other place before running 'preprocess.py'). Rename the new proprocessed testing data input and output files to 'pp_in.txt' and 'pp_out.txt' and put these testing files in the 'final/test' folder.
5. Now make changes in 'train.py' file to change the number of epochs you want to run by editing the 'training_steps' variable. Also comment the line 'saver.restore(sess,"checkpoint/here.ckpt")' in train.py when you run it for the first time because no checkpoint will exist at that point. Now run 'train.py' and you can uncomment it after running it for the first time and the checkpoints are created. Keep training until your model is trained. Please uncomment the line 'tf.saved_model.simple_save(sess,"model/",inputs={"X":X},outputs={"prediction":prediction})' from train.py when you finally want to save your model.
6. After the training is complete and the model has been saved, you can run the model and make predictions by running 'run_model.py'. Just run the file and let the user use the system and the predictions will be printed.