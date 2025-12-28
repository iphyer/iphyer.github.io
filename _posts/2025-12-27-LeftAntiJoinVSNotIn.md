---
layout: post
title: "NOT IN vs LEFT ANTI JOIN: A Performance Comparison"
date: 2025-12-27 22:54
comments: true
categories: 工作 SQL
---

When filtering data based on exclusion criteria, the choice between `NOT IN` and `LEFT ANTI JOIN` can significantly impact query performance. This post demonstrates why `LEFT ANTI JOIN` is typically the better choice.

< Revised and generated with help of Claude >

<!--more-->

## Original Approach (Inefficient)

```sql
SELECT product_id, product_category
FROM products_dim
WHERE region_id = 100
    AND product_id NOT IN (
        SELECT product_id
        FROM products_dim
        WHERE region_id = 200
    )
    AND product_category IS NOT NULL
```

## Optimized Approach (Recommended)

```sql
SELECT a.product_id, a.product_category
FROM products_dim a
LEFT ANTI JOIN (
    SELECT DISTINCT product_id
    FROM products_dim
    WHERE region_id = 200
) b ON a.product_id = b.product_id
WHERE a.region_id = 100
    AND a.product_category IS NOT NULL
```

## Why This Works

Both queries return exactly the same result: products from region 100 that don't exist in region 200.

### Key Differences

| Aspect | NOT IN | LEFT ANTI JOIN |
|--------|--------|----------------|
| **Performance** | Slower, less optimized | Faster, better optimized by Spark |
| **Broadcast Risk** | Can trigger unwanted broadcasts | Better control, prevents large broadcasts |
| **Execution Plan** | Subquery execution | Efficient join strategy |
| **NULL Handling** | Unpredictable with NULLs | Predictable behavior |

### Bottom Line

`LEFT ANTI JOIN` prevents broadcast errors while delivering the same results faster. When working with large datasets, this optimization can make a substantial difference in query execution time and resource utilization.