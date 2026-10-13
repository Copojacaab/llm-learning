import collections
import pydantic
import ollama
import argparse

# def ollama_call(invoice_txt: str):

#     response = ollama.chat(
#         model="llama3.2:3b",
#         messages=[
#             {
#                 "role": "user",
#                 "content": f"Extract the invoice number, the invoice date, the supplier name and the total from this invoice. Answer in JSON.\
#                         {invoice_txt}",
#             }
#         ],
#         stream=False,
#         format=Invoice.model_json_schema(),
#     )

#     if response is not None:
#         response_str = str(response.message.content)
#         invoice = Invoice.model_validate_json(json_data=response_str)


# def run_without_format(invoice_txt: str) -> None:
#     for i in range(5):
#         response = _ollama_call(invoice_txt)
#         try:
#             if response is not None:
#                 response_str = str(response.message.content)
#             response_json = json.loads(response_str)
#         except Exception as e:
#             print(f"Errore: {e}")


class Invoice(pydantic.BaseModel):
    invoice_number: str
    invoice_date: str
    supplier_name: str
    supplier_vat: str
    total: float
    # trap
    order_number: str | None


def _ollama_call(role: str, content: str, **options) -> ollama.ChatResponse:
    response: ollama.ChatResponse = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": role,
                "content": content,
            }
        ],
        format=Invoice.model_json_schema(),
        options=options,
    )
    return response


def extract(text, **options) -> Invoice | None:
    response: ollama.ChatResponse = _ollama_call(
        role="user", content=text, options=options
    )  # extract the fields from this invoice
    try:
        response_str = str(response.message.content)
        return Invoice.model_validate_json(response_str)
    except Exception as e:
        print(e)


def repeat(text, n=10, **options):
    results: list[Invoice | None] = []
    for i in range(n):
        invoice = extract(text, options=options)
        results.append(invoice)
    return results


def count(invoice_list: list[Invoice | None]) -> collections.Counter:
    counter = collections.Counter()

    for inv in invoices_list:
        key = inv.model_dump_json() if inv is not None else "ERRORE"
        counter[key] += 1
    return counter


if __name__ == "__main__":

    # CLI argument
    parser = argparse.ArgumentParser(
        "Estra il testo da una fattura e lo restituisce in formato JSON"
    )
    parser.add_argument(
        "--path", required=True, type=str, help="percorso al file della fattura"
    )
    args = parser.parse_args()

    path_to_invoice: str = args.path

    # Invoice text extraction
    with open(path_to_invoice, encoding="utf-8") as file:
        invoice_txt: str = file.read()

    # Step call
    # Step 1
    # run_without_format(invoice_txt)
    # Step 2
    # invoice_extracted: Invoice | None = extract(
    #     f"Extract the fields from this invoice: {invoice_txt}", temperature=0
    # )
    invoices_list: list[Invoice | None] = repeat(text=invoice_txt)
    counts: collections.Counter = count(invoices_list)

    print(f"{len(counts)} risultati diversi su 10 run.")
    for key, times in counts.most_common():
        print(f"{times}x {key}")

# ======================= MEASURE =======================
# setting                         different results
# =======================================================
# 1.extract(text)                   5 risultati diversi su 10 run.
# 2.extract(text, temperature=0)

# ====================== NEW FIELD ========================
# field                             value
# =========================================================
# order_number: str             "100", "2026/0417","Not specified"
# order_number: str | None      3xnull, "100", "conf. 100"


# # 1. 5 risultati diversi su 10 run.
# 4x {"invoice_number":"2026/0417","invoice_date":"03/09/2026","supplier_name":"Officine Bianchi S.p.A.","supplier_vat":"IT09876543210","total":1288.32}
# 3x {"invoice_number":"2026/0417","invoice_date":"03/09/2026","supplier_name":"Ferramenta Rossi S.r.l.","supplier_vat":"IT01234567890","total":1288.32}
# 1x {"invoice_number":"2026/0417","invoice_date":"2026-09-03","supplier_name":"Officine Bianchi S.p.A.","supplier_vat":"IT09876543210","total":1288.32}
# 1x {"invoice_number":"2026/0417","invoice_date":"03/09/2026","supplier_name":"Ferramenta Rossi S.R.L.","supplier_vat":"IT01234567890","total":1288.32}
# 1x {"invoice_number":"Azienda: Officine Bianchi S.p.A. - Cliente: FERRAMENTA ROSSI S.R.L. - Data: 03/09/2026 - Totale: € 1.288.32","invoice_date":"2026-09-03","supplier_name":"FERRAMENTA ROSSI S.R.L.","supplier_vat":"IT01234567890","total":1288.32}


# # 2. 5 risultati diversi su 10 run.
# 6x {"invoice_number":"2026/0417","invoice_date":"03/09/2026","supplier_name":"Officine Bianchi S.p.A.","supplier_vat":"IT09876543210","total":1288.32}
# 1x {"invoice_number":"2026/0417","invoice_date":"03/09/2026","supplier_name":"Ferramenta Rossi S.R.L.","supplier_vat":"IT01234567890","total":1288.32}
# 1x {"invoice_number":"2026/0417","invoice_date":"03/09/2026","supplier_name":"Ferramenta Rossi S.r.l.","supplier_vat":"IT01234567890","total":1288.32}
# 1x {"invoice_number":"2026/0417","invoice_date":"03/09/2026","supplier_name":"FERRAMENTA ROSSI S.R.L.","supplier_vat":"IT01234567890","total":1288.32}
# 1x {"invoice_number":"MyBill #2026/0417","invoice_date":"2026-09-03","supplier_name":"Officine Bianchi S.p.A.","supplier_vat":"IT 09876543210","total":1288.32}
