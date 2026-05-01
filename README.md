# Datathon 2026 — Round 1: The Gridbreakers

Báo cáo và mã nguồn phân tích hiệu suất sản phẩm và dự báo doanh thu cho doanh nghiệp thương mại điện tử Việt Nam (2012–2022).

## 📊 Tổng quan Dự án
Dự án tập trung vào hai phần chính:
1. **EDA & Product Analysis**: Phân tích sâu về cơ cấu sản phẩm (Streetwear chiếm 80.09% doanh thu), chẩn đoán rủi ro lợi nhuận và đề xuất chiến lược tăng trưởng.
2. **Sales Forecasting**: Xây dựng mô hình Ensemble (LightGBM, Prophet, CatBoost, Ridge) để dự báo dòng tiền 18 tháng tiếp theo với sai số tối ưu.

## 📁 Cấu trúc Thư mục
```text
├── notebooks/
│   ├── product_analysis.ipynb    # Phân tích EDA chi tiết (Phần 2)
│   └── Kaggle_Task2.ipynb        # Phân tích chẩn đoán chuyên sâu
├── report.tex                    # Mã nguồn báo cáo LaTeX (NeurIPS template)
├── report.pdf                    # Bản báo cáo hoàn chỉnh
├── .gitignore                    # Các file loại trừ khỏi git
└── README.md                     # Hướng dẫn này
```

## 🚀 Hướng dẫn Chạy lại Kết quả
### 1. Cài đặt Môi trường
```bash
pip install -r requirements.txt
```

### 2. Dữ liệu
Đặt các file dữ liệu `.csv` của cuộc thi vào thư mục `dataset/` (bao gồm `orders.csv`, `products.csv`, `inventory.csv`, v.v.).

### 3. Thực thi
- Mở `notebooks/product_analysis.ipynb` để xem các trực quan hóa và insight EDA.
- Các kết quả dự báo được thực hiện trong pipeline forecasting (chi tiết trong báo cáo).

## 💡 Key Insights (EDA)
- **Streetwear Dominance**: Chiếm 80.09% doanh thu nhưng đối mặt với rủi ro hoàn trả "Wrong Size" cao (13,967 ca).
- **August Profit Drop**: Phát hiện biên lợi nhuận âm (-5.6%) vào tháng 8 do lạm dụng khuyến mãi.
- **Casual Strategy**: Dòng Casual có biên lợi nhuận cao nhất (28.5%), là cơ hội tối ưu hóa ROI.

---
**Nhóm thực hiện:** Lê Huy Khôi, Trương Đăng Dương, Dương Khánh Ly.
