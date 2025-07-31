from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Misalkan ini hasil prediksi dan data asli untuk emosi (8 kelas)
y_true = ['joy', 'sadness', 'surprise', 'disgust', 'joy', 'anger', 'trust', 'fear']
y_pred = ['joy', 'joy', 'surprise', 'disgust', 'joy', 'anger', 'trust', 'trust']

# Kelas emosi yang ada
emotion_labels = ['joy', 'sadness', 'fear', 'anger', 'surprise', 'anticipation', 'trust', 'disgust']

# Membuat confusion matrix
cm = confusion_matrix(y_true, y_pred, labels=emotion_labels)

# Menampilkan confusion matrix dengan heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=emotion_labels, yticklabels=emotion_labels)
plt.xlabel('Prediksi')
plt.ylabel('Aktual')
plt.title('Confusion Matrix untuk Deteksi Emosi')
plt.show()

# Menghitung metrik evaluasi lainnya
print("Classification Report:")
print(classification_report(y_true, y_pred, target_names=emotion_labels))
