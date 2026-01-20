# The dataset
sales_data = """TransactionID|Date|ProductID|ProductName|Quantity|UnitPrice|CustomerID|Region
T018|2024-12-29|P107|USB Cable|8|173|C009|South
T063|2024-12-07|P110|Laptop Charger|6|1,916|C022|East
T075|2024-12-10|P106|Headphones|0|2826|C001|South
T023|2024-12-09|P109|Wireless Mouse|9|523|C022|North
T059|2024-12-29|P102|Mouse,Wireless|4|1056|C010|South
T035|2024-12-08|P102|Mouse|4|431|C011|North
T061|2024-12-10|P109|Wireless Mouse|2|775|C009|North
T057|2024-12-15|P101|Laptop,Premium|10|81896|C004|North
T034|2024-12-22|P107|USB Cable|6|324|C029|West
T050|2024-12-02|P104|Monitor,LED|10|9997|C024|East
T024|2024-12-25|P109|Wireless Mouse|5|1812|C011|North
T004|2024-12-07|P109|Wireless Mouse|9|1359|C008|West
T068|2024-12-02|P109|Wireless Mouse|6|1,692|C018|South
T066|2024-12-06|P105|Webcam|8|4,259|C023|West
T064|2024-12-16|P109|Wireless Mouse|5|604|C003|West
T045|2024-12-26|P108|External Hard Drive|9|3802|C002|North
T015|2024-12-30|P105|Webcam|9|2899|C022|East
T055|2024-12-07|P105|Webcam,HD|6|2977|C009|West
T072|2024-12-26|P103|Keyboard|3|2488||South
T076|2024-12-11|P107|USB Cable|5|-459|C025|East
T002|2024-12-22|P102|Mouse|9|478|C019|West
T051|2024-12-02|P101|Laptop,Premium|10|76246|C017|South
T005|2024-12-09|P110|Laptop Charger|1|3054|C026|South
T007|2024-12-03|P102|Mouse|7|498|C012|East
T077|2024-12-13|P109|Wireless Mouse|9|-998|C001|North
T010|2024-12-07|P110|Laptop Charger|2|1593|C022|South
T032|2024-12-22|P103|Keyboard|8|1476|C009|West
T008|2024-12-09|P110|Laptop Charger|1|2994|C015|North
T060|2024-12-27|P108|External Hard Drive,1TB|9|8763|C010|North
T062|2024-12-24|P102|Mouse|9|618|C009|East
T003|2024-12-01|P101|Laptop|2|59328|C008|North
T022|2024-12-20|P107|USB Cable|2|297|C013|West
T046|2024-12-30|P102|Mouse,Wireless|4|640|C014|West
T049|2024-12-22|P109|Wireless Mouse,Gaming|8|817|C007|East
T006|2024-12-11|P107|USB Cable|5|179|C007|East
T011|2024-12-03|P105|Webcam|4|2413|C013|East
T031|2024-12-24|P102|Mouse|8|441|C025|South
T033|2024-12-30|P104|Monitor|9|14591|C023|East
T058|2024-12-07|P109|Wireless Mouse,Gaming|9|1043|C005|East
T073|2024-12-26|P107|USB Cable|4|236||North
T029|2024-12-11|P110|Laptop Charger|8|1539|C004|East
T030|2024-12-08|P105|Webcam|1|2986|C029|North
T021|2024-12-25|P102|Mouse|1|524|C005|South
X2|2024-12-07|P110|Laptop Charger|5|1590|C023|West
T071|2024-12-29|P109|Wireless Mouse|7|1771|C024|
T070|2024-12-07|P106|Headphones|4|6,463|C004|East
T028|2024-12-25|P106|Headphones|3|5418|C025|North
T014|2024-12-24|P109|Wireless Mouse|4|834|C015|West
T019|2024-12-24|P104|Monitor|9|16609|C024|West
T054|2024-12-03|P110|Laptop Charger,65W|7|2846|C019|East
T001|2024-12-01|P102|Mouse|5|801|C008|South
T036|2024-12-18|P110|Laptop Charger|4|2705|C008|North
X611|2024-12-06|P105|Webcam|10|3087|C002|North
T020|2024-12-13|P110|Laptop Charger|6|1949|C005|West
T037|2024-12-23|P102|Mouse|1|768|C003|North
X395|2024-12-12|P107|USB Cable|6|323|C020|North
T012|2024-12-21|P108|External Hard Drive|6|4332|C012|East
T048|2024-12-13|P101|Laptop,Premium|5|74819|C010|West
T044|2024-12-09|P103|Keyboard|8|1823|C028|North
T025|2024-12-14|P105|Webcam|3|3858|C001|East
T074|2024-12-28|P101|Laptop|0|59577|C007|West
T027|2024-12-27|P105|Webcam|9|4494|C007|South
T013|2024-12-22|P104|Monitor|5|10339|C020|South
T017|2024-12-07|P102|Mouse|10|944|C007|West
T038|2024-12-03|P106|Headphones|9|2949|C009|West
T052|2024-12-17|P101|Laptop,Premium|2|57178|C003|North
T042|2024-12-02|P102|Mouse|7|994|C026|North
T053|2024-12-13|P104|Monitor,LED|2|16067|C019|North
T040|2024-12-07|P107|USB Cable|2|149|C022|West
T065|2024-12-02|P105|Webcam|1|3,366|C025|South
T039|2024-12-18|P104|Monitor|3|23488|C008|West
T016|2024-12-08|P101|Laptop|1|65673|C013|East
T041|2024-12-14|P106|Headphones|7|4825|C028|North
T043|2024-12-07|P104|Monitor|4|22700|C005|West
T009|2024-12-03|P107|USB Cable|9|250|C027|East
T056|2024-12-22|P103|Keyboard,Mechanical|5|2672|C011|North
T047|2024-12-07|P108|External Hard Drive,1TB|7|3480|C006|West
T026|2024-12-25|P109|Wireless Mouse|3|1539|C030|North
T069|2024-12-05|P107|USB Cable|1|257|C012|North
T067|2024-12-01|P109|Wireless Mouse|2|654|C029|South
"""

# This code saves that text into a physical file on your computer/Colab
with open('sales_data.txt', 'w') as f:
    f.write(sales_data.strip())

print("Conversion complete!")

def read_sales_data(filename="/content/sales_data.txt"):
    """
    Reads sales data from file handling encoding issues

    Returns: list of raw lines (strings)
    """

    encodings_to_try = ["utf-8", "latin-1", "cp1252"]

    for encoding in encodings_to_try:
        try:
            with open(filename, "r", encoding=encoding) as file:
                lines = file.readlines()
            break
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found in Colab.")
            return []

    else:
        print("Error: Unable to decode file with supported encodings.")
        return []

    # Skip header and remove empty lines
    cleaned_lines = []
    for line in lines[1:]:  # skip header
        line = line.strip()
        if line:
            cleaned_lines.append(line)

    return cleaned_lines

raw_lines = read_sales_data()

print(f"Total transaction lines read: {len(raw_lines)}")
print(raw_lines[:5])

def parse_transactions(raw_lines):
    """
    Parses raw lines into clean list of dictionaries
    """

    parsed_data = []

    expected_fields = [
        "TransactionID", "Date", "ProductID", "ProductName",
        "Quantity", "UnitPrice", "CustomerID", "Region"
    ]

    for line in raw_lines:
        parts = line.split("|")

        # Skip rows with incorrect number of fields
        if len(parts) != 8:
            continue

        (
            transaction_id,
            date,
            product_id,
            product_name,
            quantity,
            unit_price,
            customer_id,
            region
        ) = parts

        # Clean ProductName (remove commas)
        product_name = product_name.replace(",", "")

        # Clean numeric fields
        try:
            quantity = int(quantity.replace(",", ""))
            unit_price = float(unit_price.replace(",", ""))
        except ValueError:
            continue  # skip rows with bad numeric data

        record = {
            "TransactionID": transaction_id,
            "Date": date,
            "ProductID": product_id,
            "ProductName": product_name,
            "Quantity": quantity,
            "UnitPrice": unit_price,
            "CustomerID": customer_id,
            "Region": region
        }

        parsed_data.append(record)

    return parsed_data

raw_lines = read_sales_data("/content/sales_data.txt")
parsed_transactions = parse_transactions(raw_lines)

print(f"Parsed records: {len(parsed_transactions)}")
parsed_transactions[:3]

def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    """
    Validates transactions and applies optional filters

    Returns:
    (valid_transactions, invalid_count, filter_summary)
    """

    required_fields = [
        "TransactionID", "Date", "ProductID", "ProductName",
        "Quantity", "UnitPrice", "CustomerID", "Region"
    ]

    total_input = len(transactions)
    invalid_count = 0
    valid_transactions = []

    # -------------------------
    # Validation
    # -------------------------
    for tx in transactions:
        # Check required fields
        if not all(field in tx and tx[field] for field in required_fields):
            invalid_count += 1
            continue

        if (
            tx["Quantity"] <= 0 or
            tx["UnitPrice"] <= 0 or
            not tx["TransactionID"].startswith("T") or
            not tx["ProductID"].startswith("P") or
            not tx["CustomerID"].startswith("C")
        ):
            invalid_count += 1
            continue

        valid_transactions.append(tx)

    # -------------------------
    # Display available options
    # -------------------------
    regions = sorted({tx["Region"] for tx in valid_transactions})
    amounts = [tx["Quantity"] * tx["UnitPrice"] for tx in valid_transactions]

    print("Available regions:", regions)
    print(f"Transaction amount range: {min(amounts):.2f} - {max(amounts):.2f}")

    filtered_by_region = 0
    filtered_by_amount = 0

    # -------------------------
    # Region filter
    # -------------------------
    if region:
        before = len(valid_transactions)
        valid_transactions = [
            tx for tx in valid_transactions if tx["Region"] == region
        ]
        filtered_by_region = before - len(valid_transactions)
        print(f"After region filter ({region}): {len(valid_transactions)} records")

    # -------------------------
    # Amount filter
    # -------------------------
    if min_amount is not None or max_amount is not None:
        before = len(valid_transactions)

        def amount_ok(tx):
            amount = tx["Quantity"] * tx["UnitPrice"]
            if min_amount is not None and amount < min_amount:
                return False
            if max_amount is not None and amount > max_amount:
                return False
            return True

        valid_transactions = [tx for tx in valid_transactions if amount_ok(tx)]
        filtered_by_amount = before - len(valid_transactions)
        print(f"After amount filter: {len(valid_transactions)} records")

    # -------------------------
    # Summary
    # -------------------------
    filter_summary = {
        "total_input": total_input,
        "invalid": invalid_count,
        "filtered_by_region": filtered_by_region,
        "filtered_by_amount": filtered_by_amount,
        "final_count": len(valid_transactions)
    }

    return valid_transactions, invalid_count, filter_summary

parsed = parse_transactions(raw_lines)

valid_tx, invalid_count, summary = validate_and_filter(
    parsed,
    region="North",
    min_amount=5000,
    max_amount=100000
)

print("\nSummary:", summary)
print("Sample valid transaction:", valid_tx[0])