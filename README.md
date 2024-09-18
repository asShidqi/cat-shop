### link web
http://muhammad-fayyed-catshop.pbp.cs.ui.ac.id

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