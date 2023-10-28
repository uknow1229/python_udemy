import csv
from io import StringIO
from datetime import datetime
from azure.storage.blob import BlobClient

def cleanse_and_upload(blob_filename: str, csv_content: str) -> None:
    # CSVを解析
    reader = csv.DictReader(StringIO(csv_content))
    rows = list(reader)
    
    # クレンジング処理
    invalid_data = []
    normal_data = []

    for row in rows:
        # A列とC列を取得
        a_value = row.get('A', '').strip()
        c_value = row.get('C', '').strip()
        
        # NotNullの空白文字のチェック
        if not a_value or not c_value:
            invalid_data.append(row)
            continue
        
        # ここでその他の型チェックや桁数チェックなどを行う
        # 例: A列のデータが最大5文字であることを期待
        if len(a_value) > 5:
            invalid_data.append(row)
            continue
        
        # 有効なデータをefb_dataに追加
        normal_data.append(row)

    # データをBlobにアップロード
    today = datetime.today().strftime('%Y%m%d')
    blob_client_invalid = BlobClient.from_connection_string("YOUR_CONNECTION_STRING", "your_container_name", f"test/{today}/invalid_data.txt")
    blob_client_efb = BlobClient.from_connection_string("YOUR_CONNECTION_STRING", "your_container_name", f"test/{today}/normal_data.txt")

    # クレンジングされたデータをBlobにアップロード
    blob_client_invalid.upload_blob("\n".join([",".join(row.values()) for row in invalid_data]))
    blob_client_normal.upload_blob("\n".join([",".join(row.values()) for row in normal_data]))
