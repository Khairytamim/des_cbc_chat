# KIJ-F01
Tugas 1 - Implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Cipher Block Chaining (CBC)

Kelompok F01 :
- Fourir Akbar      (5114100115)
- Fikry Khairytamim (5114100192)

## Pendahuluan
Seiring dengan perkembangan teknologi informasi secara pesat, informasi dapat dengan mudah diakses oleh setiap orang. Hingga kini teknologi informasi pun menawarkan berbagai kemudahan bagi penggunanya. Maka dengan itu pula pengguna teknologi ini pun mengalami peningkatan secara pesat. Kian bertambahnya pengguna teknologi informasi dapat mengakibatkan meningkatnya berbagai tindak kejahatan dalam penggunaan teknologi informasi itu sendiri.

Pada suatu sistem jaringan, arus komunikasi data dan keamanan informasi merupakan hal pokok yang harus dijaga. Informasi penting yang dikirimkan melalui jaringan beresiko mengalami penyadapan dan bahkan pengubahan data yang sering dilakukan oleh orang-orang yang tidak bertanggung jawab. Oleh karena itu, untuk menghindari hal tersebut, kita harus melakukan pencegahan dan pengamanan agar dapat mengurangi gangguan terhadap keamanan informasi pada arus komunikasi data dalam sistem jaringan.

Salah satu cara yang dapat dilakukan untuk menjaga kerahasiaan data dan keamanan informasi pada jaringan adalah dengan melakukan teknik ekripsi. Enkripsi adalah proses mengamankan suatu informasi dengan cara mengubah informasi asli (disebut dengan plaintext) menjadi informasi yang terenkripsi (disebut dengan chipertext) dengan menggunakan kunci pada operasi algoritma tertentu, sehingga informasi asli tersebut tidak dapat diketahui secara langsung oleh pihak lain. Berkebalikan dengan proses enkripsi, proses dekripsi digunakan untuk mengembalikan informasi yang terenkripsi (chipertext) menjadi informasi asli (plaintext).

Terdapat banyak algoritma yang dapat digunakan sebagai metode enkripsi dan dekripsi, salah satunya adalah algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Cipher Block Chaining (CBC)

## Dasar Teori
### Data Encryption Standard
Pada bidang kriptografi, Data Encryption Standard (DES) adalah algoritma enkripsi kunci simetrik dan tergolong dalam jenis block cipher. Algoritma ini digunakan untuk mengenkripsi suatu blok plaintext berukuran 64-bit menjadi ciphertext berukuran 64-bit dengan menggunakan kunci yang diinputkan oleh user.

### Cipher Block Chaining
Mode operasi Cipher Block Chaining (CBC) merupakan salah satu mode operasi block cipher yang menggunakan vektor inisialisasi (initialitation vector/IV) dengan ukuran tertentu (ukurannya sama dengan satu blok plaintext). Pada mode operasi ini plaintext dibagi menjadi beberapa blok, kemudian masing-masing blok dienkripsi dengan ketentuan blok plaintext pertama dienkripsi lebih dahulu. Sebelum dienkripsi, plaintext di-XOR dengan IV. Lalu, hasil XOR tersebut dienkripsi hingga menghasilkan ciphertext. Selanjutnya, ciphertext tersebut digunakan sebagai IV untuk proses penyandian blok plaintext selanjutnya.

## Langkah Implementasi
### Langkah Pada Data Encryption Standard (DES)
1. Generate Subkeys <br/>
1.1 Memasukkan key yang ingin digunakan. Key ini akan sama dengan key yang akan digunakan untuk proses decryption.
Key juga jumlahnya harus tepat 64 bit <br/>
1.2 Key akan dipermutasi dengan menjadi 56 bit <br/>
1.3 Key akan dibagi dua menjadi C0 (28 bit pertama) dan D0 (28 bit terakhir) <br/>
1.4 Setiap C0 dan Do di shift ke kiri menjadi C1 dan D1. C1D1 akan menjadi subkey ke-1 atau K1 <br/>
1.5 Lakukan langkah 1.4 hingga didapatkan K16 <br/>

2. Generate Chiper Text <br/>
2.1 Message yang ingin dienkripsi kan dilakukan permutasi awal (Initiate Permutation)
2.2 Setalah itu, binary yang didapatkan akan dibagi dua menjadi L0 (32 bit pertama) dan R0 (32 bit terakhir) <br/>
2.3 Lalu dilakukan iterasi 16 kali dengan ketentuan L1 = R0 dan R1 = L0 = f(Ro, K1) (Rincian rumus ini akan <br/>
dilampirkan kemudian) <br/>
2.4 Hasil iterasi ke-16 adalah L16 dan R16 yang kemudian digabungkan <br/>
2.5 L16+R16 adalah hasil akhir dari chiper text <br/>

## Teknik Operasi
Berikut ini merupakan beberapa teknik operasi yang digunakan dalam implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Cipher Block Chaining (CBC):
### Permutasi
Permutasi adalah teknik operasi yang digunakan untuk menyusun urutan input biner dalam urutan yang berbeda dari urutan semula sesuai dengan urutan pada tabel mutlak atau statis yang telah ditetapkan. 
### Left Shift
Left Shift adalah teknik operasi yang digunakan untuk melakukan pergeseran urutan input biner ke arah kiri sebanyak nilai pergeseran yang telah ditetapkan pada tabel mutlak atau statis. 
### XOR
XOR (Exclusive OR) adalah teknik operasi yang digunakan untuk menghasilkan angka biner yaitu 0 atau 1. Teknik operasi ini akan menghasilkan keluaran angka biner 0 apabila kedua inputan sama, dan menghasilkan keluaran angka biner 1 apabila kedua inputan berbeda. 
### S-Box
S-Box (Substitution-Box) adalah teknik operasi yang digunakan untuk menggantikan nilai input biner menjadi nilai biner pada state yang ditunjuk pada tabel mutlak atau statis. Nilai baris yang ditunjuk merupakan gabungan nilai input biner bit pertama dan bit terakhir. Sisanya merupakan nilai kolom yang ditunjuk. 

### Langkah implementasi pada DES dengan algoritma Cipher Block Chaining
Berikut ini merupakan langkah implementasi algoritma Data Encryption Standard (DES) dengan menggunakan mode operasi Cipher Block Chaining (CBC):
1. Enkripsi <br/>
1.1 CBC menggunakan plaintext sebagai input pada algoritma DES <br/>
1.2 Plaintext nantinya akan di XOR dengan IV <br/>
1.3 Output dari XOR antara plaintext dan IV akan dienkripsi dengan key yang sudah diberikan <br/>
1.4 Hasil akhir yang keluar akan digunakan sebagai IV untuk putaran selanjutnya <br/>

2. Dekripsi <br/>
2.1 Input text yang diinputkan oleh user akan didecrypt dengan key yang sudah diberikan <br/>
2.2 Output dari hasil decrypt tersebut akan diXOR dengan IV <br/>
2.3 Hasil XOR tersebut merupakan hasil teks aslinya <br/>
2.4 Input text yang diinputkan tadi akan dijadikan sebagai IV di putaran selanjutnya <br/>

### Langkah implementasi pada DES dengan algoritma Cipher Block Chaining
1. Jalankan server.py dengan mengetikkan python server.py
![selection_004](https://cloud.githubusercontent.com/assets/16026826/24903607/22fd6180-1ed8-11e7-84e8-300295699d5c.png)
2. Jalankan client.py dengan mengetikkan python client.py
![selection_005](https://cloud.githubusercontent.com/assets/16026826/24903658/3e01f112-1ed8-11e7-8782-ff2811d079b0.png)
3. Dari client memulai mengirimkan chat ke server
![selection_006](https://cloud.githubusercontent.com/assets/16026826/24903685/51fdf968-1ed8-11e7-8213-a4fe881ab5d6.png)
4. Server menerima pesan dari client, dan server membalas mengirimkan pesan ke client
![selection_007](https://cloud.githubusercontent.com/assets/16026826/24903700/60c7b65a-1ed8-11e7-8368-5b39d2f091e3.png)

## Kesimpulan
## Saran
1. Semua implementasi algoritma yang kami buat menggunakan format yang sedang dibutuhkan. Misalkan sedang membutuhkan format string, maka kami merubahnya ke string. Lalu ketika butuh sebaga integer, kami merubahnya kembali menjadi integer.
2. Implementasi dengan bahasa C/C++ akan jauh lebih cepat dari Python. Hanya saja Python akan jauh lebih mudah untuk dibuat.
3. Terdapat library crypto pada Python. Tanpa harus membangun program sendiri, Python mempunya library untuk DES. import DES

## Terima Kasih

## Referensi
1. https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation
2. http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
3. http://homepage.usask.ca/~dtr467/400/figure2-des_block.gif
4. PPT Pak Tohari - secuity 04
