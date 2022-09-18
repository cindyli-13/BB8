#include "MeOrion.h"

static const char kMotorLeft = 'L';
static const char kMotorRight = 'R';

MeDCMotor left_motor_(M1);
MeDCMotor right_motor_(M2);

static int speed_left_ = 0;
static int speed_right_ = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int speed_left = speed_left_;
  int speed_right = speed_right_;

  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    char motor = command[0];
    int speed = command.substring(1).toInt();

    Serial.println(command);

    switch (motor) {
      case kMotorLeft:
        speed_left = speed;
        break;
      case kMotorRight:
        speed_right = speed;
        break;
      default:
        break;
    }
  }

  if (speed_left != speed_left_) {
    speed_left_ = speed_left;
  
    if (speed_left_ == 0) {
      left_motor_.stop();
    }
    else {
      left_motor_.run(speed_left_);
    }
  }

  if (speed_right != speed_right_) {
    speed_right_ = speed_right;

    if (speed_right_ == 0) {
      right_motor_.stop();
    }
    else {
      right_motor_.run(-speed_right_);
    }
  }

  delay(1);
}
