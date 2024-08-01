import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "MLCodeC19prediction@gmail.com"
receiver_email = "ananthudas2001@gmail.com"
password = "slumcavcxlgqesqw"

def play1():
    tts=gTTS("The person is affected by pneumonia")
    tts.save('1.mp3')
    sound_file='1.mp3'
    display(Audio(sound_file,autoplay=True))

def play2():
    tts=gTTS("The person is normal")
    tts.save('2.mp3')
    sound_file='2.mp3'
    display(Audio(sound_file,autoplay=True))


def predict_image(filename):
    img = load_img(filename, target_size=(64, 64))
    image = keras.preprocessing.image.img_to_array(img)
    image = image / 255.0
    image = image.reshape(1,64,64,3)
    model = tf.keras.models.load_model('pneumonia_model.h5')
    prediction = model.predict(image)
    print(prediction)
    plt.imshow(img)
    print(prediction[0])
    if(prediction[0] > 0.6):
        
        stat = prediction[0] * 100
        print("This image is %.2f percent %s"% (stat, "PNEUMONIA"))
        play1()
        display(Audio('1.mp3',autoplay=True))
        message1 ="ALERT PNEUMONIA is detected in your X-ray. Please do consult the doctor immediately!!"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, receiver_email, message1)

      
    else:
        
        stat = (1.0 - prediction[0]) * 100
        play2()
        display(Audio('2.mp3',autoplay=True))
        print("This image is %.2f percent %s" % (stat, "NORMAL"))
        message2 ="Congratulations Your X-ray is NORMAL."
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
          server.login(sender_email, password)
          server.sendmail(sender_email, receiver_email, message2)

              
   
predict_image("/content/drive/MyDrive/Colab Notebooks/chest_xray/DataSet/test/PNEUMONIA/person100_bacteria_478.jpeg")
