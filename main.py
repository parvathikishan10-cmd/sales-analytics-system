def main():
    """
    Main execution function
    """

    try:
        print("=" * 40)
        print("SALES ANALYTICS SYSTEM")
        print("=" * 40)

        # --------------------------------------------------
        # 1. READ SALES DATA
        # --------------------------------------------------
        print("\n[1/10] Reading sales data...")
        raw_lines = read_sales_data("sales_data.txt")
        print(f"Successfully read {len(raw_lines)} transactions")

        # --------------------------------------------------
        # 2. PARSE AND CLEAN
        # --------------------------------------------------
        print("\n[2/10] Parsing and cleaning data...")
        parsed_transactions = parse_transactions(raw_lines)
        print(f"Parsed {len(parsed_transactions)} records")

        # --------------------------------------------------
        # 3. FILTER OPTIONS
        # --------------------------------------------------
        regions = sorted({tx["Region"] for tx in parsed_transactions})
        amounts = [tx["Quantity"] * tx["UnitPrice"] for tx in parsed_transactions]

        print("\n[3/10] Filter Options Available:")
        print("Regions:", ", ".join(regions))
        print(f"Amount Range: ₹{min(amounts):,.0f} - ₹{max(amounts):,.0f}")

        apply_filter = input("\nDo you want to filter data? (y/n): ").strip().lower()

        if apply_filter == "y":
            region_filter = input("Enter region to filter (or press Enter to skip): ").strip()
            min_amt = input("Enter minimum amount (or press Enter to skip): ").strip()
            max_amt = input("Enter maximum amount (or press Enter to skip): ").strip()

            filtered = []
            for tx in parsed_transactions:
                amount = tx["Quantity"] * tx["UnitPrice"]

                if region_filter and tx["Region"] != region_filter:
                    continue
                if min_amt and amount < float(min_amt):
                    continue
                if max_amt and amount > float(max_amt):
                    continue

                filtered.append(tx)

            parsed_transactions = filtered
            print(f"Filtered down to {len(parsed_transactions)} records")
        else:
            print("No filters applied")

        # --------------------------------------------------
        # 4. VALIDATION
        # --------------------------------------------------
        print("\n[4/10] Validating transactions...")
        valid_tx, invalid_count, summary = validate_and_filter(parsed_transactions)
        print(f"Valid: {len(valid_tx)} | Invalid: {invalid_count}")

        # --------------------------------------------------
        # 5. ANALYSIS (PART 2)
        # --------------------------------------------------
        print("\n[5/10] Analyzing sales data...")
        region_analysis = region_wise_sales(valid_tx)
        top_products = top_selling_products(valid_tx)
        customer_stats = customer_analysis(valid_tx)
        daily_trend = daily_sales_trend(valid_tx)
        peak_day = find_peak_sales_day(valid_tx)
        low_products = low_performing_products(valid_tx)
        print("Analysis complete")

        # --------------------------------------------------
        # 6. FETCH API PRODUCTS
        # --------------------------------------------------
        print("\n[6/10] Fetching product data from API...")
        products = fetch_all_products()
        product_map = product_mapping(products)
        print(f"Fetched {len(product_map)} products")

        # --------------------------------------------------
        # 7. ENRICH SALES DATA
        # --------------------------------------------------
        print("\n[7/10] Enriching sales data...")
        enriched_data = enrich_sales_data(valid_tx, product_map)

        enriched_count = sum(1 for tx in enriched_data if tx["API_Match"])
        success_rate = (enriched_count / len(enriched_data)) * 100 if enriched_data else 0

        print(f"Enriched {enriched_count}/{len(enriched_data)} transactions ({success_rate:.1f}%)")

        # --------------------------------------------------
        # 8. SAVE ENRICHED DATA
        # --------------------------------------------------
        print("\n[8/10] Saving enriched data...")
        save_enriched_data(enriched_data)
        print("Saved to: enriched_sales_data.txt")

        # --------------------------------------------------
        # 9. GENERATE REPORT
        # --------------------------------------------------
        print("\n[9/10] Generating report...")
        generate_sales_report(valid_tx, enriched_data)
        print("Report saved to: sales_report.txt")

        # --------------------------------------------------
        # 10. COMPLETE
        # --------------------------------------------------
        print("\n[10/10] Process Complete!")
        print("=" * 40)

    except Exception as e:
        print("\n An unexpected error occurred")
        print("Error:", str(e))
        print("Please check your input files and try again.")


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------
if __name__ == "__main__":
    main()