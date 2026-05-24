# tugas-struktur-data-sorting_binary
Program tersebut dibuat untuk mengurutkan data menggunakan beberapa algoritma sorting, yaitu Merge Sort dan Quick Sort, baik untuk array maupun linked list. Semua algoritma dibuat sesuai aturan tugas, seperti hemat memori, stabil, dan tidak menggunakan fungsi bawaan Python.
Pada bagian awal terdapat class ListNode. Class ini digunakan untuk membuat node pada singly linked list. Setiap node memiliki data dan pointer menuju node berikutnya.
Kemudian terdapat class AdvancedSorter yang menjadi tempat semua fungsi sorting.
Fungsi sort_array() digunakan untuk mengurutkan array menggunakan Merge Sort. Program membuat satu array sementara di awal proses untuk membantu penggabungan data. Hal ini dilakukan supaya penggunaan memori lebih hemat karena tidak membuat array baru terus-menerus saat rekursi berlangsung.
Fungsi _rec_merge_sort() bekerja secara rekursif. Array dibagi menjadi dua bagian terus-menerus sampai setiap bagian hanya memiliki satu elemen. Setelah itu bagian-bagian kecil tersebut digabung kembali dalam keadaan terurut.
Fungsi _merge_virtual() bertugas menggabungkan dua bagian array yang sudah terurut. Program membandingkan elemen dari sisi kiri dan kanan lalu memasukkan nilai yang lebih kecil ke array sementara. Jika ada nilai yang sama, elemen kiri dipilih terlebih dahulu supaya sorting tetap stabil. Setelah proses selesai, hasilnya disalin kembali ke array utama.
Selanjutnya terdapat sort_linked_list() yang digunakan untuk mengurutkan singly linked list menggunakan Merge Sort. Merge Sort dipilih karena lebih efisien untuk linked list dibanding Quick Sort.
Fungsi _split_linked_list() digunakan untuk membagi linked list menjadi dua bagian menggunakan teknik fast pointer dan slow pointer. Slow pointer bergerak satu langkah sedangkan fast pointer bergerak dua langkah. Saat fast pointer mencapai akhir list, slow pointer berada di tengah sehingga list bisa dibagi tanpa menghitung panjang linked list terlebih dahulu.
Fungsi _merge_linked_lists() digunakan untuk menggabungkan dua linked list yang sudah terurut. Program memakai dummy node dan tail pointer agar proses penggabungan lebih mudah. Node lama langsung disambungkan kembali tanpa membuat node baru sehingga penggunaan memori tetap kecil.
Bagian berikutnya adalah partition_quick() yang digunakan pada Quick Sort. Fungsi ini memakai strategi median-of-three untuk memilih pivot. Program membandingkan elemen awal, tengah, dan akhir lalu memilih nilai tengah sebagai pivot. Strategi ini membantu mengurangi kemungkinan worst-case ketika data sudah hampir terurut atau terurut terbalik.
Setelah pivot dipilih, pointer kiri dan kanan bergerak untuk mencari elemen yang salah posisi. Jika ditemukan, kedua elemen ditukar. Setelah proses selesai, pivot ditempatkan pada posisi akhirnya.
Fungsi quick_sort() digunakan untuk menjalankan Quick Sort secara keseluruhan. Program juga menambahkan depth limiter untuk membatasi kedalaman rekursi. Jika rekursi terlalu dalam, program otomatis berpindah ke Merge Sort agar tidak mengalami kompleksitas O(n²).
Secara keseluruhan:


Merge Sort array digunakan karena stabil dan aman untuk data besar.


Merge Sort linked list digunakan karena cocok untuk manipulasi pointer.


Quick Sort dipercepat dengan median-of-three pivot.


Depth limiter digunakan agar Quick Sort tetap aman pada worst-case.


Semua algoritma dibuat hemat memori dan sesuai batasan tugas.

