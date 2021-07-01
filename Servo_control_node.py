import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
import time 
from std_msgs.msg import Float32
import RPi.GPIO as GPIO

class MinimalSubscriber(Node):
 servoPIN1 = 17 
 servoPIN2 = 18
 servoPIN3 = 25 #FOR BOTTOM SERVO
 servoPIN4 = 12 #FOR HEAD SERVO
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(servoPIN1, GPIO.OUT)
 GPIO.setup(servoPIN2, GPIO.OUT)
 GPIO.setup(servoPIN3, GPIO.OUT)
 GPIO.setup(servoPIN4, GPIO.OUT)

 p1 = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
 p2 = GPIO.PWM(servoPIN2, 50) # GPIO 17 for PWM with 50Hz
 p3 = GPIO.PWM(servoPIN3, 50) # GPIO 17 for PWM with 50Hz
 p4 = GPIO.PWM(servoPIN4, 50) # GPIO 17 for PWM with 50Hz

 p1.start(2.5) # Initialization
 p2.start(2.5) # Initialization
 p3.start(2.5) # Initialization
 p4.start(2.5) # Initialization
     
 x =Float32()
 previous_value = 2.5


 def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
         Twist,
         '/cmd_vel',
            self.listener_callback,
        10)
        '''self.p17 = self.create_publisher(Int16, '/gpio_pwm_17', 10)
        self.p18 = self.create_publisher(Int16, '/gpio_pwm_18', 10)
        self.p25 = self.create_publisher(Int16, '/gpio_pwm_25', 10)
        self.p14= self.create_publisher(Int16, '/gpio_pwm_12', 10)'''
    
    
        

 def listener_callback(self, vel_msg):
        print(vel_msg.linear.x)
        try:
            
                if(vel_msg.linear.x  == 1.0):
                    self.x = 2.5
                    self.p3.ChangeDutyCycle(self.x)
                elif(vel_msg.linear.x  == 2.0):
                    self.x = 7.5
                    self.p3.ChangeDutyCycle(self.x)
                elif(vel_msg.linear.x  == 3.0):
                    self.x = 12.5
                    self.p3.ChangeDutyCycle(self.x)

                elif(vel_msg.linear.x  == 4.0):
                    self.x = 2.5
                    self.p1.ChangeDutyCycle(self.x)
                    self.p2.ChangeDutyCycle(self.x)
                elif(vel_msg.linear.x  == 5.0):
                    self.x = 7.5
                    self.p1.ChangeDutyCycle(self.x)
                    self.p2.ChangeDutyCycle(self.x)
                elif(vel_msg.linear.x  == 6.0):
                    self.x = 12.5
                    self.p1.ChangeDutyCycle(self.x)
                    self.p2.ChangeDutyCycle(self.x)

                elif(vel_msg.linear.x  == 7.0):
                    self.x = 2.5
                    self.p4.ChangeDutyCycle(self.x)
                    print(self.x)
                elif(vel_msg.linear.x  == 8.0):
                    self.x = 7.5
                    self.p4.ChangeDutyCycle(self.x)
                    print(self.x)

                elif(vel_msg.linear.x  == 9.0):
                    self.x = 12.5
                    self.p4.ChangeDutyCycle(self.x)
                    print(self.x)
                else:
                    self.x = self.previous_value
                    self.p4.ChangeDutyCycle(self.x)
                    print(self.x)   
        

                    
                
        except KeyboardInterrupt:
            self.p1.stop()
            self.p2.stop()
            self.p3.stop()
            self.p4.stop()
            GPIO.cleanup()

        




def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()