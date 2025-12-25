import cv2
import mediapipe as mp
import serial
import time

mp_maos = mp.solutions.hands
mp_desenho = mp.solutions.drawing_utils

porta_arduino = 'COM5' 
velocidade = 9600

try:
    arduino = serial.Serial(porta_arduino, velocidade)
    time.sleep(2)
    print(f"Conectado na {porta_arduino}!")
except:
    print("ERRO DE CONEXÃO: Verifique a porta e feche o Monitor Serial.")

    exit()

maos = mp_maos.Hands(max_num_hands=1) 
webcam = cv2.VideoCapture(0)

while True:
    sucesso, frame = webcam.read()
    if not sucesso:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = maos.process(frame_rgb)

    if resultado.multi_hand_landmarks:
        print("Mão detectada! -> LIGAR")
        try:
            arduino.write(b'1')
        except:
            pass
            
        for landmarks in resultado.multi_hand_landmarks:
            mp_desenho.draw_landmarks(frame, landmarks, mp_maos.HAND_CONNECTIONS)
    else:
        print("Sem mão -> DESLIGAR")
        try:
            arduino.write(b'0')
        except:
            pass

    cv2.imshow("Detector de Mão", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
try:
    arduino.close()
except:
    pass