# OpenCV ile STOP Trafik İşareti Tespiti

Bu proje, otonom bir robotun (rover) çevresindeki "STOP" trafik işaretlerini görüntü işleme teknikleri kullanarak tespit etmesini sağlayan bir Python uygulamasıdır. Proje, renk tespiti (color detection) algoritmaları kullanılarak OpenCV kütüphanesi ile geliştirilmiştir.

##  Proje Özeti
Otonom araçların engellerden kaçınması ve trafik kurallarına uyması amacıyla, kırmızı renk filtrelemesi (HSV renk uzayı) yapılarak "STOP" tabelası tespit edilmektedir. 
Algoritma adım adım şu işlemleri gerçekleştirir:
1. Görüntüye Gaussian Blur uygulanarak gürültü azaltılır.
2. Görüntü BGR renk uzayından HSV renk uzayına çevrilir.
3. Kırmızı renk için belirlenen alt ve üst eşik değerleri (threshold) ile maskeleme yapılır.
4. Kontur tespiti (`findContours`) yapılarak en büyük kırmızı alan tespit edilir.
5. Tespit edilen işaret Bounding Box (sınır kutusu) içerisine alınır.
6. İşaretin rover'a göre konumunu anlamak için karenin merkez piksel koordinatları (x, y) hesaplanır.

##  Gereksinimler
Kodu çalıştırabilmek için bilgisayarınızda Python yüklü olmalı ve aşağıdaki kütüphanelerin kurulumu yapılmalıdır:

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy (`numpy`)

