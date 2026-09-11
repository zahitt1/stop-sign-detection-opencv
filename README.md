# stop-sign-detection-opencv
stop sign detection and coordinate extraction with opencv 
# Stop Sign Detection using OpenCV

Bu proje, görüntü işleme teknikleri (OpenCV) kullanılarak otonom araçlar (rover vb.) için Dur tabelalarının tespit edilmesini ve merkez koordinatlarının (X, Y) bulunmasını sağlar.

## Kullanılan Yöntemler
- **Görüntü İşleme:** Gaussian Blur, HSV renk uzayı dönüşümü ve Maskeleme.
- **Kontur Analizi:** En büyük alanlı kırmızı objenin bulunması ve merkez koordinatlarının hesaplanması.

## Kurulum ve Çalıştırma
Gerekli kütüphaneleri kurmak için:
`pip install opencv-python numpy`

Kodu çalıştırmak için:
`python odev.py`

---

## Analiz ve Değerlendirme Soruları

**a. Algoritma gerçek hayatta kullanılabilir mi? Ne kadar doğru çalışıyor?**
* Gerçek hayatta, özellikle otonom bir araçta tek başına kullanılması güvenli değildir. 
* Temiz veri setlerinde ve ideal ışık koşullarında (gündüz, net çekim) doğruluğu yüksektir.
* Ancak ortam karmaşıklaştığında veya hava karardığında doğruluk oranı hızla düşer. Sadece kısıtlı ve kontrollü ortamlarda işe yarar.

**b. Eğer algoritma yetersizse sebepleri nedir?**
* **Sadece renge bağımlı olması:** Kod sadece kırmızı renk tonlarına (HSV) ve alan büyüklüğüne bakıyor. Tabelanın sekizgen şeklini analiz etmiyor.
* **Işık hassasiyeti:** Gölge, gece karanlığı veya aşırı güneş parlaması kırmızı tonlarını değiştirdiği için algoritma tabelayı kaçırabiliyor.
* **Yanlış pozitifler:** Ekranda dur tabelasından daha büyük kırmızı bir nesne (örneğin kırmızı bir araba veya tuğla duvar) varsa, algoritma o nesneyi dur tabelası zannedip yanlış koordinat verir.

**c. Başka ne gibi yöntemler engel/nesne tespitinde kullanılabilir? Neden onlar tercih edilmeli?**
* **YOLO (You Only Look Once) veya SSD:** Derin öğrenme tabanlı bu modeller, nesneleri sadece rengiyle değil, şekli ve genel yapısıyla (feature extraction) öğrenir.
* **Haar Cascade veya HOG:** Klasik makine öğrenmesi yöntemleridir. Renk yerine kenar, köşe ve piksel gradyanlarına odaklanırlar.
* **LiDAR ve Ultrasonik Sensörler:** Kameradan bağımsız olarak fiziksel engelleri tespit etmek için mesafe sensörleri kullanılabilir.
* **Neden tercih edilmeli:** Bu yöntemler renk yanılsamalarına düşmez (kırmızı araba vs. dur tabelası). Işık değişimlerine karşı çok daha dirençlidirler ve gerçek zamanlı, yüksek doğruluklu sonuçlar üretirler. Eğitilmiş bir model, nesnenin gerçekten "ne" olduğunu anlar.
