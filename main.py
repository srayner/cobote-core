import zmq
import time
import traceback

from servo import Servo

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

servo = Servo()
servo.set_speed(50)
servo.set_target(180)


def service_message(message):
    global servo;
    if message == 'RESET':
        servo.set_target(0)


while True:
    servo.update_position()
    try:
        msg = socket.recv_string(zmq.NOBLOCK)
        print(msg)
        service_message(msg)
        socket.send_string(str(servo.position))
    except zmq.ZMQError as e:
        if e.errno == zmq.EAGAIN:
            pass  # no message was ready (yet!)
        else:
            traceback.print_exc()

