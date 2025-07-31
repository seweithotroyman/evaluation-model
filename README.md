### Penjelasan:

* **`y_true`**: Label asli emosi dari data uji (feedback pelanggan).
* **`y_pred`**: Hasil prediksi model untuk emosi-emosi tersebut.
* **`emotion_labels`**: Label untuk 8 kelas emosi dasar menurut Plutchik.
* **`confusion_matrix(y_true, y_pred)`**: Menghitung confusion matrix untuk klasifikasi multi-kelas.
* **`classification_report()`**: Memberikan metrik seperti precision, recall, dan F1-score untuk setiap kelas emosi.

### Output yang Diharapkan:

* Confusion Matrix: Ini akan menunjukkan **berapa banyak prediksi yang benar** dan **kesalahan klasifikasi** untuk setiap emosi. Misalnya, model mungkin keliru mengklasifikasikan emosi **joy** sebagai **surprise**.

  Confusion Matrix-nya bakal terlihat seperti ini (hanya contoh struktur):

|                  | Joy | Sadness | Fear | Anger | Surprise | Anticipation | Trust | Disgust |
| ---------------- | --- | ------- | ---- | ----- | -------- | ------------ | ----- | ------- |
| **Joy**          | 5   | 0       | 0    | 0     | 1        | 0            | 0     | 0       |
| **Sadness**      | 0   | 4       | 1    | 0     | 0        | 1            | 0     | 0       |
| **Fear**         | 0   | 0       | 3    | 1     | 0        | 0            | 1     | 0       |
| **Anger**        | 0   | 0       | 0    | 4     | 0        | 1            | 0     | 0       |
| **Surprise**     | 0   | 0       | 1    | 0     | 5        | 1            | 0     | 0       |
| **Anticipation** | 0   | 0       | 0    | 1     | 1        | 3            | 0     | 0       |
| **Trust**        | 0   | 0       | 0    | 0     | 0        | 1            | 4     | 0       |
| **Disgust**      | 0   | 1       | 0    | 0     | 0        | 0            | 0     | 5       |

### Metrik yang Dihasilkan:

Dari confusion matrix, kita bisa menghitung:

* **Precision**: Seberapa tepat model dalam mengklasifikasikan setiap emosi.
* **Recall**: Seberapa baik model mendeteksi setiap emosi.
* **F1-Score**: Kombinasi dari precision dan recall untuk menggambarkan performa model secara keseluruhan.

### Evaluasi dengan **Weighted Average**:

Karena tiap emosi mungkin nggak seimbang jumlahnya, **weighted average** untuk F1-score, precision, dan recall lebih tepat daripada menggunakan rata-rata biasa. Misalnya, beberapa emosi mungkin lebih sering muncul dalam feedback dibandingkan emosi lainnya.

### Conclusion:

Dengan **8 emosi dasar** dalam teori Plutchik, lo bisa menggunakan pendekatan yang sama seperti biasa, cuma lebih kompleks karena melibatkan lebih banyak kelas. Evaluasi dengan **Confusion Matrix** dan **Classification Report** akan sangat membantu untuk melihat apakah model lo benar-benar bisa membedakan dan mengklasifikasikan setiap emosi dengan baik.
