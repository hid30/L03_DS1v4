# Proyek Pertama : Menyelesaikan Permasalahan Human Resource Jaya-Jaya Maju

## Business Understanding 
Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun telah menjadi perusahaan yang cukup besar, perusahaan masih kesulitan dalam mengelola karyawannya. Hal tersebut berimbas pada tingginya attrition rate hingga lebih dari 10%. Attrition rate merupakan rasio dari jumlah karyawan yang keluar dengan total karyawan keseluruhan. Dalam konteks sumber daya manusia (SDM), attrition rate dapat merujuk pada tingkat perpindahan karyawan baik melalui pengunduran diri (resign), pensiun, atau pemutusan hubungan kerja oleh perusahaan. Attrition yang tinggi menjadi indikator masalah dalam pengelolaan karyawan karena perusahaan tidak mampu memenuhi kepuasan karyawan dalam bekerja baik dalam pengembangan karir, lingkungan kerja, hingga pada upah yang diberikan. Oleh karena itu diperlukan analisis lanjutan untuk mengetahui penyebab attrition yang terjadi di Jaya jaya maju agar perusahaan dapat meningkatkan dan memperbaiki pengelolaan karyawan. 

## Permasalahan Bisnis
Tingkat attrition yang tinggi membawa deretan permasalahan bisnis. Beberapa permasalahan bisnis yang diakibatkan oleh attrition yang tinggi sebagai berikut :
1. Operasional bisnis perusahaan terganggu terutama yang berkaitan dengan aspek produktivitas. Umumnya suatu pekerjaan mampu menghasilkan tingkat produktivitas yang optimal ketika jumlah tenaga kerja optimal. Ketika seseorang keluar maka ada pekerjaan yang menghadapi kekurangan tenaga kerja sehingga output yang dihasilkan tidak optimal seperti sebelumnya.
2. Operasional bisnis perusahaan yang terganggu menyebabkan penurunan output produksi. Jika perusahaan ini menjadi salah satu perusahaan yang memproduksi suatu komponen atau produk mentah (perusahaan hulu/supplier) dari sistem rantai bisnis maka perusahaan hilir akan mengganti suppplier baru.   
4. Menurunkan efisiensi biaya perusahaan, mengingat perusahaan perlu merekrut kembali tenaga kerja baru untuk menggantikan tenaga kerja yang telah keluar. Ketika proses perekrutan sering terjadi tentu akan menambah biaya perekrutan karyawan.
5. Pada akhirnya perusahaan tidak lagi kompetitif dengan kompetitor yang eksis bahkan dapat mengalami kondisi kebangkrutan.
6. Terancamnya reputasi perusahaan, perusahaan akan di cap tidak mampu mengelola karyawan dengan baik. Dalam kondisi tertentu, perusahaan dapat dituntut oleh karyawan jika karyawan yang keluar menghadapi masalah yang mengancam haknya (misalnya lingkungan kerja yang buruk yang disebabkan adanya ancaman dari atasan dsb).

## Cakupan Proyek
1. Melakukan tahapan analisis data mulai dari data wrangling hingga EDA untuk mengetahui struktur data, pola dan faktor - faktor yang mempengaruhi keluarnya karyawan (attrition).
2. Membangun model yang dapat memprediksi attrition dengan menggunakan algoritma machine learning yang relevan (logistic regression).
3. Membuat dashboard bisnis untuk memvisualisasikan hasil temuan.
4. Memberikan rekomendasi tindakan yang revelan dengan hasil analisis sebelumnya. 

## Persiapan
Sumber data yang digunakan dalam proyek ini berasal dari https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv. Dalam dataset terdiri dari 35 kolom atau fitur yakni sebagai berikut:
- EmployeeId - Employee Identifier
- Attrition - Did the employee attrition? (0=no, 1=yes)
- Age - Age of the employee
- BusinessTravel - Travel commitments for the job
- DailyRate - Daily salary
- Department - Employee Department
- DistanceFromHome - Distance from work to home (in km)
- Education - 1-Below College, 2-College, 3-Bachelor, 4-Master,5-Doctor
- EducationField - Field of Education
- EnvironmentSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
- Gender - Employee's gender
- HourlyRate - Hourly salary
- JobInvolvement - 1-Low, 2-Medium, 3-High, 4-Very High
- JobLevel - Level of job (1 to 5)
- JobRole - Job Roles
- JobSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
- MaritalStatus - Marital Status
- MonthlyIncome - Monthly salary
- MonthlyRate - Mounthly rate
- NumCompaniesWorked - Number of companies worked at
- Over18 - Over 18 years of age?
- OverTime - Overtime?
- PercentSalaryHike - The percentage increase in salary last year
- PerformanceRating - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
- RelationshipSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
- StandardHours - Standard Hours
- StockOptionLevel - Stock Option Level
- TotalWorkingYears - Total years worked
- TrainingTimesLastYear - Number of training attended last year
- WorkLifeBalance - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
- YearsAtCompany - Years at Company
- YearsInCurrentRole - Years in the current role
- YearsSinceLastPromotion - Years since the last promotion
- YearsWithCurrManager - Years with the current manager

Setup environment:
Apabila menginstal Python melalui Anaconda ataupun miniconda, Anda dapat menggunakan conda sebagai package manager dan environment management system. Berikut merupakan tahapan dalam membuat virtual environment menggunakan conda untuk melakukan prediksi.

1. Buka terminal atau PowerShell.
2. Jalankan perintah berikut.
    ```
     conda create --name prediksi_attrition python=3.9
    ```
3. Aktifkan virtual environment dengan menjalankan perintah berikut.
    ```
    conda activate prediksi_attrition
    ```
4. Instal semua library yang dibutuhkan menggunakan perintah berikut.
    ```
    pip install numpy==1.26.2 pandas==2.2.3 matplotlib==3.10.1 seaborn==0.13.2 scikit-learn==1.6.1 SQLAlchemy==2.0.41
    ```
5. Buka jupyter-notebook dengan menjalankan perintah berikut.
    ```
    jupyter-notebook
    ```
6. Buka file python prediction.py
7. Masukkan data yang ingin diprediksi pada masing - masing variabel pada dataframe baru df_new
8. Tekan tombol run code 
8. Hasil prediksi akan keluar

Namun jika menggunakan vs code, dapat mengikuti tahapan sebagai berikut: 
1. Buka VS Code.
2. Pilih File > Open Folder lalu arahkan ke folder proyek Anda.
3. Tekan Ctrl+Shift+P, cari Python: Select Interpreter, dan pilih interpreter prediksi_attrition.
4. Buka file prediction.py dan notebook.py
5. Tekan tombol run code
6. Hasil prediksi akan keluar.

## Business Dashboard
Business Dashboard digunakan untuk memvisualisasikan hasil temuan analisis. Dalam dashboard ini, dijelaskan bahwa tingkat attrition mencapai 16.9 persen atau dengan kata lain cukup tinggi. Attrition lebih banyak terjadi pada departemen RnD, kemudian Sales dan paling rendah di departemen HR. Perlu diketahui bahwa dashboard ini tidak menampilkan seluruh fitur yang ada pada dataset, namun berfokus pada isu tingginya attrition yang terjadi di departemen RnD kemudian melakukan analisis lanjutan dari sisi upah dan kepuasan bekerja.  Salah satu faktor yang membuat tingginya attrition di departemen RND adalah upah bulanan yang rendah (timpang dari 2 departemen lainnya) didukung oleh rata-rata kepuasan kerja yang rendah terutama dari segi worklife balance. Tingkat attrition lebih banyak terjadi pada kelompok usia muda (mid young atau rentang usia 25 - 35 tahun). Tenure ratio atau indikator loyalitas di departemen RnD yang rendah mencerminkan tingkat attrition yang tinggi. 

## Conclusion
Dari hasil analisis ditemukan bahwa attrition yang terjadi cukup tinggi mencapai lebih dari 15 persen. Kondisi ini dikarenakan upah yang rendah dan timpang dan kepuasan bekerja dan worklife balance yang rendah. Kondisi ini terjadi pada departemen RnD sehingga terjadi tingkat attrition yang lebih tinggi dibandingkan dua departemen lainnya.

## Rekomendasi Action Items
1. Age : Attrition lebih banyak terjadi pada kelompok usia muda, perusahaan perlu membuat lingkungan kerja yang mendukung pengembangan diri mereka baik dari segi kompetensi ataupun carrier path yang jelas.
2. MonthlyIncome : Perusahaan perlu meningkatkan upah untuk departemen setidaknya hingga tidak terlalu timpang seperti sebelumnya. Kenaikan upah secara rata-rata berkisar di angka 600 dollar. Dengan upah yang kompetitif antar departemen diharapkan karyawan dapat tetap bertahan.
3. WorklifeBalance : Pertimbangkan fleksibilitas kerja, pengaturan overtime yang jelas (tidak terlalu lama) dan tidak terlalu sering pada karyawan yang sama, serta tidak memberikan beban kerja berlebih. 

## Email dan Password Metabase
- Email : deozaofficial@gmail.com
- Password : RwcQoPlOL7YJ66RB
