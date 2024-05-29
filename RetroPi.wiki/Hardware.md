For the hardware you need a raspberry pi connected to a 32x32 matrix.

![Matrix_small](https://github.com/INF2023AI-Python/RetroPi/assets/155064927/b416a894-d0d5-4124-a014-c2b5be3174fd)

The Raspberry Pi 3 works best for the matrix, cause faster raspberrys will cause flickering on the matrix.

For the controller you can pick a normal game controller or build one by your own, but you have to adjust the the x and y axis, as well as the buttons.

In our project we have a raspberry 3b+ with a 32x32 matrix and a joystick with 4 buttons, interpreted by a arduino, which sends controller signals to the raspberry pi.

![Joystick](https://github.com/INF2023AI-Python/RetroPi/assets/155064927/a9b72ad8-afa5-4a11-ad70-3a5fa9a36403)

The top button is unused.

The left button instantly quits out of the game you are in and sends you the exit screen.

The right button is the Enter button.

The bottom button is the Space button.

The joystick is like you would expect it - top = up, bottom = down, left=left, right=right