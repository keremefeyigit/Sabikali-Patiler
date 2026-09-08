# 🐾 Sabıkalı Patiler - Dedektiflik Oyunu

[![HTML5](https://img.shields.io/badge/HTML5-Modern-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-Vanilla-blue.svg)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Security: Cleaned](https://img.shields.io/badge/Repo%20Clean-Zero%20Junk%20Files-brightgreen.svg)](#-güvenlik-ve-kod-temizliği)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSE)

Saf HTML, modern CSS ve Vanilla JavaScript kullanılarak geliştirilmiş; ipuçlarını birleştirerek şüpheli hayvan karakterleri arasından suçluyu bulmaya çalıştığınız interaktif ve eğlenceli bir dedektiflik oyunudur.

---

## 🌟 Oyun Özellikleri

- **İnteraktif Sürükle-Bırak:** Şüpheli profillerini, ipucu kağıtlarını ve kanıtları masa üstünde serbestçe taşıyabilme.
- **Dinamik Vaka Üretimi:** Her turda rastgele ve mantıksal olarak üretilen suçlular, masumlar ve ipucu örgüleri.
- **Detaylı İnceleme (Zoom):** Şüphelilerin kıyafet, aksesuar ve eşkal özelliklerini büyüteçle yakından inceleyebilme.
- **Zengin Görsel & Ses Atmosferi:** Dedektiflik noir temasına uygun ses efektleri ve kart tasarımları.

---

## 🛡️ Güvenlik ve Kod Temizliği

Public kullanıma açılmadan önce repo kapsamlı bir hijyen sürecinden geçirilmiştir:
- **Gereksiz Dosya Temizliği:** Geliştirme/tarayıcı önbelleğinden kalan ~18 MB boyutundaki yabancı betik ve Google API dosyaları (`tsWorker.js`, `editor.main.js`, `gapi` vb.) depodan tamamen temizlenmiştir.
- **Sıfır Dış Bağımlılık:** Oyun tek bir `index.html` dosyası içinde tamamen bağımsız, güvenli ve hafif olarak çalışır.
- **İstemci Tarafı Yürütme:** Sunucuya veri göndermez; gizlilik ve güvenlik açısından tamamen yerel ortamda çalışır.

---

## 🛠️ Teknolojiler

- **HTML5:** Semantik yapı ve veri bağlama.
- **CSS3:** Responsive Flexbox/Grid mimarisi, noir tema stilleri ve animasyonlar.
- **JavaScript (ES6+):** Vaka motoru, sürükle-bırak koordinat matematiği ve durum yönetimi.

---

## 💻 Nasıl Çalıştırılır?

1. Repoyu bilgisayarınıza indirin veya klonlayın:
   ```bash
   git clone https://github.com/keremefeyigit/sabikali-patiler.git
   ```
2. `index.html` dosyasını tarayıcınızda (Chrome, Firefox, Edge vb.) çift tıklayarak hemen oynamaya başlayın.

---

## 📜 Lisans ve Kullanım Koşulları

Bu proje **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)** lisansı ile lisanslanmıştır.

- **İndirme ve Oynama Serbesttir:** Projeyi kişisel/eğitim amaçlı olarak bilgisayarınıza indirebilir, kaynak kodları inceleyebilir ve yerel olarak oynayabilirsiniz.
- **Değiştirme ve Yeniden Dağıtım Yasaktır:** Kaynak kodları üzerinde değişiklik yapılması, çatallanıp türev projeler üretilmesi veya değiştirilmiş sürümlerin dağıtılması yasaktır.
- **Ticari Kullanım Yasaktır:** Proje kodları veya içerikleri ticari olarak satılamaz veya gelir getiren servislerde kullanılamaz.

Detaylı bilgi için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
