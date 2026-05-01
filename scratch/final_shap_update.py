import json
import os

path = 'd:/du an/round 1 datathon/notebooks/Kaggle_Task3_Timeseries_Forecasting.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Bảng Mapping bạn cung cấp, đã được chuẩn hóa cho SHAP
feature_mapping_code = """FEATURE_MAPPING = {
    'enc_md_rev': 'Lịch sử Doanh thu (Cùng kỳ)',
    'enc_md_cog': 'Lịch sử Chi phí (Cùng kỳ)',
    'enc_dw_rev': 'Lịch sử Doanh thu (Theo Thứ/Tuần)',
    'enc_dw_cog': 'Lịch sử Chi phí (Theo Thứ/Tuần)',
    'lag365_rev': 'Doanh thu Trễ (365 Ngày)',
    'lag365_cog': 'Chi phí Trễ (365 Ngày)',
    'lag730_rev': 'Doanh thu Trễ (730 Ngày)',
    'lag730_cog': 'Chi phí Trễ (730 Ngày)',
    'lag1095_rev': 'Doanh thu Trễ (1095 Ngày)',
    'lag1095_cog': 'Chi phí Trễ (1095 Ngày)',
    't_days': 'Xu hướng Biến đổi (Tính bằng Ngày)',
    't_years': 'Xu hướng Biến đổi (Tính bằng Năm)',
    'year': 'Năm Hệ thống',
    'dow': 'Thứ trong tuần (DOW)',
    'regime_2019': 'Chế độ Tiền Khủng hoảng (2019)',
    'regime_pre2019': 'Chế độ Tiền Khủng hoảng (<2019)',
    'promo_urban_blowout_since': 'Khoảng cách từ đợt Urban Blowout',
    'promo_urban_blowout_until': 'Thời gian đếm ngược Urban Blowout',
    'tet_days_diff': 'Số ngày chênh lệch với Tết Âm lịch',
    'cos_m1': 'Biến đổi Mùa vụ (Fourier Cos M1)',
    'cos_m2': 'Biến đổi Mùa vụ (Fourier Cos M2)',
    'sin_m2': 'Biến đổi Mùa vụ (Fourier Sin M2)',
    'sin_w1': 'Biến đổi Mùa vụ (Fourier Sin W1)',
}"""

shap_logic_code = """
import shap
import matplotlib.pyplot as plt
import numpy as np

# ---- Chỉ sử dụng SHAP Analysis theo yêu cầu ----
print("Đang tính toán SHAP values cho Mô hình Doanh thu (lấy mẫu 500 điểm)...")
try:
    explainer = shap.TreeExplainer(bf_rev)
    # Lấy mẫu ngẫu nhiên để đảm bảo tốc độ xử lý
    np.random.seed(42)
    sample_idx = np.random.choice(X_tr.shape[0], 500, replace=False)
    X_sample = X_tr[sample_idx]
    shap_values = explainer.shap_values(X_sample)

    # Dịch tên biến sang tiếng Việt dựa trên FEATURE_MAPPING
    display_cols = [FEATURE_MAPPING.get(c, c.replace('_', ' ').title()) for c in cols]

    plt.figure(figsize=(12, 8))
    shap.summary_plot(shap_values, X_sample, feature_names=display_cols, show=False)
    plt.title("Phân tích SHAP: Tác động của các đặc trưng tới Doanh thu", fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig("shap_analysis.png", dpi=300, bbox_inches='tight')
    plt.show()
    print("Đã lưu ảnh shap_analysis.png")
except Exception as e:
    print(f"Lỗi khi chạy SHAP: {e}. Vui lòng đảm bảo đã cài đặt thư viện 'shap'.")
"""

# Tìm cell giải thích cũ (chứa plot_combined_importance hoặc mapping cũ) và thay thế
new_cells = []
for cell in nb['cells']:
    # Nếu là cell giải thích cũ (chứa FEATURE_MAPPING hoặc plot_combined_importance), ta thay thế nó
    if cell['cell_type'] == 'code' and ('FEATURE_MAPPING' in ''.join(cell['source']) or 'plot_combined_importance' in ''.join(cell['source'])):
        cell['source'] = [feature_mapping_code + "\n" + shap_logic_code]
        new_cells.append(cell)
    # Loại bỏ các cell SHAP thừa nếu có (do các lần update trước)
    elif cell['cell_type'] == 'code' and 'shap.TreeExplainer' in ''.join(cell['source']):
        continue
    else:
        new_cells.append(cell)

nb['cells'] = new_cells

with open(path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print('Notebook updated: Removed Gain, using only SHAP with new mapping.')
