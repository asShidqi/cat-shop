### link web
http://muhammad-fayyed-catshop.pbp.cs.ui.ac.id

# tugas 5
### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

urutan dari yang paling prioritas
1. Inline style
2. External dan internal style sheets
3. Browser default
jika beberapa selector memiliki spesifikasi yang sama, urutan deklarasi di CSS akan diambil, dengan aturan terakhir yang akan diterapkan.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

karena memastikan tampilan dan fungsionalitas aplikasi web dapat menyesuaikan berbagai ukuran layar, dari ponsel hingga desktop. Hal ini meningkatkan user experience karena mereka dapat mengakses aplikasi dengan nyaman tanpa perlu zoom atau scroll berlebihan.

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

- Margin adalah ruang di luar border elemen. Mengatur jarak antar elemen yang berdekatan.
- Border adalah garis yang mengelilingi konten dan padding elemen. Border bisa memiliki ketebalan, warna, dan gaya yang berbeda.
- Padding adalah ruang antara konten elemen dan border. Menambah ruang di dalam elemen tanpa mempengaruhi elemen lain.

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

- Flexbox adalah sistem layout yang digunakan untuk mengatur elemen dalam satu dimensi sebaris atau sebaris kolom. Berguna untuk membuat layout yang dinamis dan mudah diatur tanpa memerlukan banyak pengaturan float atau positioning.
- Grid layout adalah sistem layout dua dimensi (baris dan kolom) yang memungkinkan pengaturan elemen lebih kompleks dan rapi. Grid mempermudah pengaturan layout halaman dengan presisi. Berguna untuk membuat layout yang terstruktur dengan jelas seperti galeri foto atau layout halaman utama.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

- menambahkan fitur untuk hapus cat pada aplikasi dengan menambahkan fungsi baru pada views.py dan menghubungkan padda urls.py. Kemudian tambahkan buttonnya agar interaktif. Lakukan hal yang sama dengan fitur mengedit product. 
- hubungkan project kita dengan tailwind dengan menambah script CDN pada head.html
- buat file global.css di /static/css untuk membuat custom css yang sudah didefinisikan sendiri kemudian tambahkan pada head.html juga seperti tailwind tadi.
- buat styling pada halaman login,register,dan tambah product menggunakan tailwind pada file htmlnya. Kemudian tambahkan navbar yang responsive menggunakan tailwind dengan menambahkan file navbar.html pada templates/ di root directory.


# tugas 4
### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect argumen pertama hanya dapat berupa url sedangkan redirect dapat menerima model,view, atau urls sebagai argumen sehingga lebih fleksibel dan dinamis dalam penggunaannya

### 2. Jelaskan cara kerja penghubungan model Product dengan User!

Pertama, kita menghubungkan model dengan user melalui relasi, seperti menggunakan ForeignKey untuk menghubungkan CatEntry dengan User. Setelah itu, dalam views, kita menambahkan kondisi agar objek dari form tidak langsung disimpan ke database sehingga kita bisa menandai objek tersebut sebagai milik user yang sedang login. Di fungsi view, misalnya pada show_main, kita bisa memfilter entri berdasarkan user yang login menggunakan CatEntry.objects.filter(user=request.user), agar hanya entri milik pengguna tersebut yang ditampilkan. Nama pengguna juga bisa ditampilkan di template dengan mengakses request.user.username melalui context. Setelah semua perubahan ini, kita perlu menjalankan perintah makemigrations dan migrate untuk memperbarui database.

### 3.Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

- Authentication adalah proses verifikasi apakah username dan password yang kita masukan saat login sesuai dengan dalam database
- Authorization adalah memberikan hak akses mengenai apa saja yang dapat diakses oleh pengguna yang login.
- Ketika pengguna login, Django memverifikasi kredensial melalui authentication. Jika valid, Django membuat sesi untuk pengguna dan menyimpan informasi sesi tersebut di cookies pengguna, memungkinkan Django untuk mengenali pengguna pada setiap request berikutnya.
- Penggunaan Authentication Django memiliki modul bawaan django.contrib.auth yang menangani login, logout, dan validasi pengguna.
- Penggunaan Authorization Django menggunakan sistem permissions dan groups yang bisa diatur melalui model User. Django juga menyediakan decorators seperti @login_required untuk membatasi akses ke view tertentu.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan menggunakan sesi yang disimpan di cookies. Setelah login berhasil, Django membuat entri sesi di database dan mengirimkan session ID ke browser pengguna, yang kemudian dikirim kembali pada setiap permintaan untuk mengenali pengguna tersebut. Selain untuk mengelola sesi, cookies juga digunakan untuk menyimpan preferensi pengguna, melacak aktivitas, atau menyimpan data sementara seperti item keranjang belanja. Namun, tidak semua cookies aman, karena ada risiko seperti session hijacking atau cross-site scripting.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

- Aktifkan Virtual Environment: Pastikan virtual environment Django sudah aktif sebelum melanjutkan ke langkah berikutnya.
- Fungsi Registrasi: Tambahkan fungsi register di views.py yang menggunakan UserCreationForm untuk menangani pendaftaran pengguna baru. Jika pendaftaran berhasil, pengguna akan diarahkan ke halaman login dengan pesan sukses.
- Fungsi Login dan Logout: Buat fungsi login_user dan logout_user di views.py. Fungsi login_user menggunakan AuthenticationForm untuk memverifikasi kredensial pengguna dan mengelola sesi pengguna, sedangkan logout_user akan mengakhiri sesi pengguna dan mengarahkan kembali ke halaman login.
- Buat Halaman Template: Buat berkas HTML untuk tampilan register.html dan login.html di direktori main/templates, sehingga pengguna dapat berinteraksi dengan fungsi registrasi dan login.
- Hubungkan Model CatEntry dengan User: Di models.py, tambahkan kolom user sebagai ForeignKey dalam kelas CatEntry, sehingga setiap entri cat dapat diasosiasikan dengan satu pengguna. Dalam fungsi create_cat_entry, pastikan entri cat yang dibuat dihubungkan dengan pengguna yang sedang login.
- Menampilkan Informasi Pengguna: Di fungsi show_main, tambahkan informasi pengguna yang sedang login, termasuk username dan cookie last_login untuk menunjukkan waktu terakhir pengguna login.
- Migrasi Model: Setelah melakukan semua perubahan, jalankan perintah makemigrations dan migrate untuk menerapkan perubahan pada database. Pastikan untuk menjalankan proyek untuk memverifikasi bahwa semua fitur berfungsi dengan baik.

# tugas 3
### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

data delivery dalam sebuah platform berfungsi agar web yang ditampilkan menjadi dynamic yang berubah-ubah bergantung dengan input di database

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

Menurut saya, JSON lebih baik untuk digunakan karena 
memiliki format yang dapat langsung digunakan oleh bebearapa bahasa pemrograman yang lain sehingga mudah untuk melakukan parsing, tetapi tergantung dengan pemakaian juga tidak selalu harus menggunakan JSON untuk implementasi.

JSON lebih populer karena lebih ringan, memiliki sintaks lebih sederhana (mirip dengan objek yang ada di javascript), dan mudah untuk melakukan parsing

### 3.  Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

method is_valid() pada django memudahkan kita untuk memvalidasi data yang dikirim seperti tipe datanya atau aturan yang lain kita terapkan. Hal itu membantu kita untuk memvalidasi apakah input kita valid dan aman untuk diproses.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Kita memerlukan csrf_token untuk menghindari serangan CSRF (Cross-Site Request Forgery). Serangan ini adalah jenis serangan yang memanfaatkan sesi pengguna yang sudah diautentikasi untuk melakukan serangan berbahaya tanpa sepengetahuan.

Jika tidak menambahkan csrf_token akn rentan terhadap penyerangan CSRF. Penyerang dapat membuat permintaan palsu seolah-olah berasal dari pengguna yang sah. Misalya dengan sesi login pengguna yang masih aktif.

Penyerang dapat membuat situs palsu yang jika button di web tersebut di klik dan usernya sudah login di situs kita penyerang dapat mengirim request tanpa disadari oleh pengguna. 

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- pertama sebelum membuat input form saya mengimplementasikan skeleton sebagai kerangka views di base.html agar mengurangi redundansi codenya. Kemudian mengganti primary key menjadi UUID agar id nya tergenerate string random supaya lebih aman.
- Membuat form dengan membuat berkas baru di main forms.py dengan membuat class baru yang meng-inherith dengan ModelForm. Kemduain membuat fungsi baru bernama create_cat_entry untuk menerima parameter request agar dapat menambahkan cat entry agar secara otomatis ketika di submit. Buat juga berkan HTML pada main/templates untuk menampilkan tabel form. tambahkan juga hasil formnya di main.html agar menampilkan hasil cat yang telah dimasukkan. Jangan lupa atur urlpatterns nya gar dapat mengakses file-file tadi.
- buat fungsi yagn dapat mengelola request XML, JSON, XML by ID, dan JSON by ID. Import serialize dan HTTPResponse untuk memprosesnya. Buat fungsi show_xml dan show_json agar menampilkannya dalam format XML dan JSON. Buat juga show_xml_by_id dan show_json_by_id untuk menampilkan data dalam format XML dan JSON dengan ID yang ingin dicari.
- tambahkan semua fungsi sebelumnya untuk melakukan router di urlpattern agar dapat dipanggil di dalam file urls.py

### Mengakses XML
![](/img/xml.png)
### Mengakses JSON
![](/img/json.png)
### Mengakses XML dengan ID tertentu
![](/img/xml_id.png)
### Mengakses JSON dengan ID tertentu
![](/img/json_id.png)


# tugas 2
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- membuat repository di lokal directory dengan nama cat-shop. Mensetup env dan mengactivate. Menginstall requirement. Dan menjalankan startproject untuk membuat project.
- mengpush dari repository lokal ke github.
- membuat aplikasi main dengan startapp pada manage.py
- membuat template main.html untuk tampilan website
- setup models.py untuk mendapat data dari database yang memiliki tabel name, price, description kemudian memigrasinya.
- Kemudian mengonfigurasi router url dari urls.py pada project kemudian meneruskannya pada urls.py pada aplikasi main
- terakhir mendeploy pada pws

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

'''
client request -> urls.py -> views.py -> models.py -> html -> response client
'''

urls.py akan memproses request dan mencocokannya dengan pola URL kemudian akan diarahkan pada view.py. Di dalam view.py akan memproses request dan mengambil data dari database melalui models.py kemudian memasukkan context yang diperlukan untuk dijalankan pada HTML.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

Fungsi git adalah untuk menghubungkan repository lokal kita dengan github sehingga dalam repository lokal kita sendiri juga terstruktur karena memiliki setiap history(commit) dari code kita. Dan juga memudahkan tim kita untuk berkolaborasi karena dapat melakukan brach lebih leluasa untuk setiap orang yang berkontribusi.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django dijadikan permulaan pembelajaran menurut saya karena Django merupakan framework yang memakai bahasa python sehingga lebih friendly untuk newbie karena relatif lebih mudah dipakai. Kemudian Django juga menggunakan MVT yang memisahkan model, view, dan template sehingga dapat membuat pemula consern dalam pemisahan antara tampilan, data, dan logika bisnisnya untuk pengembangan perangkat lunak.

### 5. Mengapa model pada Django disebut sebagai ORM?

Karena Django memungkinkan kita untuk berinteraksi dengan langsung antara database dengan menggunakan objek dalam code daripada menggunakan query SQL secara langsung. Django dapat mengintegrasikan code kita dengan database menggunakan perintah migrate.