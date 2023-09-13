Nama      : Muhammad Mariozulfandy

NPM       : 2206041404

Kelas     : PBP C

Aplikasi  : https://booklist.adaptable.app/main/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

= -Pertama, membuat direktori baru pada lokal untuk menyimpan proyek Django ini. Didalam direktori tersebut akan dibuat virtual environment untuk mengisolasi proyek Django yang akan dibuat. Kemudian, membuat projek Django bernama book_list pada direktori tersebut serta menginstall dependenciesnya (library, framework, atau package).

-Langkah kedua, membuat aplikasi main pada proyek Django tersebut.

-Langkah ketiga, melakukan routing pada proyek agar dapat menjalankan aplikasi main. Ini dilakukan dengan menambahkan main ke list installed app pada settings.py proyek book_list.

-Langkah keempat, membuat model pada aplikasi main dengan menambahkan kelas Item pada models.py dan memiliki atribut wajib name sebagai nama item dengan tipe CharField, amount sebagai jumlah item dengan tipe IntegerField, dan description sebagai deskripsi item dengan tipe TextField.

-Langkah kelima, membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam template HTML main.html yang menampilkan nama aplikasi, nama, dan kelas. Pada langkah ini, dibuat fungsi show_main untuk melakukan render tampilan main.html pada request http yang diminta sesuai dengan dictionary context yang dibuat untuk ditampilkan pada views.py. Kemudian, template main.html akan dibuat dengan memasukkan key dari dictionary context pada views.py untuk menampilkan valuesnya.

-Langkah keenam, membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. Akan ditambahkan path kosong untuk langsung memanggil fungsi yang telah dibuat di views.py yaitu fungsi untuk menampilkan template main.html.

-Langkah ketujuh, menambahkan urls yang dibuat pada aplikasi main pada proyek utama book_list dengan menambahkan path main/ pada urls.py proyek book list.

-Langkah kedelapan, melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat. Hal ini dilakukan dengan membuat repository pada github kemudian melakukan inisialisasi git pada direktori book_list yang pertama dibuat untuk membuat repository lokal dan menambahkan remote untuk menghubungkan repository lokal dan github. Kemudian, melakukan push pada repository github agar berisi proyek yang sudah dibuat. Setelah repository github berisi proyek book_list, menambahkan aplikasi baru pada Adaptable dan melakukan deployment berdasarkan repository yang sudah dibuat.

-Langkah kesembilan, membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta menjawab beberapa pertanyaan.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html!

=![image](https://github.com/riozulfandy/book_list/assets/119402060/8ef346ab-3cf5-46e1-87a6-66520fbbb33a)


3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

= Alasan kita membutuhkan virtual enviroment adalah karena dengan virtual enviroment yang kita buat pada setiap proyek, proyek tersebut dapat kita isolasikan sehingga memiliki dependencies (library, framework, atau package) yang mereka butuhkan sesuai versinya masing-masing. Kita hanya memfokuskan satu proyek pada virtual enviroment yang kita buat sehingga dapat lebih rapih dalam manajemen dependencies proyek. Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun kita sulit menerapkan dependencies yang kita inginkan pada aplikasi ini jika kita memiliki proyek lain pada lokal yang memiliki dependencies yang berbeda.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

=
MVC (Model, View, Controller):

-Model adalah komponen utama arsitektur ini dan mengelola data, logika, serta batasan aplikasi lainnya.

-View berkaitan dengan bagaimana data akan ditampilkan kepada pengguna dan menyediakan berbagai komponen representasi data.

-Controller adalah inti dari logika aplikasi yang memanipulasi Model dan merender tampilan dengan bertindak sebagai jembatan antara keduanya.

MVT (Model, View, Template)

-Model yang mirip dengan MVC ini bertindak sebagai antarmuka untuk data Anda dan pada dasarnya merupakan struktur logis di balik seluruh aplikasi web yang diwakili oleh database seperti MySql, PostgreSQL.

-View menjalankan logika penggunaan website dan berinteraksi dengan Model serta merender template. Ia menerima permintaan HTTP dan kemudian mengembalikan respons HTTP.

-Template adalah komponen yang membuat MVT berbeda dari MVC. Template bertindak sebagai lapisan presentasi dan pada dasarnya adalah kode HTML yang merender data. Konten dalam file-file ini dapat bersifat statis atau dinamis.

MVVM (Model Viem ViewModel)

-Model: Lapisan ini bertanggung jawab atas abstraksi sumber data. Model dan ViewModel bekerja sama untuk mendapatkan dan menyimpan data.

-View: Tujuan dari lapisan ini adalah untuk menginformasikan ViewModel tentang tindakan pengguna. Lapisan ini mengamati ViewModel dan tidak mengandung logika aplikasi apa pun.

-ViewModel: Ini memperlihatkan aliran data yang relevan dengan Tampilan. Selain itu, ini berfungsi sebagai penghubung antara Model dan Tampilan.

Perbedaaan utamanya adalah bagaimana mereka mengatur dan memisahkan tanggung jawab komponen dalam arsitektur aplikasi:

-MVC adalah pola yang banyak digunakan yang dengan jelas memisahkan Model, View, dan Controller. Controller bertindak sebagai jembatan antara Model dan View.

-MVT adalah variasi dari MVC yang digunakan dalam kerangka web Django. Ini menggantikan Controller dengan Template, yang lebih fokus pada logika presentasi data dalam format tampilan HTML.

-MVVM adalah pola yang mendominasi pengembangan aplikasi berbasis data. ViewModel mengambil peran yang lebih kuat dalam mengelola UI dan memastikan bahwa View selalu mencerminkan data yang benar dari Model. Hal ini memungkinkan pemisahan yang kuat antara logika aplikasi (Model), lapisan presentasi (View), dan logika presentasi (ViewModel).
