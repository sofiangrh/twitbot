Readme Versi 1.0 ( Still under construction README, plesse be patient for better documentation  :) )

By Zea (www.zeaja.com)


#Screeshot

![](https://fbcdn-sphotos-g-a.akamaihd.net/hphotos-ak-ash3/1424400_5001940341419_40210314_n.jpg)


# Intro

Ini adalah aplikasi Bot/Robot (Di Program menggunakana bahasa Python) yang berfungsi melakukan "auto favorite" pada twit dengan keyword tertentu. Bot ini menggunakan modul Python Twitter (https://pypi.python.org/pypi/twitter/1.10.0) dan Twitter API untuk melakukan fungsi data mining dan oAuth (auntentikasi).

# Cara Kerja

Mekanisme dasar atau cara kerja bot ini yaitu, anda akan memberikan kata kunci seperti "python", lalu bot akan mencari twit untuk kata kunci tersebut. Setelah selesai mencari, maka bot  akan mulai "mem-favoriting" tweets tsb dari atas ke bawah.

# FYI

Ini BUKANLAH bot penambah follower otomatis!, karna itu akan mengundang aksi banned dari Twitter. Bot ini akan membantu anda menambah follower dengan cara yg lebih "sehat". Yaitu bila anda mem-favorit kan Twit seseorang, mungkin dia akan penasaran siapa yg mem-favoritkan Twit nya. Lalu dia akan mengunjungi profil anda dan akan mengikuti anda jika dia suka dengan twit anda.

# Persiapan

1. Buat dulu sebuah aplikasi di https://dev.twitter.com/
2. dapatkan consumer key, secret dan token nya.
3. Masukan/copas consumer key, secret dan token pada skrip twitbot.py

# Cara install

1. $ git clone https://github.com/alzearafat/twitbot.git
2. $ cp twitbot/twitbot.py /usr/bin
3. $ cd /usr/bin
4. $ sudo easy_install twitter
5. $ python

6.  import twitbot
7.  twitbot.auto_fav('python','6')

NOTE : Silahkan ganti keyword 'python' dengan keyword lain, dan jumlah twit '6' dengan jumlah yg anda inginkan.


# Tested On

1. Linux Fedora 19
2. Python 3
3. Terminator (Terminal Emulator)


# Greetz

1. HN-Community (www.hacker-newbie.org)
2. Linux Fedora Indonesia (www.fedora.or.id)
3. Rara Syakira  <3 (fb.com/syakirah.die)

#END OFF

# Zea

Contact : fb.com/alzea.arafat
