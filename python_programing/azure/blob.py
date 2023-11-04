from azure.storage.blob import BlobClient
import csv
from io import BytesIO

def first_activity_function(context: df.DurableActivityContext) -> dict:
    connection_string = 'YOUR_CONNECTION_STRING'
    container_name = 'YOUR_CONTAINER_NAME'
    blob_filename = 'YOUR_BLOB_FILENAME'

    blob_client = BlobClient.from_connection_string(connection_string, container_name, blob_filename)

    # Blobからデータをダウンロード
    stream = BytesIO(blob_client.download_blob().readall())
    
    # CSVを読み込む
    csv_reader = csv.reader(stream.decode('utf-8').splitlines())
    column_A = []
    column_C = []

    for row in csv_reader:
        column_A.append(row[0])  # A列
        column_C.append(row[2])  # C列

    # ファイル名の一部を取得
    part_of_filename = blob_filename.split('_')[1]  # 例えば、'prefix_123_suffix.csv'から'123'を取得

    # データを辞書としてまとめる
    data = {
        'filename_part': part_of_filename,
        'column_A': column_A,
        'column_C': column_C
    }

    return data