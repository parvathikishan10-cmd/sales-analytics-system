def calculate_total_revenue(transactions):
    """
    Calculates total revenue from all transactions

    Returns: float (total revenue)
    """

    total_revenue = 0.0

    for tx in transactions:
        total_revenue += tx["Quantity"] * tx["UnitPrice"]

    return round(total_revenue, 2)

raw_lines = read_sales_data("/content/sales_data.txt")
parsed = parse_transactions(raw_lines)
valid_tx, _, _ = validate_and_filter(parsed)

total_revenue = calculate_total_revenue(valid_tx)
print("Total Revenue:", total_revenue)

def region_wise_sales(transactions):
    """
    Analyzes sales by region

    Returns: dictionary with region statistics
    """

    region_data = {}
    overall_total = 0.0

    # -------------------------
    # Aggregate totals
    # -------------------------
    for tx in transactions:
        region = tx["Region"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        overall_total += amount

        if region not in region_data:
            region_data[region] = {
                "total_sales": 0.0,
                "transaction_count": 0
            }

        region_data[region]["total_sales"] += amount
        region_data[region]["transaction_count"] += 1

    # -------------------------
    # Calculate percentages
    # -------------------------
    for region in region_data:
        percentage = (
            region_data[region]["total_sales"] / overall_total * 100
            if overall_total > 0 else 0
        )
        region_data[region]["percentage"] = round(percentage, 2)

    # -------------------------
    # Sort by total_sales (descending)
    # -------------------------
    sorted_region_data = dict(
        sorted(
            region_data.items(),
            key=lambda item: item[1]["total_sales"],
            reverse=True
        )
    )

    return sorted_region_data

region_stats = region_wise_sales(valid_tx)

for region, stats in region_stats.items():
    print(region, stats)

ctio

def top_selling_products(transactions, n=5):
    """
    Finds top n products by total quantity sold

    Returns:
    List of tuples:
    (ProductName, TotalQuantity, TotalRevenue)
    """

    product_stats = {}

    # -------------------------
    # Aggregate by ProductName
    # -------------------------
    for tx in transactions:
        product = tx["ProductName"]
        quantity = tx["Quantity"]
        revenue = tx["Quantity"] * tx["UnitPrice"]

        if product not in product_stats:
            product_stats[product] = {
                "total_quantity": 0,
                "total_revenue": 0.0
            }

        product_stats[product]["total_quantity"] += quantity
        product_stats[product]["total_revenue"] += revenue

    # -------------------------
    # Convert to list of tuples
    # -------------------------
    result = [
        (
            product,
            stats["total_quantity"],
            round(stats["total_revenue"], 2)
        )
        for product, stats in product_stats.items()
    ]

    # -------------------------
    # Sort by total quantity (descending)
    # -------------------------
    result.sort(key=lambda x: x[1], reverse=True)

    # -------------------------
    # Return top n products
    # -------------------------
    return result[:n]

top_5_products = top_selling_products(valid_tx, n=5)
top_5_products

def customer_analysis(transactions):
    """
    Analyzes customer purchase patterns

    Returns:
    Dictionary of customer statistics sorted by total_spent (descending)
    """

    customer_stats = {}

    # -------------------------
    # Aggregate per customer
    # -------------------------
    for tx in transactions:
        customer = tx["CustomerID"]
        amount = tx["Quantity"] * tx["UnitPrice"]
        product = tx["ProductName"]

        if customer not in customer_stats:
            customer_stats[customer] = {
                "total_spent": 0.0,
                "purchase_count": 0,
                "products_bought": set()
            }

        customer_stats[customer]["total_spent"] += amount
        customer_stats[customer]["purchase_count"] += 1
        customer_stats[customer]["products_bought"].add(product)

    # -------------------------
    # Final calculations
    # -------------------------
    for customer, stats in customer_stats.items():
        stats["avg_order_value"] = round(
            stats["total_spent"] / stats["purchase_count"], 2
        )
        stats["total_spent"] = round(stats["total_spent"], 2)
        stats["products_bought"] = sorted(list(stats["products_bought"]))

    # -------------------------
    # Sort by total_spent (descending)
    # -------------------------
    sorted_customers = dict(
        sorted(
            customer_stats.items(),
            key=lambda item: item[1]["total_spent"],
            reverse=True
        )
    )

    return sorted_customers

customer_results = customer_analysis(valid_tx)
customer_results

def daily_sales_trend(transactions):
    """
    Analyzes sales trends by date

    Returns:
    Dictionary sorted by date (YYYY-MM-DD)
    """

    daily_stats = {}

    # -------------------------
    # Group by date
    # -------------------------
    for tx in transactions:
        date = tx["Date"]
        amount = tx["Quantity"] * tx["UnitPrice"]
        customer = tx["CustomerID"]

        if date not in daily_stats:
            daily_stats[date] = {
                "revenue": 0.0,
                "transaction_count": 0,
                "unique_customers": set()
            }

        daily_stats[date]["revenue"] += amount
        daily_stats[date]["transaction_count"] += 1
        daily_stats[date]["unique_customers"].add(customer)

    # -------------------------
    # Final formatting
    # -------------------------
    for date, stats in daily_stats.items():
        stats["revenue"] = round(stats["revenue"], 2)
        stats["unique_customers"] = len(stats["unique_customers"])

    # -------------------------
    # Sort chronologically
    # -------------------------
    sorted_daily_stats = dict(sorted(daily_stats.items()))

    return sorted_daily_stats

daily_trend = daily_sales_trend(valid_tx)
daily_trend

def find_peak_sales_day(transactions):
    """
    Identifies the date with highest revenue

    Returns:
    Tuple: (date, revenue, transaction_count)
    """

    daily_stats = {}

    # -------------------------
    # Aggregate by date
    # -------------------------
    for tx in transactions:
        date = tx["Date"]
        amount = tx["Quantity"] * tx["UnitPrice"]

        if date not in daily_stats:
            daily_stats[date] = {
                "revenue": 0.0,
                "transaction_count": 0
            }

        daily_stats[date]["revenue"] += amount
        daily_stats[date]["transaction_count"] += 1

    # -------------------------
    # Find peak day
    # -------------------------
    peak_date, peak_data = max(
        daily_stats.items(),
        key=lambda item: item[1]["revenue"]
    )

    return (
        peak_date,
        round(peak_data["revenue"], 2),
        peak_data["transaction_count"]
    )

find_peak_sales_day(valid_tx)

def low_performing_products(transactions, threshold=10):
    """
    Identifies products with low sales volume

    Returns:
    List of tuples:
    (ProductName, TotalQuantity, TotalRevenue)
    """

    product_stats = {}

    # -------------------------
    # Aggregate by ProductName
    # -------------------------
    for tx in transactions:
        product = tx["ProductName"]
        quantity = tx["Quantity"]
        revenue = tx["Quantity"] * tx["UnitPrice"]

        if product not in product_stats:
            product_stats[product] = {
                "total_quantity": 0,
                "total_revenue": 0.0
            }

        product_stats[product]["total_quantity"] += quantity
        product_stats[product]["total_revenue"] += revenue

    # -------------------------
    # Filter low-performing products
    # -------------------------
    low_products = [
        (
            product,
            stats["total_quantity"],
            round(stats["total_revenue"], 2)
        )
        for product, stats in product_stats.items()
        if stats["total_quantity"] < threshold
    ]

    # -------------------------
    # Sort by TotalQuantity (ascending)
    # -------------------------
    low_products.sort(key=lambda x: x[1])

    return low_products

low_performers = low_performing_products(valid_tx, threshold=10)
low_performers