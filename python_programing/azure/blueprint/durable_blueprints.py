import logging
import azure.functions as func
import azure.durable_functions as df

# To learn more about blueprints in the Python prog model V2,
# see: https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators#blueprints

# Note, the `func` namespace does not contain Durable Functions triggers and bindings, so to register blueprints of
# DF we need to use the `df` package's version of blueprints.
bp = df.Blueprint()

# We define a standard function-chaining DF pattern

@bp.route(route="startOrchestrator")
@bp.durable_client_input(client_name="client")
async def start_orchestrator(req: func.HttpRequest, client):
    function_name = req.route_params.get('functionName')
    # クエリパラメータからファイル名の文字列を取得
    file_names_str = req.params.get('filenames')

    # ファイル名がクエリパラメータにない場合、リクエストボディをチェック
    if not file_names_str:
        try:
            req_body = await req.get_body()
            data = json.loads(req_body)
            file_names_str = data.get('filenames')
        except ValueError:
            return func.HttpResponse(
                body="Invalid JSON in request body",
                status_code=400
            )

    # ファイル名の文字列をリストに変換
    if file_names_str:
        file_names = file_names_str.split(',')
    else:
        return func.HttpResponse(
            body="File names are required.",
            status_code=400
        )

    # 空のファイル名や余分な空白を取り除く
    file_names = [name.strip() for name in file_names if name.strip()]

    # ファイル名リストが空ではないことを確認
    if not file_names:
        return func.HttpResponse(
            body="File names are required and must be a non-empty list.",
            status_code=400
        )

    # オーケストレーター関数を非同期で起動
    instance_id = await client.start_new(function_name, None, file_names)

    # クライアントにステータスチェック用のレスポンスを作成して返す
    response = client.create_check_status_response(req, instance_id)
    return response
    # instance_id = await client.start_new("my_orchestrator")
    
    # logging.info(f"Started orchestration with ID = '{instance_id}'.")
    # return client.create_check_status_response(req, instance_id)

@bp.orchestration_trigger(context_name="context")
def my_orchestrator(context: df.DurableOrchestrationContext):
    result1 = yield context.call_activity('say_hello', "Tokyo")
    result2 = yield context.call_activity('say_hello', "Seattle")
    result3 = yield context.call_activity('say_hello', "London")
    return [result1, result2, result3]

@bp.activity_trigger(input_name="city")
def say_hello(city: str) -> str:
    return f"Hello {city}!"