import csv
from io import StringIO
from datetime import datetime
from azure.storage.blob import BlobClient


def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    # Durable Functions の操作を行うためのクライアントを初期化

    # APIからファイル名を取得
    blob_filename = req.params.get('blob_filename')
    if not blob_filename:
        return func.HttpResponse("blob_filename parameter is required", status_code=400)

    instance_id = client.start_new("orchestrator_function", None, blob_filename)
    # client.start_new() はオーケストレーター関数を開始するためのメソッド
    # req.route_params['functionName'] で指定されたオーケストレーター関数を開始
    
    return client.create_check_status_response(req, instance_id)


def orchestrator_function(context: df.DurableOrchestrationContext):

    # 1つ目のアクティビティ関数を呼び出す
    cleanse_and_upload = yield context.call_activity('FirstActivityFunction', None)

    # 2つ目のアクティビティ関数を呼び出し、取得したデータを引数として渡す
    result_from_second_activity = yield context.call_activity('SecondActivityFunction', cleanse_and_upload)

    return result_from_second_activity


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
