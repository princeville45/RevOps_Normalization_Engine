def aggregate_revenue(entity_data_list):
    """Aggregates revenue across multiple legal entities into a single reporting currency."""
    total_rev = sum([item['revenue_usd'] for item in entity_data_list])
    return round(total_rev, 2)