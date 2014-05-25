> This python script polls the keyboard for one of two keypresses:
  >> (A) INSERT -- 'x52'
  >> (B) DELETE -- 'x53'

> Each time a button is pressed, a check is done based on a randomly generated 
  flag. Depending on the result, one of two actions happen:
   >> (I)  A buzzer is played at SSH via a HTTP request.
   >> (II) A bright light is flashed in the users face.

> Opting to press both buttons simultaneously or in too short a period of time 
  will result in option (II) occurring.

> NOTE:  To use PyDev, make sure you have the latest Python 2.7 installed
         and have setup your interpreter for PyDev under the name 'Python_2-7'.
         Once both of those are completed, you should be able to import
         from existing if you choose to debug via Eclipse && PyDev.




