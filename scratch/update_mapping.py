import json
import os

path = 'd:/du an/round 1 datathon/notebooks/Kaggle_Task3_Timeseries_Forecasting.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Định nghĩa Mapping chuẩn học thuật và dễ hiểu cho SHAP
new_mapping = {
    'enc_md_rev': 'Trung bình Doanh thu theo Ngày (Lịch sử)',
    'enc_md_cog': 'Trung bình Chi phí theo Ngày (Lịch sử)',
    'enc_mn_rev': 'Trung bình Doanh thu theo Tháng',
    'enc_mn_cog': 'Trung bình Chi phí theo Tháng',
    'lag365_rev': 'Doanh thu cùng kỳ năm trước (Lag 365)',
    'lag365_cog': 'Chi phí cùng kỳ năm trước (Lag 365)',
    'lag730_rev': 'Doanh thu cùng kỳ 2 năm trước',
    'lag1095_rev': 'Doanh thu cùng kỳ 3 năm trước',
    'tet_days_diff': 'Khoảng cách tới Tết Âm lịch (Ngày)',
    't_days': 'Xu hướng thời gian (Số ngày từ 2020)',
    't_years': 'Xu hướng thời gian (Số năm)',
    'promo_urban_blowout': 'Trạng thái Urban Blowout (0/1)',
    'promo_urban_blowout_since': 'Số ngày từ khi bắt đầu Urban Blowout',
    'promo_urban_blowout_until': 'Số ngày tới khi kết thúc Urban Blowout',
    'days_to_eom': 'Số ngày tới cuối tháng',
    'is_weekend': 'Ngày cuối tuần (Thứ 7/CN)',
    'sin_y1': 'Chu kỳ mùa vụ Năm (Fourier Sin)',
    'cos_y1': 'Chu kỳ mùa vụ Năm (Fourier Cos)',
    'regime_post2019': 'Giai đoạn hậu đại dịch (>=2020)',
    'regime_pre2019': 'Giai đoạn ổn định (<2019)',
}

# Tìm cell chứa FEATURE_MAPPING và cập nhật
updated = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and 'FEATURE_MAPPING' in ''.join(cell['source']):
        # Tạo lại nội dung cell mapping
        mapping_str = "FEATURE_MAPPING = {\n"
        for k, v in new_mapping.items():
            mapping_str += f"    '{k}': '{v}',\n"
        mapping_str += "}\n"
        
        # Giữ lại phần logic vẽ biểu đồ phía sau mapping
        source_lines = ''.join(cell['source']).split('FEATURE_MAPPING = {')
        # Lấy phần code phía sau dấu đóng ngoặc } của mapping cũ
        remaining_code = source_lines[1].split('}', 1)[1] if '}' in source_lines[1] else ""
        
        cell['source'] = [mapping_str + remaining_code]
        updated = True
        break

if updated:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
    print('FEATURE_MAPPING đã được cập nhật chuẩn SHAP.')
else:
    print('Không tìm thấy cell chứa FEATURE_MAPPING.')
