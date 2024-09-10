### link web
http://pbp.cs.ui.ac.id/muhammad.fayyed/catshop

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