import RPi.GPIO as GPIO
from logging import getLogger, DEBUG

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


def main():
    logger = getLogger(__name__)
    logger.debug('agent program start ...')

    lt = LineTrace()

    lt.run()


class TraceModule:
    """ line trace module. belong to 1 motor and 3 sensor """

    def __init__(self, pin_map):
        self.logger = getLogger(__name__)

        self.__motor_pin = pin_map['motor']
        self.__left_sensor_pin = pin_map['left_sensor']
        self.__mid_sensor_pin = pin_map['mid_sensor']
        self.__right_sensor_pin = pin_map['right_sensor']

        GPIO.setup(__motor_pin, GPIO.OUT)
        GPIO.setup(__left_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(__mid_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(__right_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.motor = GPIO.PWM(__motor_pin, 50)
        self.motor.start(0)

    def __del__(self):
        self.motor.stop()
        GPIO.cleanup()


class LineTrace:
    """ line trace logic """

    def __init__(self):
        self.logger = getLogger(__name__)

        __pin_map_1['motor'] = 1
        __pin_map_1['left_sensor'] = 2
        __pin_map_1['mid_sensor'] = 3
        __pin_map_1['right_sensor'] = 4

        __pin_map_2['motor'] = 1
        __pin_map_2['left_sensor'] = 2
        __pin_map_2['mid_sensor'] = 3
        __pin_map_2['right_sensor'] = 4

        __pin_map_3['motor'] = 1
        __pin_map_3['left_sensor'] = 2
        __pin_map_3['mid_sensor'] = 3
        __pin_map_3['right_sensor'] = 4

        __pin_map_4['motor'] = 1
        __pin_map_4['left_sensor'] = 2
        __pin_map_4['mid_sensor'] = 3
        __pin_map_4['right_sensor'] = 4

        self.trace_module[1] = TraceModule(__pin_map_1)
        self.trace_module[2] = TraceModule(__pin_map_2)
        self.trace_module[3] = TraceModule(__pin_map_3)
        self.trace_module[4] = TraceModule(__pin_map_4)

        self.head = 1

        self.logger.debug("Line Trace robot initialized")

    def go_forward(self):
        pass

    def change_front_face(self):
        pass

    def run(self):
        pass

    def __del__(self):
        for module_iter in self.trace_module:
            del module_iter

        self.logger.debug('free all instance')


if __name__ == "__main__":
    main()
