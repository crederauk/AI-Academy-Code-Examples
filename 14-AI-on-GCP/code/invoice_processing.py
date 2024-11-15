import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


def generate():
    vertexai.init(project="YOUR_GCP_PROJECT", location="europe-west4")
    model = GenerativeModel(
        "gemini-1.5-flash-002",
    )
    responses = model.generate_content(
        [document1, text1],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

document1 = Part.from_data(
    mime_type="application/pdf",
    data=base64.b64decode("""YOUR_INVOICE_PATH""")
text1 = """You are a document entity extraction specialist. Given a document, your task is to extract the text value of the following entities:
{
	\"amount_paid_since_last_invoice\": \"\",
	\"carrier\": \"\",
	\"currency\": \"\",
	\"currency_exchange_rate\": \"\",
	\"delivery_date\": \"\",
	\"due_date\": \"\",
	\"freight_amount\": \"\",
	\"invoice_date\": \"\",
	\"invoice_id\": \"\",
	\"line_items\": [
		{
			\"amount\": \"\",
			\"description\": \"\",
			\"product_code\": \"\",
			\"purchase_order\": \"\",
			\"quantity\": \"\",
			\"unit\": \"\",
			\"unit_price\": \"\"
		}
	],
	\"net_amount\": \"\",
	\"payment_terms\": \"\",
	\"purchase_order\": \"\",
	\"receiver_address\": \"\",
	\"receiver_email\": \"\",
	\"receiver_name\": \"\",
	\"receiver_phone\": \"\",
	\"receiver_tax_id\": \"\",
	\"receiver_website\": \"\",
	\"remit_to_address\": \"\",
	\"remit_to_name\": \"\",
	\"ship_from_address\": \"\",
	\"ship_from_name\": \"\",
	\"ship_to_address\": \"\",
	\"ship_to_name\": \"\",
	\"supplier_address\": \"\",
	\"supplier_email\": \"\",
	\"supplier_iban\": \"\",
	\"supplier_name\": \"\",
	\"supplier_payment_ref\": \"\",
	\"supplier_phone\": \"\",
	\"supplier_registration\": \"\",
	\"supplier_tax_id\": \"\",
	\"supplier_website\": \"\",
	\"total_amount\": \"\",
	\"total_tax_amount\": \"\",
	\"vat\": [
		{
			\"amount\": \"\",
			\"category_code\": \"\",
			\"tax_amount\": \"\",
			\"tax_rate\": \"\",
			\"total_amount\": \"\"
		}
	]
}

- The JSON schema must be followed during the extraction.
- The values must only include text found in the document
- Do not normalize any entity value.
- If an entity is not found in the document, set the entity value to null."""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]

generate()