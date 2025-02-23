# Smart City E-Government Game

## Deskripsi

Smart City E-Government Game adalah permainan simulasi di mana Anda berperan sebagai kepala dinas Smart City yang bertugas mengembangkan layanan e-government untuk meningkatkan pelayanan publik, kepuasan masyarakat, dan infrastruktur digital. Permainan ini menggunakan logika fuzzy dan pembelajaran AI sederhana untuk mengevaluasi performa dan menyesuaikan tingkat kesulitan permainan.

## Fitur

- **Sistem Evaluasi Berbasis Fuzzy Logic**: Menggunakan logika fuzzy untuk mengevaluasi performa kota berdasarkan tiga parameter utama: kepuasan masyarakat, anggaran, dan infrastruktur.
- **AI Adaptif**: Menggunakan pembelajaran AI sederhana untuk menyesuaikan tingkat kesulitan permainan berdasarkan performa pemain.
- **Layanan E-Government**: Implementasikan berbagai layanan untuk meningkatkan kepuasan masyarakat dan infrastruktur.
- **Event Acak**: Hadapi berbagai event acak yang dapat mempengaruhi anggaran, kepuasan masyarakat, dan infrastruktur.

## Instalasi

1. Pastikan Anda memiliki Python 3.10 atau versi yang lebih baru terinstal di sistem Anda.
2. Clone repositori ini:

    ```sh
    git clone https://github.com/imadenugraha/smartcity-board-game-ai.git
    cd smartcity-board-game-ai
    ```

3. Instal dependensi menggunakan Poetry:

    ```sh
    poetry install
    ```

## Cara Bermain

1. Jalankan permainan dengan perintah berikut:

    ```sh
    poetry run python main.py
    ```

2. Ikuti instruksi di layar untuk mengelola kota Anda, implementasikan layanan, dan hadapi event acak.
3. Tujuan Anda adalah untuk meningkatkan kepuasan masyarakat, membangun infrastruktur, dan mengelola anggaran dengan bijak.

## Struktur Proyek

```tree
.
├── main.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── src
    ├── AILearning.py
    ├── FuzzyLogic.py
    ├── __init__.py
    └── SmartCityGame.py
```

## Penjelasan Kode

- [main.py](main.py): Titik masuk utama untuk menjalankan permainan.
- [AILearning.py](src/AILearning.py): Mengandung kelas [AILearning](src/AILearning.py) yang mengatur tingkat kesulitan permainan berdasarkan performa pemain.
- [FuzzyLogic.py](src/FuzzyLogic.py): Mengandung kelas [FuzzyLogic](src/FuzzyLogic.py) yang mengevaluasi performa kota menggunakan logika fuzzy.
- [SmartCityGame.py](src/SmartCityGame.py): Mengandung kelas [SmartCityGame](src/SmartCityGame.py) yang mengatur alur permainan, termasuk implementasi layanan dan penanganan event.
