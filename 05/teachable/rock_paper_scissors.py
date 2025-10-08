# Rock-Paper-Scissors with Teachable Machine and Live Camera

## import the libraries
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import cv2
import random


class RockPaperScissors:
    def __init__(self, model_path='model/keras_model.h5', labels_path='model/labels.txt'):
        # Load the trained model
        self.model = load_model(model_path, compile=False)
        
        # Load class labels
        with open(labels_path, 'r') as f:
            self.class_names = [line[2:].strip() for line in f.readlines()]
        
        # Image size expected by the model
        self.size = (224, 224)

        self.imoji_dict = {
            "rock": "✊",
            "paper": "✋",
            "scissors1": "✌️",
            "scissors2": "✌️"
        }
        
    def predict(self, frame):
        # Resize the frame to the size expected by the model
        resized_frame = cv2.resize(frame, self.size)
        
        # Convert the image to a numpy array
        image_array = np.asarray(resized_frame)
        
        # Normalize the image array
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        
        # Create a batch of one image
        data = np.expand_dims(normalized_image_array, axis=0)
        
        # Predict
        prediction = self.model.predict(data, verbose=0)
        index = np.argmax(prediction)
        #class_name = self.class_names[index]
        confidence_score = prediction[0][index]
        
        return index, confidence_score
    

    ## Function to get computer's random choice
    def computer_choice(self):
        # 0: rock, 1: paper, 2: scissors (scissors1 or scissors2)
        return random.choice([0, 1, 2, 3])
    

    ## Function to determine the winner
    def get_winner(self, computer_choice, user_choice):
        # 0: rock, 1: paper, 2: scissors1, 3: scissors2
        # Treat both 2 and 3 as scissors
        def is_scissors(choice):
            return choice == 2 or choice == 3

        if computer_choice == user_choice or (is_scissors(computer_choice) and is_scissors(user_choice)):
            return "tie"
        elif (computer_choice == 0 and is_scissors(user_choice)) or \
            (computer_choice == 1 and computer_choice != user_choice and not is_scissors(user_choice) and user_choice == 0) or \
            (is_scissors(computer_choice) and user_choice == 1):
            return "computer"
        else:
            return "user"


    def play(self):
        # Open webcam
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Could not open video stream.")
            return
        
        # Game instructions
        print("*="*40)
        print(f"👾 Welcome to {self.imoji_dict['rock']}, {self.imoji_dict['paper']}, {self.imoji_dict['scissors1']}   Rock-Paper-Scissors Game!")
        print("📌 Press 'p' to play (ready your hand in front of the camera) or 'q' to exit.")
        
        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to grab frame.")
                    break
                
                cv2.imshow('Rock-Paper-Scissors', frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('p'):  # Press 'p' to predict
                    index, confidence_score = self.predict(frame)
                    #print(f"Predicted: {class_name} ({confidence_score * 100:.2f}%)")

                    your_choice = index
                    computer_choice = self.computer_choice()
                    winner = self.get_winner(computer_choice, your_choice)
                    
                    # Display results
                    print("-"*40)
                    output1 = f"Your choice: {self.imoji_dict[self.class_names[your_choice]]}, "
                    output2 = f"Computer's choice: {self.imoji_dict[self.class_names[computer_choice]]}  ==> "
                    print(output1 + output2, end="")

                    if winner == "tie":
                        print("😜 It's a tie!")
                    elif winner == "user":
                        print("😀 You win!")
                    else:
                        print("🙄 Computer wins!")
                    
                elif key == ord('q'):  # Press 'q' to quit
                    break
        finally:
            cap.release()
            cv2.destroyAllWindows()