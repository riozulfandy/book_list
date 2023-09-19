# Tugas 3

Nama      : Muhammad Mariozulfandy

NPM       : 2206041404

Kelas     : PBP C

Aplikasi  : Book List

1. Apa perbedaan antara form POST dan form GET dalam Django?

= GET digunakan untuk membaca/mengambil data dari server web. GET mengembalikan kode status HTTP 200 (OK) jika data berhasil diambil dari server. Sementara POST digunakan untuk mengirim data (file, data form, dll) ke server. Jika pembuatan berhasil, ia mengembalikan kode status HTTP 201. Berikut beberapa perbedaannya:

POST:

-Nilai variabel tidak ditampilkan di URL

-Lebih aman

-Tidak dibatasi panjang string

-Pengambilan variabel dengan request.POST.get

-Biasanya untuk input data melalui form

-Digunakan untuk mengirim data-data penting seperti password

GET:

-Nilai variabel ditampilkan di URL sehingga user dapat dengan mudah memasukkan nilai variabel baru

-Kurang aman

-Dibatasi panjang string sampai 2047 karakter

-Pengambilan variabel dengan request.POST.get

-Biasanya untuk input data melalui link

-Digunakan untuk mengirim data-data tidak penting

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

= XML adalah bahasa markup yang sangat fleksibel dan dapat digunakan untuk mendefinisikan struktur data yang kompleks. Ini menggunakan tag yang dapat disesuaikan oleh pengguna untuk mendefinisikan elemen data dan hierarki. JSON adalah format data ringkas yang berbasis teks dan memiliki struktur yang mirip dengan objek JavaScript. Ini terdiri dari pasangan nama-nilai (key-value pairs). HTML adalah bahasa markup yang digunakan untuk membuat halaman web. Ini memiliki struktur yang lebih terbatas dan dirancang untuk menampilkan konten dalam bentuk halaman web. Perbedaan utama diantaranya adalah XML digunakan untuk mendefinisikan struktur data yang kompleks, JSON digunakan untuk pertukaran data dalam format ringkas, sedangkan HTML digunakan untuk membuat halaman web dan menampilkan konten. 

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

= JSON adalah format data yang ringkas dan mudah dibaca oleh programmer dalam bentuk (key-value pairs). JSON bagian integral dari JavaScript, sehingga memudahkan penggunaannya dalam lingkungan pengembangan web yang berbasis JavaScript. JSON juga mendukung struktur data yang bersarang (nested), yang memungkinkan representasi data yang kompleks dan hierarkis. Selain itu, format data JSON yang ringan dalam hal ukuran. Ini menghasilkan overhead yang lebih rendah dalam pertukaran data antara klien dan server, yang dapat meningkatkan kinerja dan kecepatan dalam aplikasi web.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

= 

**a. Membuat input form untuk menambahkan objek model (item) pada app sebelumnya.**

- Membuat file baru dengan nama forms.py pada aplikasi main untuk membuat struktur form yang dapat menerima data baru.

```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```

Item merupakan model yang digunakan untuk form (yang telah dibuat pada Tugas 1). Ketika data dari form disimpan, isi dari form akan disimpan menjadi sebuah objek class Item. Fields berisi field dari model Item yang digunakan untuk form.

- Membuat template HTML baru bernama create_item.html untuk menampilkan form untuk membuat item baru.

```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```


- Import beberapa package dan membuat fungsi baru dengan nama create_item yang menerima parameter request untuk membuat form yang membuat objek item baru.

```python
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
```
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_item.html", context)
```
Melakukan render tampilan template create_item.html kemudian membuat objek ItemForm berdasarkan QueryDict yang diinput user, dilakukan validasi, disimpan, dan redirect ke page main.

- Menambahkan button pada main.html yang mengarah url dari fungsi create_item pada view yang telah dibuat untuk membuat form.
```html
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Item
        </button>
    </a>
```

- Membuat routing url pada urls.py yang mengarah ke fungsi create_item untuk pembuatan form. Dengan menambahkan ```path('create-item', create_item, name='create_item')``` pada list urlpatterns.

**b. Menambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.**

- Melihat objek yang sudah ditambahkan dalam format HTML dilakukan dengan memperbarui fungsi show_main dengan menambahkan setiap objek Ttem yang sudah ditambahkan sebelumnya. Karena show_main melakukan render terhadap main.html, main.html juga diperbarui dengan menambahkan tabel yang berisi setiap atribut dari objek Item yang telah dibuat sebelumnya (name, amount, description, date_added).

```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'Nama': 'Muhammad Mariozulfandy',
        'Kelas': 'PBP C',
        'Aplikasi': 'Book List',
        'items': items
    }

    return render(request, "main.html", context)
```
```html
<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
        <th>Date Added</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.description}}</td>
            <td>{{item.date_added}}</td>
        </tr>
    {% endfor %}
</table>
```

- Melihat objek yang sudah ditambahkan dalam format XML, JSON, JSON by ID, dan XML by ID dilakukan dengan memanfaatkan ```django.core.serializers``` untuk transformasi data menjadi format lain seperti XML dan JSON. Untuk XML dan JSON, data yang ditransformasi adalah semua objek pada Item yang telah ditambahkan sebelumnya. Sementara JSON by ID dan XML by ID, data yang ditransformasi adalah data dengan ID yang ditetapkan. Implementasi dilakukan dengan menambahkan fungsi show_xml dan show_json yang menerima parameter request dan show_xml_by_id dan show_json_by_id yang menerima parameter request dan ID.
```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

**c. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin b.**

Ini dilakukan dengan menambahkan path pada list urlpatterns di urls.py untuk masing-masing fungsi views yang telah dibuat.
```python
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), #Menambahkan variabel id karena dipakai sebagai parameter
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), #Menambahkan variabel id karena dipakai sebagai parameter
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tugas 2

Nama      : Muhammad Mariozulfandy

NPM       : 2206041404

Kelas     : PBP C

Aplikasi  : Book List

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
