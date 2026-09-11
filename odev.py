import cv2 
import numpy as np
import os
import glob

girdi_klasoru = "StopSignDataset/StopSignDataset"  
cikti_klasoru = "output_dataset"  

if not os.path.exists(cikti_klasoru):
    os.makedirs(cikti_klasoru)

resim_yollari = glob.glob(os.path.join(girdi_klasoru, "*.*"))

for yol in resim_yollari:
    img = cv2.imread(yol)
    if img is None:
        continue
        
    dosya_adi = os.path.basename(yol)
    
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    alt_kirmizi1 = np.array([0, 100, 100])
    ust_kirmizi1 = np.array([10, 255, 255])
    maske1 = cv2.inRange(hsv, alt_kirmizi1, ust_kirmizi1)
    
    alt_kirmizi2 = np.array([160, 100, 100])
    ust_kirmizi2 = np.array([180, 255, 255])
    maske2 = cv2.inRange(hsv, alt_kirmizi2, ust_kirmizi2)
    
    tam_maske = maske1 + maske2
    
    contours, _ = cv2.findContours(tam_maske, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        en_buyuk_kontur = max(contours, key=cv2.contourArea)
        if cv2.contourArea(en_buyuk_kontur) > 500:
            x, y, w, h = cv2.boundingRect(en_buyuk_kontur)
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            
            merkez_x = x + (w // 2)
            merkez_y = y + (h // 2)
            print(f"[{dosya_adi}] STOP İşareti Merkez Konumu -> X: {merkez_x}, Y: {merkez_y}")
            
            cv2.circle(img, (merkez_x, merkez_y), 5, (255, 0, 0), -1)
            cv2.putText(img, f"Merkez: {merkez_x}, {merkez_y}", (x, y-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cikti_yolu = os.path.join(cikti_klasoru, dosya_adi)
    cv2.imwrite(cikti_yolu, img)

print("Tüm resimler işlendi ve kaydedildi!")
