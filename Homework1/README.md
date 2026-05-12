# Homework 1 — Weather Temperature Guessing Game (TCP Socket)

CMPE 472 ödev 1 kapsamında geliştirilen, **TCP soketleri** kullanan bir istemci–sunucu uygulaması.

## 🎯 Amaç

Sunucu, `weathers.xlsx` dosyasından **rastgele bir şehir** seçer ve istemciden o şehrin sıcaklığını **3 deneme** içinde tahmin etmesini bekler. İstemci her tahminin ardından `Higher` / `Lower` ipuçları alır. Tahmin, gerçek değerin **±%10 toleransı** içindeyse başarılı sayılır.

## 📁 Dosyalar

| Dosya | Açıklama |
| --- | --- |
| `server.py` | `localhost:8888` üzerinde dinleyen, Excel'den şehir seçip oyunu yöneten sunucu. |
| `client.py` | Sunucuya bağlanıp kullanıcıdan tahmin alan istemci. |
| `weathers.xlsx` | Şehir (`City`) ve sıcaklık (`Temp`) sütunlarını içeren veri kaynağı. |
| `CMPE472_HW1EnginSametDedeSection1.pdf` | Ödev raporu. |

## 🚀 Çalıştırma

```bash
# 1) Sunucuyu başlat
python server.py

# 2) Yeni bir terminalde istemciyi çalıştır
python client.py
```

İstemci tarafında istendiğinde sıcaklık tahmininizi girin. Oyunu sonlandırmak için `END` yazabilirsiniz.

## 📦 Gereksinimler

```bash
pip install pandas openpyxl
```
