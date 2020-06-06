from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import time
import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from .dataset import *
from django.contrib.auth.models import User,auth

import cv2
import os

from sklearn.metrics import confusion_matrix
from datetime import timedelta

# Create your views here.
def index(request):
    ho="active"
    fn=request.session['uname']
    return render(request,"index.html",{'ho':ho,'fn':fn})



def Img(request):
    fn=request.session['uname']
    im="active"
    return render(request,"index.html",{'im':im,'fn':fn})

def dis(request):
    di="active"
    fn=request.session['uname']
    diss=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']
    return render(request,"index.html",{'di':di,'fn':fn,'sys':diss})

def patlogin(request):
    ho="active"
    uname = request.POST.get('uname')
    passw = request.POST.get('passw')
    
  
    if patreg.objects.filter(uname=uname).exists():

        if patreg.objects.filter(passw=passw).exists():
            meg="Login sucessfully"
            reg=patreg.objects.get(uname=uname)
            fn=reg.uname
            request.session['uname']=uname
            return render(request,'index.html',{'ho':ho,'msg':meg,'fn':fn})
        else:
            print("password is not correct")
            meg="password is not correct..."
            return render(request,'home.html',{'msg':meg})   
    else:
        print('username is not there...')
        print(uname)
        meg="username is not there..."
        return render(request,"home.html",{'msg':meg})

def patientreg(request):
    ho="active"
    uname = request.POST.get('uname')
    passw = request.POST.get('passw')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    address = request.POST.get('address')
    regg=patreg(uname=uname,passw=passw,email=email,contact=contact,address=address)
    if patreg.objects.filter(uname=uname).exists():
        msg="Username is already taken"
    else:
        regg.save();
        msg="Register Successfully"
    return render(request,"home.html",{'msg':msg})

def home(request):
    return render(request,"home.html")

def disea(request):
    s1 = request.POST.get('s1')
    s2 = request.POST.get('s2')
    s3 = request.POST.get('s3')
    s4 = request.POST.get('s4')
    print(s1,s2,s3,s4)
    l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

    disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
    'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
    ' Migraine','Cervical spondylosis',
    'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
    'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
    'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
    'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
    'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
    'Impetigo']

    l2=[]
    for x in range(0,len(l1)):
        l2.append(0)

    # TESTING DATA df -------------------------------------------------------------------------------------
    df=pd.read_csv("C:/Users/Python2/Django/project/skindisease/Training.csv")

    df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

    # print(df.head())

    X= df[l1]

    y = df[["prognosis"]]
    np.ravel(y)
    # print(y)

    # TRAINING DATA tr --------------------------------------------------------------------------------
    tr=pd.read_csv("C:/Users/Python2/Django/project/skindisease/Testing.csv")
    tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

    X_test= tr[l1]
    y_test = tr[["prognosis"]]
    np.ravel(y_test)
    # ------------------------------------------------------------------------------------------------------
    
    
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [s1,s2,s3,s4]
    print(psymptoms,"sas")
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        print(disease[a])
        
    else:
        print("notfound")
    
    msg=" You have the disease is " + disease[a]
    fn=request.session['uname']

    return render(request,"index.html",{'msg':msg,'fn':fn})

def check(request):
   # Convolutional Layer 1.
    filter_size1 = 3
    num_filters1 = 32

    # Convolutional Layer 2.
    filter_size2 = 3
    num_filters2 = 32

    # Convolutional Layer 3.
    filter_size3 = 3
    num_filters3 = 64

    # Fully-connected layer.
    fc_size = 128# Number of neurons in fully-connected layer.

    # Number of color channels for the images: 1 channel for gray-scale.
    num_channels = 3

    # image dimensions (only squares for now)
    img_size = 32

    # Size of image when flattened to a single dimension
    img_size_flat = img_size * img_size * num_channels

    # Tuple with height and width of images used to reshape arrays.
    img_shape = (img_size, img_size)

    # class info
    classes = ['acne closed comedo','ACUTE_PARONYCHIA','Blue Nevus Ota','Halo Nevus','Livido Reticularis','Phototoxic Reactions','Pyogenic Granuloma','Vasculitis','Venous Lake']
    num_classes = len(classes)

    # batch size
    batch_size = 1

    # validation split
    validation_size = .20

    # how long to wait after validation loss stops improving before terminating training
    early_stopping = None

    train_path = 'C:/Users/Python2/Django/project/skindisease/skin/data/train'
    test_path = 'C:/Users/Python2/Django/project/skindisease/skin/data/test'
    checkpoint_dir = "models/"


    data = read_train_sets(train_path, img_size, classes, validation_size=validation_size)
    test_images, test_ids = read_test_set(test_path, img_size)

    print("Size of:")
    print("- Training-set:/t/t{}".format(len(data.train.labels)))
    print("- Test-set:/t/t{}".format(len(test_images)))
    print("- Validation-set:/t{}".format(len(data.valid.labels)))

    ##Helper-function for plotting images

    def plot_images(images, cls_true, cls_pred=None):
        
        if len(images) == 0:
            print("no images to show")
            return 
        else:
            random_indices = random.sample(range(len(images)), min(len(images), 9))
            
            
        images, cls_true  = zip(*[(images[i], cls_true[i]) for i in random_indices])
        
        # Create figure with 3x3 sub-plots.
        fig, axes = plt.subplots(3, 3)
        fig.subplots_adjust(hspace=0.3, wspace=0.3)

        for i, ax in enumerate(axes.flat):
            # Plot image.
            ax.imshow(images[i].reshape(img_size, img_size, num_channels))

            # Show true and predicted classes.
            if cls_pred is None:
                xlabel = "True: {0}".format(cls_true[i])
            else:
                xlabel = "True: {0}, Pred: {1}".format(cls_true[i], cls_pred[i])

            # Show the classes as the label on the x-axis.
            ax.set_xlabel(xlabel)
            
            # Remove ticks from the plot.
            ax.set_xticks([])
            ax.set_yticks([])
        
        # Ensure the plot is shown correctly with multiple plots
        # in a single Notebook cell.
     


    # Get some random images and their labels from the train set.

    images, cls_true  = data.train.images, data.train.cls

    # Plot the images and labels using our helper-function above.
    plot_images(images=images, cls_true=cls_true)


    ##Helper-functions for creating new variables

    def new_weights(shape):
        return tf.Variable(tf.truncated_normal(shape, stddev=0.05))
    def new_biases(length):
        return tf.Variable(tf.constant(0.05, shape=[length]))
    def new_conv_layer(input,              # The previous layer.
                    num_input_channels, # Num. channels in prev. layer.
                    filter_size,        # Width and height of each filter.
                    num_filters,        # Number of filters.
                    use_pooling=True):  # Use 2x2 max-pooling.

        shape = [filter_size, filter_size, num_input_channels, num_filters]

        # Create new weights aka. filters with the given shape.
        weights = new_weights(shape=shape)

        # Create new biases, one for each filter.
        biases = new_biases(length=num_filters)
        layer = tf.nn.conv2d(input=input,
                            filter=weights,
                            strides=[1, 1, 1, 1],
                            padding='SAME')

        # Add the biases to the results of the convolution.
        # A bias-value is added to each filter-channel.
        layer += biases

        if use_pooling:
            layer = tf.nn.max_pool(value=layer,
                                ksize=[1, 2, 2, 1],
                                strides=[1, 2, 2, 1],
                                padding='SAME')

        layer = tf.nn.relu(layer)
        return layer, weights

    def flatten_layer(layer):
        # Get the shape of the input layer.
        layer_shape = layer.get_shape()
        num_features = layer_shape[1:4].num_elements()
        layer_flat = tf.reshape(layer, [-1, num_features])
        return layer_flat, num_features

    def new_fc_layer(input,          
                    num_inputs,     
                    num_outputs,    
                    use_relu=True): 

        # Create new weights and biases.
        weights = new_weights(shape=[num_inputs, num_outputs])
        biases = new_biases(length=num_outputs)
        layer = tf.matmul(input, weights) + biases

        # Use ReLU?
        if use_relu:
            layer = tf.nn.relu(layer)

        return layer

    x = tf.placeholder(tf.float32,  name='x')
    x_image = tf.reshape(x, [-1, img_size, img_size, num_channels])###############
    y_true = tf.placeholder(tf.float32,  name='y_true')
    y_true_cls = tf.argmax(y_true, dimension=1)############################


    ##Convolutional Layer 1
    layer_conv1, weights_conv1 = \
        new_conv_layer(input=x_image,
                    num_input_channels=num_channels,
                    filter_size=filter_size1,
                    num_filters=num_filters1,
                    use_pooling=True)


    layer_conv1   # layer 1 output image data

    layer_conv2, weights_conv2 = \
        new_conv_layer(input=layer_conv1,
                    num_input_channels=num_filters1,
                    filter_size=filter_size2,
                    num_filters=num_filters2,
                    use_pooling=True)

    layer_conv3, weights_conv3 = \
        new_conv_layer(input=layer_conv2,
                    num_input_channels=num_filters2,
                    filter_size=filter_size3,
                    num_filters=num_filters3,
                    use_pooling=True)
    layer_conv2
    layer_conv3
    ##Flatten Layer

    layer_flat, num_features = flatten_layer(layer_conv3)
    ## Fully-Connected Layer 
    layer_fc1 = new_fc_layer(input=layer_flat,
                            num_inputs=num_features,
                            num_outputs=fc_size,
                            use_relu=True)
    layer_fc2 = new_fc_layer(input=layer_fc1,
                            num_inputs=fc_size,
                            num_outputs=num_classes,
                            use_relu=False)

    ## class prediction
    y_pred = tf.nn.softmax(layer_fc2)
    y_pred_cls = tf.argmax(y_pred, dimension=1)


    ## Cost-function to be optimized
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=layer_fc2,
                                                            labels=y_true)


    ##Optimization Method
    cost = tf.reduce_mean(cross_entropy)
    optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)
    ##Performance Measures
    correct_prediction = tf.equal(y_pred_cls, y_true_cls)
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    ####TENSORFLOW SESSION
    session = tf.Session()

    session.run(tf.initialize_all_variables())
    train_batch_size = batch_size


    ##Helper-function to perform optimization iterations
    def print_progress(epoch, feed_dict_train, feed_dict_validate, val_loss):
        # Calculate the accuracy on the training-set.
        acc = session.run(accuracy, feed_dict=feed_dict_train)
        val_acc = session.run(accuracy, feed_dict=feed_dict_validate)
        msg = "Epoch {0} --- Training Accuracy: {1:>6.1%}, Validation Accuracy: {2:>6.1%}, Validation Loss: {3:.3f}"
        print(msg.format(epoch + 1, acc, val_acc, val_loss))

    # Counter for total number of iterations performed so far.
    total_iterations=0

    def optimize(num_iterations):
        # Ensure we update the global variable rather than a local copy.
        global total_iterations

        # Start-time used for printing time-usage below.
        start_time = time.time()
        
        best_val_loss = float("inf")
        patience = 0

        for i in range(0,
                    0 + num_iterations):
            x_batch, y_true_batch, _, cls_batch = data.train.next_batch(train_batch_size)
            x_valid_batch, y_valid_batch, _, valid_cls_batch = data.valid.next_batch(train_batch_size)

            # Convert shape from [num examples, rows, columns, depth]
            # to [num examples, flattened image shape]

            x_batch = x_batch.reshape(train_batch_size, img_size_flat)
            x_valid_batch = x_valid_batch.reshape(train_batch_size, img_size_flat)

            # Put the batch into a dict with the proper names
            # for placeholder variables in the TensorFlow graph.
            feed_dict_train = {x: x_batch,
                            y_true: y_true_batch}
            
            feed_dict_validate = {x: x_valid_batch,
                                y_true: y_valid_batch}
            session.run(optimizer, feed_dict=feed_dict_train)
            

            # Print status at end of each epoch (defined as full pass through training dataset).
            if i % int(data.train.num_examples/batch_size) == 0: 
                val_loss = session.run(cost, feed_dict=feed_dict_validate)
                epoch = int(i / int(data.train.num_examples/batch_size))
                
                print_progress(epoch, feed_dict_train, feed_dict_validate, val_loss)
                
                if early_stopping:    
                    if val_loss < best_val_loss:
                        best_val_loss = val_loss
                        patience = 0
                    else:
                        patience += 1

                    if patience == early_stopping:
                        break
        total_iterations=0
        # Update the total number of iterations performed.
        total_iterations += num_iterations

        # Ending time.
        end_time = time.time()

        # Difference between start and end-times.
        time_dif = end_time - start_time

        # Print the time-usage.
        print("Time elapsed: " + str(timedelta(seconds=int(round(time_dif)))))

    
    ##Helper-function to plot example errors
    def plot_example_errors(cls_pred, correct):
        incorrect = (correct == False)
        
        # Get the images from the test-set that have been
        # incorrectly classified.
        images = data.valid.images[incorrect]
        
        # Get the predicted classes for those images.
        cls_pred = cls_pred[incorrect]

        # Get the true classes for those images.
        cls_true = data.valid.cls[incorrect]
        
        # Plot the first 9 images.
        plot_images(images=images[0:9],
                    cls_true=cls_true[0:9],
                    cls_pred=cls_pred[0:9])
    def plot_confusion_matrix(cls_pred):
        cls_true = data.valid.cls
        
        # Get the confusion matrix using sklearn.
        cm = confusion_matrix(y_true=cls_true,
                            y_pred=cls_pred)

        # Print the confusion matrix as text.
        print(cm)
        # Plot the confusion matrix as an image.
        plt.matshow(cm)

        # Make various adjustments to the plot.
        plt.colorbar()
        tick_marks = np.arange(num_classes)
        plt.xticks(tick_marks, range(num_classes))
        plt.yticks(tick_marks, range(num_classes))
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.show()
    ##Helper-function for showing the performance
    def print_validation_accuracy(show_example_errors=False,
                            show_confusion_matrix=False):

        # Number of images in the test-set.
        num_test = len(data.valid.images)
        cls_pred = np.zeros(shape=num_test, dtype=np.int)
        i = 0

        while i < num_test:
            # The ending index for the next batch is denoted j.
            j = min(i + batch_size, num_test)

            # Get the images from the test-set between index i and j.
            images = data.valid.images[i:j, :].reshape(batch_size, img_size_flat)
            

            # Get the associated labels.
            labels = data.valid.labels[i:j, :]

            # Create a feed-dict with these images and labels.
            feed_dict = {x: images,
                        y_true: labels}

            # Calculate the predicted class using TensorFlow.
            cls_pred[i:j] = session.run(y_pred_cls, feed_dict=feed_dict)

            # Set the start-index for the next batch to the
            # end-index of the current batch.
            i = j

        cls_true = np.array(data.valid.cls)
        cls_pred = np.array([classes[x] for x in cls_pred]) 

        # Create a boolean array whether each image is correctly classified.
        correct = (cls_true == cls_pred)
        correct_sum = correct.sum()
        acc = float(correct_sum) / num_test

        # Print the accuracy.
        msg = "Accuracy on Test-Set: {0:.1%} ({1} / {2})"
        print(msg.format(acc, correct_sum, num_test))

        # Plot some examples of mis-classifications, if desired.
        if show_example_errors:
            print("Example errors:")
            plot_example_errors(cls_pred=cls_pred, correct=correct)

        # Plot the confusion matrix, if desired.
        if show_confusion_matrix:
            print("Confusion Matrix:")
            plot_confusion_matrix(cls_pred=cls_pred)


    optimize(num_iterations=5000)  # We performed 100 iterations above.
    ##print_validation_accuracy(show_example_errors=True)
    ##print_validation_accuracy(show_example_errors=True, show_confusion_matrix=True)

    ##### TESTING IMAGE INPUT  ######
    files = request.FILES.get('upload')
    print(files)
    fil=imagee(id=1,image=files)
    fil.save();
    fi=imagee.objects.get(id=1)
    im=fi.image
    im=str(im)
    pathh="media/"+im
    inputface = cv2.imread(pathh)
    inputface = cv2.resize(inputface, (img_size, img_size), cv2.INTER_LINEAR) / 255
    ##plt.imshow(inputface.reshape(img_size, img_size, num_channels))


    def sample_prediction(test_im):
        
        feed_dict_test = {
            x: test_im.reshape(1, img_size_flat),
            y_true: np.array([[2,1,0]])
        }

        test_pred = session.run(y_pred_cls, feed_dict=feed_dict_test)
        return classes[test_pred[0]]

    print("output test data: {}".format(sample_prediction(inputface)))
    msg="Skin disease : {}".format(sample_prediction(inputface))


    def plot_conv_weights(weights, input_channel=0):
        # Assume weights are TensorFlow ops for 4-dim variables
        # e.g. weights_conv1 or weights_conv2.
        
        # Retrieve the values of the weight-variables from TensorFlow.
        # A feed-dict is not necessary because nothing is calculated.
        w = session.run(weights)

        # Get the lowest and highest values for the weights.
        # This is used to correct the colour intensity across
        # the images so they can be compared with each other.
        w_min = np.min(w)
        w_max = np.max(w)

        # Number of filters used in the conv. layer.
        num_filters = w.shape[3]

        # Number of grids to plot.
        # Rounded-up, square-root of the number of filters.
        num_grids = math.ceil(math.sqrt(num_filters))
        
        # Create figure with a grid of sub-plots.
        fig, axes = plt.subplots(num_grids, num_grids)

        # Plot all the filter-weights.
        for i, ax in enumerate(axes.flat):
            # Only plot the valid filter-weights.
            if i<num_filters:
                # Get the weights for the i'th filter of the input channel.
                # See new_conv_layer() for details on the format
                # of this 4-dim tensor.
                img = w[:, :, input_channel, i]

                # Plot image.
                ax.imshow(img, vmin=w_min, vmax=w_max,
                        interpolation='nearest', cmap='seismic')
            
            # Remove ticks from the plot.
            ax.set_xticks([])
            ax.set_yticks([])
        
        # Ensure the plot is shown correctly with multiple plots
        # in a single Notebook cell.
        plt.show()

    def plot_conv_layer(layer, image):
        # Assume layer is a TensorFlow op that outputs a 4-dim tensor
        # which is the output of a convolutional layer,
        # e.g. layer_conv1 or layer_conv2.
        
        image = image.reshape(img_size_flat)

        # Create a feed-dict containing just one image.
        # Note that we don't need to feed y_true because it is
        # not used in this calculation.
        feed_dict = {x: [image]}

        # Calculate and retrieve the output values of the layer
        # when inputting that image.
        values = session.run(layer, feed_dict=feed_dict)

        # Number of filters used in the conv. layer.
        num_filters = values.shape[3]

        # Number of grids to plot.
        # Rounded-up, square-root of the number of filters.
        num_grids = math.ceil(math.sqrt(num_filters))
        
        # Create figure with a grid of sub-plots.
        fig, axes = plt.subplots(num_grids, num_grids)

        # Plot the output images of all the filters.
        for i, ax in enumerate(axes.flat):
            # Only plot the images for valid filters.
            if i<num_filters:
                # Get the output image of using the i'th filter.
                # See new_conv_layer() for details on the format
                # of this 4-dim tensor.
                img = values[0, :, :, i]

                # Plot image.
                ax.imshow(img, interpolation='nearest', cmap='binary')
            
            # Remove ticks from the plot.
            ax.set_xticks([])
            ax.set_yticks([])
        
        # Ensure the plot is shown correctly with multiple plots
        # in a single Notebook cell.
        

    return render(request,"index.html",{'msg':msg})