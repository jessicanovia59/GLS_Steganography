# GLS_Steganography

Tugas forum GLS untuk Steganography sebagai alternatif C&C

Nama : Jessica Novia 
NIM : 2301866315 
Kelas : LB07 
Jurusan : Cyber Security

Mata Kuliah : COMP6548001 - Programming for Penetration Testing

Steganography sebagai alternatif C&C
Buatlah covert communication dengan memanfaatkan teknik steganography. Injeksi kan command dalam image yang kemudian akan di eksekusi oleh client. Image dapat di simpan di area yang not protected, misalnya IMGUR. Client victim (agent) di arahkan untuk mendownload image dari lokasi tertentu di IMGUR. Setelah di download, maka baca isi steganography yang ada di dalamnya, dan eksekusi. Hasil eksekusi di masukkan kembali ke dalam image dan di upload ke IMGUR.
 
Hints:
1. Gunakan API di IMGUR.
2. Gunakan Image file format PNG. Jangan JPEG. Pelajari struktur PNG,
3. Gunakan Base64 encode untuk informasi yang akan di injek ke Image.
 
 
