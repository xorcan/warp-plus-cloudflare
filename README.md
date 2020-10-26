<h2 align="center"><a href="https://www.google.com/search?&q=s%C4%B1n%C4%B1rs%C4%B1z+warp%2B+verisi+xorcan" alt="Sınırsız WARP+ Verisi (betik)"><img src="https://github.com/xorcan/warp-plus-cloudflare/raw/main/pic.png" width="250"></a></br>
<b>Sınırsız 1.1.1.1 WARP+ Verisi (betik)</b></h2><h4 align="center">buradaki betiklerle 1.1.1.1 WARP+ hesabınızı süresiz olarak reşarj edebilirsiniz.</h4>


<p align="center"><img src="https://img.shields.io/github/languages/code-size/xorcan/warp-plus-cloudflare" alt="Kod Boyutu"> <img src="https://img.shields.io/github/languages/top/xorcan/warp-plus-cloudflare" alt="sınırsız warp+ verisi alma yöntemi"> <img src="https://img.shields.io/github/stars/xorcan/warp-plus-cloudflare" alt="GitHub Yıldızı"> <img src="https://img.shields.io/github/license/xorcan/warp-plus-cloudflare" alt="Lisans"> <img src="https://img.shields.io/github/issues/xorcan/warp-plus-cloudflare" alt="Hatalar"> <img src="https://img.shields.io/github/forks/xorcan/warp-plus-cloudflare" alt="Forklar">

**not: bu betik benim tarafımdan yazılmamıştır. sadece tamamlanmış, türkçeleştirilmiş ve "tek başına çalıştırılabilirlik" eklenmiştir.** 😉

### [?] warp+ nedir?
warp+, daha yüksek hızlar elde etmek ve bağlantınızın internet'in uzun vadede şifrelenmesini sağlamak için cloudflare’nin argo olarak bilinen sanal özel omurgasını kullanır. [daha fazla bilgi (ingilizce)](https://blog.cloudflare.com/announcing-warp-plus/)

### [?] betik nasıl kullanılır? *( windows, mac, linux )*
- öncelikle python'u sisteminize kurun. [python 3.8+](https://www.python.org/downloads/)
  - windows 10 kullanıyorsanız: 
  - herhangi bir klasörde shift tuşuyla birlite sağ tıklayıp powershell'i açın
  - `python` yazın ve enterlayın, sizi mağazaya yönlendirecek.
  - yönlendirse de yönlendirmese de mağazadan python'u ayrıca indirip kurun.
- modül isteklerini yükleyelim:
- aynı yöntemlerle cmd / terminale kopyalayın ve enterlayın: `pip install requests`
- [buradan](https://github.com/xorcan/warp-plus-cloudflare/archive/main.zip) projeyi indirin ve çıkartın (unzip)
- ayıklanan dizinde bir cmd / terminal / kabuk açın
- şu satırı girin: `python warp1.py`
- komut dosyasını çalıştırın ve kullanın

### [?] tek başına çalışabilir betik (warp2.py)
- normal bir kullanıcı için yukarıdaki gayet iyidir. bu sürümü yalnızca ne yaptığınızı biliyorsanız kullanın.
- teknik olarak hiçbir fark yok. ancak bu sürümdeki dosya tek komutta işinizi halleder.
- ayrıca size kimlik sormaz, rahatsız etmez.
- `warp2.py` dosyasını bir düzenleyici ile açın ve `xorcan` değeri yerine warp+ kimliğinizi yazıp kaydedin.
- çalıştırmak için: `python warp2.py`

![](https://github.com/xorcan/warp-plus-cloudflare/blob/master/win.jpg)

### [?] androidde çalıştırmak

- [termux](https://play.google.com/store/apps/details?id=com.termux&hl=tr) uygulamasını yükleyin, açın ve şu komutları sıra sıra girin (kopyalayıp yapıştırabilirsiniz):
- `pkg install git`
- `pkg install python`
- `pip install requests`
- ardından şu komutla giti kendi cihazınıza klonlayın (indirin): 
- `git clone https://github.com/xorcan/warp-plus-cloudflare.git`
- betiğin dizinini açın:
- `cd warp-plus-cloudflare`
- betiği çalıştını:
- `python warp{sürüm numarası}.py`

### [?] warp+ kimliğini (id) nasıl alırım?

1. 1.1.1.1 uygulamasını açın.
2. menü (üç nokta) işaretine tıklayın ☰
3. gelişmiş (advanced) > tanılamalar (diagonistics)
4. i̇stemci yapılandırması (client configuration)'nın altındaki kimlik (id) > basılı tutun ve kopyalayın.

![](https://github.com/xorcan/warp-plus-cloudflare/blob/master/id.jpg)

## [!] uyarı

Bu makaledeki uygulamaların gizlilik sözleşmelerini okuyunuz. Eğer ne yaptığınızı bilmiyorsanız bu işlemlerden uzak durun. Her cihazın yapısı farklıdır, oluşabilecek sorunlardan makale editörü sorumlu tutulamaz.

## [?] lisans

[![GNU GPLv3 Image](https://www.gnu.org/graphics/gplv3-127x51.png)](http://www.gnu.org/licenses/gpl-3.0.en.html)

Tüm sorumluluk kullanıcıya aittir. Kullanabilir, çalışabilir ve paylaşmayı istediğiniz gibi geliştirebilirsiniz. Özellikle, Özgür Yazılım Vakfı tarafından yayımlanan [GNU Genel Kamu Lisansı](https://www.gnu.org/licenses/gpl.html) koşulları altında, lisansın 3. sürümü veya daha sonraki sürümlerinde yeniden dağıtabilir ve/veya değiştirebilirsiniz.
