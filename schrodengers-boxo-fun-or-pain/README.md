> This python script polls the keyboard for one of two keypresses:
  >> (A) INSERT -- 0x82
  >> (B) DELETE -- 0x83

> Each time a button is pressed, a check is done based on a randomly generated 
  flag. Depending on the result, one of two actions happen:
   >> (I)  A buzzer is played at SSH via a HTTP request.
   >> (II) A bright light is flashed in the users face.

> Opting to press both buttons simultaneously or in too short a period of time 
  will result in option (II) occurring.




