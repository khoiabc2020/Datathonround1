# Datathon 2026 --- The Gridbreakers (Round 1)

Báo cáo và mã nguồn phân tích hiệu suất sản phẩm và dự báo doanh thu cho doanh nghiệp thương mại điện tử thời trang Việt Nam (2012--2022).

---

## 1. Tổng quan Dự án
Dự án được xây dựng nhằm giải quyết bài toán tối ưu hóa vận hành cho doanh nghiệp thời trang thông qua dữ liệu lịch sử 10 năm. Chúng tôi tập trung vào 2 trụ cột chính:

1. **Phân tích EDA chuyên sâu (DDPP):** Chẩn đoán các điểm mù về lợi nhuận và hoàn hàng của dòng Streetwear.
2. **Hệ thống Dự báo (Sales Forecasting):** Kiến trúc Ensemble đa mô hình (LightGBM, Prophet, CatBoost, Ridge) đạt độ chính xác cao (658k MAE).

---

## 2. Key Insights (EDA)
Dưới đây là các phát hiện quan trọng nhất từ dữ liệu:

*   **Streetwear Dominance:** Đóng góp 80.09% doanh thu toàn hệ thống.
*   **August Profit Drop:** Phát hiện biên lợi nhuận âm (-5.6%) vào tháng 8 do chiến lược clearance chưa tối ưu.
*   **Casual Potential:** Dòng Casual sở hữu biên lợi nhuận cao nhất (28.5%), là động lực tăng trưởng ROI mới.
*   **Return Crisis:** Thiệt hại 371 triệu VND do rủi ro "Wrong Size" (13,967 trường hợp).

---

## 3. Cấu trúc Thư mục
```text
├── notebooks/
│   ├── product_analysis.ipynb    # EDA & Trực quan hóa (Phần 2)
│   └── Kaggle_Task2.ipynb        # Phân tích Chẩn đoán chuyên sâu
├── report.tex                    # Mã nguồn báo cáo (NeurIPS LaTeX)
├── report.pdf                    # Báo cáo kỹ thuật hoàn chỉnh
├── requirements.txt              # Thư viện cần thiết
└── README.md                     # Tài liệu hướng dẫn
```

---

## 4. Hướng dẫn Cài đặt và Thực thi
### 4.1 Cài đặt Môi trường
Sử dụng pip để cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

### 4.2 Dữ liệu
Vui lòng đặt toàn bộ các file .csv (orders, products, inventory, v.v.) vào thư mục dataset/ để mã nguồn có thể tự động nhận diện.

### 4.3 Chạy Notebook
Mở notebooks/product_analysis.ipynb để theo dõi toàn bộ luồng phân tích từ Mô tả đến Đề xuất hành động.

---

## 5. Thành viên thực hiện
*   Lê Huy Khôi
*   Trương Đăng Dương
*   Dương Khánh Ly

---
Báo cáo dự thi Datathon 2026 - PTIT. Đơn vị tổ chức: VinTelligence.
