# python-denemeler
Bazı Python Scriptleri

### [Gauss Alan Hesabı - Shoelace formula](https://github.com/vyscnktn/python-denemeler/blob/main/gauss-area-calculation.py)

Ayakkabı bağı formülü, ayakkabı bağı algoritması veya ayakkabı bağı yöntemi, köşeleri düzlemdeki Kartezyen koordinatlarıyla tanımlanan basit bir çokgenin alanını belirlemek için matematiksel bir algoritmadır.

Bir poligonun alanını hesaplarken sıklıkla Gauss alan yöntemini kullanırız. 
<img width="1291" alt="image" src="https://user-images.githubusercontent.com/49782611/174577261-3dbb9f18-1627-48f1-8461-2f9344286116.png">
Alanı hesaplamak her ne kadar basit olsa da, fazla işlem yapıyor olmamızdan dolayı hata yapmamız oldukça muhtemeldir. Yukarıda göründüğü gibi bir karne üzerine doldurmak hata yapmamıza engel olsa da basit bir işlemin oldukça uzamasına sebep oluyor. Basit bir fonksiyon ile numpy array tipinde verilen koordinat bilgisini hesaplayabiliriz.

### [Rastgele Sayı Üretimi](https://github.com/vyscnktn/python-denemeler/blob/main/random_operations.py)

[0.0, 1.0] aralığında, herbiri eşit olasılıkla dağılmış x1, x2, …xn sayılarını üretmek istiyoruz. Bunun için, herhangi bir x0 (başlatıcı) değerinden başlayarak çarpma ve toplamalarla bir x1 sayısı üretir, sonra bunu [0,1] aralığına getiririz. Bu x1 sayısına aynı kuralı uygulayıp x2 sayısını buluruz, Buna göre, n. iterasyondaki sayı xn ise,

xn+1 = (axn + b) % c

bağıntısıyla bulunan xn+1 sayısı giderek rastgele bir karakter alır.

Örneğin,

a = 7, b = 11, c = 10 olsun ve x0 = 12 sayısıyla başlamış olalım:

x1 = 7 * 12 + 11 % 10 = 95 % 10 = 5 → x1 = 0.5

x2 = 7 * 5 + 11 % 10 = 46 % 10 = 6 → x2 = 0.6

x3 = 7 * 6 + 11 % 6 = 53 % 10 = 3 → x3 = 0.3

olur. Bu 0.5, 0.6, 0.3 sayıları başlangıç değer 12 için üretilmiş oldular.

Böyle çalışan bir fonksiyonu oluşturmak için iki şey gerekir;

Uygun a, b, c sabitleri,
Program başlatıcı bir x0 değeri.
Hangi (a, b, c) üçlülerinin uygun olduğu literatürde belirlenmiştir. (http://numerical.recipes/book/book.html)

Bu kitaptan alınan üç sayı,

a = 211, b = 1663, c = 7875

![image](https://user-images.githubusercontent.com/49782611/175520046-b4b670e4-297f-4952-b061-4a0588770cbd.png)

Her ne olursa olsun bu fonksiyon bize [0,1] aralığında düzgün dağılmış rastgele sayıları verecektir. “RandomState” değerinin aynı olduğu durumda da hangi bilgisayarda olduğu farketmeksizin aynı çıktıları alırız.

Peki bu sayılar gerçekten rassal mıdır? Hayır rassal değildir. Eğer gerçekten rassal olsaydı her seferinde aynı başlatıcı değerini kullansak bile farklı çıktılar elde ederdik.

Bu şekilde [0,100] aralığında dağılımı incelemek istediğimizde, düzgün bir şekilde dağıldığını görürüz. (Normal Dağılım değil!)

![image](https://user-images.githubusercontent.com/49782611/175520299-e3509350-e3c6-4bcf-bf78-455510d1f4e9.png)

Burada önemli olan nokta şudur: Üretecin verdiği sayıların dizilişi, rastgele dizilişin iyi bir temsili olur. Yani binlerce kez yazı-tura atarsak, yazı gelme olasılığı 0.5'e yakınsar.

