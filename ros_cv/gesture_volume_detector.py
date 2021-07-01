import cv2
import time
import numpy as np
from hand_tracking import HandTrackingModule as htm 
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
import math


class MinimalPublisher(Node):
   def __init__(self):
      super().__init__('minimal_publisher')
      p1 = self.create_publisher(Twist, '/cmd_vel', 10)
      #p2 = self.create_publisher(Bool, '/gpio_output_17', 10)
      vel_msg = Twist() 
      #x=Bool()
      
      
      wCam, hCam = 640, 480
      cap = cv2.VideoCapture(0) 
      cap.set(3, wCam)
      cap.set(4, hCam)
      pTime=0
      detector = htm.handDetector(detectionCon=0.7)

      def recognizeHandGesture(landmarks):
        

        thumbState = 'UNKNOW'
        indexFingerState = 'UNKNOW'
        middleFingerState = 'UNKNOW'
        ringFingerState = 'UNKNOW'
        littleFingerState = 'UNKNOW'
        recognizedHandGesture = None


        
      

        pseudoFixKeyPoint = landmarks[2][1]
        if (landmarks[3][1] < pseudoFixKeyPoint and landmarks[4][1] < landmarks[3][1]):
          thumbState = 'CLOSE'    
        elif (pseudoFixKeyPoint < landmarks[3][1] and landmarks[3][1] < landmarks[4][1]):
          thumbState = 'OPEN'    

        pseudoFixKeyPoint = landmarks[6][2]
        if (landmarks[7][2] < pseudoFixKeyPoint and landmarks[8][2] < landmarks[7][2]):
          indexFingerState = 'OPEN'    
        elif (pseudoFixKeyPoint < landmarks[7][2] and landmarks[7][2] < landmarks[8][2]):
          indexFingerState = 'CLOSE'     

        pseudoFixKeyPoint = landmarks[10][2]
        if (landmarks[11][2] < pseudoFixKeyPoint and landmarks[12][2] < landmarks[11][2]):
          middleFingerState = 'OPEN'    
        elif (pseudoFixKeyPoint < landmarks[11][2] and landmarks[11][2] < landmarks[12][2]):
          middleFingerState = 'CLOSE'

        pseudoFixKeyPoint = landmarks[14][2]
        if (landmarks[15][2] < pseudoFixKeyPoint and landmarks[16][2] < landmarks[15][2]):
          ringFingerState = 'OPEN'    
        elif (pseudoFixKeyPoint < landmarks[15][2] and landmarks[15][2] < landmarks[16][2]):
          ringFingerState = 'CLOSE'
        
        pseudoFixKeyPoint = landmarks[18][2]
        if (landmarks[19][2] < pseudoFixKeyPoint and landmarks[20][2] < landmarks[19][2]):
          littleFingerState = 'OPEN'    
        elif (pseudoFixKeyPoint < landmarks[19][2] and landmarks[19][2] < landmarks[20][2]):
          littleFingerState = 'CLOSE'
          
       
        if(thumbState == 'CLOSE'):  
              
          if (indexFingerState == 'OPEN' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
            recognizedHandGesture = 1
            print(recognizedHandGesture) # "FOUR"

            if (vel_msg.linear.x != 1.0):
              vel_msg.linear.x = 1.0          
              p1.publish(vel_msg)  

          elif ( indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'CLOSE' and littleFingerState == 'CLOSE'):
            recognizedHandGesture = 2
            print(recognizedHandGesture) # "TREE"   
            if (vel_msg.linear.x != 2.0):
              vel_msg.linear.x = 2.0          
              p1.publish(vel_msg)  

          elif (indexFingerState == 'OPEN' and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' and littleFingerState == 'CLOSE'):
            recognizedHandGesture = 3
            print(recognizedHandGesture) # "TWO"'''
            if (vel_msg.linear.x != 3.0):
              vel_msg.linear.x = 3.0          
              p1.publish(vel_msg)  

          elif (indexFingerState == 'CLOSE' and middleFingerState == 'CLOSE' and ringFingerState == 'CLOSE' and littleFingerState == 'OPEN'):
            recognizedHandGesture = 4
            print(recognizedHandGesture)
            if (vel_msg.linear.x != 4.0):
              vel_msg.linear.x = 4.0          
              p1.publish(vel_msg)   # "FIST"

          elif (indexFingerState == 'CLOSE' and middleFingerState == 'CLOSE' and ringFingerState == 'OPEN'  and littleFingerState == 'OPEN'):
            recognizedHandGesture = 5
            print(recognizedHandGesture)
            if (vel_msg.linear.x != 5.0):
              vel_msg.linear.x = 5.0          
              p1.publish(vel_msg)    # "rocknroll"

          elif ( indexFingerState == 'CLOSE' and middleFingerState == 'OPEN' and ringFingerState == 'OPEN' and littleFingerState == 'OPEN'):
            recognizedHandGesture = 6
            print(recognizedHandGesture)
            if (vel_msg.linear.x != 6.0):
              vel_msg.linear.x = 6.0          
              p1.publish(vel_msg)   # "promise"    
          else:
            recognizedHandGesture = 0
            if(vel_msg.linear.x != 0.0):
              vel_msg.linear.x = 0.0
              p1.publish(vel_msg)
              print('not recognized ')

        if(thumbState == 'OPEN'):
            x1 , y1 = lmList[4][1], lmList[4][2]
            x2 , y2 = lmList[8][1], lmList[8][2]
            cx ,cy = (x1+x2)//2 , (y1+y2)//2

          
            cv2.circle(img,(x1,y1),15,(255,0,255), cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(255,0,255), cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(img,(cx,cy),15,(255,0,255), cv2.FILLED)

            length = math.hypot(x2-x1, y2-y1)
            print(length)
            #hand range 50 - 300 
            #servo_pwm_duty cicle 0 - 100 

            if(length < 50 ):
              #print(vel_msg.linear.x)
              print(recognizedHandGesture)

              cv2.circle(img,(cx,cy),15,(0 ,255,0),cv2.FILLED)
              if(vel_msg.linear.x != 7.0):
                vel_msg.linear.x = 7.0 
                p1.publish(vel_msg) 

            if(length >50 and length< 150):
              print(recognizedHandGesture)
              #print(vel_msg.linear.x)
              if(vel_msg.linear.x != 8.0):
                vel_msg.linear.x = 8.0
                p1.publish(vel_msg)

            if(length > 150):
              print(recognizedHandGesture)
              #print(vel_msg.linear.x)
              if(vel_msg.linear.x != 9.0):
                vel_msg.linear.x = 9.0
                p1.publish(vel_msg)    

        return recognizedHandGesture

        
      while True:

        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:

          #recognizeHandGesture()

          #print(lmList[2])
            recognizedHandGesture = recognizeHandGesture(lmList)
            print("recognized hand gesture: ", recognizedHandGesture) # print: "recognized hand gesture: 5"
      


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                      1, (255, 0, 0), 3)

        cv2.imshow("Img", img)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()          
