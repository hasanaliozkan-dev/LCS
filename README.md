# Learning Classifier Systems

## Öğrenme Sınıflandırıcı Sistemi (LCS) Nedir?
Öğrenme Sınıflandırıcı Sistemleri(LCS) Makine Öğrenmesi(ML) ve Genetik Algoritmaların(GA) birleşiminden ortaya çıkmış bir kavramdır. Sınıflandırma problemi, belirli sınıflara ait ögeler kullanılarak sınıf ve öge arasındaki ilişkinin öğrenilmesi ve bu öğrenilen ilişki ile yeni ögelerin sınıflarının tahmin edilmesidir. Öğrenme sınıflandırıcı sistemleri bu işlemi doğadaki evrimsel süreçleri temel alarak gerçekleştirir. Bu öğrenme sınıflandırıcı sistemlerini derin öğrenme sistemleri gibi bir kara kutu olmaktan çıkarır. Biyoloji ve Matematik bilgisi ile öğrenme adımları kolayca açıklanabilir. Öğrenme sınıflandırıcı sistemler sınıflandırma yapmak için konu ile alakalı bir takım kural setlerini kullanırlar. Bu sistemleri genetik algoritmaların sadece sınıflandırma problemleri için modifiye edilmiş versiyonu gibi düşünebiliriz. Genetik algoritmalar ile ilgili Medium makaleme buradan ulaşabilirsiniz. Eğer kural setlerini önceden belirlerseniz en doğru sınıflandırmaya daha hızlı erişeceğiniz aşikardır. Çoğu makine öğrenme yöntemi istatistik temelli olduğu için genellikle yüksek miktarda veriye ihtiyaç duyarken öğrenme sınıflandırıcı sistemleri kural tabanlı işlemler gerçekleştirdiği için çok fazla veri olmadan da iyi belirlenmiş kurallar ile güzel sonuçlar doğurabilir. Tabii ki kural tabanlı dememiz işin içerisinde genetik algoritmalardan kaynaklı rastgeleliğin ortadan kalktığını düşündürtmesin çünkü hala bir rastgelelikten söz etmeliyiz. Çoğu öğrenme sınıflandırıcı sistemler ayrık veriler üzerinde çalışır, bu nedenle eğer devamlı bir veriniz var ise bunu ayrık hale getirmeniz gerekebilir (örneğin bir yaş sütununuz var ve 10 ile 75 arasında değişiyor, sizin bu yaşları küçük aralıklara bölüp her bir aralığı tek bir veri ile ifade etmeniz gerekli → 10–25: 1, 25–45: 2, 45–75:3 gibi). Bu da elimizdeki ayrıntılı veriyi daha sade hale getirdiğimiz için aradaki ilişkiyi kşefetmemizi engelleyebilir aynı zamanda istatiksel olarak veri kaybına dolayısı ile bilgi kaybına yol açar.

## Öğrenme Sınıflandırıcı Sistemlerindeki Terimler

**Kural (Rule):** Basit koşullar. Bu kurallar öğrenme sınıflandırıcı sistemileri tarafından zamanla evrimleşir ve değişir. </br></br>
**Koşul(Condition):** Öğrenme sınıfldandırıcı sisteminin girdisi, diğer bir deyişle bir aksiyon için sağlanması gereken koşul. </br></br>
**Aksiyon (Action):** Öğrenme sınıflandırıcı sisteminin çıktısı, diğer bir deyişle herhangi belirli bir koşul sağlandıktan sonra yapılacak olan eylem. </br></br>
**Örnek Uzay (Sample Space):** Problem alanında bulunan benzersiz(unique) örnekler. </br></br>
**Arama Uzayı (Search Space):** Oluşturulabilecek benzersiz kurallar ve arama uzayı. Aram uzayı öğrenme sınıflandırıcı sisteminin belirlenen kural gösterimi ile örnek uzayına bağlıdır.</br></br>
**Sınıflandırıcı (Classifier):** Kurallar kullanılarak veri setinden öğrenilen istatistiklerdir.</br></br>
**Kapsam (Coverage):** Bir kuralın koşul kısmına uyan örnek uzay.</br></br>
**Niş (Niche):** Bir alanın örnek uzayında komşu örnekler arasında paylaşılan özellik ile karakterize bölge, ortak genler.</br></br>
**Popülasyon (Population):** Çevreden elde edilerek çıkarılım yapılan kuralların tümü.</br></br>
**Eşleşme Kümesi (Match Set):** Öğrenme sınıfladırıcı sistemlerindeki koşullarla eşleşen sınıflandırıcılar. Bu küme aksiyon kümesinin(pekiştirmeli öğrenme), doğru kümesinin(denetimli öğrenme) ve yanlış kümesinin(denetimli öğrenme) üst kümesidir.</br></br>
**Aksiyon Kümesi (Action Set):** Koşulla eşleşen tüm örnekler kümesi. Bu set aynı zamanda pekiştirmeli öğrenmede çevre ile etkileşime girecek bir eylem seçmeye de yarar.</br></br>
**Doğru Kümesi (Correct Set):** Denetimli öğrenmede doğru sınıfı belirten tüm örneklerin kümesi.</br></br>
**Yanlış Kümesi (Incorrect Set):** Denetimli öğrenmede yanlış sınıfı belirten tüm örneklerin kümesi.</br></br>

## Öğrenme Sınıflandırıcı Sistem Tipleri
Birçok farklı Öğrenme sınıflandırıcı sistem vardır fakat bunların hepsi temelde iki tip öğrenme sınıfladırıcı sisteminden gelmektedir. Yazının bu kısmında bu temel iki tip öğrenme sınıflandırıcı sistemden bahsedeceğim.

### 1) Michigan Tipi (Michigan-Style | Cognitive System One)
Michigan Tipi öğrenme sınıflandırıcı sistemi ilk olarak Holland tarafından sunulmuştur [1]. Aşağıdaki şemada bu sistemin ayrıntılı adımları yer almakta. Bu sistemdeki adımlar kullanıcı tarafından belirlenen bir durma kriterine bağlı olarak çalışır. Bu kriter bir eşik değeri ya da belirli bir döngü sayısı olabilir.



### Michigan Tipi Öğrenme Sınıflandırıcı Sistemi Nasıl Çalışır?

**Adım 1:** Bu adımda sistem bir tane örneği çevreden alır ve döngü başlar. Sistem veri kalmayana kadar her bir örneği tek tek alır. Tüm veriler sistemden geçtikten sonra en baştaki örnekten veriler tekrar alınmaya devam eder.
</br></br>
**Adım 2:** Bu adımda örnekler popülasyona [P] geçirilir. Bu kısım sistemin merkezidir. Popülasyon sistemin keşfettiği tüm kuralları içerir. Öğrenme sınıflandırıcı sistemin başlangıçta bir popülasyona ihtiyacı olmadığı için popülasyon genellikle başlangıçta boştur. Eğer ki popülasyon boş ise başka bir kural öğrenme mekanizması olan Kapsam(Coverage) tetiklenir. Kapsam mekanizması sıradaki örnek ile aynı sınıfta rastgele sınıflandırıcılar oluşturur.
</br></br>
**Adım 3:** Bu adımda öğrenme sınıflandırıcı sistemi, mevcut örneğin özellik durumlarıyla eşleşen koşula sahip sınıflandırıcıları popülasyondan seçerek bir eşleştirme kümesi (match set) [M] oluşturur.
</br></br>
**Adım 4:** Bu adımda sistem eşleşme kümesindeki her bir sınıflandırıcının mevcut örnek sınıfını tahminine göre doğru kümesi [C] ve yanlış kümesi [I] olarak iki ayrı kümeye ayırır.
</br></br>
**Adım 5:** Bu adımda eğer doğru kümesi boş ise sistem Kapsam(Coverage) mekanizmasını tekrar tetikler ve mevcut örnek sınıfıyla doğru eşleşen sınıflandırıcılar üretir. Bunun sonucunda eşleşme kümesi [M] ve doğru kümesi [C] güncellenir.
</br></br>
**Adım 6:** Eşleşme kümesindeki her bir eleman için bazı kural parametreleri güncellenir burada güncelleme yaparken elemanın doğru küme ya da yanlış kümeye ait olup olmadığı bir etkendir.
</br></br>
**Adım 7:** Günümüzde içerme(subsumption) mekanizması çoğu sisteme eklenmektedir. Bu mekanizma eşleşme setindeki birebir aynı olan sınıflandırıcıları birleştirip teke düşürür bu adımın sonucunda da eşleşme seti [M] güncellenir.
</br></br>
**Adım 8:** Genetik algoritma bu adımda uygulanır. Genellikle öğrenme sınıflandırıcı sistemler seçici bir genetik algoritma kullanılarlar bunun sonucunda kural popülasyonunun büyük bir kısmı değişmez.
</br></br>
**Adım 9:** Son adım ise silme adımıdır. Bu adımda eğer popülasyon sayısı belirlenen popülasyon sayısının üzerindeyse(genellikle öyledir). Sistem birebir aynı olan sınıflandırıcılardan bir tane kalana kadar siler. Bu durum genetik algoritma uygulamasından sonra popülasyonun küçülmesini ve sonsuzluğa doğru büyümesini engeller.

### 2) Pittsburgh Tipi (Pittsburgh-Style | Learning System One)
Holland'dan sonra Smith ve arkadaşları Pittsburgh Tipi öğrenme sınıflandırıcı sistemini sunmuşlardır[2]. Bu yeni sistem daha çok genetik algoritma işlemi barındırır. Aşağıdaki figürde Pittsburgh tipi öğrenme sınıflandırıcı sistemi gösterilmektedir.

## Literatürdeki Öğrenme Sınıflandırıcı Sistemleri
Yukarıda anlattığım iki model üzerine literatürde bir çok farklı sistem geliştirilmiştir. Bunlar genellikle alanlara özel sınıflandırıcı sistemler olmuştur. Bunlardan ilki Wilson tarafından geliştirilen Sıfırıncı Seviye Sınıflandırıcı(Zeroth-level Classifier)'dır [3]. Bu sistemde popülasyondaki mevcut sınıflandırıcılar ikili alfabe kullanır(0 ve 1). Buna ek olarak '#' sembolü kullanılır. '#' sembolü hem 1 olabilir hem de 0 olabilir. Aslında bu sembolün denk geldiği genler sınıflandırma açısından pekte bir fark yaratmaz. Bir sonraki çıkan sistemde yine Wilson tarafından sunulmuş Genişletilmiş Sınıflandırma Sistemi(Extended Classifier System)'dir[4]. Bu iki sistemin arasındaki fark ise barındırdıkları genetik algoritma içerisindeki uygunluk değerlendirmesi metodu fark etmektedir. Sonrasında yine Wilson tarafından bu sisteme de eklemeler yapılarak XCSF sistemi geliştirilmiştir [5]. Ardından sadece denetimli öğrenme görevleri için Denetimli Sınıflandırıcı Sistemi (Supervised Classifier System - UCS) geliştirilmiştir [6]. Ardından Larry Bull tarafından Genişletilmiş Sınıflandırma Sistemi üzerine kurulu YCS sistemi geliştirilmiştir[7]. Bununla beraber Biyoinformatik amaçlı Hiyerarşik Öğrenme (BioHell) geliştirilmiştir[8]. Son olarak da 2015'te Genişletilmiş Denetimli Takip ve Sınıflandırma Sistemi(Extended Supervised Tracking and Classifying System) geliştirilmiştir[9]. Bu sistemlerin makalelerini referanslar kısmına ekledim eğer ilgileniyorsanız oradan ulaşabilirsiniz. Aynı zamanda Michigan Tipi bir Öğrenme Sınıflandırıcı Sistemi yazdığım Github repo'ma buradan ulaşabilirsiniz.Yukarıda anlattığım iki model üzerine literatürde bir çok farklı sistem geliştirilmiştir. Bunlar genellikle alanlara özel sınıflandırıcı sistemler olmuştur. Bunlardan ilki Wilson tarafından geliştirilen Sıfırıncı Seviye Sınıflandırıcı(Zeroth-level Classifier)'dır [3]. Bu sistemde popülasyondaki mevcut sınıflandırıcılar ikili alfabe kullanır(0 ve 1). Buna ek olarak '#' sembolü kullanılır. '#' sembolü hem 1 olabilir hem de 0 olabilir. Aslında bu sembolün denk geldiği genler sınıflandırma açısından pekte bir fark yaratmaz. Bir sonraki çıkan sistemde yine Wilson tarafından sunulmuş Genişletilmiş Sınıflandırma Sistemi(Extended Classifier System)'dir[4]. Bu iki sistemin arasındaki fark ise barındırdıkları genetik algoritma içerisindeki uygunluk değerlendirmesi metodu fark etmektedir. Sonrasında yine Wilson tarafından bu sisteme de eklemeler yapılarak XCSF sistemi geliştirilmiştir [5]. Ardından sadece denetimli öğrenme görevleri için Denetimli Sınıflandırıcı Sistemi (Supervised Classifier System - UCS) geliştirilmiştir [6]. Ardından Larry Bull tarafından Genişletilmiş Sınıflandırma Sistemi üzerine kurulu YCS sistemi geliştirilmiştir[7]. Bununla beraber Biyoinformatik amaçlı Hiyerarşik Öğrenme (BioHell) geliştirilmiştir[8]. Son olarak da 2015'te Genişletilmiş Denetimli Takip ve Sınıflandırma Sistemi(Extended Supervised Tracking and Classifying System) geliştirilmiştir[9]. Bu sistemlerin makalelerini referanslar kısmına ekledim eğer ilgileniyorsanız oradan ulaşabilirsiniz. Aynı zamanda Michigan Tipi bir Öğrenme Sınıflandırıcı Sistemi yazdığım Github repo'ma buradan ulaşabilirsiniz.
## Referanslar
1. J. H. Holland, "Adaptation," Progress in theoretical biology, pp. 263–293, 1976. </br></br>
2. L. Bull, "Learning Classifier Systems: A Brief Introduction." </br></br>
3. S. W. Wilson, "ZCS: A Zeroth Level Classifier System." </br></br>
4. S. W. Wilson, "Classifier Fitness Based on Accuracy." </br></br>
5. S. W. Wilson, "Classifiers that approximate functions," 2002.</br></br>
6. E. Bernadó-Mansilla and J. M. Garrell-Guiu, "Accuracy-Based Learning Classifier Systems: Models, Analysis and Applications to Classification Tasks," Evol Comput, vol. 11, no. 3, pp. 209–238, Sep. 2003, doi: 10.1162/106365603322365289. </br></br>
7. L. Bull, "A Simple Accuracy-based Learning Classifier System." </br></br>
8. N. Krasnogor and J. Bacardit, "BioHEL: Bioinformatics-oriented Hierarchical Evolutionary Learning," 2006. [Online]. Available: https://www.researchgate.net/publication/28692976 </br></br>
9. R. J. Urbanowicz and J. H. Moore, "ExSTraCS 2.0: description and evaluation of a scalable learning classifier system," Evol Intell, vol. 8, no. 2–3, pp. 89–116, Sep. 2015, doi: 10.1007/s12065–015–0128–8.

