#!/usr/bin/env python3
"""
multiple_category_matcher.py

Finds results that match ALL of the specified categories in a SQLite database.

Usage:
    python multiple_category_matcher.py <db_path> --categories <id1> <id2> ...

Example:
    python multiple_category_matcher.py results.db --categories 1 4 6 7 11
"""

import argparse
import sqlite3
import sys

import pandas as pd


def fetch_matched_results(db_path: str, category_ids: list[int]) -> list[sqlite3.Row]:
    """
    Query the SQLite database for results that match ALL of the given category IDs.

    Args:
        db_path:      Path to the SQLite database file.
        category_ids: List of category IDs that must all be matched.

    Returns:
        A list of sqlite3.Row objects with columns:
            - result_id          (int)
            - content            (str)
            - matched_categories (str, comma-separated category names)
    """
    setup_query = """
        DROP TABLE IF EXISTS wanted_categories;

        CREATE TEMP TABLE wanted_categories (
            category_id INTEGER PRIMARY KEY
        );
    """

    main_query = """
        WITH matched_results AS (
            SELECT
                rc.result_id
            FROM result_category rc
            WHERE rc.match = 'yes'
              AND rc.category_id IN (
                  SELECT category_id FROM wanted_categories
              )
            GROUP BY rc.result_id
            HAVING COUNT(DISTINCT rc.category_id) =
                   (SELECT COUNT(*) FROM wanted_categories)
        )
        SELECT
            r.result_id,
            r.content,
            GROUP_CONCAT(c.category_name, ', ') AS matched_categories
        FROM matched_results m
        JOIN result r
          ON r.result_id = m.result_id
        JOIN result_category rc
          ON rc.result_id = m.result_id
        JOIN category c
          ON c.category_id = rc.category_id
        WHERE rc.match = 'yes'
          AND rc.category_id IN (
              SELECT category_id FROM wanted_categories
          )
        GROUP BY
            r.result_id,
            r.content
    """

    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        conn.executescript(setup_query)
        conn.executemany(
            "INSERT INTO wanted_categories (category_id) VALUES (?)",
            [(cid,) for cid in category_ids],
        )
        cursor = conn.execute(main_query)
        return cursor.fetchall()


def build_dataframe(rows: list[sqlite3.Row]) -> pd.DataFrame | None:
    """
    Build a pandas DataFrame from query results.

    The content column is truncated to the first three non-empty lines for
    readability.

    Args:
        rows: List of sqlite3.Row objects as returned by fetch_matched_results.

    Returns:
        A DataFrame with columns result_id, content, and matched_categories,
        or None if there are no results.
    """
    if not rows:
        return None

    def truncate_content(text: str) -> str:
        return "\n".join(
            line for line in str(text).splitlines()[:3] if line.strip()
        )

    return pd.DataFrame(
        [
            {
                "result_id": row["result_id"],
                "content": truncate_content(row["content"]),
                "matched_categories": row["matched_categories"],
            }
            for row in rows
        ]
    )


def main() -> None:
    """
    Entry point for the command-line interface.

    Parses arguments (db_path, --categories, and optional --limit), calls
    fetch_matched_results, and prints the results via print_table. Exits with
    code 1 on database errors.
    """
    parser = argparse.ArgumentParser(
        description="Find results matching ALL specified categories in a SQLite DB."
    )
    parser.add_argument("db_path", help="Path to the SQLite database file")
    parser.add_argument(
        "--categories",
        nargs="+",
        type=int,
        required=True,
        metavar="ID",
        help="One or more category IDs that must ALL match",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        metavar="N",
        help="Only print the first N results",
    )
    args = parser.parse_args()

    try:
        rows = fetch_matched_results(args.db_path, args.categories)
        if args.limit is not None:
            rows = rows[: args.limit]
        df = build_dataframe(rows)
        if df is None:
            print("No results found.")
        else:
            pd.set_option("display.max_colwidth", 80)
            pd.set_option("display.width", None)
            pd.set_option("display.max_rows", None)
            print(df.to_string(index=False))
            print(f"\n{len(df)} row(s) returned.")
    except sqlite3.OperationalError as e:
        print(f"Database error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
